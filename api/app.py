from flask import Flask, make_response
from flask_restful import Api
from flask_cors import CORS
from api_controllers.login import LoginController
from api_controllers.user import UserCRUDController
from flask_jwt_extended import JWTManager
from db import db
import config

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
jwt = JWTManager(app)

db.init_app(app)
app.app_context().push()
db.create_all(app=app)

# config.jsonify_app(app)
config.define_callbacks(app)

app.config['JWT_SECRET_KEY'] = 'super-secret'

api.add_resource(LoginController, '/auth')
api.add_resource(UserCRUDController, '/users', '/users/<id>')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)
