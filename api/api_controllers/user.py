from flask import request
from flask_restful import Resource, marshal_with
from db import user_crud
from models import User


class UserCRUDController(Resource):
	""" handles user Create, Read, Update and Delete operations """
	@marshal_with(User.api_fields)
	def get(self, id=None):
		if id:
			user = user_crud.get_user_by_id(id)
			if user:
				return user
			else:
				return user, 404
		else:
			return user_crud.get_all_users()

	@marshal_with(User.api_fields)
	def post(self):
		username = request.json.get('username', None)
		password = request.json.get('password', None)

		result, user = user_crud.create_user(username, password)
		if result:
			return user
		else:
			return None

	@marshal_with(User.api_fields)
	def put(self):
		data = request.json

		result, user = user_crud.update_user(data)

		return user