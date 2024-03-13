from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate 

# import flask migrate here

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URL'] = 'lab4_user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'c0a47aa0a8c95249ac5ecbe0d940ca7826a8cfd12f4bc47de6131c854036f227'


db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here
migrate = Migrate(app, db) 

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'




from app import views
