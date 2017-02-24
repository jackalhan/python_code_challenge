from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from python_code_challenge.database.models import Command
    db.drop_all()
    db.create_all()

