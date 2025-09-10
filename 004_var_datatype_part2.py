# Date: 08-Sep-2025

# age = int(input('How old are you? '))
# future_age = age + 100
# print(f"Your age in 100 years: {future_age}")
# future_year = 100 - age + 2025
# print(f"You will turn 100 in year {future_year}")

# name = 'Amira'
# age = 19
# print(f"Hi {name}. Today is Monday. You are {age} years old. And 2+3 is {2+3}")
# print("Hi", name, '. Today is Monday. You are', age, ' years old. And 2+3 is ', (2+3), sep='')


# x = ["first", "second", "third", "fourth"]
# print(f'{x=}')
# print(f"{x[:3]=}")
# print("This is the result", x[-2:])

#    0  1  2   3    4   5   6 
#   -7 -6 -5  -4   -3  -2  -1
# l = [4, 5, 8 , 12 , 45, 42, 16]

# # 45, 12, 8, 5
# print(f'{l[4:0:-1]=}')
# print(f'{l[-3:-7:-1]=}')

# print(f'{l=}')
# print(f'{l[0:4]=}')
# print(f'{l[:4]=}')
# print(f'{l[-7:-3]=}')

# print(f'{l[2:4]=}')

# print(f'{l[::2]=}')
# print(f'{l[1::2]=}')

# print(f'{l[::-1]=}')


# my_list = [0,1,2,3,4,5,6,7,8]

# print(my_list)
# print(my_list[0])
# print(my_list[-1])
# print(my_list[0:4]) # opg. 4
# second_list = my_list[-1:-4:-1] # [-1:-4:-1] [-3:]
# print(second_list)

# my_list = [0,1,0,0,0,2,3,4,5,6,7,8]
# my_list.append('bob')
# my_list.append(['bob', 'alice'])
# print(my_list)
# my_list.remove(['bob', 'alice'])
# print(my_list)
# my_list.remove(0)
# print(my_list)
# my_list.clear()
# print(my_list)



# l = [4, 6, 15, 17, -3]
# print(f'{min(l)=}')
# print(f'{max(l)=}')

# l = ['a', 'f', 'A']
# print(f'{min(l)=}')
# print(f'{max(l)=}')


my_list = []
my_list += [2, 1, 3] 
my_list = my_list + [2, 1, 3]

print(f'After 1. (new method) {my_list}')

my_list.extend([2, 1, 3])
print(f'After 1. {my_list}')
my_list.append('cyber')
print(f'After 2. {my_list}')

print(f'Index of cyber is {my_list.index('cyber')}') # opg. 3
my_list.remove('cyber') # opg. 4
my_list.sort()
print(my_list)