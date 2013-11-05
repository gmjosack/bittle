.PHONY: README test

README:
	pandoc --from=markdown --to=rst --output=README README.md

test:
	python -m unittest -v bittle.tests
