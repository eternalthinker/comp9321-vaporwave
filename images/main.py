from flask import Flask, redirect, render_template, request, url_for, jsonify, Response, make_response
from flask_restful import reqparse

app = Flask(__name__)
app.config["SECRET_KEY"] = "Very very secret key"


@app.route('/', methods=['GET','POST'])
def index():
				return "index page"


@app.route("/images", methods=['POST'])
def get_images():

	# List of slugs
	content = request.json




	return str(content)


if __name__ == "__main__":
    app.run(port = 6000)