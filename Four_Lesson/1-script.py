import math

class Krug:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius


krug1 = Krug(5, "красный")
krug2 = Krug(10, "синий")
krug3 = Krug(2.5, "зелёный")

print("Круг 1:", krug1.color, "радиус =", krug1.radius)
print("Площадь:", krug1.area())
print("Длина окружности:", krug1.circumference())

print("Круг 2:", krug2.color, "радиус =", krug2.radius)
print("Площадь:", krug2.area())
print("Длина окружности:", krug2.circumference())

print("Круг 3:", krug3.color, "радиус =", krug3.radius)
print("Площадь:", krug3.area())
print("Длина окружности:", krug3.circumference())