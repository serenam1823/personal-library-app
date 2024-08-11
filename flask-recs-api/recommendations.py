from flask import Flask

app = Flask(__name__)

@app.route('/api/recs')
def get_book_recs():
    return {"books": ['book1', 'book2', 'book3']}