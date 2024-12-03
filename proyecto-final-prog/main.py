from flask import Flask, render_template, request, redirect, url_for, session
import products 

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Clave secreta para sesiones

# Usuarios válidos
usuarios_validos = {
    'admin': 'admin',
    'yendry': 'mejia123'
}

# Rutas
@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', products=products.get_products())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        
        if username in usuarios_validos and usuarios_validos[username] == password:
            session['user'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Login fallido. Inténtalo de nuevo.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_products = [products.get_product_by_id(pid) for pid in session.get('cart', [])]
    return render_template('cart.html', cart_products=cart_products)

@app.route('/checkout')
def checkout():
    return "Compra realizada con éxito!"

if __name__ == '__main__':
    app.run(debug=True)
