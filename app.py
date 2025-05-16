from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

books_db = []
reviews_db = []

# Route: GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify([]), 500  # Intentionally fail

# Route: POST a new book
@app.route('/books', methods=['POST'])
def add_book():
    return jsonify({}), 400  # Intentionally fail

# Route: GET a book by ID
@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    return jsonify({}), 404  # Intentionally fail

# Route: login (GET and POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Unauthorized", 401
    return render_template("login.html")

# Route: POST a review
@app.route('/api/reviews', methods=['POST'])
def post_review():
    return jsonify({}), 400  # Intentionally fail

# Route: GET reviews
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    return jsonify([]), 500  # Intentionally fail

# Home page
@app.route('/')
def home():
    return "", 500

if __name__ == '__main__':
    app.run(debug=True)
