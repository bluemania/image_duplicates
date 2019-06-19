from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config.from_object('duplicates.config.base_config.BaseConfig')

	db = None

	return app, db

app = Flask(__name__)

app, db = create_app()

import duplicates.views
