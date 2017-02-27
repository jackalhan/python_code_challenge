from flask_restplus import fields
from python_code_challenge.api.restplus import api

command_serializer = api.model('Command object', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a command'),
    'file_name' : fields.String(required=True, description='The file name stored by concatenating timestamp.'),
    'command_string': fields.String(required=True, description='The command as a string'),
    'length': fields.Integer(required=True, description='The length of command'),
    'duration': fields.Integer(required=True, description='The time to complete'),
    'output': fields.String(description='The output of the command')
})

file_serializer = api.model('File input object', {
    'filename': fields.String(readOnly=True, description='Filename of the commands text file to parse which exists on the server (Filename should be posted with the extension.)', required=True)
})

command_collection_serializer= api.model('Command Collections', {
    'commands': fields.List(fields.Nested(command_serializer))
})

