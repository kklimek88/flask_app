from flask import Flask, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/price')
def get_price():
    url = "https://www.bergfreunde.eu/la-sportiva-otaki-climbing-shoes/"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_spans = soup.find_all('span', class_='js-fprice')

    if price_spans and price_spans[-1].span:
        price = price_spans[-1].span.get_text(strip=True)
        return jsonify({'price': price})

    return jsonify({'error': 'Price not found'}), 404

if __name__ == "__main__":
    app.run(debug=True)
