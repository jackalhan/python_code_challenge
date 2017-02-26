from python_code_challenge.database import db
from python_code_challenge.database.models import Command


def create_command(data):
    command_id = data.get('id')
    file_name = data.get('file_name')
    command_string = data.get('command_string')
    length = data.get('length')
    duration = data.get('duration')
    output = data.get('output')

    command = Command(file_name, command_string, length, duration, output)
    if command_id:
        command.id = command_id


    db.session.add(command)
    db.session.commit()


def update_command(command_id, data):
    command = Command.query.filter(Command.id == command_id).one()
    command.file_name = data.get('file_name')
    command.command_string = data.get('command_string')
    command.length = data.get('length')
    command.duration = data.get('duration')
    command.output = data.get('output')
    db.session.add(command)
    db.session.commit()


def delete_command(command_id):
    command = Command.query.filter(Command.id == command_id).one()
    db.session.delete(command)
    db.session.commit()
