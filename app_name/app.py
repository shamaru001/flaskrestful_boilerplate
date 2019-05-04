from flask import Flask, jsonify, request
from .database import db
from flask_restful import Api, abort
from app.resources.hello import hello
from .settings import DATABASE_URLS, DB_ENGINE, DEBUG, APP_NAME
import app.resources.status_code as HTTP
from flask_migrate import Migrate

app = Flask(APP_NAME)
api = Api(app)

if DEBUG:
    app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URLS[DB_ENGINE]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

app.url_map.strict_slashes = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True


@app.route('/favicon.ico')
def favicon():
        # return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
    abort(HTTP.NOT_FOUND)


api.add_resource(hello, '/')

# Init Database Configutation
db.init_app(app)
if __name__ == '__main__':
    app.run()
