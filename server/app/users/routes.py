from flask import Blueprint, request, jsonify
from .models import UsersModel, RevokedTokenModel
from app import jwt
import flask_jwt_extended as flask_jwt
import json

users_blueprint = Blueprint('users', __name__)

# support of token blacklisting
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


@users_blueprint.route('/', methods=['POST'])
def create_user():
    try:
        data = json.loads(request.data)

        username = data['username']
        password = data['password']

        if UsersModel.find_by_username(username):
            return jsonify({'message': f'User {username} already exists'}), 500

        new_user = UsersModel(
            username=username,
            password=UsersModel.generate_hash(password)
        )
        new_user.save_to_db()
        access_token = flask_jwt.create_access_token(
            identity={"id": new_user.id, "username": new_user.username})
        refresh_token = flask_jwt.create_refresh_token(
            identity={"id": new_user.id, "username": new_user.username})

        return jsonify({
            'message': f'User {username} was created',
            'access_token': access_token,
            'refresh_token': refresh_token
        }), 200
    except Exception as e:
        return jsonify({'message': 'Something went wrong during saving \
            new user to db'}), 500


@users_blueprint.route('/login', methods=['POST'])
def login():
    try:
        data = json.loads(request.data)
        username = data['username']
        password = data['password']
        current_user = UsersModel.find_by_username(username)

        if not current_user:
            return jsonify({'message': f'User {username} doesn\'t exist'}), 400

        if UsersModel.verify_hash(password, current_user.password):
            access_token = flask_jwt.create_access_token(
                identity={"id": current_user.id,
                          "username": current_user.username})
            refresh_token = flask_jwt.create_refresh_token(
                identity={"id": current_user.id,
                          "username": current_user.username})
            return jsonify({
                'message': f'Logged in as {current_user.username}',
                'access_token': access_token,
                'refresh_token': refresh_token
            }), 200
        else:
            return jsonify({'message': 'Wrong credentials'}), 400
    except Exception as e:
        return jsonify({'message': 'Something went wrong during login'}), 500


@users_blueprint.route('/logout/access', methods=['POST'])
@flask_jwt.jwt_required
def logout_access():
    jti = flask_jwt.get_raw_jwt()['jti']
    try:
        revoked_token = RevokedTokenModel(jti=jti)
        revoked_token.add()
        return jsonify({'message': 'Access token has been revoked'}), 200
    except Exception as e:
        return jsonify({'message': 'Something went wrong'}), 500


@users_blueprint.route('/logout/refresh', methods=['POST'])
@flask_jwt.jwt_refresh_token_required
def logout_refresh():
    jti = flask_jwt.get_raw_jwt()['jti']
    try:
        revoked_token = RevokedTokenModel(jti=jti)
        revoked_token.add()
        return jsonify({'message': 'Refresh token has been revoked'}), 200
    except Exception as e:
        return jsonify({'message': 'Something went wrong'}), 500


@users_blueprint.route('/token/refresh', methods=['POST'])
@flask_jwt.jwt_refresh_token_required
def token_refresh():
    current_user = flask_jwt.get_jwt_identity()
    access_token = flask_jwt.create_access_token(
        identity={"id": current_user['id'],
                  "username": current_user['username']})
    return jsonify({'access_token': access_token}), 200
