from flask import Flask
from dbhelpers import run_statement
import json

app = Flask(__name__)

@app.get('/hello')
def get_hello():
    return "Hello World"

@app.get('/books')
def get_books():
    result = run_statement("CALL get_author_booktitle()")
    print(result)
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        return result_json
    else:
        return "Sorry, something went wrong"

@app.get('/books_authored')
def get_auth_written():
    result = run_statement("CALL get_author_bookswritten()")
    print(result)
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        return result_json
    else:
        return "Sorry, something went wrong"


@app.get('/best_selling_book')
def get_best_seller():
    result = run_statement("CALL get_mostcopiessold_alpha()")
    print(result)
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        return result_json
    else:
        return "Sorry, something went wrong"

@app.get('/best_selling_author')
def get_best_author_list():
    result = run_statement("CALL get_top_auth_list()")
    print(result)
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        return result_json
    else:
        return "Sorry, something went wrong"




app.run(debug = True)