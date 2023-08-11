# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/search')
def search():
    """Add a and b."""
   
    term = request.args["term"]
    return f"<h1>Search results for term: {term}</h1>"
   
#@app.route('/add')
#def addition():
    """Add a and b."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"This is your calculated sum: {add(a,b)}"



@app.route('/math/<operation>')
def mathing(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    operations = { 
    'add' : add(a,b),
    'sub' : sub(a,b),
    'mult' : mult(a,b),
    'div' : div(a,b)
    }
    the_math = operations[operation]
    return f"This is your requested calcuation: {the_math}"





  
    
   
