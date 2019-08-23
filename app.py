import os
import sys
from config import app, db_file, db
from flask import render_template, make_response, redirect, flash, url_for
from models import Product


catalogue_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if catalogue_path not in sys.path:
    sys.path.append(catalogue_path)

if not os.path.exists(db_file):
    db.create_all()


@app.route("/")
@app.route("/products_list")
def products_list():
    """Renders the main page. products_list location is used
    for a redirect form a product_id that does not exists.
    """
    return render_template('products_list.html', products=Product.query.all())


@app.route("/product_info/<int:product_id>")
def product_info(product_id):
    """Renders a single-product page. Rises a flash message on the main page
    in case if there is no product with a given product_id.
    """
    product = Product.query.get(product_id)  # else @app.errorhandler(404)
    if product:
        return render_template(
            'product_info.html',
            product_id=product_id,
            product=product
        )
    else:
        flash('Product with ID %s was not found.' % product_id, 'danger')
        return redirect(url_for('products_list'))


@app.errorhandler(404)
def not_found(error):
    """Sets the code state to 404. You can also set extra headers here:
    response.headers['X-Something'] = '404 Not found'
    """
    response = make_response(render_template('error.html'), 404)
    return response


if __name__ == '__main__':
    app.run()
