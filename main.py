from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/book/1")
def book_one():
    return jsonify({
        'sentences': [
            'The world is everything that is the case.',
            'What is the case (a fact) is the existence of states of affairs.',
            'A logical picture of facts is a thought.',
            'A thought is a proposition with a sense',
            'A proposition is a truth-function of elementary proporsitions. (An elementary proposition is a truth-function of itself.)',
            'The general form a proposition is the general form of a truth function, which is [stuff]. This is the general form of a proposition.',
            'Whereof one cannot speak, thereof one must be silent.'
        ]
    })
