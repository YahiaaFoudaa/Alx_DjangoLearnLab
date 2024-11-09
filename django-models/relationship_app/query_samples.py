from models import Author,Book,Library,Librarian

author = Author.objects.get(name = "J.K. Rowling")

books = Book.objects.all()

librarian = Librarian.objects.get(Library = "mktba")