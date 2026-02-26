class Student:

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def get_status(self):
        average = self.calculate_average()

        if average >= 4.5:
            return "Отличник"
        elif average >= 3.5:
            return "Хорошист"
        else:
            return "Троечник"


student1 = Student("Александр", 20, [5, 5, 4])
student2 = Student("Екатерина", 19, [4, 3, 4])
student3 = Student("Даниил", 21, [3, 3, 3])


print(student1.name, student1.calculate_average(), student1.get_status())
print(student2.name, student2.calculate_average(), student2.get_status())
print(student3.name, student3.calculate_average(), student3.get_status())