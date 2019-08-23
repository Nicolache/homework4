import os
from sqlalchemy.schema import UniqueConstraint
import sys

from config import db

catalogue_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if catalogue_path not in sys.path:
    sys.path.append(catalogue_path)



class ProductAttributes(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.id'), primary_key=True)
    value = db.Column(db.String(100))
    product = db.relationship("Product", back_populates="attributes")
    attribute = db.relationship("Attribute", back_populates="products")
    __table_args__ = (UniqueConstraint('product_id', 'attribute_id', name='_p2a_unique'),)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    shop_url = db.Column(db.String(200), nullable=False)  # ссылка на товар в магазине
    main_image_path = db.Column(db.String(200), nullable=False)  # изображение товара
    __table_args__ = (UniqueConstraint('name', 'shop_url', name='_prod_unique'),)
    attributes = db.relationship("ProductAttributes", back_populates="product")

    def __repr__(self):
        return '<%s %s>' % (self.__class__, self.name)

    def __str__(self):
        return '%s %r' % (self.__class__, self.name)


class Attribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    products = db.relationship("ProductAttributes", back_populates="attribute")

    def __repr__(self):
        return '<%s %s>' % (self.__class__, self.name)

    def __str__(self):
        return '%s %r' % (self.__class__, self.name)


if __name__ == '__main__':
    pass
