import logging

from flask import json
from flask_restplus import Resource

from python_code_challenge.api.command.business import create_command, delete_command, update_command
from python_code_challenge.api.command.parsers import pagination_arguments
from python_code_challenge.api.command.serializers import command_serializer, command_collection_serializer
from python_code_challenge.api.restplus import api
from python_code_challenge.database.models import Command

log = logging.getLogger(__name__)

ns = api.namespace('/', description='Command Operations')

"""
@ns.route('/')
class CommandItem(Resource):

    @api.response(200, 'Command successfully created.')
    @api.expect(command_serializer)
    def post(self):


        Create command in database
        ---
        tags: [commands]
        parameters:

        responses:
          200:
            description: Processing OK
          409:
            description: Record is already exists

        data = request.json
        try:
            create_command(data)
            code = 200
            description = 'Command successfully created.'
        except IntegrityError as ex:
            code = 409
            description = 'Command is already exist in database with the following fields : [File Name = ' + data.get('file_name') + ', Command = ' + data.get('command_string') + ']'
        return description, code
"""
@ns.route('/get_command_output')
@api.response(400, 'Commands not found.')
class CommandCollection(Resource):

    @api.marshal_with(command_collection_serializer)
    def get(self):
        """
        Returns as json the all stored commands that have been processed
        ---
        tags: [commands]
        responses:
          200:
            description: Commands returned OK
          400:
            description: Commands not found
        """
        command_list = Command.query.all()

        #id = command_list['id']
       # if not id :
       #     return 400
       # else :
        return json.dumps(command_list)

#
# @ns.route('/<int:id>')
# @api.response(404, 'Command not found.')
# class CommandItem(Resource):
#     @api.marshal_with(command_serializer)
#     def get(self, id):
#         """
#         Returns a category with a list of posts.
#         """
#         return Command.query.filter(Command.id == id).one()
#
#     @api.expect(command_serializer)
#     @api.response(204, 'Command successfully updated.')
#     def put(self, id):
#         """
#         Updates a blog category.
#
#         Use this method to change the name of a blog category.
#
#         * Send a JSON object with the new name in the request body.
#
#         ```
#         {
#           "name": "New Category Name"
#         }
#         ```
#
#         * Specify the ID of the category to modify in the request URL path.
#         """
#         data = request.json
#         update_command(id, data)
#         return None, 204
#
#     @api.response(204, 'Command successfully deleted.')
#     def delete(self, id):
#         """
#         Deletes blog category.
#         """
#         delete_command(id)
#         return None, 204
