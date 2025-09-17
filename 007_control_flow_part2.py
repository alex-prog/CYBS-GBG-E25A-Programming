# 17-Sep-2025

# port = int(input('Enter port no: '))

# match port:
#     case 22:
#         print('SSH')
#     case 20 | 21:
#         print('FTP')
#     case peter:
#         print(f'I dont understand {peter}')

# if 1 <= port <= 1023: 
#     print(f'{port} - Well-known system ports')

# if port in range(1,1024):
#     print(f'{port} - Well-known system ports')

# if (1 <= port) and (port <= 1023):
#     print(f'{port} - Well-known system ports')


# alert_timer = 5

# print("Security Alert: System will lock in:")
# while alert_timer > 0:
#     print(f"{alert_timer} seconds...")
#     alert_timer -= 1

# print("System locked!")


# print("\n--- Scanning for threats ---")
# threat_level = 1

# while threat_level <= 10:
#   input(f'Threat level is {threat_level} (press enter to continue)..')
#   if threat_level == 3:
#     print(f"Level {threat_level}: Low priority - skipping")
#     threat_level += 1
#     continue
  
#   if threat_level == 8:
#     print(f"Level {threat_level}: CRITICAL THREAT DETECTED!")
#     break
  
#   print(f"Level {threat_level}: Normal")
#   threat_level += 1

# print("Threat scan complete")



# while True:
#     password = input('Enter pass: ')
#     print(f'You enterd {password}')
#     is_len_ok = False
#     if len(password) < 12:
#         print(f'Pass is too short {len(password)}')
#         is_len_ok = False
#     else:
#         is_len_ok = True

#     is_digit_ok = False
#     i = 0
#     while i < len(password):
#         is_digit_ok = password[i].isdigit()
#         i = i + 1

#     if is_digit_ok and is_len_ok:
#         print('Strong password accepted!')
#         break

    


# ports = [22, 80, 443, 21]

# for port in ports:
#   print(f'Scanning port {port}')

# print('-'*26)
# x = 0
# while x < len(ports):
#   print(f'Scanning port {ports[x]}')
#   x = x + 1
    


print('\nScanning IP range:')
for i in range(1, 254):
    print(f'192.168.1.{i} - checking...')
