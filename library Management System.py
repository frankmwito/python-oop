# Library Management System

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        
    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []  # Store all book objects in a list
        
    def add_book(self):
        num_of_books = int(input("Enter the number of books to add: "))
        for i in range(num_of_books):
            print(f"\nAdding book {i + 1}")
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            year = int(input("Enter the year of the book: "))
            isbn = int(input("Enter the ISBN of the book: "))
            self.books.append(Book(title, author, year, isbn))  # Create a new Book and add to the list
        
        print("\nBooks added successfully!\n")
    
    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library")
                return
        print(f"Book '{title}' not found in the library")
    
    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks currently in the library:")
            for book in self.books:
                print(book.get_details())  # Use the get_details method to display book info


# Sample testing
library = Library()

# Adding books
library.add_book()

# Display books in the library
library.display_books()

# Removing a book
library.remove_book()

# Display books after removing
library.display_books()

        
        
    
    
