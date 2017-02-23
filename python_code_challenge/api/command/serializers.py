from flask_restplus import fields
from python_code_challenge.api.restplus import api

commands = api.model('Command', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a command'),
    'command_string': fields.String(required=True, description='Command as a string'),
    'length': fields.Integer(required=True, description='Length of command'),
    'duration': fields.Integer(required=True, description='Time to complete'),
    'output': fields.Integer(description='Time to complete')
})
