# Dieser Code extrahiert alle Artikeltitel von der Seite „New York Times“ und speichert sie
# in der Datei „title_articles.json“ (POST /fetch_titles).
# Beautiful Soup ist eine Python-Bibliothek zum Extrahieren von Daten aus HTML- und XML-Dateien.
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

import json

app = Flask(__name__)


ARTICLES_FILE_PATH = "title_articles.json"


def load_articles():
    try:
        with open(ARTICLES_FILE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_articles(articles):
    with open(ARTICLES_FILE_PATH, "w") as file:
        json.dump(articles, file, indent=4)


@app.route("/")
def home():
    return "Welcome !"


@app.route("/titel_articles", methods=["POST"])
def display_titels():
    url = "https://www.nytimes.com/"
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "html.parser")
    articles = load_articles()

    new_articles = []
    for story_heading in soup.find_all(class_="story-wrapper"):

        if story_heading.p:
            titel = story_heading.p.text.replace("\n", " ").strip()

        else:
            titel = None

        if titel:
            id_article = (
                max([a.get("id", 0) for a in articles], default=0) + 1
            )  # Générer un ID unique

            new_article = {"id": id_article, "titel": titel}
            articles.append(new_article)
            new_articles.append(new_article)
    save_articles(articles)

    if not new_articles:
        return jsonify({"message": "No article found!."}), 200

    return (
        jsonify(new_articles),
        201,
    )  # Retourne uniquement les nouveaux articles ajoutés


if __name__ == "__main__":
    app.run(debug=True, port=6060)
