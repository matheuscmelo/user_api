from db import user_crud
from models import User

def test_create_user_basic():
	user_crud.create_user("ronaldo", "fenomeno123")
	user = user_crud.get_user_by_username("ronaldo")
	assert user == User("ronaldo", "fenomeno123")

def test_create_user_repeated_username():
	user_crud.create_user("ronaldo", "fenomeno123")
	user_crud.create_user("ronaldo", "fenomeno123")
	user = user_crud.get_user_by_id(2)
	assert user is None

def test_create_user_ids():
	user_crud.create_user("ronaldinho", "j0g4muit0")
	user1 = user_crud.get_user_by_id(1)
	user2 = user_crud.get_user_by_id(2)
	assert user1 == User("ronaldo", "fenomeno123")
	assert user2 == User("ronaldinho", "j0g4muit0")

def test_update_user():
	d = {}
	d["username"] = "ronaldo"
	d["password"] = "fenomeno"
	user_crud.update_user(d)
	user = user_crud.get_user_by_username("ronaldo")
	assert user.password == "fenomeno"

def test_get_all_users():
	users = user_crud.get_all_users()
	assert users == [User("ronaldo", "fenomeno"), User("ronaldinho", "j0g4muit0")]

def test_delete_user():
	user_crud.delete_user(2)
	assert user_crud.get_user_by_id(2) is None
	assert user_crud.get_all_users() == [User("ronaldo", "fenomeno")]