from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db, User, Movie, Review, Genre, MovieGenre
from watcher import watcher_bp
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'You will never walk Alone'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)

# Register the blueprint
app.register_blueprint(watcher_bp, url_prefix='/api')

@app.route("/")
def index():
    return "<h1>PROJECT</h1>"

if __name__ == "__main__":
    app.run(port=5555, debug=True)
