from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "super_secret_hospitality_key"

# Dummy Data
HOTELS = [
    {
        "id": 1,
        "name": "The Grand Oasis",
        "description": "Luxurious 5-star hotel with breathtaking sea views.",
        "image": "https://picsum.photos/seed/hotel1/800/600",
        "rating": 4.9,
        "price_per_night": 250
    },
    {
        "id": 2,
        "name": "Urban Retreat",
        "description": "Modern rooms in the heart of the bustling city.",
        "image": "https://picsum.photos/seed/hotel2/800/600",
        "rating": 4.5,
        "price_per_night": 150
    },
    {
        "id": 3,
        "name": "Cozy Pine Resort",
        "description": "A peaceful getaway surrounded by nature and forests.",
        "image": "https://picsum.photos/seed/hotel3/800/600",
        "rating": 4.7,
        "price_per_night": 180
    }
]

RESTAURANTS = [
    {
        "id": 1,
        "name": "Spice Symphony",
        "cuisine": "Indian Fine Dining",
        "image": "https://picsum.photos/seed/resto1/800/600",
        "rating": 4.8,
        "menu": ["Butter Chicken", "Truffle Naan", "Saffron Biryani"]
    },
    {
        "id": 2,
        "name": "Oceanic Bites",
        "cuisine": "Seafood & Grill",
        "image": "https://picsum.photos/seed/resto2/800/600",
        "rating": 4.6,
        "menu": ["Grilled Salmon", "Lobster Bisque", "Oysters"]
    },
    {
        "id": 3,
        "name": "La Piazza",
        "cuisine": "Authentic Italian",
        "image": "https://picsum.photos/seed/resto3/800/600",
        "rating": 4.7,
        "menu": ["Wood-fired Margherita", "Penne Arrabbiata", "Tiramisu"]
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hotels")
def hotels():
    return render_template("hotels.html", hotels=HOTELS)

@app.route("/restaurants")
def restaurants():
    return render_template("restaurants.html", restaurants=RESTAURANTS)

@app.route("/booking", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        service = request.form.get("service")
        date = request.form.get("date")
        
        flash(f"Thank you, {name}! Your {service} booking for {date} has been confirmed.", "success")
        return redirect(url_for("booking"))
    
    return render_template("booking.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        flash(f"Thank you, {name}! We have received your message.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
