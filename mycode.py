# Проверка четности x
x = 7

if x % 2 == 0:
    print("Число", x, "является четным")
else:
    print("Число", x, "является нечетным")
# Выводим число пока оно меньше 5
print("Выводим число пока оно меньше 5")
a = 0
while a < 5:
    print(a)
    a +=1

#Работы с циклом for
print("Цикл for")
numbers = [1,2,3]
for i in numbers:
    print(i)

#Массивы
print("Работа с массивом")
my_array = [1,2,3,4,5]
print(my_array[0], my_array[2])
print(my_array[0:5])
my_array[2]=9
print(my_array)
my_array.append(6)
print(my_array)
my_array.insert(0, 0)
print(my_array)
print(len(my_array))

#Работа с кортежами
print("Работа с кортежами")
my_tuple = ("DevOps", 5, False)
title, years_in_company, coder = my_tuple
print(title, years_in_company)

def my_function():
    return 1, 2, 3
c, d, e = my_function()
print(c, d, e)

#Работа со словарями
print("Работа со словарями")
my_dict = {"fruits" : "apple", "veg" : ["tomato", "potatoe", "carrot"]}
print(my_dict["veg"][1])
my_dict["fruits"] = ["apple", "orange"]
print(my_dict)
print(my_dict["veg"])
items_list = list(my_dict.values())
print(items_list)
