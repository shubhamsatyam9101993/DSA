## Lints the codebase
lint:
	autopep8 src/ tests/  --recursive --diff --pep8-passes 2000 --exit-code


## Lint-fixes the codebase
lint-fix:
	autopep8 src/ tests/ --recursive --in-place --pep8-passes 2000 -j 8
	make lint
	@echo ">>> autopep8 might have fixed few linting errors. Add files to git now. <<<"

test:
	py.test tests/*