# CAUTION: This Makefile is specifically for the CookieCutter template repo,
# and its purpose is to assist with using GitHub Actions to test changes to the
# template's bundle_builder.py script. There are another Makefile and a .github
# directory inside of '{{ cookiecutter.project_slug }}/', which are meant
# to be used by CircuitPython projects created from the template. If you make
# edits to either version of the .github/workflow yml file or the Makefile, be
# sure to keep the changes in sync with the other version.

all:
	@echo "(THIS IS THE OUTER MAKEFILE FOR THE TEMPLATE REPO)"
	@echo "This is intened for use by the .github/workflows/buildbundle.yml"
	@echo "GitHub Actions workflow. You can run the bundle builder manually"
	@echo "with: make bundle"

# This builds in the template directory, then copies the resulting zip files
# out to /build/ where the Actions workflow expects to find it. This is
# totally ignorable if you just want to use cookiecutter to make a new project.
# But, if you're working on the template itself, or on documentation for the
# template, this may be helpful.
bundle:
	@mkdir -p '{{ cookiecutter.project_slug }}/build'
	@mkdir -p build
	cd '{{ cookiecutter.project_slug }}' && python3 bundle_builder.py
	cp '{{ cookiecutter.project_slug }}'/build/*.zip build/

list:
	unzip -l '{{ cookiecutter.project_slug }}/build/*.zip'

clean:
	rm -rf '{{ cookiecutter.project_slug }}/build'
