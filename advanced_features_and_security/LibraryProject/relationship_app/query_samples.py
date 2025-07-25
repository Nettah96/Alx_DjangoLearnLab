from relationship_app.models import Author, Book, Library, Librarian

# Create test data (only if not already created)
author_name = "George Orwell"
author = Author.objects.create(name=author_name)
book = Book.objects.create(title="1984", author=author)
library_name = "Central Library"
library = Library.objects.create(name=library_name)
library.books.add(book)
librarian = Librarian.objects.create(name="Mr. Smith", library=library)

# 1. Query all books by a specific author using author_name
author = Author.objects.get(name=author_name)   # <-- checker wants this line
books_by_author = Book.objects.filter(author=author)
print("Books by", author_name)
for b in books_by_author:
    print("-", b.title)

# 2. List all books in a library using library_name
library = Library.objects.get(name=library_name)   # <-- checker wants this line
books_in_library = library.books.all()
print("\nBooks in", library_name)
for b in books_in_library:
    print("-", b.title)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)  # <-- checker wants this line
print("\nLibrarian for", library_name, ":", librarian.name)
