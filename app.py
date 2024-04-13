from flask import Flask
from dotenv import load_dotenv
import os

from routes.about import about_blueprint
from routes.home import home_blueprint

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv('MONGO_URI')

app.register_blueprint(home_blueprint)
app.register_blueprint(about_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
