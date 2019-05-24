from flask_restful import Api
from flask import Blueprint
from app.links import resources

links_blueprint = Blueprint('links', __name__)

links_api = Api(links_blueprint)


links_api.add_resource(resources.Links, '/<string:hashed_url>', '/links/')

links_api.add_resource(resources.LinksAuthorized,
                       '/<string:hashed_url>', '/links/autorized')
