from classes import Book, Library, InvalidBookAttributeError

# Пример использования
library = Library()

try:
    book1 = Book(pages=300, year=2022, author="Иванов И.И.", price=500.0)
    book2 = Book(pages=200, year=2021, author="Петров П.П.", price=400.0)
    book3 = Book(pages=400, year=2020, author="Сидоров С.С.", price=600.0)
except InvalidBookAttributeError as e:
    print(e)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(f"Книга с id {book1.book_id}: {book1}")
print(f"Книга с id {book2.book_id}: {book2}")
print(f"Книга с id {book3.book_id}: {book3}")

print("Книги, отсортированные по цене:")
print(sorted(library.books))

print("Книги, найденные по авторам:")
print(library.find_books_by_author("Иванов И.И.", "Петров П.П."))
print(library.find_books_by_author(["Сидоров С.С."]))
