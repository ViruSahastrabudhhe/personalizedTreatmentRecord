from flask import Flask

app=Flask(__name__)
app.config['SECRET_KEY'] = 'superdupersecretkey'
app.config['UPLOADED_FILES_DEST'] = '/awesomers/static/imgs'
app.config['UPLOAD_FOLDER'] = '/awesomers/static/imgs'

from .functions.authentication import authentication as authentication_bp
app.register_blueprint(authentication_bp)

app.static_folder = 'static'
app.template_folder = 'templates'