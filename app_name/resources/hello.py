from flask_restful import fields, marshal_with, abort, Resource, request, reqparse
import communities.resources.status_code as STATUS


# resource_fields = {
#     'field': fields.Integer, #FIELD DATA TYPE
# }


class communities(Resource):
    """
      * Rosource docstring
    """
    # parser = reqparse.RequestParser(bundle_errors=True)
    # parser.add_argument('field', required=True, help='help')

    @marshal_with(resource_fields)
    def get(self, community_id=None):
        return 'hello world!', STATUS.OK
