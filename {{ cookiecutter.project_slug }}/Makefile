# The "bundle" make target is used by the .github/workflows/buildbundle.yml"
# GitHub Actions workflow. You can also use it as a convenient way to obtain
# mpy files for libraries that you want to install on on your CIRCUITPY drive.

all:
	@echo "build project bundle:    make bundle"
	@echo "sync code to CIRCUITPY:  make sync"

bundle:
	@mkdir -p build
	python3 bundle_builder.py

list:
	unzip -l 'build/*.zip'

# This is for syncing current code and libraries to CIRCUITPY drive on macOS.
# To use this on other operating systems, adjust the "/Volumes/CIRCUITPY" path
# as needed. You might also want to read the rsync manual (try "man rsync" from
# a Terminal shell on macOS or Linux).
sync: bundle
	xattr -cr 'build/{{ cookiecutter.project_slug }}'
	rsync -rcvO 'build/{{ cookiecutter.project_slug }}/CircuitPython 9.x/' /Volumes/CIRCUITPY
	sync

clean:
	rm -rf build
