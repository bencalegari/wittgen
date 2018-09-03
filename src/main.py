from flask import render_template, jsonify
from db import get_db, query_db
from init import create_app

app = create_app()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/api/books/1')
def books_one():
    return (jsonify(json_dict()), { 'Access-Control-Allow-Origin': '*' })

def sentence_identifiers(sentences):
    sentence_identifiers = []
    for sentence in sentences:
        sentence_identifiers.append({
            'type': 'sentence',
            'id': str(sentence['id'])
        })
    return sentence_identifiers

def sentence_objects(sentences):
    sentence_objects = []
    for sentence in sentences:
        sentence_objects.append({
            'type': 'sentence',
            'id': str(sentence['id']),
            'attributes': {
                'body': sentence['body']
            },
            'relationships': {
                'book': {
                    'data': {'type': 'user', 'id': str(sentence['book_id'])}
                },
                'parent': {
                    'data': {'type': 'sentence', 'id': str(sentence['parent_id'])}
                }
            }
        })
    return sentence_objects

def json_dict():
    book = query_db('select * from book where id = ?', [1], one=True)
    author = query_db('select * from user where id = ?', [book['author_id']], one=True)
    sentences = query_db('select * from sentence where book_id = ?', [1])

    return {
        'data': {
           'type': 'book',
           'id': str(book['id']),
           'attributes': {
               'title': str(book['title'])
           },
           'relationships': {
               'author': {
                    'data': {'type': 'user', 'id': str(book['author_id'])}
               },
               'sentences': {
                    'data': sentence_identifiers(sentences)
               }
           }
        },
        'included': [book, *sentence_objects(sentences)]
    }
