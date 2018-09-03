# wittgen

## getting started
* make sure you run `source ./env/bin/activate` to run your local python.
* run `elm make Main.elm --output src/templates/index.html` to build your frontend
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

# elm/frontend
I followed the instructions here: https://guide.elm-lang.org/install.html
I also set up my IDE via the instructions found there. My IDE is Atom.

* to build the index.html file in templates, run `elm make --output templates/index.html`

## other
* the `Procfile` is for Heroku deployment
* while still using sqlite3, use this command to quickly reset the db
`rm witt.db && sqlite3 -init src/schema.sql witt.db`
you will then have to quit out of the interactive terminal: `.quit`

## api
This application tries to conform to the json api specification (jsonapi.org).
For example, when requesting book data, e.g., `/api/books/1`, a successful
response looks like the following:
```
{
	"data": {
		"type": "book",
		"id": "1",
		"attributes": {
			"title": "Tractatus Logico-Philosophicus",
		},
		"relationships": {
			"author": {
				"data": {"type": "user", "id": "1"}
			},
			"sentences": {
				"data": [
					{"type": "sentence", "id": "1"},
					{"type": "sentence", "id": "2"}
				]
			}
		}
	},
	"included": [
		{
			"type": "user",
			"id": 1,
			"attributes": {
				"name": "Ludwig Wittgenstein"
			}
		},
		{
			"type": "sentence",
			"id": "1",
			"attributes": {
				"body": "The world is everything that is the case."
			},
			"relationships": {
				"author": {
					"data": {"type": "user", "id": 1}
				},
				"book": {
					"data": {"type": "book", "id" 1}
				}
			}
		},
		{
			"type": "sentence",
			"id": "2",
			"attributes": {
				"body": "The world is the totality of facts, not of things.",
			},
			"relationships": {
				"author": {
					"data": {"type": "user", "id": 1}
				},
				"book": {
					"data": {"type": "book", "id" 1}
				},
				"parent": {
					"data": {"type": "sentence", "id": 1}
				}
			}
		}
	]
}
```
