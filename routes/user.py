from flask import Blueprint, request, jsonify, g
from models import db
from auth import create_api_token, check_jwt_token
import models
import bcrypt



bp = Blueprint("user", __name__, url_prefix="/user")

@bp.route('/create', methods=['POST'])
def create():
    content = request.form
    
    return "Hello, User!"