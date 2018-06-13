from db import db
from flask_restful import fields

class User(db.Model):
	""" defines a user """

	api_fields = {
					"id" : fields.Integer,
					"username" : fields.String
	}

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return 'User %r' % self.username

	def __eq__(self, other):
		return other.username == self.username and other.password == self.password