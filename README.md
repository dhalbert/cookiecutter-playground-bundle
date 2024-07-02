# CookieCutter Playground Bundle

Actions workflow demo for creating CircuitPython project bundles to use with
"Download Project Bundle" buttons in Adafruit Playground guides.

The template in this repository is meant to contribute to ongoing discussion
about how to add a project bundle download feature to the Adafruit Playground
editor. For related discussion, refer to the "In the weeds" section of the
[June 24, 2024 CircuitPython weekly meeting](https://github.com/adafruit/adafruit-circuitpython-weekly-meeting/blob/main/2024/2024-06-24.md#2737-in-the-weeds).


## How do I use this CookieCutter template?

There are two ways to use this repo as a template for your CircuitPython
project:

1. Fancy way: Use the `cookiecutter` commandline tool to start a new project
   from the template in this repository. See the
   [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html)
   readthedocs documentation for an explanation of how to use CookieCutter.

2. Manual way: Copy all of the files inside of the
   [{{ cookiecutter.project_slug }}](%7B%7B%20cookiecutter.project_slug%20%7D%7D)
   directory into the directory for your project's github repo, then edit the
   README.md and LICENSE files to fill in the correct project and author info.
   For example, in terminal shell, you could do something like this:

   ```
   git clone $MY_NEW_REPO
   git clone $COOKIECUTTER_TEMPLATE
   cd $COOKIECUTTER_TEMPLATE
   cp -r '{{ cookiecutter.project_slug }}'/* ../$MY_NEW_REPO/
   cp -r '{{ cookiecutter.project_slug }}'/.git* ../$MY_NEW_REPO/
   cd ../$MY_NEW_REPO
   vim README.md
   vim LICENSE
   git status
   ```

Once you add the files to your new project repo, commit the changes, and push
them to GitHub, you will have a GitHub Actions workflow that makes project
bundle zip files. To trigger the bundle builder, you can make a
[tagged release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
on GitHub (the tag triggers the workflow). Assuming the bundle builder works as
planned, it should attach a zip file to the GitHub page for your tagged release.
To check for bundle builder errors (perhaps a typo in the config file?), refer
to GitHub's
[Viewing workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history)
documentation page.

Note that you will probably need to edit the `bundle_manifest.cfg` file in your
new repo. The bundle manifest determines which code files and library versions
get included in your project bundle zip file.


## How does this work?

This repository is a proof of concept for using a GitHub Actions workflow to
create CircuitPython project bundle zip files each time you publish a release.

The Actions workflow goes like so:

1. [.github/workflows/bundle_builder.yml](.github/workflows/bundle_builder.yml)
   is triggered by the creation of tags (such as when publishing a release).
   Note that there are two different `.github/workflows/bundle_builder.yml`
   files. The one at the root level of this repo is meant to help with testing
   the bundle builder template. The one in
   [{{ cookiecutter.project_slug }}](%7B%7B%20cookiecutter.project_slug%20%7D%7D)
   gets copied into new projects created using `cookiecutter`.

2. `bundle_builder.yml` calls `make bundle` to run
   [{{ cookiecutter.project_slug }}/bundle_builder.py](%7B%7B%20cookiecutter.project_slug%20%7D%7D/bundle_builder.py).
   Note that there are two Makefiles. The one at the root level of this repo is
   meant to help with testing the bundle builder template. The one in
   [{{ cookiecutter.project_slug }}](%7B%7B%20cookiecutter.project_slug%20%7D%7D)
   gets copied into new projects created using `cookiecutter`.

3. `bundle_builder.py` reads
   [{{ cookiecutter.project_slug }}/bundle_manifest.cfg](%7B%7B%20cookiecutter.project_slug%20%7D%7D/bundle_manifest.cfg)
   to determine which files to copy from the repository (`code.py`, etc) into
   the build directory for the project bundle zip file (**note: this is not
   finished yet; copying of libraries is not finished, but the rest of it
   works**)

4. Once the bundle zip is ready, `.github/workflows/bundle_builder.yml` uses
   a `gh release upload ...` shell command to upload the bundle zip file to a
   release (this works, see
   [release v0.0.0-1](https://github.com/samblenny/cookiecutter-playground-bundle/releases/tag/v0.0.0-1))


## What is this for?

The Adafruit Learning System includes a tool called BundleFly to help Learn
guide authors share example code with Learn guide readers. As of June 2024,
BundleFly is not currently available for
[Adafruit Playground](https://adafruit-playground.com/) authors. For various
reasons, it might not be practical to add BundleFly to the Playground editor in
the same way as the Learning System editor.

But, by using a GitHub Actions workflow, Playground guide authors can make
their own project bundle zip files in the style of BundleFly.

By adding a copy of the GitHub Action defined in this template to the GitHub
repository for your own project, you can generate a project bundle zip file as
an asset file for a tagged release. Once you have the zip file's GitHub link,
you can make a big blue "Download Project Bundle" using the Adafruit Playground
editor. For Playground guide readers, the end result will look and feel similar
to a Learn guide project bundle button.


## Links, Context, and Glossary

This section has notes that may be helpful for people who want to understand
discussions about writing Adafruit Playground or Learning System guides.

### GitHub Actions

[GitHub Actions workflows](https://docs.github.com/en/actions/using-workflows)
are a way to have GitHub's servers run code when you do things like push a
commit or create the tag for a new release. Actions workflows are commonly
used for things like running tests or building downloadable release files. You
can use a GitHub Actions workflow to make a new project bundle zip file when you
make updates to example code.

Some Adafruit repositories use
[CircuitPython_Library_Screenshot_Maker](https://github.com/circuitpython/CircuitPython_Library_Screenshot_Maker)
in GitHub Actions workflows to make CIRCUITPY drive screenshots suitable for
including in a Learn guide.


### CookieCutter

Setting up the GitHub repo for a new CircuitPython project or library can be a
bit complicated. So, people often start by copying from a template or a Learn
guide example.

[CookieCutter](https://pypi.org/project/cookiecutter/) is a command line tool
to help set up the working folder for a new project using a project template.
In discussions among CircuitPython developers, a GitHub repository containing a
project template may sometimes be called a "cookie cutter". If you see someone
mention "cookie cutter", "CookieCutter", etc. on Adafruit Discord, they might
be talking about input to the `cookiecutter` command (a template). They might
be talking output from the `cookiecutter` command (a new project folder created
from a template). Or, they might be talking about the `cookiecutter` command
itself.

For more context on using CookieCutter to help start a CircuitPython library,
see the
[Cookie cutter](https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/creating-a-library#cookie-cutter-2866283)
section of the "Creating and sharing a CircuitPython library" Learn guide.


### Code Boxes, Download Buttons, and Project Bundles

Code boxes with blue download buttons are an important part of the Adafruit
Learn guide style. Project bundle zip files make it easy to install all the
code, libraries, and other files needed to run Learn guide examples. While
other methods are possible, zip files are good for beginners because they work
without the need to install additional developer tools
([xkcd 1987](https://xkcd.com/1987/)).

According to Ladyada's
[What is BundleFly?](https://www.youtube.com/watch?v=UgekT8epJjo) video, the
blue
[Download Project Bundle](https://learn.adafruit.com/qtpy-lemon-mechanical-keypad-macropad/code#download-project-bundle-3094704)
buttons in Learn guides provide zip files created by BundleFly. BundleFly is an
internal Adafruit tool, so I'm not sure exactly how it works. The rest of this
section focuses on the observable results of what BundleFly does. I'm curious
about details of how it works, but I wasn't able to find documentation for it.

Anyhow, in addition to code boxes with "Download Project Bundle" buttons, there
are also code boxes with "Download File" buttons. Based on clicking "View on
GitHub" links at the bottom of several example code boxes in various Learn
guides, it seems that many project bundles are built from code, libraries, and
asset files hosted in the
[Adafruit\_Learning\_System\_Guides](https://github.com/adafruit/Adafruit_Learning_System_Guides)
GitHub repo. But, some of the project bundles also come from an `examples/`
directory in a project-specific repo.

The top level directory of the Adafruit\_Learning\_System\_Guides repo has many
folders for individual projects, along with some folders for project categories
like `MagTag` and `QT_Py`. I'm not clear about the rules BundleFly follows for
naming project bundle zip files. They may be based on the project folder name
on GitHub. For code examples that come from an `examples/` directory in a
project-specific repo, the zip file can be named `examples.zip`, which is a bit
confusing. But, some of the zip files have names that match names of folders
inside of the Adafruit\_Learning\_System\_Guides repo.

The project bundle file names, and the folders they contain when expanded,
don't always obviously relate to page or section names in the Learn guides. In
some cases, the project bundles appear to be from another Learn guide that uses
the same example code. That makes sense, because the Learning System editor is
set up so that sub-sections of Learn guides can be re-used in other Learn
guides.

Also, there were a few GitHub Pull Requests mentioning the need to move or
rename certain files so they would be detected by BundleFly. It seems as though
BundleFly has rules about expected files and folder locations, but I don't know
what they are.


#### Example 1: MagTag Internet Test

On the "CircuitPython Internet Test" page of the
[Adafruit MagTag](https://learn.adafruit.com/adafruit-magtag/internet-connect)
Learn guide, there's a code box near the top of the page. The code box's
"View on GitHub" link points to
[Adafruit\_Learning\_System\_Guides/ESP32\_S2\_WiFi\_Tests/CPy\_Native\_WiFi\_Test/code.py](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/ESP32_S2_WiFi_Tests/CPy_Native_WiFi_Test/code.py)
on GitHub repo. When I click the code box's
blue "Download Project Bundle" button, it gives me a file named
`CPy_Native_WiFi_Test.zip`. When I expand the zip file, it gives me a folder
named `ESP32_S2_WiFi_Tests`, which contains another folder named
`CPy_Native_WiFi_Test`. The full directory tree looks like this:

```
.
├── CPy_Native_WiFi_Test.zip
└── ESP32_S2_WiFi_Tests
    └── CPy_Native_WiFi_Test
        ├── CircuitPython 8.x
        │   ├── code.py
        │   ├── lib
        │   │   ├── adafruit_connection_manager.mpy
        │   │   └── adafruit_requests.mpy
        │   └── settings.toml
        ├── CircuitPython 9.x
        │   ├── code.py
        │   ├── lib
        │   │   ├── adafruit_connection_manager.mpy
        │   │   └── adafruit_requests.mpy
        │   └── settings.toml
        └── README.txt
```

On GitHub, going up one level from `code.py` to
[Adafruit\_Learning\_System\_Guides/ESP32\_S2\_WiFi\_Tests/CPy\_Native\_WiFi\_Test](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/ESP32_S2_WiFi_Tests/CPy_Native_WiFi_Test),
the contents of that directory are just `code.py` and `settings.toml`. So, it
seems like BundleFly has some method to know that the
`adafruit_connection_manager` and `adafruit_requests` packages are needed and
some method to obtain the appropriate `.mpy` files to satisfy that dependency.

Also, the Learn guide code box shows only `code.py`, but BundleFly apparently
knows that it should look at the folder containing `code.py` for other files
(in this case, `settings.toml`). I'm curious how the editor UI works for
specifying the GitHub repo and directory. Maybe you provide a link to `code.py`
and the rest is auto-detected? Maybe you provide a link to the folder that
contains `code.py`? Perhaps there is a way to specify libraries that should be
included rather than relying on auto-detection (which could be troublesome)?

A complication for auto-detecting library dependencies is that CircuitPython
allows each board to be configured in the build system for a different set of
built in (frozen) libraries. This helps with managing RAM and flash, but it
complicates the process of determining what needs to go in the `CIRCUITPY/lib/`
directory.

If there is an automatic tool to resolve `import` dependencies in `code.py`
against lists of frozen packages for various CircuitPython boards, I haven't
seen it. The docs for [circup](https://github.com/adafruit/circup) say it can
update your installed libraries, but I found no mention of a feature to detect
if you are missing libraries that need to be installed. I'm guessing people
usually handle that problem by running the code and watching for import errors.

I don't know how or if BundleFly decides which libraries to include in project
bundles. But, for creating Playground guide project bundles, it seems like a
practical approach would be to require a manifest file listing the libraries to
include in the bundle.


#### Example 2: Lemon Mechanical Keypad

On the "Code" page of the
[Lemon Mechanical Keypad](https://learn.adafruit.com/qtpy-lemon-mechanical-keypad-macropad/code)
Learn guide, the code box's "View on GitHub" link points to
[Adafruit\_Learning\_System\_Guides/QT\_Py/QT\_Py\_RP2040\_Lemon\_Keypad
/code.py](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/QT_Py/QT_Py_RP2040_Lemon_Keypad/code.py).
The blue "Download Project Bundle" button gives a zip file named
`QT_Py_RP2040_Lemon_Keypad.zip`, which contains a folder named `QT_Py`. The
full directory tree looks approximately like this:


```
.
├── QT_Py_RP2040_Lemon_Keypad.zip
└── QT_Py
    └── QT_Py_RP2040_Lemon_Keypad
        ├── CircuitPython 9.x
        │   ├── code.py
        │   └── lib
        │       ├── adafruit_hid
        │       │   └── ...
        │       ├── adafruit_pixelbuf.mpy
        │       ├── neopixel.mpy
        │       └── adafruit_led_animation
        │           └── ...
        ├── CircuitPython 8.x
        │   ├── code.py
        │   └── lib
        │       ├── adafruit_hid
        │       │   └── ...
        │       ├── adafruit_pixelbuf.mpy
        │       ├── neopixel.mpy
        │       └── adafruit_led_animation
        │           └── ...
        └── README.txt
```

