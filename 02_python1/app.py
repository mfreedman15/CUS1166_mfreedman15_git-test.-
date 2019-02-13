#Note how to define parameterized routes
from flask import flask

app






#Note that the template variable <String:course> is passed as a keyword argument
# to the decorated fucntion 'welcome' Thus the function welcome MUST define a variable
#
@app.route("/Welcome/<string:courese>")
def welcome(course):
    #course = course.captialize()
    return f"Welcome to {course}"


    #Note that the route defines two parameters
    #- Note route returns html page
    @app.route("/Welcome/<string:course>/<int:size>/<int:color>")
    def welcome_h(course,size, color):
        colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'lime']
        return (f"<h{size} style='color: {colors[color]}'> Welcome to {course} <h{size}>")
