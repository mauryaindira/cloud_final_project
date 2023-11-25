# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import sqlite3
#from requests import request
from flask import Flask,render_template, redirect, request #, send_mail
import os
from google.cloud import pubsub_v1

#Setting path pub/sub
os.environ["GCLOUD_PROJECT"] = "teak-formula-362813"
cred_path = "./resources//application_default_credentials.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = cred_path
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/', methods=['POST'])

def order_post():
    # if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    selected_items = request.form.getlist('order[]')

    # publisher code
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("teak-formula-362813", "M21AIE228_token1")
    # Data must be a bytestring
    data = "Hi " + name + ", your orders are: " + ", ".join(selected_items)
    print(selected_items)
    data = data.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())

    # Send order confirmation email
    confirmation_email = f"Thank you for your order, {name}! You have selected the following items: {selected_items}"
    #send_mail(name, "Order Confirmation", confirmation_email)

    # Save order to database
    # Connect to the database
    conn = sqlite3.connect('mysql_database.db')
    cursor = conn.cursor()

    #Create table for order
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')
    # Create a new order record
    cursor.execute("INSERT INTO orders (name, email) VALUES (?, ?)", (name, email))
    order_id = cursor.lastrowid
    
    # Create table for order_item
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        item TEXT,
        FOREIGN KEY (order_id) REFERENCES orders (id)
    )
''')

    # Insert each selected item into the order_items table
    for item in selected_items:
        cursor.execute("INSERT INTO order_items (order_id, item) VALUES (?, ?)", (order_id, item))

    # Commit the changes to the database
    conn.commit()
    conn.close()

    # Redirect to thank you page
    return render_template('thankyou.html')



@app.route('/', methods=['GET'])

def order_get():
    return render_template('order.html')
    
 
if __name__== "__main__":
    app.run(debug= True)





