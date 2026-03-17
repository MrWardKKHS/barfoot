from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_articles():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row

    articles = conn.execute("""
        SELECT *
        FROM articles
        LIMIT 4
    """).fetchall()

    return articles

@app.route('/')
def index():
    articles = get_articles()
    return render_template('index.html', articles=articles)

if __name__ == "__main__":
    app.run(debug=True)