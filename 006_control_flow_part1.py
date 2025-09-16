a = 10
b = 20
c = 20
print(f'{a=} {b=} {c=}')
if a > b and a > c :
    print(f'a is the highest {a=}')
elif b >= c and b > a:
    print(f'b is the highest {b=}')
    c = b   

if c > a and c >= b:
    print(f'c is the highest {c=}')
else:
    print('I give up')
print(f'{a=} {b=} {c=}')

# print(max(a,b,c))