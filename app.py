# Comienzo del código de la aplicación generadora de chistes
# Código escrito por Fabián Hevia

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?lang=es"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

@app.route('/')
def index():
    joke = get_joke()
    return render_template('index.html', joke=joke)

if __name__ == '__main__':
    app.run(debug=True)