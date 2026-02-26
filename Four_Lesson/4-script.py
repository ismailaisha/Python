class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}"

    def update_info(self, title=None, author=None, year=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if year:
            self.year = year


book1 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866)
book3 = Book("Анна Каренина", "Лев Толстой", 1877)


print(book1.get_info())
print(book2.get_info())
print(book3.get_info())


book1.update_info(year=1966)
book2.update_info(title="Идиот")

print("После изменений:")
print(book1.get_info())
print(book2.get_info())