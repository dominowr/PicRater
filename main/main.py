import requests
from flask import Flask, jsonify, abort
from config import Config
from extensions import db, migrate, cors
from models import Product, ProductUser
from producer import publish


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    return app


app = create_app()


@app.route('/api/products/')
def index():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:id>/like/', methods=['POST'])
def like(id):
    response = requests.get('http://docker.for.mac.localhost:8000/api/user/')
    json = response.json()

    try:
        product_user = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(product_user)
        db.session.commit()

        publish('product_liked', id)
    except:
        abort(400, 'You already like this product!')

    return jsonify({
        'message': 'success'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
