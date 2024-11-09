# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    # Find the author by name
    try:
        author = Author.objects.get(name=author_name)
        # Query all books related to that author
        books = author.books.all()
        if books:
            print(f"Books by {author_name}:")
            for book in books:
                print(f"- {book.name}")
        else:
            print(f"No books found for author {author_name}.")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}.")

def list_books_in_library(library_name):
    """List all books in a specific library."""
    # Find the library by name
    try:
        library = Library.objects.get(name=library_name)
        # Get all books associated with this library
        books = library.books.all()
        if books:
            print(f"Books in library {library_name}:")
            for book in books:
                print(f"- {book.name}")
        else:
            print(f"No books found in library {library_name}.")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}.")

def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a specific library."""
    # Find the library by name
    try:
        library = Library.objects.get(name=library_name)
        # Retrieve the librarian associated with this library
        librarian = library.librarian
        if librarian:
            print(f"The librarian for {library_name} is {librarian.name}.")
        else:
            print(f"No librarian assigned to the library {library_name}.")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for library {library_name}.")

if __name__ == "__main__":
    # Sample queries to test
    query_books_by_author('J.K. Rowling')
    print("-" * 50)
    list_books_in_library('Central Library')
    print("-" * 50)
    retrieve_librarian_for_library('Central Library')
