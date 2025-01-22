from flask import Flask, request, jsonify

app = Flask(__name__)

# In-Memory "Datenbank"
products = []


# POST - Ein neues Produkt hinzufügen
@app.route("/products", methods=["POST"])
def create_product():
    new_product = request.get_json()
    if not new_product or "name" not in new_product or "price" not in new_product:
        return jsonify({"error": "Invalid input"}), 400

    new_product["id"] = max([p["id"] for p in products], default=0) + 1
    products.append(new_product)
    return jsonify(new_product), 201


# GET - Alle Produkte abrufen
@app.route("/products", methods=["GET"])
def get_products():
    name_filter = request.args.get("name")
    if name_filter:
        filtered_products = [
            p for p in products if name_filter.lower() in p["name"].lower()
        ]
        return jsonify(filtered_products), 200
    return jsonify(products), 200


@app.route("/products/<int:id>", methods=["GET"])
def get_products_id(id):
    final_product = None
    for p in products:
        if p["id"] == id:
            final_product = p

    if final_product == None:
        return "User could not be found "

    return f"The Product is {final_product}"


if __name__ == "__main__":
    app.run(debug=True)
