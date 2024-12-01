"""
Homework 14.1.

Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та
"середній бал". Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал
студента. Виведіть інформацію про студента та змініть його середній бал.

1) ств. клас + його атрибути
2) створити об"єкт(клон, екземпляр, інстанс,) для цього класу
3) додати метод до класу, що дозволяє змінювати середній бал
4) вивести інформацію та змінити середній бал
"""


class Student:
    """class Student created."""

    def __init__(self, first_name, last_name, age, av_grade):
        """init."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.av_grade = av_grade


student1 = Student('Eric', 'Scott', 17, 90)

student1.av_grade = 87
print(student1.__dict__)
print(f"{student1.first_name}'s new average grade is {student1.av_grade}.")
