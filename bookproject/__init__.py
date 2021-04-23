from flask import Flask
from bookproject import views
from .views import bp
from .extensions import mongo

def create_app(config_object="bookproject.settings"):
    app = Flask(__name__)

    app.config.from_object(config_object)
    
    mongo.init_app(app)
    
    app.register_blueprint(bp)
    return app


if __name__ == "__main__":
    app.run(debug=True)