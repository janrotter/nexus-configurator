all: test
.PHONY: test all lint

groovy:
	./build.sh

test: groovy
	pytest -vv

lint:
	pylama
