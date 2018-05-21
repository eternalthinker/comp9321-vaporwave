from flask import Flask

app = Flask(__name__)


@app.route('/episodes/<season_num>/<episode_num>/')
def get_episode():
				return 'Hello World!'


if __name__ == '__main__':
				app.run()