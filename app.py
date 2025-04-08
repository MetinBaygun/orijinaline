from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['GET'])
def verify_website():
    site_name = request.args.get('site')
    if not site_name:
        return render_template('index.html', official_website=None)

    # Google'da siteyi arama
    search_url = f"https://www.google.com/search?q={site_name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(search_url, headers=headers)

    # BeautifulSoup ile HTML parse etme
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all('a', href=True)

    # İlk doğru URL'yi bulma
    for link in result:
        if 'http' in link['href']:
            official_website = link['href']
            break
    else:
        official_website = None

    return render_template('index.html', official_website=official_website)

if __name__ == '__main__':
    app.run(debug=True)