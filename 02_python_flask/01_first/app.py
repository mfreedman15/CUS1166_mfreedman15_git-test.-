#Importing Flask class from the flask module
from flask import flask

#Create an instane of Flask class
app = Flask(__name__)

#This we define a new route
# -- Flask is designed in terms of routes
#-- Routes are part of the URL a client is requesting
#-- When a user goes to the default route -- this is the function I want to run.
#-- app.route() is a decorator.
@app.route("/")
def index():
    return "<h1 style='color:red'>Hello World!!</h1><h2> Hello World!!! </h2><h3> Hello World!!! </h3>"

    if__name__ == "__main__":
    app.run()
