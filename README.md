# CookieCutter Playground Bundle

**Work in progress (alpha)**

A helper template for adding project bundles to Adafruit Playground guides.

The template in this repository is meant to contribute to ongoing discussion
about how to add a project bundle download feature to the Adafruit Playground
editor. For related discussion, refer to the "In the weeds" section of the
[June 24, 2024 CircuitPython weekly meeting](https://github.com/adafruit/adafruit-circuitpython-weekly-meeting/blob/main/2024/2024-06-24.md#2737-in-the-weeds).


## What is this for?

The Adafruit Learning System includes a tool called BundleFly to help Learn
guide authors share example code with Learn guide readers. As of June 2024,
BundleFly is not currently available for
[Adafruit Playground](https://adafruit-playground.com/) authors. For various
reasons, it might not be practical to add BundleFly to the Playground editor in
the same way as for Learning System editor.

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
be talking about input to the `cookiecutter` command line tool (a template).
They might be talking output from the `cookiecutter` command line tool (a new
project repo created from a template). Or, they might be talking about the
`cookiecutter` command line tool itself.

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

According to LadyAda's
[What is BundleFly?](https://www.youtube.com/watch?v=UgekT8epJjo) video, the
blue
[Download Project Bundle](https://learn.adafruit.com/qtpy-lemon-mechanical-keypad-macropad/code#download-project-bundle-3094704)
buttons in Learn guides provide zip files created by BundleFly. BundleFly is an
internal Adafruit tool, so I'm not sure exactly how it works. The following
description is my best guess based on public information.

Anyhow, in addition to code boxes with "Download Project Bundle" buttons, there
are also code boxes with "Download File" buttons. Based on clicking "View on GitHub" links at the bottom of several example code
boxes in various Learn guides, it seems that many project bundles are made code
hosted in the
[Adafruit\_Learning\_System\_Guides](https://github.com/adafruit/Adafruit_Learning_System_Guides)
GitHub repo. But, some of them come from an `examples/` directory in a
project-specific repo.

The top level directory of the Adafruit\_Learning\_System\_Guides repo has many
folders for individual projects and also some folders for project categories
like `MagTag` and `QT\_Py`. I'm not clear about the rules BundleFly follows for
naming project bundle zip files. They may be based on the project folder name
on GitHub. For code examples that come from an `examples/` directory in a
project-specific repo, the zip file can be named `examples.zip`, which is a bit
confusing. But, some of the zip files have names that match names of folders
inside of the Adafruit\_Learning\_System\_Guides repo.

The project bundle file names, and the folders they contain when expanded,
don't always obviously relate to page or section names in the Learn guides. In
some cases, the project bundles appear to be from another project that uses the
same example code. That makes sense, because the Learning System editor is set
up so that sub-sections of Learn guides can be re-used in other Learn guides.

Also, there were a few GitHub Pull Requests mentioning the need to move or
rename certain files so they would be detected by BundleFly. It seems as though
BundleFly has rules about expected files and folder locations, but I don't know
what they are.


#### Example 1: MagTag Internet Test

On the "CircuitPython Internet Test" page of the
[Adafruit MagTag](https://learn.adafruit.com/adafruit-magtag/internet-connect)
Learn guide, there's a code box near the top of the page. The code box's
"View on GitHub" link points to
[ESP32\_S2\_WiFi\_Tests/CPy\_Native\_WiFi\_Test/code.py](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/ESP32_S2_WiFi_Tests/CPy_Native_WiFi_Test/code.py)
in the Adafruit\_Learning\_System\_Guides repo. When I click the code box's
blue "Download Project Bundle" button, it gives me a file named
`CPy_Native_WiFi_Test.zip`. When I expand the zip file, it gives me a folder
named `ESP32\_S2\_WiFi\_Tests`, which contains another folder named
`CPy\_Native\_WiFi\_Test`. The full directory tree looks like this:

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
