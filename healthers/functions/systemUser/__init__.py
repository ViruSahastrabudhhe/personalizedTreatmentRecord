from flask import Blueprint

systemUser=Blueprint('systemUser', __name__)

from . import routes