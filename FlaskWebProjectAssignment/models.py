from FlaskWebProjectAssignment import db
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin
from FlaskWebProjectAssignment import login

class User(UserMixin, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    address = db.Column(db.String(256),index = True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    orders = db.relationship('Order', backref ='order',lazy='dynamic')
    def __repr__(self):
        return '<User {}>'.format(self.username)  

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))
class Order(UserMixin, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    Base = db.Column(db.String(128), index= True)
    Icing = db.Column(db.String(128), index= True)
    Flavour = db.Column(db.String(128), index= True)
    Decoration = db.Column(db.String(128), index= True)
    EggEggless = db.Column(db.Boolean, index= True , default=True)
    usr_id= db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Order {}>'.format(self.Base)  