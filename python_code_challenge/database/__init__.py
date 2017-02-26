from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = db
def create_all() :
    with app.app_context():
        db.create_all()

def drop_all() :
    with app.app_context():
        db.drop_all()