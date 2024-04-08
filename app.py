from flask import Flask

from routes.about import about_blueprint
from routes.home import home_blueprint

app = Flask(__name__)

app.register_blueprint(home_blueprint)
app.register_blueprint(about_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
