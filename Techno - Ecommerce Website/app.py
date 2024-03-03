from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='techno_ecommerce'
)

@app.route('/')
def index():
    pages = [("Home", "index"), ("Products", "products"), ("About Us", "aboutUs"), ("Contact Us", "contactUs"), ("Account", "account"), ("Cart", "cart")]
    return render_template('index.html', pages=pages)

@app.route('/products')
def products():
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products')
    products_data = cursor.fetchall()
    cursor.close()

    return render_template('products.html', products=products_data)

@app.route('/aboutUs')
def aboutUs():
    # Your other page logic here
    return render_template('aboutUs.html')

@app.route('/contactUs')
def contactUs():
    # Your page 3 logic here
    return render_template('contactUs.html')

@app.route('/account')
def account():
    # Your page 3 logic here
    return render_template('account.html')

@app.route('/cart')
def cart():
    # Your page 3 logic here
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
