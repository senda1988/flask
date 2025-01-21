from flask import Flask, request
from users import users

app = Flask(__name__)


@app.route("/")
def home():
    return "welcome!"


@app.route("/user/<int:id>")
def get_user(id):
    for user in users:
        if user["id"] == id:
            user_final = user
            return f"Nutzerdetails => {user_final}"

    return "User not found!"


@app.route("/login/<int:id>")
def get_login(id):

    for user in users:
        if user["id"] == id:
            return f"User {user['name']} successfully logged in!"
    return f"ID {id} does not exist !"


@app.route("/search")
def get_search():
    name = request.args.get("name")
    for user in users:
        # print("AAA")
        if user["name"].lower() == name.lower():
            return f"Found user: {user['name']}"

    return f"No user found with name:{name}"


if __name__ == "__main__":
    app.run(debug=True, port=6060)
