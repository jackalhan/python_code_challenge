import logging

from flask_restplus import Resource
from python_code_challenge.api.restplus import api
from python_code_challenge.database import db

log = logging.getLogger(__name__)

ns = api.namespace('database', description='Database Operation')


@ns.route('/make_db')
class DatabaseMake(Resource):
    @api.response(200, 'Database successfully created.')
    def post(self):
        """
        Creates database schema
        ---
        tags: [db]
        responses:
          200:
            description: DB Creation OK
        """
        db.create_all()
        return 'Database successfully created.', 200

@ns.route('/drop_db')
class DatabaseMake(Resource):
    @api.response(200, 'Database successfully dropped.')
    def delete(self):
        """
          Drops all db tables
          ---
          tags: [db]
          responses:
            200:
              description: DB table drop OK
        """
        db.drop_all()
        return 'Database successfully dropped.', 200
