from flask import Blueprint, request, jsonify, g
from models import db
from auth import create_api_token, check_jwt_token
import models
import bcrypt



bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route('/login', methods=['POST'])
def login():
    content = request.form
    
    return "Logged In!"