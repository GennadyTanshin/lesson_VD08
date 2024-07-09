from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    quote, author = get_random_quote()
    return render_template('index.html', quote=quote, author=author)

@app.route('/quote')
def quote():
    quote, author = get_random_quote()
    return jsonify(quote=quote, author=author)

def get_random_quote():
    response = requests.get('https://api.quotable.io/random')
    data = response.json()
    return data['content'], data['author']

if __name__ == '__main__':
    app.run(debug=True)