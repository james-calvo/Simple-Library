class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Library Books:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. Title: {book.title}, Author: {book.author}, Genre: {book.genre}")

    def search_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print("Books with title '{}' found:".format(title))
            for i, book in enumerate(found_books, start=1):
                print(f"{i}. Title: {book.title}, Author: {book.author}, Genre: {book.genre}")
        else:
            print("No books found with title '{}'.".format(title))

    def search_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        if found_books:
            print("Books by author '{}' found:".format(author))
            for i, book in enumerate(found_books, start=1):
                print(f"{i}. Title: {book.title}, Author: {book.author}, Genre: {book.genre}")
        else:
            print("No books found by author '{}'.".format(author))


def main():
    library = Library()

    while True:
        print("\nOptions:")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Search books by title")
        print("4. Search books by author")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")
            new_book = Book(title, author, genre)
            library.add_book(new_book)
            print("Book added successfully!")

        elif choice == '2':
            library.list_books()

        elif choice == '3':
            search_title = input("Enter the title to search for: ")
            library.search_by_title(search_title)

        elif choice == '4':
            search_author = input("Enter the author to search for: ")
            library.search_by_author(search_author)

        elif choice == '5':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
