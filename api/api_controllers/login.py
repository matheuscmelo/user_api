from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from models import User
from db import user_crud
class LoginController(Resource):
	""" controls the JWT token business logic """

	def post(self):
		"""
		returns the JWT access token if username and password match to a
		registered user, or errors if don't
		"""

		username = request.json.get('username', None)
		password = request.json.get('password', None)

		if not username or not password:
			return {"message" : "Missing username or password parameter", "access_token" : None }, 400

		user = user_crud.get_user_by_username(username)

		if not user:
			return {"message" : "User not found", "access_token" : None}, 404


		if username != user.username or password != user.password:
			return {"message" : "Bad username or password", "access_token" : None}, 401

		access_token = create_access_token(identity=username)

		return {"message": "User authenticated successfully" ,"access_token" : access_token}