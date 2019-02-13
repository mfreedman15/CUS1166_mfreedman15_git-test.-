















def index():
    return render_template("index.html")


#Separation of UI
#Example of passing parameters to the template
@app.route("/Welcome/<string:course>")
def welcome(course):
    return render_template("index2.html", course=course)



#Example of conditional rendering in templates.
@app.route("/do/i/teach/<string:course>")
def doiteach(course):
    doTeach = (course == "CUS1166") or (course == "CUS615)")
    return render_template("index3.html", course=course, doTeach = doTeach)


#Example of loops in templates
@app.route"/roster/<string:course>")
def roster(course):
    roster = [{"John","A"}, ("Tom","B"), ("Mary", "C"),("Lucas","B-"),("Joan","D")]
    return render_template("index4.html",)
