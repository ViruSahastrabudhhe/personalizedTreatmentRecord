from flask import Blueprint

nurse=Blueprint('nurse', __name__)

from . import routes, views, getters