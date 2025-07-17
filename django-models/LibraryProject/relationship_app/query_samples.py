from relationship_app.models import Author, Book, Library, Librarian

# Create sample data (optional, only if not already created)
author = Author.objects.create(name="George Orwell")
book = Book.objects.create(title="1984", author=author)
library = Library.objects.create(name="Central Library")
library.books.add(book)
librarian = Librarian.objects.create(name="Mr. Smith", library=library)

# 1. Query all books by a specific author
books_by_orwell = Book.objects.filter(author=author)
print("Books by George Orwell:", books_by_orwell)

# 2. List all books in a library
books_in_library = library.books.all()
print("Books in Central Library:", books_in_library)

# ✅ 3. Retrieve the librarian for a library using the required query
librarian = Librarian.objects.get(library=library)
print("Librarian for Central Library:", librarian.name)
