from flask import Blueprint
api_learn = Blueprint('api_learn', __name__)
from . import views
