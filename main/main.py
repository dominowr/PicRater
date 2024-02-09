from flask import Flask
from config import Config
from extensions import db, migrate, cors


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    return app


app = create_app()


@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
