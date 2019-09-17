# models.py
import flask_sqlalchemy, app


# app.app = app modules app variable
app.app.config['SQLALCHEMY_DATABASE_URI']  = # you need to put your info here
db = flask_sqlalchemy.SQLAlchemy(app.app)

class Message(db.Model):
    id = # we need to put something here
    text = # we need to put something here
    
    def __init__(self, text):
        self.text = text
        
    def __repr__(self):
        return '<Message text: %s>' % self.text 
