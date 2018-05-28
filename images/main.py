from flask import Flask, redirect, render_template, request, url_for, jsonify, Response, make_response
from flask_restful import reqparse
from pathlib import Path

app = Flask(__name__)
app.config["SECRET_KEY"] = "Very very secret key"

port_number = 1337

@app.route("/images", methods=['POST'])
def get_images():

	# List of slugs
	content = request.json

	# Dictionary to return
	resources = {}

	for slug in content:
		path_string = "./static/" + slug + ".jpeg"
		print(path_string)

		file_name = Path(path_string)

		if file_name.is_file():
			resources[slug] = "http://localhost:" + str(port_number) + "/static/" + slug + ".jpeg"
		else:
			resources[slug] = None

	return jsonify(resources)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=port_number)