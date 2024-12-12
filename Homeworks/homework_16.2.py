"""
Завдання 2.

Створіть абстрактний клас "Фігура" з абстрактними методами
для отримання площі та периметру. Наслідуйте від нього
декілька (> 2) інших фігур, та реалізуйте математично вірні
для них методи для площі та периметру. Властивості
по типу “довжина сторони” й т.д. повинні бути приватними,
та ініціалізуватись через конструктор.

Створіть Декілька різних об’єктів фігур, та у циклі
порахуйте та виведіть в консоль площу та периметр кожної.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Абстрактний клас для фігури."""

    @abstractmethod
    def area(self):
        """Повертає площу фігури."""
        pass

    @abstractmethod
    def perimeter(self):
        """Повертає периметр фігури."""
        pass


class Rectangle(Shape):
    """Клас для прямокутника."""

    def __init__(self, width, height):
        """Ініціація прямокутника - довжина, ширина."""
        self.__width = width
        self.__height = height

    def area(self):
        """Функція, що обчислює площу."""
        return self.__width * self.__height

    def perimeter(self):
        """Функція, що обчислює периметр."""
        return 2 * (self.__width + self.__height)


class Circle(Shape):
    """Клас для кола."""

    def __init__(self, radius):
        """Ініціація кола - радіус."""
        self.__radius = radius

    def area(self):
        """Функція, що обчислює площу."""
        return math.pi * self.__radius ** 2

    def perimeter(self):
        """Функція, що обчислює периметр."""
        return 2 * math.pi * self.__radius


class Triangle(Shape):
    """Клас для прямокутного трикутника."""

    def __init__(self, base, height, hypotenuse):
        """Ініціація трикутника - довжина сторони, гіпотенуза."""
        self.__base = base
        self.__height = height
        self.__hypotenuse = hypotenuse

    def area(self):
        """Функція, що обчислює площу."""
        return 0.5 * self.__base * self.__height

    def perimeter(self):
        """Функція, що обчислює периметр."""
        return self.__base + self.__height + self.__hypotenuse


# Створення об'єктів
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(3, 4, 5),  # Прямокутний трикутник
]

# Обчислення площі та периметру у циклі
for shape in shapes:
    print(f'Figure: {shape.__class__.__name__}')
    print(f'  Area: {shape.area():.2f}')
    print(f'  Perimeter: {shape.perimeter():.2f}')
    print()
