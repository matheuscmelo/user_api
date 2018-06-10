from db import db
from models import User

""" User CRUD operations """

def create_user(username, password):
	""" 
	creates a user with specified username and password
	and returns a boolean indicating if it was created or not
	"""

	if User.query.filter_by(username=username).first() is None:
		user = User(username, password)
		db.session.add(user)
		db.session.commit()
		return True

	return False

def get_user_by_username(username):
	""" 
	queries a user by it's username
	returns a User object or None if it doesn't exists
	"""

	return User.query.filter_by(username=username).first()

def get_user_by_id(id):
	""" 
	queries a user by it's id
	returns a User object or None if it doesn't exists
	"""

	return User.query.get(id)

def get_all_users():
	"""
	returns a list with all users
	"""

	return User.query.all()

def update_user(username, user_data):
	"""
	updates a user with given user data
	"""

	user = get_user_by_username(username)

	if user:
		for attr in user_data.keys():
			if hasattr(user, attr):
				setattr(user, attr, user_data[attr])

	db.session.commit()

def delete_user(id):
	user = get_user_by_id(id)
	db.session.delete(user)
	db.sessions.commit()