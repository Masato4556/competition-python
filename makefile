make_folder:
	poetry run python command/make_folder.py -c $(wordlist 1, $(MAKECMDGOALS))
fetch:
	poetry run python command/fetch_testcase.py $(wordlist 2, 3, $(MAKECMDGOALS))
test:
	poetry run python command/test.py $(wordlist 2, 3, $(MAKECMDGOALS))