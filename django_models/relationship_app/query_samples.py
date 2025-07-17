from relationship_app.models import Author, Book, Library, Librarian

# Create sample author
author = Author.objects.create(name="George Orwell")

# Create books
book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)

# Create library and add books
library = Library.objects.create(name="Central Library")
library.books.set([book1, book2])

# Create librarian for the library
librarian = Librarian.objects.create(name="Alice", library=library)
