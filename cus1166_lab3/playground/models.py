from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# Define a Flight model.
class Course(db.Model):
# Map this model to a course table
__tablename__= "courses"
# Specify the columns/ fields of the model.
id = db.Column(db.Integer,primary_key=True)
course_number = db.Column(db.String, nullable = False)
course_title = db.Column(db.String, nullable = False)

# Specify any relationship fields.
professors = db.relationship("Professor", backref="courses", lazy=True)
# specify any utility methods associated with the model.
def add_student(self,name,id):
# Notice that we set the foreign key for the passenger class.
new_course = ourse(name=name, course_number = self.number, id=self.id )
db.session.add(new_course)
db.session.commit()
#Define a Passenger model.
class RegisteredStudent(db.Model):
__tablename__ = "RegisteredStudent"
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String, nullable = False)
grade = db.Column(db.String, nullable=False)
# Notice, this field serves as a foreighKey.
id = db.Column(db.Integer, db.ForeignKey('RegisteredStudent.id'), nullable=False
