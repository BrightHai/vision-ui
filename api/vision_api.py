from flask import jsonify
from flask import request
from flask import Blueprint
from utils.image_diff import ImageDiff
from utils.image_merge import Stitcher
from utils.image_similar import HashSimilar
from utils.image_text import get_text_roi
from utils.image_utils import get_pop_v

vision = Blueprint('vision', __name__, url_prefix='/vision')


@vision.route('/diff', methods=["POST"])
def vision_diff():
    data = {
        "code": 0,
        "data": ImageDiff().get_image_score(request.json['image1'], request.json['image2'],
                                            request.json['image_diff_name'])
    }
    return jsonify(data)


@vision.route('/merge', methods=["POST"])
def vision_merge():
    data = {
        "code": 0,
        "data": Stitcher(request.json['image_list']).image_merge(request.json['name'])
    }
    return jsonify(data)


@vision.route('/similar', methods=["POST"])
def vision_similar():
    data = {
        "code": 0,
        "data": HashSimilar().get_hash_similar(request.json['image1'], request.json['image2'])
    }
    return jsonify(data)


@vision.route('/pop', methods=["POST"])
def vision_pop():
    data = {
        "code": 0,
        "data": get_pop_v(request.json['image'])
    }
    return jsonify(data)


@vision.route('/text', methods=["POST"])
def vision_text():
    data = {
        "code": 0,
        "data": get_text_roi(request.json['image'])
    }
    return jsonify(data)
