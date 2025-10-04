# Date: 29-Sep-2025

# my_path = 'test.txt'
# my_file = open(my_path, 'r')

# my_lines = my_file.readlines()
# print(my_lines)

# # my_line = my_file.readline()
# # print(my_line)

# for ln in my_lines:
#     print(ln.strip())

from pathlib import Path

# my_path = Path(r'C:\coag_temp\cybE25A\test.txt')
# p = my_path.cwd().joinpath('test.txt')
# print(p)
# my_file = open(my_path, 'r')

# my_lines = my_file.readlines()
# print(my_lines)

# # my_line = my_file.readline()
# # print(my_line)

# for ln in my_lines:
#     print(ln.strip())


# print(Path.cwd())
# cwd = Path.cwd()
# fname = 'test.txt'
# my_path = cwd.joinpath(fname)
# my_file = open(my_path, 'r')
# first_ln = my_file.readline()
# print(first_ln)
# my_file.close()

# with open('wow.txt', 'w') as f:
#     f.write('Nice to meet you\n')
#     f.write('bob\n')

# with open('wow.txt', 'a') as f:
#     f.write('Alice here\n')
#     f.write('Hi, bob\n')

# with open('numbers.txt', 'w') as f:
#     f.write('0\n')

with open('numbers.txt', 'r+') as f:
    lns = f.readlines()
    last_no = int(lns[-1])
    new_no = last_no + 1

    f.write(str(new_no) + '\n') 