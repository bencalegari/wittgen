# wittgen

## getting started
* make sure you run `source ./env/bin/activate` to run your local python.
* run `elm make Main.elm --output templates/index.html` to build your frontend
* run `FLASK_APP=main.py flask run`
* by default the app will be hosted on port 5000

## workstation setup
# python/backend
I began with the python3 and pip3 bins that came by default with my machine, Ubuntu 18.04.

* `pip3 install virtualenv`
* `cd path/to/wittgen`
* `python3 -m virtualenv env`
	* virtualenv will generate the gitignored env/ subdirectory
* `source env/bin/activate`
* `pip install pipenv`
* e.g., `pipenv install flask`
	* pipenv will generate your Pipfile and Pipfile.lock

#elm/frontend
I forget what I did to install the elm binary.
I assume I followed the instructions here: https://guide.elm-lang.org/install.html
I also set up my IDE via the instructions found there, which is Atom.

* to build the index.html file in templates, run `elm make --output templates/index.html`

## other
* the `Procfile` is for Heroku deployment
