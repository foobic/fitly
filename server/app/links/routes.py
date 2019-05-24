import json
from flask import Blueprint, jsonify
from flask import request, redirect
from .models import LinksModel
import flask_jwt_extended as flask_jwt

links_blueprint = Blueprint('links', __name__)


@links_blueprint.route('/links/authorized', methods=['POST'])
@flask_jwt.jwt_required
def create_link():
    try:
        data = json.loads(request.data)
        # ???????????????
        current_user = flask_jwt.get_jwt_identity()
        print("!!!USER", current_user)

        new_link = LinksModel(url=data['url'])
        if current_user:
            new_link.user_id = current_user.id

        new_link.save_to_db()
        return jsonify({
            "original_url": data['url'],
            "hashed_url": new_link.hashed_url
        }), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'Something went wrong during saving \
            new link to db'}), 500


@links_blueprint.route('/links/', methods=['POST'])
def create_link2():
    try:
        data = json.loads(request.data)

        new_link = LinksModel(url=data['url'])

        new_link.save_to_db()
        return jsonify({
            "original_url": data['url'],
            "hashed_url": new_link.hashed_url
        }), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'Something went wrong during saving \
            new link to db'}), 500


@links_blueprint.route('/l/<hashed_url>', methods=['GET'])
def get_original_url(hashed_url):
    try:
        link = LinksModel.find_by_hashed_url(hashed_url)
        link.increment_count_visited()
        return redirect(link.url, code=302)
    except Exception as e:
        print(e)
        return jsonify({'e': "Wrong link url"}), 500
