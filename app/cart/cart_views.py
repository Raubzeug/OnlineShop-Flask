from flask import Blueprint, render_template

cart = Blueprint('cart', __name__, template_folder='templates')


@cart.route('/')
def cart_page():
    return render_template('cart.html')