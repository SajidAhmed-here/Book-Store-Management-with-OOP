class Book:
    def __init__(self, title, author, book_id, genre, price, quantity):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.genre = genre
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (f"Title: {self.title}, Author: {self.author}, ID: {self.book_id}, Genre: {self.genre}, Price: {self.price}, Quantity: {self.quantity}")

    @staticmethod
    def add_book(books):
        try:
            title = input("Enter book title: ")
            author = input("Enter author: ")
            book_id = input("Enter book ID: ")
            genre = input("Enter genre: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity in stock: "))
            
            if price < 0 or quantity < 0:
                raise ValueError("Price and quantity must be non-negative.")
            
            if book_id in books:
                print("Error: Book with this ID already exists.")
                return
            
            books[book_id] = Book(title, author, book_id, genre, price, quantity)
            print("Book added successfully.")
        except ValueError as e:
            print(f"Invalid input: {e}")

    @staticmethod
    def view_books(books):
        if not books:
            print("No books available.")
            return
        
        for book in books.values():
            print(book)

    @staticmethod
    def search_book(books):
        book_id = input("Enter book ID to search: ")
        book = books.get(book_id)
        if book:
            print(book)
        else:
            print("Book not found.")

    @staticmethod
    def remove_book(books):
        book_id = input("Enter book ID to remove: ")
        if book_id in books:
            del books[book_id]
            print("Book removed successfully.")
        else:
            print("Error: Book not found.")

def save_books_to_file(books, filename='books.txt'):
    with open(filename, 'w') as file:
        for book in books.values():
            file.write(f"{book.title},{book.author},{book.book_id},{book.genre},{book.price},{book.quantity}\n")

def load_books_from_file(filename='books.txt'):
    books = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                title, author, book_id, genre, price, quantity = line.strip().split(' ')
                books[book_id] = Book(title, author, book_id, genre, float(price), int(quantity))
    except FileNotFoundError:
        pass 
    return books




def main_menu(books):
    while True:
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            Book.add_book(books)
        elif choice == '2':
            Book.view_books(books)
        elif choice == '3':
            Book.search_book(books)
        elif choice == '4':
            Book.remove_book(books)
        elif choice == '5':
            save_books_to_file(books)
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    books = load_books_from_file()
    main_menu(books)
    save_books_to_file(books)

if __name__ == "__main__":
    main()