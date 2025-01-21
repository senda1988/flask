from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "welcome!"


@app.route("/brand/<int:id>")
def get_brand_id(id):
    type_brand = request.args.get("type")
    condition = request.args.get("condition")
    return f"Brand-ID: {id}, Type: {type_brand}, Condition: {condition}"


@app.route("/product/<int:product_id>")
def get_product(product_id):
    return f"Product-ID: {product_id}"


@app.route("/search")
def get_search():
    query = request.args.get("query")
    return f"Searching for: {query}"


if __name__ == "__main__":
    app.run(debug=True, port=6060)
