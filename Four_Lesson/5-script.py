class Car:

    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def get_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Цвет: {self.color}, Год: {self.year}"

    def update_info(self, brand=None, model=None, color=None, year=None):
        if brand:
            self.brand = brand
        if model:
            self.model = model
        if color:
            self.color = color
        if year:
            self.year = year


car1 = Car("Toyota", "Camry", "Белый", 2020)
car2 = Car("BMW", "X5", "Черный", 2022)
car3 = Car("Mercedes", "C200", "Серый", 2019)


print(car1.get_info())
print(car2.get_info())
print(car3.get_info())


car1.update_info(color="Красный")
car2.update_info(year=2023)

print("После изменений:")
print(car1.get_info())
print(car2.get_info())