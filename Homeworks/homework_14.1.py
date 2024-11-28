"""
Homework 14.1.

Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та
"середній бал". Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал
студента. Виведіть інформацію про студента та змініть його середній бал.

1) ств. клас + його атрибути
2) створити об'єкт(клон, екземпляр, інстанс) для цього класу
3) додати метод до класу, що дозволяє змінювати середній бал
4) вивести інформацію та змінити середній бал
"""


class Student:
    """class Student created."""

    def __init__(self, first_name, last_name, age):
        """init."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.av_score = 0

    def av_score_set(self, av_score):
        """Set average score."""
        self.av_score = av_score

    def print(self):
        """Print."""
        print(f'First name: {self.first_name}\nLast name: {self.last_name}\n'
              f'Age: {self.age}\nAverage score: {self.av_score}')


student1 = Student('Eric', 'Scott', 17)
student1.av_score_set(av_score=89)
student1.print()
