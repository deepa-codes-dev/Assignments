#library management system with feature of add,remove books from the library,searchfor books by title or author, and display list of all available books 
class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        name=input("Enter the name of the book: ")
        author=input("Enter the author of the book: ")
        id=input("Enter the ID of the book: ")
        book={"name":name,"author":author,"id":id}
        self.books.append(book)
        print("Book added successfully!")

    def remove_book(self):
        book_id=input("Enter the ID of the book to remove: ")
        for book in self.books:
            if book["id"]==book_id:
                self.books.remove(book)
                print("Book removed successfully!")
                return
        print("Book not found!")


    def search_book(self):
        book_id=input("Enter the ID of the book to search: ")
        book_author=input("Enter the author of the book to search: ")
        for book in self.books:
            if book["id"]==book_id and book["author"]==book_author:
                print("Book found!")
                print(f"Name: {book['name']}, Author: {book['author']}, ID: {book['id']}")
                return 
            print("Book not found!")

    def display_books(self):
        if len(self.books)==0:
            print("No books available!")
        else:
            print("List of available books:")
            for book in self.books:
                print(f"Name: {book['name']}, Author: {book['author']}, ID: {book['id']}")
s1=Library()
while True:
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Exit")

    choice=input("Enter your choice: ")

    if choice=="1":s1.add_book()
    elif choice=="2":s1.remove_book()
    elif choice=="3":s1.search_book()
    elif choice=="4":s1.display_books()
    elif choice=="5":break
    else:
        print("Invalid choice!")