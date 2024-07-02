all:
	@echo "This is intened for use by the .github/workflows/buildbundle.yml"
	@echo "GitHub Actions workflow. You can run the bundle builder manually"
	@echo "with: make bundle"

bundle:
	@mkdir -p build
	python3 bundle_builder.py

list:
	unzip -l 'build/*.zip'

clean:
	rm -rf build
