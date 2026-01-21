from flask import Flask, render_template, request, session, jsonify

app = Flask(__name__)
app.secret_key = "edujoy"

products = [
    {"id": 1, "name": "WORLD MIX", "price": 180, "image": "worldmix.jpg"},
    {"id": 2, "name": "ROLE PLAY", "price": 150, "image": "roleplay.jpg"},
    {"id": 3, "name": "MY HOUSE", "price": 200, "image": "myhouse.jpg"},
    {"id": 4, "name": "PUZZLE", "price": 120, "image": "puzzle.jpg"}
]

def get_cart():
    return session.setdefault("cart", {})

@app.route("/")
def home():
    return render_template("home.html", cart=get_cart())

@app.route("/shop")
def shop():
    return render_template("index.html", products=products, cart=get_cart())

@app.route("/cart")
def cart_view():
    cart = get_cart()
    items = []
    total = 0
    for pid, qty in cart.items():
        product = next((p for p in products if p["id"] == int(pid)), None)
        if product:
            items.append({"product": product, "qty": qty})
            total += product["price"] * qty
    return render_template("cart.html", items=items, total=total, cart=cart)

@app.route("/contact")
def contact():
    return render_template("contact.html", cart=get_cart())

@app.post("/add")
def add():
    pid = str(request.form["id"])
    cart = get_cart()
    cart[pid] = cart.get(pid, 0) + 1
    session.modified = True
    return jsonify(sum(cart.values()))

@app.post("/minus")
def minus():
    pid = str(request.form["id"])
    cart = get_cart()
    if pid in cart:
        cart[pid] -= 1
        if cart[pid] <= 0:
            del cart[pid]
        session.modified = True
    return jsonify(sum(cart.values()))

@app.post("/clear")
def clear():
    session["cart"] = {}
    session.modified = True
    return jsonify(0)

if __name__ == "__main__":
    app.run(debug=True)
