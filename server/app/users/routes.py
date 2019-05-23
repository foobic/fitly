from flask_restful import Api
from flask import Blueprint
from app.users import resources

users_blueprint = Blueprint('users', __name__)

users_api = Api(users_blueprint)


users_api.add_resource(resources.UserRegistration, '/')
users_api.add_resource(resources.UserLogin, '/login')
users_api.add_resource(resources.TokenRefresh, '/token/refresh')
users_api.add_resource(resources.UserLogoutAccess, '/logout/access')
users_api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
