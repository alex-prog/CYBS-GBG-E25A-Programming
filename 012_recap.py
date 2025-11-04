# Date 03-Nov-2025

# print("hello world")
# bob_age = 11
# # print(type(bob_age))
# bob_age = bob_age + 1
# bob_age += 1 
# print(bob_age)

# # 12, 13
# alice_age = 12

# ages = [bob_age, alice_age]
# print(ages)
# sum_ages = ages[0] + ages[1]
# print(sum_ages)
# sum_ages = sum(ages)
# print(sum_ages)

# conn = ('127.0.0.1', 80)
# print(type(conn))
# print(conn[1])
# conn[1] = 8080
# print()

# conn_list = list(conn)
# conn_list[1] = 8080
# conn = tuple(conn_list)
# print(conn)

# conn = ('127.0.0.1', '88')
# # port can be 0-80
# if int(conn[1]) > 80:
#     print('port too high')

# x = [1, 3, 4, 5, 6, 7, 8, 9]
# for i in x[::2]:
#     print(i)


# bob: 10,
# alice: 7,
# hasan: 12
# grades = dict()
# grades['bob'] = 10
# grades['alice'] = 7
# grades['hasan'] = 12

# print(grades)
# avg_grade = grades['bob']
# sum_grades = 0
# for g in grades:
#     sum_grades += grades[g] 

# avg_grade = sum_grades / len(grades)
# print(avg_grade)

# import statistics

# # x = [10, 7, 12]
# print(statistics.mean(grades.values()))

# print(grades.values())
# print(grades.keys())
# print(grades.items())

# grades['julius'] = 12

# for name, grade in grades.items():
#     print(name, grade)


# def my_sum(x, y):
#     try:
#         s = int(x) + int(y)
#         return s
#     except:
#         print('ERROR: x, y needs to be int')
#         return 0

# print(my_sum(3, 'bob'))

# print('all good')

# def magic(x):
#     if x > 42:
#         print('Bigger than 42')
#     elif x == 42:
#         print('MAGIC 42')
#     else:
#         print('Less than 42')

# magic(43)

students = []

with open('s.txt', 'r') as f:
    for ln in f:
        x = ln.strip().split()
        s = dict()
        s['name'] = x[0]
        s['email'] = x[1]
        s['grade'] = x[2]
        students.append(s)

# print(students)

students_emails = []
for s in students:
    students_emails.append(s['email'])

# print(*students_emails, sep=', ')

# print(1, 2, 3, 4, 5, sep='#$#')
all_emails=''
for e in students_emails:
    all_emails += e + ', '

print(all_emails)