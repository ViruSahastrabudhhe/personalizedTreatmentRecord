from flask import Flask
from .extensions import mail

app=Flask(__name__)
app.config['SECRET_KEY'] = 'superdupersecretkey'

from .functions.authentication import authentication as authentication_bp
app.register_blueprint(authentication_bp)
from .functions.nurse import nurse as nurse_bp
app.register_blueprint(nurse_bp)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']='awesomersecommerce@gmail.com'
app.config['MAIL_PASSWORD']='veop zyzn bpwp ymbk '
app.config['MAIL_USE_TLS']=True
app.config["MAIL_USE_SSL"]=False

mail.init_app(app)

app.static_folder = 'static'
app.template_folder = 'templates'