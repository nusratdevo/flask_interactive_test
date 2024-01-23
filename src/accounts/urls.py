from flask import request, Blueprint

# from ..app import app
from .controllers import (
    list_all_books,
    create_book,
    retrieve_book,
    update_book,
    delete_book,
)

bookurl = Blueprint("bookurl", __name__, url_prefix="/")


@bookurl.route("/books", methods=["GET", "POST"])
def list_create_accounts():
    if request.method == "GET":
        return list_all_books()
    if request.method == "POST":
        return create_book()
    else:
        return "Method is Not Allowed"


@bookurl.route("/books/<book_id>", methods=["GET", "PUT", "DELETE"])
def retrieve_update_destroy_accounts(book_id):
    if request.method == "GET":
        return retrieve_book(book_id)
    if request.method == "PUT":
        return update_book(book_id)
    if request.method == "DELETE":
        return delete_book(book_id)
    else:
        return "Method is Not Allowed"
