import csv

users = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('users.csv', 'w', encoding='utf-8') as f:
    fields = ['name', 'age', 'job']
    write = csv.DictWriter(f, fields, delimiter=';')
    write.writeheader()
    for ln in users:
        write.writerow(ln)
    
