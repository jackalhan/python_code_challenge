import logging

from flask import request
from flask_restplus import Resource
from python_code_challenge.api.command.business import create_command, delete_command, update_command
from python_code_challenge.api.command.serializers import command
from python_code_challenge.api.restplus import api
from python_code_challenge.database.models import Command

log = logging.getLogger(__name__)

ns = api.namespace('command/commands', description='Command Operations')


@ns.route('/')
class CommandCollection(Resource):
    @api.marshal_list_with(command)
    def get(self):
        """
        Returns list of commands.
        """
        commands = Command.query.all()
        return commands

    @api.response(201, 'Command successfully created.')
    @api.expect(command)
    def post(self):
        """
        Creates a new category.
        """
        data = request.json
        create_command(data)
        return None, 201

#
# @ns.route('/<int:id>')
# @api.response(404, 'Category not found.')
# class CommandItem(Resource):
#     @api.marshal_with(category_with_posts)
#     def get(self, id):
#         """
#         Returns a category with a list of posts.
#         """
#         return Category.query.filter(Category.id == id).one()
#
#     @api.expect(category)
#     @api.response(204, 'Category successfully updated.')
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
#         update_category(id, data)
#         return None, 204
#
#     @api.response(204, 'Category successfully deleted.')
#     def delete(self, id):
#         """
#         Deletes blog category.
#         """
#         delete_category(id)
#         return None, 204
