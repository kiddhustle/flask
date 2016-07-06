from flask import Blueprint

main = Blueprint('main', __name__)
pink = 'blue'

from . import views, errors
