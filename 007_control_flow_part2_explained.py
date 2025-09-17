"""
Session 07: Control Flow - Part 2 (Loops and Advanced Patterns)
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Master while loops and their control mechanisms
- Understand for loops and iteration patterns
- Learn break and continue statements
- Work with range() function and numeric sequences
- Practice with loop control in real-world scenarios
- Explore match statements (pattern matching)
- Apply loops to practical programming problems

Author: Programming Instructor
Date: 17-Sep-2025
"""

# =============================================================================
# LOOPS AND ADVANCED CONTROL FLOW
# =============================================================================

print("Welcome to Session 07: Loops and Advanced Control Flow")
print("=" * 55)
print()

# -----------------------------------------------------------------------------
# 1. INTRODUCTION TO MATCH STATEMENTS (PATTERN MATCHING)
# -----------------------------------------------------------------------------

print("1. Match Statements - Pattern Matching")
print("-" * 35)

# Match statements provide a clean way to handle multiple conditions
# Similar to switch statements in other languages
print("Example: Network port identification")

# Simulating user input
port = 22  # This would be: int(input('Enter port no: '))
print(f"Checking port: {port}")

match port:
    case 22:
        service = "SSH"
        print("SSH - Secure Shell")
    case 20 | 21:  # Multiple values with | (or)
        service = "FTP"
        print("FTP - File Transfer Protocol")
    case 23:
        service = "Telnet"
        print("Telnet - Telecommunication Network")
    case 25:
        service = "SMTP" 
        print("SMTP - Simple Mail Transfer Protocol")
    case 53:
        service = "DNS"
        print("DNS - Domain Name System")
    case 80:
        service = "HTTP"
        print("HTTP - Hypertext Transfer Protocol")
    case 443:
        service = "HTTPS"
        print("HTTPS - HTTP Secure")
    case unknown_port:  # Catch-all variable
        service = "Unknown"
        print(f"Unknown service on port {unknown_port}")

print(f"Service identified: {service}")
print()

print("Match statement advantages:")
print("- Cleaner syntax than multiple if-elif statements")
print("- Can match multiple values with | operator")
print("- Can capture unmatched values in variables")
print("- More readable for complex pattern matching")
print()

# -----------------------------------------------------------------------------
# 2. RANGE CHECKING WITH MULTIPLE METHODS
# -----------------------------------------------------------------------------

print("2. Range Checking - Multiple Approaches")
print("-" * 38)

port = 80
print(f"Checking if port {port} is in well-known range (1-1023)")

# Method 1: Chained comparison (most readable)
if 1 <= port <= 1023:
    print(f"Method 1: Port {port} is a well-known system port")

# Method 2: Using range() function
if port in range(1, 1024):  # range(1, 1024) creates 1 to 1023
    print(f"Method 2: Port {port} is a well-known system port")

# Method 3: Separate conditions with 'and'
if (1 <= port) and (port <= 1023):
    print(f"Method 3: Port {port} is a well-known system port")

print()
print("Best practice: Use chained comparison (1 <= port <= 1023)")
print("- Most readable and Pythonic")
print("- Efficient and clear intent")
print("- Less prone to logical errors")
print()

# -----------------------------------------------------------------------------
# 3. WHILE LOOPS - COUNTDOWN TIMER
# -----------------------------------------------------------------------------

print("3. While Loops - Countdown Timer")
print("-" * 30)

print("Example: Security system countdown")
alert_timer = 5

print("Security Alert: System will lock in:")
while alert_timer > 0:
    print(f"{alert_timer} seconds...")
    alert_timer -= 1  # Decrease by 1 each iteration

print("System locked!")
print()

print("Key components of while loops:")
print("- Condition: alert_timer > 0")
print("- Loop body: code that runs while condition is True")
print("- Update: alert_timer -= 1 (prevents infinite loop)")
print("- Exit: when condition becomes False")
print()

print("Common while loop pattern:")
print("1. Initialize counter variable")
print("2. Check condition")
print("3. Execute loop body")
print("4. Update counter")
print("5. Repeat until condition is False")
print()

# -----------------------------------------------------------------------------
# 4. WHILE LOOPS WITH BREAK AND CONTINUE
# -----------------------------------------------------------------------------

print("4. While Loops with Break and Continue")
print("-" * 37)

print("Example: Threat detection system")
print("Scanning for threats...")

threat_level = 1

