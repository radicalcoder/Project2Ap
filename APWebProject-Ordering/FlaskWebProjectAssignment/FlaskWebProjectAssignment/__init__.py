"""
The flask application package.
"""

from flask import Flask
from config import Config, Configorder
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

#migrate = Migrate(app, db)
login = LoginManager(app)


@app.before_first_request
def create_tables():

    from FlaskWebProjectAssignment.models import User, Order
    #Test code to delete old db   
    #db.drop_all()    
    db.create_all() 
    admin = User(username='susan', email='susan@example.com')
    users = User.query\
			.join(Order)\
			.join(Order.test1)\
            .filter(User.id==1).all()



from FlaskWebProjectAssignment import views, models

