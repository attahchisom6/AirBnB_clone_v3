#!/usr/bin/python3
"""
The init files
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')


# import storage engine and classes
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

# Now import flask views
from api.v1.views.index import *