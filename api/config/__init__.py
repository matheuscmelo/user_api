from werkzeug.exceptions import default_exceptions, HTTPException
from flask import request, jsonify

def jsonify_app(app):
	def make_json_error(ex):
		response = jsonify(message=str(ex))
		response.status_code = ex.code if isinstance(ex, HTTPException) else 500
		return response
	for code in default_exceptions.keys():
		app.error_handler_spec[None][code] = make_json_error


def define_callbacks(app):

	@app.before_request
	def verify_json():
		if not request.method == 'GET' and not request.is_json:
			return jsonify({"message" : "Missing JSON in request"}), 400