#
#

import os
from flask import Flask, render_template, request, redirect

#provides access to the create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#Initialize the database connection
basedir = os.path.abspath(os.path.dirnamel)


engine = create_engine(DATABASE_URL)

#Use scoped_session to managge multiple connetion in the database
db - scoped_session(sessionmaker(bind=engine))



app = Flask(__name__)
