from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None
        self.due_date = None

    def borrow(self, user, days=14):
        if self.is_borrowed:
            raise Exception(f"The book '{self.title}' is already borrowed.")
        self.is_borrowed = True
        self.borrowed_by = user
        self.due_date = datetime.now() + timedelta(days=days)
        user.borrowed_books.append(self)

    def return_book(self, user):
        if not self.is_borrowed or self.borrowed_by != user:
            raise Exception(f"The book '{self.title}' was not borrowed by this user.")
        self.is_borrowed = False
        self.borrowed_by = None
        self.due_date = None
        user.borrowed_books.remove(self)

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book, days=14):
        book.borrow(self, days)

    def return_book(self, book):
        book.return_book(self)

    def calculate_fines(self):
        fine = 0
        for book in self.borrowed_books:
            if book.due_date and datetime.now() > book.due_date:
                overdue_days = (datetime.now() - book.due_date).days
                fine += overdue_days
        return fine

    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id})"


class Librarian:
    def __init__(self, name):
        self.name = name

    def search_books(self, books, keyword):
        return [book for book in books if keyword.lower() in book.title.lower()]

    def calculate_fine(self, user):
        return user.calculate_fines()

    def __str__(self):
        return f"Librarian: {self.name}"


# Example usage
if __name__ == "__main__":
    # Create books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("1984", "George Orwell", "0987654321")
    book3 = Book("Python Programming", "John Zelle", "1122334455")

    # Create users
    user1 = User("Alice", "U001")
    user2 = User("Bob", "U002")

    # Create librarian
    librarian = Librarian("Mr. Smith")

    # Borrow books
    user1.borrow_book(book1)
    user1.borrow_book(book2)

    # Search books
    books = [book1, book2, book3]
    search_results = librarian.search_books(books, "Python")
    print("Search Results:", [str(book) for book in search_results])

    # Return a book
    user1.return_book(book1)

    # Calculate fines
    print(f"Fines for {user1.name}: ${librarian.calculate_fine(user1)}")