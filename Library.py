# ========================= # ENTITY CLASSES # ========================= 
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)
        print("BOOK ADDED SUCCESSFULLY.")

    def add_member(self, member_id, name):
        member = Member(member_id, name)
        self.members.append(member)
        print("MEMBER ADDED SUCCESSFULLY.")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, book_id, member_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if member is None:
            print("MEMBER NOT FOUND!")
            return
        if book is None:
            print("BOOK NOT FOUND!")
            return
        if not book.available:
            print("BOOK ALREADY BORROWED.")
            return
            
        book.available = False  # FIXED: Changed from True to False
        member.borrowed_books.append(book)
        print("BOOK BORROWED SUCCESSFULLY.")

    def return_book(self, book_id, member_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if member is None:
            print("MEMBER NOT FOUND!")
            return
        if book is None:
            print("BOOK NOT FOUND!")
            return
        if book not in member.borrowed_books:
            print("MEMBER DIDNT BORROW THIS BOOK.")
            return
            
        member.borrowed_books.remove(book)
        book.available = True
        print("BOOK RETURNED SUCCESSFULLY.")

# ========================= # EXECUTION INTERFACE # ========================= 
library = Library()

while True:
    print("\n---------- LIBRARY MANAGEMENT SYSTEM ----------")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    
    try:
        choice = int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("Invalid Choice! Please enter a number.")
        continue
        
    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        library.add_book(book_id, title, author)
        
    elif choice == 2:
        member_id = int(input("Enter Member ID: "))
        name = input("Enter Member Name: ")
        library.add_member(member_id, name)
        
    elif choice == 3:
        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))
        # FIXED: Passed variables in correct order matching method definition (book_id, member_id)
        library.borrow_book(book_id, member_id)
        
    elif choice == 4:
        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))
        # FIXED: Passed variables in correct order matching method definition (book_id, member_id)
        library.return_book(book_id, member_id)
        
    elif choice == 5:
        print("Thank You!")
        break
    else:
        print("Invalid Choice")
