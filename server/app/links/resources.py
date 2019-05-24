from flask_restful import Resource, reqparse
from .models import LinksModel
import flask_jwt_extended as flask_jwt
from flask import redirect

from app import jwt

parser = reqparse.RequestParser()
parser.add_argument(
    'url', help='This field cannot be blank', required=True)


class Links(Resource):
    def post(self):
        data = parser.parse_args()
        url = data["url"]

        new_link = LinksModel(url=url)

        try:
            new_link.save_to_db()
            return {
                "original_url": url,
                "hashed_url": new_link.hashed_url
            }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    def get(self, hashed_url):
        link = LinksModel.find_by_hashed_url(hashed_url)
        try:
            link.increment_count_visited()
            return redirect(link.url, code=302)
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class LinksAuthorized(Resource):
    @flask_jwt.jwt_required
    def post(self):
        data = parser.parse_args()
        url = data["url"]

        current_user = flask_jwt.get_jwt_identity()

        new_link = LinksModel(url=url)

        try:
            new_link.save_to_db()
            print('1111231231', current_user)
            return {
                "original_url": url,
                "hashed_url": new_link.hashed_url
            }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500
