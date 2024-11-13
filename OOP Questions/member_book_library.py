"""
Question:
    Design a simple library management system in Python using object-oriented programming. The system should have the following features:

Classes:
    Book: Represents a book with attributes like title, author, and isbn.
    Member: Represents a library member with attributes like name, member_id, and a list of borrowed books.
    Library: Manages the collection of books and members and handles borrowing and returning books.

Methods:
    Library.add_book(book): Adds a new book to the library.
    Library.add_member(member): Registers a new member to the library.
    Library.borrow_book(member_id, isbn): Allows a member to borrow a book if it's available.
    Library.return_book(member_id, isbn): Allows a member to return a borrowed book.

Requirements:
    A book can only be borrowed if it is currently available in the library.
    Each member can only borrow up to a certain number of books (e.g., 3 books at a time).
    Ensure proper error handling if a book is not available or if a member tries to borrow more than the allowed limit.
"""


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.id = member_id
        self.books = {}

    def remove_book(self, isbn):
        returned = self.books[isbn]
        del self.books[isbn]
        return returned


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book
        print(f'Book {book.id} has been added to the library.')

    def get_book(self, isbn):
        checkout = self.books[isbn]
        del(self.books[isbn])
        return checkout

    def add_member(self, member):
        self.members[member.id] = member
        print(f'Member {member.name} with id of {member.id}, has been added.')

    def is_available(self, isbn):
        if isbn in self.books:
            print(f"Book {isbn} is in stock.")
            return isbn in self.books
        print(f"Book {isbn} is not currently available.")

    def borrow_book(self, member_id, isbn):
        if self.is_available(isbn) and len(self.members[member_id].books) < 3:
            book = self.get_book(isbn)
            self.members[member_id].books[book.isbn] = book
        else:
            print(f'Either book {isbn} is not available or member {member_id} is at borrow capacity.')

    def return_book(self, member_id, isbn):
        book = self.members[member_id].remove_book(isbn)
        self.books[book.isbn] = book
        print(f'Book {isbn} has been returned to library')