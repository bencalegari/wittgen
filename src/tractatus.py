tractatus = {
    'type': 'book',
    'id': 1,
    'relationships': {
        'author': {
            'data': {
                'type': 'book',
                'id': 1
            }
        },
        'sentences' {
            'data': {
                'type': 'sentence',
            }
        }
    }
}

wittgenstein = {
    'type': 'user',
    'id': 1,
    'relationships': {
        'book': {
            'data': {
                'type': 'book',
                'id': 1
            }
        }
    }
}

sentenceRelationships = {
    'book': {
        'data': {
            'type': 'book',
            'id': 1
        }
    },
    'author': {
        'data': {
            'type': 'user',
            'id': 1
        }
    }
}

one = {
    'type': 'sentence',
    'id': 1,
    'attributes': {
        'text': 'The world is everything that is the case',
    }
}

oneone = {
    'type': 'sentence',
    'id': 4,
    'attributes': {
        'text': 'The world is the totality of facts, not of things.'
    }
}

oneoneone = {
    'type': 'sentence',
    'id': 5,
    'attributes': {
        'text': 'The world is determined by the facts, and by these being all the facts.'
    }
}

two = {
    'type': 'sentence',
    'id': 2,
    'attributes': {
        'text': 'What is the case (a fact) is the existence of states of affairs.'
    }
}

twozeroone = {
    'type': 'sentence',
    'id': 2,
    'attributes': {
        'text': 'An atomic fact is a combination of objects (entities, things)'
    }
}

three = {
    'type': 'sentence',
    'id': 3,
    'attributes': {
        'text': 'A logical picture of facts is a thought.'
    }
}
