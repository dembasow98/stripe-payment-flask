#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request, jsonify, render_template

import stripe
# This is your test secret API key.
stripe.api_key = 'sk_test_51Nkj5GIOTMVAfupfHkwYxfPQ9CTIWo0QJyNJ25mMNdVKtRqCT4dj6jKqT6GLYsLGEdF9dMqow6kGvLsiu5BfnrR900i85VWeyq'

app = Flask(__name__, static_url_path='', static_folder='public')

YOUR_DOMAIN = 'http://localhost:4242'


@app.route('/')
def home():
    try:
        return render_template('checkout.html')
    except Exception as e:
        return str(e)

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1NlVloIOTMVAfupfyyouW9Dk',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
            automatic_tax={'enabled': True},
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    app.run(port=4242)