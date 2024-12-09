"""
Завдання 1.

Створіть клас Employee, який має атрибути name та salary.
Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
Клас Manager повинен мати додатковий атрибут department,
а клас Developer - атрибут programming_language.

Тепер створіть клас TeamLead, який успадковується як від Manager,
так і від Developer. Цей клас представляє керівника з команди розробників.
Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
а також атрибут team_size, який вказує на кількість розробників
у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрибутів
з Manager та Developer у класі TeamLead
"""


class Employee:
    """Базовий клас для співробітників."""

    def __init__(self, name, salary):
        """
        Ініціалізація екземпляра Employee.

        :param name: ім'я співробітника.
        :param salary: зарплата співробітника.
        """
        self.name = name
        self.salary = salary


class Manager(Employee):
    """Клас для менеджерів."""

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    """Клас для розробників."""

    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    """Клас для TeamLead."""

    def __init__(self, name, salary, department, programming_language, team_size):
        # Викликаємо ініціалізатор Manager і Developer, передаючи всі необхідні аргументи
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


# Тестування
def test_teamlead_attributes():
    """Тест перевіряє наявність атрибутів у класі TeamLead."""
    team_lead = TeamLead(
        name='John Doe',
        salary=5300,
        department='Software Development',
        programming_language='Python',
        team_size=8
    )

    # Перевірка атрибутів із класу Manager
    assert hasattr(team_lead, 'name'), "TeamLead має мати атрибут 'name' із класу Employee"
    assert hasattr(team_lead, 'salary'), "TeamLead має мати атрибут 'salary' із класу Employee"
    assert hasattr(team_lead, 'department'), "TeamLead має мати атрибут 'department' із класу Manager"

    # Перевірка атрибутів із класу Developer
    assert hasattr(team_lead,
                   'programming_language'), "TeamLead має мати атрибут 'programming_language' із класу Developer"

    print('Усі атрибути успішно перевірені!')


test_teamlead_attributes()
