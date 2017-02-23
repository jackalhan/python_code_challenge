from python_code_challenge.database import db
from python_code_challenge.database.models import Command

def create_command(data):
    command_id = data.get('id')
    command_string = data.get('command_string')
    length = data.get('length')
    duration = data.get('duration')
    output = data.get('output')

    command = Command(command_string, length, duration, output)
    if command_id:
        command.id = command_id

    db.session.add(command)
    db.session.commit()

def update_category(command_id, data):
    command = Command.query.filter(Command.id == category_id).one()
    category.name = data.get('name')
    db.session.add(category)
    db.session.commit()


def delete_category(category_id):
    category = Category.query.filter(Category.id == category_id).one()
    db.session.delete(category)
    db.session.commit()
