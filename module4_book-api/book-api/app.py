"""
This is a CRUD API for managing books.

Author: Kristen Swaim
Course: SDEV 220 - Python APIs

Book Model:
    - id: auto-incremented integer
    - book_name: string
    - author: string
    - publisher: string

Endpoints:
    - GET /books Returns a list of all books
    - POST /books Adds a new book
    - PUT /books/<book_id> Updates a book by id
    - DELETE /books/<book_id> Deletes a book by id

"""

from flask import Flask, request, jsonify

app = Flask(__name__)

books = []

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    book = {
        "id": len(books) + 1,
        "book_name": request.json.get("book_name"),
        "author": request.json.get("author"),
        "publisher": request.json.get("publisher")
    }
    books.append(book)
    return jsonify(book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book["id"] == book_id:
            book.update(request.json)
            return jsonify(book)
    return {"error": "Book not found"}, 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return {"message": "Book deleted"}

if __name__ == '__main__':
    app.run(debug=True)
