deps:
	pip install -r requirements.txt

test:
	python parser_test.py --verbose && \
	python evaluator_test.py --verbose
