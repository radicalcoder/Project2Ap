"""
The flask application package.
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)

#migrate = Migrate(app, db)



@app.before_first_request
def create_tables():  
    from FlaskWebProjectAssignment.models import Order, User
    #Test code to delete old db   
    #db.drop_all()    
    db.create_all() 

from FlaskWebProjectAssignment import views, models