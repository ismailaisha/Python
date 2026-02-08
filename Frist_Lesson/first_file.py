
print ("Привет!")

name = input("Как тебя зовут? ")
print ("Приятно познакомиться, " + name + "!")

print (2 + 2)
a= 2
b= 2
print (a + b)

for i in range(1, 11):
    print (i)
age = int(input("Сколько вам лет? "))
print ("Вам " + str(age) + " лет.")

с = input("Введите первое число: ")
d = input("Введите второе число: ")
print ("Сумма чисел: " + str(int(с) + int(d)))

word = input("Введите слово: ")
print ("Первая буква слова: " + word[0])

nuber = int(input("Введите число: "))
print ("Квадрат числа: " + str(nuber ** 2))

for i in range(1, 11):
    print (f"5 x {i} = {5 * i}")

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
average = (num1 + num2) / 2
print ("Среднее арифметическое: " + str(average))