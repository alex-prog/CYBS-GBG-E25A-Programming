# Date: 10-Nov-2025

# def validate_ip_address(ip_string):
#     '''
#     This will validate IPv4 address format and range.
#     Args:
#         ip_string (str): IP address to validate    
#     Returns:
#         bool: True if valid, False otherwise
#     Raises:
#         ValueError: If IP format is invalid
#     Example:
#         * validate_ip_address('192.168.1.1')
#         True
#         * validate_ip_address('999.999.999.999')
#         False
#     Bob:
#         If you use this, tell Alice. 
#     '''
#     pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
#     if not re.match(pattern, ip_string):
#         return False
    
#     octets = ip_string.split('.')
#     return all(0 <= int(octet) <= 255 for octet in octets)


# def check_password_strength(password):
#     '''
#     this will validate your password.
#     Args:
#         password - type: str - this is the str to validate
#     Returns:
#         bool - if pass good True, else False 
    
#     '''
#     if len(password) < 12:
#         return False
    
#     isspecial, islower, isupper, isdigit = False, False, False, False
    
#     for c in password:
#         if c.isupper():
#             isupper=True
#         if c.islower():
#             islower=True
#         if c.isdigit():
#             isdigit=True
#         if c in '!@#$%^&*()':
#             isspecial=True
#     return isupper and islower and isdigit and isspecial



# print(check_password_strength.__doc__)


# for i in range(2):
#     breakpoint()
#     for j in range(2):
#         print(str(i) + str(j), end=', ')

# name = 'bob' 
# print(name)


def calculate_avg_age(students):
    age=0
    for student_idx in range(len(students)-1):
        age=age+students[student_idx]
    return age/len(students)

students=[20,20,30,30]
print(calculate_avg_age(students))
