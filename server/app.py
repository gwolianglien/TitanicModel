from flask import Flask
from api.titanic import titanic

def create_app(config_file):
    # Create Flask app object
    app = Flask(__name__)  

    # Store config file
    app.config.from_pyfile(config_file)

    # Import routes
    app.register_blueprint(titanic, url_prefix='/titanic')
    return app


if __name__ == '__main__':
    app = create_app('config.py')
    app.run()  # .run() activates the application
