#Aggregation - represents a relationship where on object (the whole)
#              contains references to one or more INDEPENDENT objects ( the parts )

# the parts can extist independently of the parent classes as well
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []  # Aggregation: Library "has" a list of Book objects

    def addBook(self, book):
        self.books.append(book)

    def listBooks(self):
        for book in self.books:
            print(book)

book1 = Book("Half Girlfriend","Chetan Bhagat")
book2 = Book("RichDad PoorDad","Someone")

library = Library()
library.addBook(book1)
library.addBook(book2)

library.listBooks()