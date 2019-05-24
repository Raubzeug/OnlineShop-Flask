from flask import render_template, flash, redirect, url_for, session, request, make_response
from app.forms import LoginForm, AddToCart
from app.products import Product
from werkzeug.exceptions import NotFound
from app import errors
from app.cart.cart_views import cart


from app import app
app.register_blueprint(cart, url_prefix='/cart/')

product1 = Product('product1', 7000, ['the best ever'])
product2 = Product('product2', 9000, ['the better then the best'])
products = [product1, product2]


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/products', methods=['GET', 'POST'])
def index_page():
    user = {'username': 'Elena'}
    return render_template('index.html', user=user, products=products)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index_page'))
    return render_template('login.html', title='Sign in', form=form)


@app.route('/products/<productid>/', methods=['GET', 'POST'])
def product_page(productid=None):
    if productid is not None:
        for product in products:
            if product.id == int(productid):
                form = AddToCart()
                if form.validate_on_submit():
                    flash('You added {0} items of {1} to cart'.format(form.quantity.data, product.name))
                return render_template('products_base.html', title='Product page', product=product, form=form)
        raise NotFound




