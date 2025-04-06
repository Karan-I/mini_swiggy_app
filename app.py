from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret123'

# Dummy menu data
menu = [
    {
        "id": 1,
        "name": "Chicken Lolipop",
        "price": 120,
        "image": "https://cdn.pixabay.com/photo/2021/07/02/05/09/pakoda-6380888_1280.jpg"
    },
    {
        "id": 2,
        "name": "Chicken Biryani",
        "price": 180,
        "image": "https://cdn.pixabay.com/photo/2023/06/27/15/16/rice-8092512_1280.jpg"
    },
    {
        "id": 3,
        "name": "Veg Pizza",
        "price": 100,
        "image": "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_960_720.jpg"
    },
    {
        "id": 4,
        "name": "Baby Corn Fried Rice",
        "price": 130,
        "image": "https://cdn.pixabay.com/photo/2021/05/31/01/10/fried-rice-6297406_1280.jpg"
    },
    {
        "id": 5,
        "name": "Gulab Jamun",
        "price": 40,
        "image": "https://cdn.pixabay.com/photo/2014/06/18/15/48/indian-sweet-371357_1280.jpg"
    },
    {
        "id": 6,
        "name": "Melon cocktail",
        "price": 90,
        "image": "https://cdn.pixabay.com/photo/2018/07/16/19/01/melon-cocktail-3542609_1280.jpg"
    },
    {
        "id": 7,
        "name": "Chicken Burger",
        "price": 70,
        "image": "https://cdn.pixabay.com/photo/2016/03/05/19/02/french-fries-1238247_960_720.jpg"
    }
]


@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/add_to_cart/<int:item_id>')
def add_to_cart(item_id):
    item = next((i for i in menu if i['id'] == item_id), None)
    if item:
        cart = session.get('cart', [])
        cart.append(item)
        session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/order')
def place_order():
    session.pop('cart', None)
    return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)
