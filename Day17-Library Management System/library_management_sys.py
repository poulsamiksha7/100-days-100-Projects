class Book():
    def __init__(self,title,author,isbn,available):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=available
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library():
    def __init__(self,name,list_of_books):
        self.name=name
        self.list_of_books=list_of_books
            
    def add_book(self,book):
        self.list_of_books.append(book)
        return self.list_of_books
    def return_book(self ,isbn):
        for book in self.list_of_books:
            if book.isbn==isbn:
                book.available=True
                return True
        return False
            
    def list_available(self):
        available_books = []
        for lists in self.list_of_books:
            if lists.available == True:
                available_books.append(lists)
        return available_books

    def search_by_title(self,title):
        for book in self.list_of_books:
            if book.title == title:
                return book
        return None
    def borrow_book(self,isbn):
        for book in self.list_of_books:
            if book.isbn==isbn:
                book.available = False
                return True
        return False

    def total_books(self):
        return len(self.list_of_books)
b1 = Book("Atomic Habits", "James Clear", 101, True)
library = Library("City Library", [])
library.add_book(b1)
print(library.total_books())
print(library.list_available())
print(library.borrow_book(101))

