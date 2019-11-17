"""
The flask application package.
"""

from flask import Flask
from config import Config, Configorder
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)
ord = Flask(__name__)
app.config.from_object(Config)
ord.config.from_object(Configorder)
db = SQLAlchemy(app)
dborder = SQLAlchemy(ord)
#migrate = Migrate(app, db)
login = LoginManager(app)


@app.before_first_request
def create_tables():

    from FlaskWebProjectAssignment.models import User, Order
    #Test code to delete old db   
    #db.drop_all()    
    db.create_all() 
    admin = User(username='susan', email='susan@example.com')
    p = Order(id = '1')
    db.session.add(admin)
    db.session.add(p)
    db.session.commit
   

from FlaskWebProjectAssignment import views, models

