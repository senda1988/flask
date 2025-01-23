# Code Beschreibung:
# Ich habe eine Funktion generation_psw erstellt, die ein Passwort generiert. Das Passwort muss mindestens einen Großbuchstaben, einen Kleinbuchstaben, ein Sonderzeichen und eine Zahl von 0 bis 9 enthalten.
# Ich habe eine Route /users/registration erstellt, über die wir einen Benutzer aus dem JSON-Body hinzufügen und das Passwort mithilfe der zuvor erstellten Funktion generation_psw generieren.
# Ich habe eine Funktion load_users() erstellt, die die Daten aus einer JSON-Datei lädt.
# users.json ist die JSON-Datei, in der wir die Benutzer speichern.
# Jede Änderung wird in der Datei users.json gespeichert.

from flask import Flask, request
from users_list import users
import json
import random
import string

app = Flask(__name__)
# Pfad zur Datei, in der die Benutzerdaten gespeichert werden
USERS_FILE_PATH = "users.json"


# Funktion zum Laden der Benutzerdaten aus der JSON-Datei
def load_users():
    try:
        with open(USERS_FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Wenn die Datei noch nicht existiert, gib eine leere Liste zurück
        return []


# Funktion zum Speichern der Benutzerdaten in die JSON-Datei
def save_users(users):
    with open(USERS_FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)


# Benutzerliste laden
users = load_users()


def generation_psw(len):
    num = string.digits
    sym = string.punctuation
    car = random.choice(string.ascii_letters)
    # car_upper= random.choice(string.ascii_uppercase)
    password = ""
    password_caracter = num + sym + car
    for _ in range(len):
        x = random.choice(password_caracter)
        password += x
    # for i in range(len):
    return password


@app.route("/")
def home():
    return "welcom!"


@app.route("/users/registration", methods=["Post"])
def registration():

    new_user = request.get_json()
    if (
        "username" not in new_user
        or "firstName" not in new_user
        or "familyName" not in new_user
    ):
        return "Parameters are missing", 400

    id_user = max([u["id"] for u in users], default=0) + 1
    new_user["id"] = id_user
    new_user["password"] = generation_psw(8)

    users.append(new_user)
    save_users(users)
    return new_user, 201


@app.route("/users/update_pwd/<int:id>", methods=["PUT"])
def update_pwd(id):
    new_user = request.get_json()

    if "password" not in new_user:
        return "Password field is missing", 400
    password = new_user["password"]
    # characters = string.ascii_letters + string.digits + string.punctuation
    # Überprüfen, ob das Passwort die Anforderungen erfüllt
    car_letter = any(c in string.ascii_letters for c in password)
    car_digit = any(c in string.digits for c in password)
    car_punctuation = any(c in string.punctuation for c in password)
    if not (car_letter and car_digit and car_punctuation):
        return (
            "password must contain at least one lowercase letter, one uppercase letter, one number and one symbol",
            400,
        )

    for u in users:
        if u["id"] == id:

            u["password"] = new_user["password"]
            save_users(users)
            return f"password updated successfully! {new_user}"
    return "Error!"


if __name__ == "__main__":
    app.run(debug=True, port=6060)
