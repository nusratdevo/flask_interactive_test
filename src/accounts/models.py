from sqlalchemy import inspect
from datetime import datetime

# from flask_validator import ValidateEmail, ValidateString, ValidateCountry
from sqlalchemy.orm import validates
from sqlalchemy.sql import expression

# from __init__.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

# ----------------------------------------------- #


# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Book(db.Model):
    __tablename__ = "books"
    # Auto Generated Fields:
    id = db.Column(db.String(100), primary_key=True, nullable=False, unique=True)
    isbn = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    published_year = db.Column(db.DateTime, default=datetime.utcnow)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated = db.Column(
        db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )

    def __repr__(self):
        return f"Book('{self.title}','{self.author}')"

    def to_json(self):
        return {
            "id": self.id,
            "author": self.author,
            "title": self.title,
            "published_year": self.published_year,
            "isbn": self.isbn,
            "created": self.created,
            "updated": self.updated,
        }

    # One to Many Relationship
    """The Account may own many Items, but the Item is owned by one Account!
class Account(db.Model):
     id = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
     .
     .
# Relations:
  items = db.relationship("Item", back_populates='account')
  
class Item(db.Model):
  id = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
     .
     .
# Relations:
  account_id = db.Column(db.String(100), db.ForeignKey("account.id"))
  account    = db.relationship("Account", back_populates="items")
    """