while threat_level <= 10:
    print(f"Checking threat level {threat_level}")
    
    # Skip level 3 (continue statement)
    if threat_level == 3:
        print(f"Level {threat_level}: Low priority - skipping")
        threat_level += 1
        continue  # Skip rest of loop body, go to next iteration
    
    # Stop at level 8 (break statement)
    if threat_level == 8:
        print(f"Level {threat_level}: CRITICAL THREAT DETECTED!")
        print("Stopping scan immediately!")
        break  # Exit the loop completely
    
    # Normal processing
    print(f"Level {threat_level}: Normal - continuing scan")
    threat_level += 1

print("Threat scan complete")
print()

print("Break vs Continue:")
print("- continue: Skip current iteration, go to next")
print("- break: Exit the loop completely")
print("- Both are powerful tools for loop control")
print()

# -----------------------------------------------------------------------------
# 5. INFINITE LOOPS WITH CONDITIONAL EXIT
# -----------------------------------------------------------------------------

print("5. Infinite Loops with Conditional Exit")
print("-" * 37)

print("Example: Password validation system")
attempts = 0
max_attempts = 3

while True:  # Infinite loop - be careful!
    attempts += 1
    print(f"Password attempt {attempts}")
    
    # Simulate password input
    if attempts == 1:
        password = "weak"
    elif attempts == 2:
        password = "stronger123"
    else:
        password = "securepass123"
    
    print(f"You entered: {password}")
    
    # Check password length
    is_length_ok = False
    if len(password) < 12:
        print(f"Password is too short: {len(password)} characters (minimum 12)")
        is_length_ok = False
    else:
        print("Password length: OK")
        is_length_ok = True
    
    # Check for digits
    is_digit_ok = False
    i = 0
    while i < len(password):
        if password[i].isdigit():
            is_digit_ok = True
            break  # Found a digit, no need to check further
        i += 1
    
    if is_digit_ok:
        print("Password contains digits: OK")
    else:
        print("Password must contain at least one digit")
    
    # Final validation
    if is_digit_ok and is_length_ok:
        print("Strong password accepted!")
        break  # Exit the infinite loop
    else:
        print("Password rejected - try again")
        
        # Prevent infinite attempts
        if attempts >= max_attempts:
            print("Maximum attempts reached - account locked")
            break

print("Password validation complete")
print()

print("Infinite loop safety tips:")
print("- Always have a break condition")
print("- Use counters to limit attempts")
print("- Test thoroughly to avoid actual infinite loops")
print("- Consider using while condition instead of while True when possible")
print()

# -----------------------------------------------------------------------------
# 6. FOR LOOPS WITH LISTS
# -----------------------------------------------------------------------------

print("6. For Loops with Lists")
print("-" * 20)

print("Example: Network port scanning")
ports = [22, 80, 443, 21, 23, 25, 53]

print("Method 1: For loop (recommended)")
for port in ports:
    print(f"Scanning port {port}")
    # Simulate port scanning logic
    if port == 80:
        print("  -> HTTP service detected")
    elif port == 443:
        print("  -> HTTPS service detected")
    elif port == 22:
        print("  -> SSH service detected")

print()

print("Method 2: While loop (traditional approach)")
print("Equivalent while loop implementation:")
x = 0
while x < len(ports):
    port = ports[x]
    print(f"Scanning port {port}")
    x += 1

print()

print("For loop advantages:")
print("- More readable and concise")
print("- Less error-prone (no manual indexing)")
print("- Automatically handles list bounds")
print("- More Pythonic style")
print()

# -----------------------------------------------------------------------------
# 7. FOR LOOPS WITH RANGE()
# -----------------------------------------------------------------------------

print("7. For Loops with Range Function")
print("-" * 30)

print("Example: IP address scanning")
print("Scanning local network range...")

# For demonstration, we'll scan a smaller range
print("Scanning first 10 addresses:")
for i in range(1, 11):  # range(1, 11) gives us 1 to 10
    ip_address = f"192.168.1.{i}"
    print(f"{ip_address} - checking...")
    
    # Simulate some devices being found
    if i in [1, 5, 10]:
        print(f"  -> Device found at {ip_address}")

print()

print("Range function variations:")
print("range(5)        -> 0, 1, 2, 3, 4")
print("range(1, 6)     -> 1, 2, 3, 4, 5") 
print("range(0, 10, 2) -> 0, 2, 4, 6, 8")
print("range(10, 0, -1)-> 10, 9, 8, 7, 6, 5, 4, 3, 2, 1")
print()

# Demonstration of different range patterns
print("Range pattern examples:")

print("Counting by 2s:")
for i in range(0, 11, 2):
    print(f"Count: {i}")

print()

print("Countdown from 5:")
for i in range(5, 0, -1):
    print(f"Countdown: {i}")

print("Launch!")
print()

