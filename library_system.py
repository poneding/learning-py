# %%
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def find_book(self, title):
        find_books = [book for book in self.books if book.title == title]
        if find_books:
            print(f"Found: {', '.join(str(book) for book in find_books)}")
        else:
            print(f"No book found with title '{title}'.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)


library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.list_books()
library.find_book("1984")
library.remove_book("1984")
library.list_books()
library.find_book("1984")
library.add_book(Book("Brave New World", "Aldous Huxley"))
library.list_books()
library.remove_book("Nonexistent Book")
library.list_books()

# %%
