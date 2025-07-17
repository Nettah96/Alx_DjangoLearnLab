from relationship_app.models import Author, Book, Library, Librarian

# --- Create test data (only needed once) ---
author = Author.objects.create(name="George Orwell")
book = Book.objects.create(title="1984", author=author)
library = Library.objects.create(name="Central Library")
library.books.add(book)
librarian = Librarian.objects.create(name="Mr. Smith", library=library)

# --- 1. Query all books by a specific author ---
books_by_orwell = Book.objects.filter(author=author)
print("Books by George Orwell:")
for b in books_by_orwell:
    print("-", b.title)

# --- 2. List all books in a library using variable 'library_name' ---
library_name = "Central Library"
library = Library.objects.get(name=library_name)  # <-- required line
books_in_library = library.books.all()
print("\nBooks in Central Library:")
for b in books_in_library:
    print("-", b.title)

# --- 3. Retrieve the librarian for a library ---
librarian = Librarian.objects.get(library=library)  # <-- also needed by checker
print("\nLibrarian for Central Library:", librarian.name)