# -----------------------------------------------------------------------------
# 8. NESTED LOOPS
# -----------------------------------------------------------------------------

print("8. Nested Loops")
print("-" * 14)

print("Example: Network subnet scanning")

# Scan multiple subnets
subnets = ["192.168.1", "192.168.2"]
important_ports = [22, 80, 443]

for subnet in subnets:
    print(f"Scanning subnet {subnet}.x:")
    
    # Scan first 3 addresses in each subnet
    for host in range(1, 4):
        ip = f"{subnet}.{host}"
        print(f"  Checking {ip}")
        
        # Check important ports on each host
        for port in important_ports:
            print(f"    Port {port}: ", end="")
            # Simulate port check
            if host == 1 and port == 22:
                print("OPEN")
            elif host == 2 and port == 80:
                print("OPEN")
            else:
                print("CLOSED")

print("Subnet scan complete")
print()

print("Nested loop considerations:")
print("- Inner loop completes fully for each outer loop iteration")
print("- Be careful with performance - loops multiply execution time")
print("- Keep nesting levels reasonable for readability")
print("- Consider breaking complex nested loops into functions")
print()

# -----------------------------------------------------------------------------
# 9. PRACTICAL LOOP PATTERNS
# -----------------------------------------------------------------------------

print("9. Practical Loop Patterns")
print("-" * 25)

print("Pattern 1: Processing with enumeration")
services = ["Web Server", "Database", "Email Server", "File Server"]

for index, service in enumerate(services):
    print(f"{index + 1}. {service} - Status: Running")

print()

print("Pattern 2: Loop with accumulation")
response_times = [45, 32, 78, 23, 56, 67, 43]
total_time = 0
count = 0

for time in response_times:
    total_time += time
    count += 1
    print(f"Response {count}: {time}ms")

average_time = total_time / count
print(f"Average response time: {average_time:.1f}ms")
print()

print("Pattern 3: Filtering during iteration")
log_levels = ["INFO", "DEBUG", "ERROR", "INFO", "WARNING", "ERROR", "INFO"]

print("Filtering for errors and warnings:")
for level in log_levels:
    if level in ["ERROR", "WARNING"]:
        print(f"Alert: {level} message found")

print()

print("Pattern 4: Early exit with flag")
user_list = ["alice", "bob", "admin", "charlie", "david"]
target_user = "admin"
found = False

for user in user_list:
    print(f"Checking user: {user}")
    if user == target_user:
        print(f"Target user '{target_user}' found!")
        found = True
        break

if not found:
    print(f"Target user '{target_user}' not found")
print()

# -----------------------------------------------------------------------------
# 10. EXERCISES FOR PRACTICE
# -----------------------------------------------------------------------------

print("10. Try It Yourself!")
print("-" * 22)
print("Practice exercises to master loops and control flow:")
print()

print("Exercise 1: Number guessing game")
print("- Use a while loop to keep asking for guesses")
print("- Give hints (too high/too low)")
print("- Break when correct number is found")
print("- Limit to maximum 5 attempts")
print()

print("Exercise 2: Password strength analyzer")
print("- Check multiple criteria: length, digits, uppercase, lowercase")
print("- Use loops to examine each character")
print("- Provide detailed feedback on what's missing")
print("- Continue until strong password is entered")
print()

print("Exercise 3: Data processing")
print("- Process a list of temperatures")
print("- Calculate average, min, max using loops")
print("- Count how many are above/below average")
print("- Skip any invalid readings (use continue)")
print()

print("Exercise 4: Multiplication table")
print("- Use nested loops to create a multiplication table")
print("- Format output neatly")
print("- Allow user to specify table size")
print("- Add headers and borders")
print()

# TODO for students: Uncomment and complete these exercises

# # Exercise 1: Number guessing game
# print("\n--- Exercise 1: Number guessing game ---")
# secret_number = 42
# attempts = 0
# max_attempts = 5
# # Implement guessing game with while loop

# # Exercise 2: Password strength analyzer
# print("\n--- Exercise 2: Password strength analyzer ---")
# test_password = "TestPass123"
# # Check various criteria using loops and conditions

# # Exercise 3: Data processing
# print("\n--- Exercise 3: Data processing ---")
# temperatures = [23.5, 19.2, 25.8, -2.0, 30.1, 22.7, 999, 18.9]
# # Process temperatures, skip invalid readings (like 999)

# # Exercise 4: Multiplication table
# print("\n--- Exercise 4: Multiplication table ---")
# size = 5
# # Create multiplication table using nested loops

print("\n" + "=" * 55)
print("End of Session 07 - Great work with loops and control flow!")
print("Loops are essential for automation - practice these patterns!")