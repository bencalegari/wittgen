# wittgen

## workstation setup
I began with the python3 and pip3 bins that came by default with my machine, Ubuntu 18.04.

* `pip3 install virtualenv`
* `cd path/to/wittgen`
* `python3 -m virtualenv env`
	* virtualenv will generate the gitignored env/ subdirectory
* `source env/bin/activate`
* `pip install pipenv`
* e.g., `pipenv install flask`
	* pipenv will generate your Pipfile and Pipfile.lock
