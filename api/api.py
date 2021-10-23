from flask import Flask, jsonify, request

app = Flask(__name__)

app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route("/", methods=["GET"])
def home():
    return "Test rah mande Flask"

@app.route('/api/books', methods=["GET"])
def api_books():
    return jsonify(books)

@app.route('/api/books/id/', methods=["GET"])
def api_books_byId():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error! No ags [id] provided!"
    
    result = []
    for book in books:
        if book['id'] == id:
            result.append(book)
    return jsonify(result)
    
app.run()

