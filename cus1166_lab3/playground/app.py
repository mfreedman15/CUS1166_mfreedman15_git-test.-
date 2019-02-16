@app.route("/")
def index():

course = Course.query.all()
return render_template('index.html', courses = courses)

@app.route("/add_course",methods=["post"])
def add_course():
# Get information from the form.
course_number = request.form.get("course_number")
course_title = request.form.get("course_title")
id = request.form.get("id")
course = Course(course_number="LH",course_title=course_title, id = id;)
db.session.add(course)
db.session.commit()

@app.route("/register_student/", methods=["GET", "POST"])
def register_student(id):

course = Course.query.get(course_title)

if request.method == 'POST':
id = request.form.get("id")
course_title = request.form.get("course_title")
course.register_student(id,course_title)
RegisteredStudent = course.RegisteredStudent
return render_template("index.html", course = course, RegisteredStudent = RegisteredStudent)
def main():
if (len(sys.argv)==2):
print(sys.argv)
if sys.argv[1] == 'createdb':
db.create_all()
else:
print("Run app using 'flask run' . To create a database use 'python app.py createdb' ")
