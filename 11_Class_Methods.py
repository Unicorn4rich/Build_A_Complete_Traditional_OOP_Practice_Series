# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. 
# Add a class method increment_book_count() to increase the count when a new book is added.


class Books:
  total_books = 0

  @classmethod
  def increment_book_count(cls, new_book: str):
    cls.total_books += 1
    print("New book added:", new_book)
    print("now we have books:", cls.total_books)


books1 = Books()   
books1.increment_book_count("Rich dad")
books1.increment_book_count("The secret book")

print(f"\nThis is total number of books {books1.total_books}")
