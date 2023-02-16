from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, request
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import model_house
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB="hogwarts"