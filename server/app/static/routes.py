import os
import json
from flask import (Blueprint, jsonify,
                   request, render_template, url_for, send_from_directory)

static_folder = '../../../front/dist/'
static_blueprint = Blueprint('static', __name__, static_folder=static_folder)

static_file_dir = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), static_folder)


@static_blueprint.route('/')
def app():
    return send_from_directory(static_file_dir, 'index.html')


@static_blueprint.route('/<query>')
def app_routes(query):
    return send_from_directory(static_file_dir, 'index.html')


@static_blueprint.route('/<path:path>')
def static_proxy(path):
    """ static folder serve """
    file_name = path.split('/')[-1]
    dir_name = os.path.join(static_file_dir, '/'.join(path.split('/')[:-1]))
    return send_from_directory(dir_name, file_name)
