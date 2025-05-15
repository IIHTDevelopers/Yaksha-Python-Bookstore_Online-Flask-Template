from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Dummy data for use in endpoints
books_db = [
    {"id": 1, "title": "Flask for Beginners", "author": "John Doe"},
    {"id": 2, "title": "Advanced Python", "author": "Jane Smith"}
]

reviews_db = []

# Route to list all books or add a new one
@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        # TODO: Return the list of all books in JSON format
        pass
    elif request.method == 'POST':
        # TODO: Receive JSON data for a new book and add to books_db
        # TODO: Return the added book with status code 201
        pass

# Route to get a single book by ID using a route variable
@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    # TODO: Search for a book by ID in books_db
    # TODO: Return the book if found, else return 404 with 'Not Found'
    pass

# Route to search for books by title using query string
@app.route('/search')
def search():
    # TODO: Get the 'q' query parameter from request
    # TODO: Return books whose titles contain the keyword (case-insensitive)
    pass

# Route for login via form data
@app.route('/login', methods=['GET', 'POST'])
def login():
    VALID_USERNAME = "admin"
    VALID_PASSWORD = "secret"

    if request.method == 'POST':
        # TODO: Get 'username' and 'password' from submitted form
        # TODO: Check credentials and return 200 if valid, else return 401
        pass
    # TODO: Render the login form HTML
    pass

# Route to post a review using JSON
@app.route('/api/review', methods=['POST'])
def post_review():
    # TODO: Get review data from JSON body
    # TODO: Append review to reviews_db and return it with status code 201
    pass

# Home page displaying books using a template
@app.route('/')
def home():
    # TODO: Render home.html template and pass books_db to it
    pass

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
