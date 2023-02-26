.DEFAULT_GOAL := init

init: requirements.txt
	pip install -r requirements.txt