# Date 29-Oct-2025

# import sqlite3

# conn = sqlite3.connect('t.db')
# c = conn.cursor()

# q = '''CREATE TABLE IF NOT EXISTS user(
#             user_id INTEGER PRIMARY KEY NOT NULL,
#             first_name TEXT NOT NULL,
#             height INTEGER
#             )
# '''

# c.execute(q)

# c.execute("INSERT INTO user (user_id, first_name, height) VALUES (3, 'Bob', '150')")
# c.execute("INSERT INTO user VALUES (1, 'Alice', '200')")


# conn.commit()
# conn.close()




# import sqlite3

# conn = sqlite3.connect('students.db')
# c = conn.cursor()

# q = '''CREATE TABLE IF NOT EXISTS students(
#             stud_id INTEGER PRIMARY KEY NOT NULL,
#             first_name TEXT NOT NULL,
#             grade INTEGER
#             )
# '''

# c.execute(q)

# # studs = [{'stud_id':1, 'first_name': 'Alice', 'grade': 10},
# #          {'stud_id':2, 'first_name': 'Bob', 'grade': 7},
# #          {'stud_id':3, 'first_name': 'Hasan', 'grade': 12}]

# studs = []

# while True:
#     s = input('Enter name and grade (type exit to finish):')
#     # Bob 10
#     if s.lower() == 'exit' or s.lower() == 'e':
#         break
#     ss = s.split()
#     student = {'first_name': ss[0], 'grade': ss[1] }
#     studs.append(student)


# for s in studs:
#     q = f''' INSERT INTO students (first_name, grade) 
#     VALUES ('{s['first_name']}','{s['grade']}') '''
#     try:
#         c.execute(q)
#     except:
#         print('nooooooooooooo')

# conn.commit()
# conn.close()

def read_students():
    import sqlite3

    conn = sqlite3.connect('students.db')
    c = conn.cursor()

    data = c.execute('SELECT first_name, grade FROM students ORDER BY grade DESC').fetchall()

    # print(data)

    for name, grade in data:
        print(f'{name:10} {grade}')


import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()

q = '''DELETE FROM students WHERE first_name='Alice' OR first_name='Bob' 
            OR (first_name='Hasan' AND grade=12)   '''
c.execute(q)

conn.commit()
conn.close()

read_students()
