from relationship_app.models import Library, Book, Author, Librarian

# Query a library by name
library_name = "Central Library"
library = Library.objects.get(name=library_name)

# 1. Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:", books_by_author)

# 2. List all books in a library
books_in_library = library.books.all()
print(f"Books in {library.name}:", books_in_library)

# 3. Retrieve the librarian for a library
librarian = library.librarian  # This works if you used OneToOneField
print(f"Librarian for {library.name}:", librarian.name)
