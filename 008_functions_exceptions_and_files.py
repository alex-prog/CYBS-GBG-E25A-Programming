# Date: 22-Sep-2025
# def password_checker(password, min_len):
#     if len(password) <= min_len and len(password)<=6:
#         print('Pass is good enough')
#     elif len(password) > 64:
#         print('pass too big')
#     elif len(password) < min_len:
#         print('pass is to short')

# def password_checker(password, min_len):
#     if min_len < 6 or min_len > 64:
#         print('invalid min_len')
#     elif len(password) > min_len:
#         print('The password is good enough')
#     elif len(password) < min_len or len(password) < 6:
#         print('The password is too short ')




# password_checker('bob2', 3)
# # password_checker('bob2', 6)
# # password_checker('a'*37, 36)
# # password_checker('bob2'*100, 100)

# print('hello from this file')




# def s(a,b) -> int:
#     t = a + b
#     return t

# ss = s(10, 20)
# print(ss)
# print(s(20, 10))


# print(1,2,3, sep='***', end=' ')
# print(3,4,5, end='!!', sep='%%%')

# def s(a=1,b=10):
#     return a+b

# print(s(5))   # 15
# print(s(5,5)) # 10
# print(s(b=2)) # 

def isnumber(x):
    try:
        no = int(x)
        return True
    except:
        raise Exception('You stupid. This is not a number')

try:
    # print(5/0)
    i = input('Type a number:')
    if isnumber(i):
        print('Good job')
except Exception as johannes:
    print(f'Error: {johannes}')
finally:
    print('I will always run')


print('Have a nice day!')