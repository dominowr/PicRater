from extensions import db
from dataclasses import dataclass
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped


@dataclass
class Product(db.Model):
    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title: Mapped[str] = db.Column(db.String(200))
    image: Mapped[str] = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')