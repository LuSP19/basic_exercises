# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from collections import defaultdict


students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

name_counter = defaultdict(int)

for student in students:
    name_counter[student['first_name']] += 1

for name, count in name_counter.items():
    print(f'{name}: {count}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

name_counter = defaultdict(int)

for student in students:
    name_counter[student['first_name']] += 1

print(
    f'Самое частое имя среди учеников: '
    f'{max(name_counter, key=name_counter.get)}'
)


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for count, class_ in enumerate(school_students, start=1):
    name_counter = defaultdict(int)

    for student in class_:
        name_counter[student['first_name']] += 1

    print(
        f'Самое частое имя в классе {count}: '
        f'{max(name_counter, key=name_counter.get)}'
    )


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for class_ in school:
    gender_counter = defaultdict(int)
    for student in class_['students']:
        if is_male[student['first_name']]:
            gender_counter['male'] += 1
        else:
            gender_counter['female'] += 1
    print(
        f'Класс {class_["class"]}: '
        f'девочки {gender_counter["female"]}, '
        f'мальчики {gender_counter["male"]}'
    )


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

female_counter = defaultdict(int)
male_counter = defaultdict(int)

for class_ in school:
    for student in class_['students']:
        if is_male[student['first_name']]:
            male_counter[class_['class']] += 1
        else:
            female_counter[class_['class']] += 1

print(
    f'Больше всего мальчиков в классе '
    f'{max(male_counter, key=male_counter.get)}'
)
print(
    f'Больше всего девочек в классе '
    f'{max(female_counter, key=female_counter.get)}'
)
