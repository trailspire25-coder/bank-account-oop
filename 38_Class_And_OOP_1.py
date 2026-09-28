class Book:
    category = "Books"

    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def display_info(self):
        print(f"{self.title} by {self.author} ({self.year}) - ${self.price}")

    def apply_discount(self, percentage):
       discount = self.price * (percentage/ 100)
       self.price = self.price - discount

    def get_book_age(self, current_year):
        return current_year - self.year

        
book1 = Book("Atomic Habits", "James Clear", 2018, 20)
book2 = Book("Think and Grow Rich", "Napoleon Hills", 1937, 10)
book3 = Book("The 7 Habits of Highly Effective People", "Stephen Covey", 1989, 15)
book4 = Book("How to Win Friends and Influence People", "Dale Carnegie", 1936, 12)
book5 = Book("The Psychology of Money", "Morgan Housel", 2020, 18)

print(book1.author)
print(book4.title)
print(book3.price)
print(book5.year)
print(book3.author)
print(book2.title)

book4.price = 13
print(book4.price)

book1.display_info()
book2.display_info()
book3.display_info()
book4.display_info()
book5.display_info()

book5.apply_discount(43)
print(book5.price)

age = book3.get_book_age(2026)
print(age)

print(book1.category)
print(book2.category)
print(book3.category)
print(Book.category)