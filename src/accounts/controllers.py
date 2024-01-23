from flask import abort, make_response, request, jsonify
import uuid
from src.constants.http_status_codes import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT,
)

from .. import db
from .models import Book


def list_all_books():
    books = Book.query.all()
    if books:
        return jsonify([book.to_json() for book in books])
    return jsonify({"message": "No Item Found"}), HTTP_404_NOT_FOUND


def create_book():
    if not request.json:
        abort(400)
    book = Book(
        id=str(uuid.uuid4()),
        title=request.json.get("title"),
        author=request.json.get("author"),
        isbn=request.json.get("isbn"),
    )
    db.session.add(book)
    db.session.commit()
    return jsonify(
        {"Book": book.to_json(), "message": "Book Created"}, HTTP_201_CREATED
    )
    # return make_response(jsonify({"message": "Book not found"}), 404)


def retrieve_book(book_id):
    book = Book.query.get_or_404(book_id)
    if not book:
        return jsonify({"message": "Item not found"}), HTTP_404_NOT_FOUND

    return (
        jsonify(book.to_json()),
        HTTP_200_OK,
    )


def update_book(book_id):
    if not request.json:
        abort(400)
    book = Book.query.get(book_id)
    if book is None:
        abort(404)
    book.title = request.json.get("title", book.title)
    book.author = request.json.get("author", book.author)
    book.isbn = request.json.get("isbn", book.isbn)
    db.session.commit()
    response = book.to_json()
    return jsonify(response), HTTP_200_OK


def delete_book(book_id):
    bookmark = Book.query.filter_by(id=book_id).first()
    if not bookmark:
        return jsonify({"message": "Item not found"}), HTTP_404_NOT_FOUND

    db.session.delete(bookmark)
    db.session.commit()

    # return jsonify({}), HTTP_204_NO_CONTENT
    return ('Item with Id "{}" deleted successfully!').format(book_id)
