# Accept a Payment with Stripe Checkout

Stripe Checkout is the fastest way to get started with payments. 
Included are some basic build and run scripts you can use to start up the application.

## Running the sample

1. Build the server
set FLASK_APP=server.py


~~~
pip3 install -r requirements.txt
~~~

2. Run the server

~~~
export FLASK_APP=server.py
python3 -m flask run --port=4242
~~~

3. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)

4. TEST THE APP:
Payment succeeds

4242 4242 4242 4242
Payment requires authentication

4000 0025 0000 3155
Payment is declined

4000 0000 0000 9995