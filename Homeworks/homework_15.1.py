"""
Створіть клас геометричної фігури "Ромб".

Клас повинен мати наступні атрибути:
сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а,
значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__.
Module that defines a geometric figure class 'Rhombus'.
"""


class Rhombus:
    """Class 'Rhombus' created."""

    def __init__(self, side_a, angle_a):
        """
        Initialize a rhombus instance.

        :param side_a: Length of the side of the rhombus.
        :param angle_a: Angle between two adjacent sides (in degrees).
        :raises ValueError: If side_a <= 0 or

        angle_a is not in the range (0, 180).
        """
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        """
        Set attribute with validation.

        :param key: Attribute name to set.
        :param value: Value to assign.
        :raises ValueError: If side_a <= 0

        or angle_a not in the range (0, 180).
        :raises AttributeError: If attempting to set angle_b directly.
        """
        if key == 'side_a':
            if value <= 0:
                raise ValueError('The length of the side should be > 0.')
            super().__setattr__(key, value)
        elif key == 'angle_a':
            if not (0 < value < 180):
                raise ValueError('Angle should be in betwee 0 and 180.')
            super().__setattr__(key, value)
            super().__setattr__('angle_b', 180 - value)
        elif key == 'angle_b':
            raise AttributeError('Angle can be only set automatically.'
                                 'You cannot change it.')
        else:
            super().__setattr__(key, value)

    def __repr__(self):
        """
        Return a string representation of the rhombus.

        :return: String in the format

        'Rhombus(side_a=..., angle_a=..., angle_b=...)'.
        """
        return (
            f'Rhombus('f'side_a={self.side_a},'
            f'angle_a={self.angle_a},'
            f'angle_b={self.angle_b})'
        )


# Checking
try:
    rhombus = Rhombus(5, 60)
    print(rhombus)
    print('-' * 40)

    # check length
    rhombus.side_a = -2
except ValueError as e:
    print(e)
    print('-' * 40)

try:
    # check angle
    rhombus.angle_a = 200
except ValueError as e:
    print(e)
    print('-' * 40)

try:
    # ckeck angle_b
    rhombus.angle_b = 50
except AttributeError as e:
    print(e)
