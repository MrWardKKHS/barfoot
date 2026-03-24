from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_articles():
    articles = [
        {
            'link_href': 'market-update',
            'img_src': 'images/image1.jpg',
            'img_alt': 'View over Auckland harbour and suburbs',
            'title': 'Latest Housing Market Update',
            'summary': 'Low Auckland house prices attract strong sales activity.',
            'link_text': "Read February's housing market update"
        },
        {
            'link_href': 'febuary-2026-rental-report',
            'img_src': 'images/image2.jpg',
            'img_alt': 'Front entrance of a modern house',
            'title': 'Latest Monthly Rental Update',
            'summary': 'Rental demand rises for third consecutive month.',
            'link_text': "Read February's monthly rental report"
        },
        {
            'link_href': 'big-things',
            'img_src': 'images/image3.jpg',
            'img_alt': 'Real estate agent shaking hands with a client in front of a sold house',
            'title': 'Do Big Things',
            'summary': "Like sell your place and chase your dreams. Whatever your next big thing is, we'll help make it happen.",
            'link_text': 'Do big things with us'
        },
        {
            'link_href': 'community',
            'img_src': 'images/image4.jpg',
            'img_alt': 'Football team celebrating on a field',
            'title': 'Supporting our community',
            'summary': 'We love being a part of what makes Auckland, Northland and the Bay of Plenty a great place to live.',
            'link_text': 'See how we support our community'
        }
    ]
    return articles

@app.route('/')
def index():
    articles = get_articles()
    return render_template('index.html', articles=articles)

@app.route('/market-update')
def market():
    return render_template('market.html')

if __name__ == "__main__":
    app.run(debug=True)