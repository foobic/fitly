from flask_restful import Resource, reqparse
from .models import UserModel, RevokedTokenModel
import flask_jwt_extended as flask_jwt

from app import jwt

parser = reqparse.RequestParser()
parser.add_argument(
    'username', help='This field cannot be blank', required=True)
parser.add_argument(
    'password', help='This field cannot be blank', required=True)


# support of token blacklisting
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        username = data['username']
        password = data['password']

        if UserModel.find_by_username(username):
            return {'message': f'User {username} already exists'}

        new_user = UserModel(
            username=username,
            password=UserModel.generate_hash(password)
        )

        try:
            new_user.save_to_db()
            access_token = flask_jwt.create_access_token(
                identity=username)
            refresh_token = flask_jwt.create_refresh_token(
                identity=username)
            return {
                'message': f'User {username} was created',
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except Exception:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        username = data['username']
        password = data['password']
        current_user = UserModel.find_by_username(username)

        if not current_user:
            return {'message': f'User {username} doesn\'t exist'}

        if UserModel.verify_hash(password, current_user.password):
            access_token = flask_jwt.create_access_token(
                identity=username)
            refresh_token = flask_jwt.create_refresh_token(
                identity=username)
            return {
                'message': f'Logged in as {current_user.username}',
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Wrong credentials'}


class UserLogoutAccess(Resource):
    @flask_jwt.jwt_required
    def post(self):
        jti = flask_jwt.get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except Exception:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @flask_jwt.jwt_refresh_token_required
    def post(self):
        jti = flask_jwt.get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except Exception:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @flask_jwt.jwt_refresh_token_required
    def post(self):
        current_user = flask_jwt.get_jwt_identity()
        access_token = flask_jwt.create_access_token(identity=current_user)
        return {'access_token': access_token}
