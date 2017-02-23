from flask_restplus import fields
from python_code_challenge.api.restplus import api

commands = api.model('Command', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a command'),
    'file_name' : fields.String(required=True, description='The file name stored by concatenating timestamp.'),
    'command_string': fields.String(required=True, description='The command as a string'),
    'length': fields.Integer(required=True, description='The length of command'),
    'duration': fields.Integer(required=True, description='The time to complete'),
    'output': fields.Integer(description='Time to complete')
})
