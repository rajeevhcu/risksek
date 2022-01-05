from flask import (
    Blueprint, request
)
from flask_restful import Api, Resource
from ..common import log
from ..service.organization import get_org_list

bp = Blueprint('farm', __name__, url_prefix='/getOrganizations')
api = Api(bp)


class GitOrganization(Resource):
    def get(self):
        log.info(f"Entry into GitOrganization: GET")
        page_number = request.args.get('page_number')
        page_size = request.args.get('page_size')
        log.info(f"GitOrganization: GET: page_number: {page_number} | page_size: {page_size}")
        return get_org_list(page_number, page_size)

api.add_resource(GitOrganization,"/")