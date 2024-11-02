﻿"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку 
здійснюється за механізмом 
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення, 
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""
students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
# ваш код нижче !!!!!!!! вище нічого не змінюємо
# 1
new_student = {
    "Олексій Іванов": {
        'Пошта': 'Oleksii@gmail.com',
        'Вік': 12,
        'Номер телефону': '+380987654321',
        'Середній бал': 88.5
    }
}
students["Олексій Іванов"] = new_student
# 2
my_students = {
    'Іван Петров': {
        'Вік': 12,
        'Номер телефону': '+380385771221',
        'Середній бал': 95.8

    },
    'Женя Курич': {
        'Вік': 14,
        'Номер телефону': '+380382603221',
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 91
    },
    "Олексій Іванов": {
        'Вік': 10,
        'Номер телефону': '+380385794711',
        'Середній бал': 78.5
    },
}
for student in my_students:
    if my_students[student]['Середній бал'] > 90:
        print(my_students[student]['Середній бал'])
        print(student)
    else:
        print("")
# 3
average = 0
count_students = 0
for student in my_students:
    count_students = count_students + 1
    average = average + my_students[student]['Середній бал']
group_average = average / count_students
print(group_average)
# 4
for student in my_students:
    my_students[student]['Номер телефону'] = my_students[student].get('Номер телефону' == None , 'Номер телефону батьків')
print(my_students)