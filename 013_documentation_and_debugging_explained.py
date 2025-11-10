"""
Session 13: Documentation and Debugging Techniques
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Master writing clear and comprehensive documentation
- Understand docstring conventions and best practices
- Learn debugging techniques and strategies
- Practice using Python's debugging tools
- Identify and fix common programming errors
- Develop systematic problem-solving approaches
- Apply documentation standards to real projects
- Build debugging skills for efficient troubleshooting

Author: Programming Instructor
Date: 10-Nov-2025
"""

# =============================================================================
# DOCUMENTATION AND DEBUGGING TECHNIQUES
# =============================================================================

print("Welcome to Session 13: Documentation and Debugging")
print("=" * 51)
print()

print("This session covers essential development skills:")
print("- Writing clear documentation with docstrings")
print("- Understanding documentation formats")
print("- Debugging techniques and tools")
print("- Common error patterns and solutions")
print("- Systematic troubleshooting approaches")
print()

# -----------------------------------------------------------------------------
# 1. INTRODUCTION TO DOCUMENTATION
# -----------------------------------------------------------------------------

print("1. Introduction to Documentation")
print("-" * 31)

print("Why documentation matters:")
print("- Helps others understand your code")
print("- Reminds you how your code works later")
print("- Makes code maintainable and professional")
print("- Required in team environments")
print("- Essential for API and library development")
print()

print("Types of documentation:")
print("- Inline comments: Brief explanations within code")
print("- Docstrings: Function/class/module descriptions")
print("- README files: Project overview and setup")
print("- API documentation: Interface specifications")
print("- User guides: How to use the software")
print()

print("Documentation best practices:")
print("- Write documentation as you code, not after")
print("- Keep it clear, concise, and accurate")
print("- Update documentation when code changes")
print("- Explain WHY, not just WHAT")
print("- Use examples to illustrate usage")
print()

# -----------------------------------------------------------------------------
# 2. DOCSTRING BASICS
# -----------------------------------------------------------------------------

print("2. Docstring Basics")
print("-" * 17)

print("What are docstrings?")
print("- Documentation strings using triple quotes")
print("- First statement in function/class/module")
print("- Accessible via __doc__ attribute")
print("- Used by help() function and documentation tools")
print()

# Basic docstring example
def greet_user(name):
    """
    Greet a user by name.
    
    Args:
        name (str): The name of the user to greet
    
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! Welcome to the system."

print("Example function with basic docstring:")
print(greet_user("Alice"))
print()

print("Accessing docstring:")
print(greet_user.__doc__)
print()

print("Using help() function:")
help(greet_user)
print()

# -----------------------------------------------------------------------------
# 3. COMPREHENSIVE DOCSTRING FORMAT
# -----------------------------------------------------------------------------

print("3. Comprehensive Docstring Format")
print("-" * 34)

import re

def validate_ip_address(ip_string):
    """
    Validate IPv4 address format and range.
    
    This function checks if a given string represents a valid IPv4 address
    by verifying both the format (four octets separated by dots) and the
    range (each octet must be 0-255).
    
    Args:
        ip_string (str): The IP address string to validate
    
    Returns:
        bool: True if the IP address is valid, False otherwise
    
    Raises:
        TypeError: If ip_string is not a string
    
    Examples:
        >>> validate_ip_address('192.168.1.1')
        True
        >>> validate_ip_address('255.255.255.255')
        True
        >>> validate_ip_address('999.999.999.999')
        False
        >>> validate_ip_address('192.168.1')
        False
    
    Note:
        This function only validates IPv4 addresses, not IPv6.
        It does not check if the IP is reserved or private.
    """
    if not isinstance(ip_string, str):
        raise TypeError("IP address must be a string")
    
    # Check format using regex
    pattern = r'^(\\d{1,3}\\.){3}\\d{1,3}$'
    if not re.match(pattern, ip_string):
        return False
    
    # Check range for each octet
    octets = ip_string.split('.')
    return all(0 <= int(octet) <= 255 for octet in octets)

print("Example: Comprehensive docstring for IP validation")
print()

# Test the function
test_ips = ['192.168.1.1', '255.255.255.255', '999.999.999.999', '192.168.1']
print("Testing IP validation:")
for ip in test_ips:
    result = validate_ip_address(ip)
    print(f"  {ip:<20} -> {'Valid' if result else 'Invalid'}")
print()

print("Docstring sections explained:")
print("- Summary: One-line description")
print("- Description: Detailed explanation (optional)")
print("- Args: Parameters with types and descriptions")
print("- Returns: Return value type and description")
print("- Raises: Exceptions that may be raised")
print("- Examples: Usage examples with expected output")
print("- Note/Warning: Additional important information")
print()

# -----------------------------------------------------------------------------
# 4. DOCSTRING EXAMPLE - PASSWORD VALIDATION
# -----------------------------------------------------------------------------

print("4. Docstring Example - Password Validation")
print("-" * 41)

def check_password_strength(password):
    """
    Validate password strength based on security requirements.
    
    This function checks if a password meets minimum security requirements:
    - At least 12 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (!@#$%^&*())
    
    Args:
        password (str): The password string to validate
    
    Returns:
        bool: True if password meets all requirements, False otherwise
    
    Examples:
        >>> check_password_strength('WeakPass')
        False
        >>> check_password_strength('StrongP@ssw0rd123')
        True
        >>> check_password_strength('Short1!')
        False
    
    Note:
        This is a basic implementation. Production systems should use
        additional checks like common password dictionaries and entropy
        calculation.
    
    Security:
        Do not log or print passwords in production code.
    """
    # Check minimum length
    if len(password) < 12:
        return False
    
    # Initialize check flags
    has_special = False
    has_lower = False
    has_upper = False
    has_digit = False
    
    # Check each character
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in '!@#$%^&*()':
            has_special = True
    
    # All conditions must be met
    return has_upper and has_lower and has_digit and has_special

print("Example: Password strength validation")
print()

test_passwords = [
    'short',
    'nouppercase123!',
    'NOLOWERCASE123!',
    'NoDigits!',
    'NoSpecialChar123',
    'StrongP@ssw0rd123'
]

print("Testing passwords:")
for pwd in test_passwords:
    result = check_password_strength(pwd)
    status = "Strong" if result else "Weak"
    print(f"  {pwd:<25} -> {status}")
print()

# Accessing docstring
print("Password checker documentation:")
print(check_password_strength.__doc__[:200] + "...")
print()

# -----------------------------------------------------------------------------
# 5. INLINE COMMENTS VS DOCSTRINGS
# -----------------------------------------------------------------------------

print("5. Inline Comments vs Docstrings")
print("-" * 32)

def process_security_log(log_line):
    """
    Parse and categorize a security log entry.
    
    Args:
        log_line (str): A single line from the security log
    
    Returns:
        dict: Parsed log entry with timestamp, level, and message
    """
    # Split the log line into components
    parts = log_line.split(' ', 2)  # Limit split to 3 parts
    
    if len(parts) < 3:
        # Invalid log format - return error indicator
        return {'error': 'Invalid log format'}
    
    # Extract timestamp (first part)
    timestamp = parts[0]
    
    # Extract log level (second part)
    level = parts[1].upper()
    
    # Extract message (everything after level)
    message = parts[2] if len(parts) > 2 else ''
    
    # Build result dictionary
    result = {
        'timestamp': timestamp,
        'level': level,
        'message': message,
        'severity': 'HIGH' if level in ['ERROR', 'CRITICAL'] else 'LOW'
    }
    
    return result

print("Inline comments guidelines:")
print("- Use for complex logic that needs explanation")
print("- Explain WHY something is done, not WHAT")
print("- Keep comments short and relevant")
print("- Update comments when code changes")
print("- Don't state the obvious")
print()

print("BAD comment example:")
print("  # Increment counter by 1")
print("  counter += 1")
print()

print("GOOD comment example:")
print("  # Skip invalid entries to prevent processing errors")
print("  if not is_valid(entry):")
print("      continue")
print()

# Test the function
sample_log = "2025-11-10 ERROR Database connection failed"
parsed = process_security_log(sample_log)
print(f"Parsed log entry: {parsed}")
print()

# -----------------------------------------------------------------------------
# 6. INTRODUCTION TO DEBUGGING
# -----------------------------------------------------------------------------

print("6. Introduction to Debugging")
print("-" * 27)

print("What is debugging?")
print("- Finding and fixing errors in code")
print("- Understanding program behavior")
print("- Identifying logic problems")
print("- Systematic problem-solving process")
print()

print("Types of errors:")
print("- Syntax errors: Code structure mistakes (caught by Python)")
print("- Runtime errors: Errors during execution (exceptions)")
print("- Logic errors: Code runs but produces wrong results")
print("- Semantic errors: Code doesn't do what you intended")
print()

print("Debugging strategies:")
print("1. Read error messages carefully")
print("2. Print intermediate values")
print("3. Use debugger to step through code")
print("4. Simplify the problem (divide and conquer)")
print("5. Check assumptions about data and logic")
print("6. Use test cases to isolate issues")
print()

# -----------------------------------------------------------------------------
# 7. COMMON ERRORS AND DEBUGGING
# -----------------------------------------------------------------------------

print("7. Common Errors and Debugging")
print("-" * 30)

print("Example 1: Off-by-one error")
print()

def calculate_avg_age_buggy(students):
    """Calculate average age (with bug)"""
    age = 0
    # BUG: range(len(students)-1) misses last student!
    for student_idx in range(len(students) - 1):
        age = age + students[student_idx]
    return age / len(students)

def calculate_avg_age_fixed(students):
    """Calculate average age (fixed version)"""
    age = 0
    # FIX: Use range(len(students)) to include all students
    for student_idx in range(len(students)):
        age = age + students[student_idx]
    return age / len(students)

def calculate_avg_age_pythonic(students):
    """Calculate average age (Pythonic version)"""
    # Even better: use built-in sum() function
    return sum(students) / len(students)

students = [20, 20, 30, 30]

print(f"Student ages: {students}")
print(f"Buggy version result: {calculate_avg_age_buggy(students)}")
print(f"Fixed version result: {calculate_avg_age_fixed(students)}")
print(f"Pythonic version result: {calculate_avg_age_pythonic(students)}")
print(f"Expected average: {(20 + 20 + 30 + 30) / 4}")
print()

print("How to find off-by-one errors:")
print("- Add print statements inside loops")
print("- Check loop boundaries carefully")
print("- Test with small datasets")
print("- Verify first and last iterations")
print()

print("Example 2: Type errors")
print()

def add_numbers_unsafe(a, b):
    """Add two numbers without type checking"""
    return a + b

def add_numbers_safe(a, b):
    """Add two numbers with type checking"""
    try:
        # Convert to numbers if possible
        num_a = float(a)
        num_b = float(b)
        return num_a + num_b
    except (ValueError, TypeError) as e:
        print(f"Error: Cannot add {a} and {b} - {e}")
        return None

print("Testing addition functions:")
print(f"add_numbers_safe(5, 10) = {add_numbers_safe(5, 10)}")
print(f"add_numbers_safe('5', '10') = {add_numbers_safe('5', '10')}")
print(f"add_numbers_safe('5', 'abc') = {add_numbers_safe('5', 'abc')}")
print()

print("Example 3: Index out of bounds")
print()

def get_first_three_safe(items):
    """Safely get first three items from list"""
    result = []
    
    # Check if list has at least 3 items
    if len(items) < 3:
        print(f"Warning: List only has {len(items)} items")
        return items.copy()
    
    # Safe to access first three items
    return items[:3]

test_lists = [
    [1, 2, 3, 4, 5],
    [1, 2],
    []
]

print("Testing safe list access:")
for lst in test_lists:
    result = get_first_three_safe(lst)
    print(f"  {lst} -> {result}")
print()

# -----------------------------------------------------------------------------
# 8. DEBUGGING TECHNIQUES
# -----------------------------------------------------------------------------

print("8. Debugging Techniques")
print("-" * 21)

print("Technique 1: Print debugging")
print()

def find_maximum_value(numbers):
    """Find maximum value in list with debug prints"""
    if not numbers:
        return None
    
    max_value = numbers[0]
    print(f"DEBUG: Starting with max_value = {max_value}")
    
    for i, num in enumerate(numbers[1:], start=1):
        print(f"DEBUG: Checking numbers[{i}] = {num}")
        
        if num > max_value:
            print(f"DEBUG: Found new maximum: {num} > {max_value}")
            max_value = num
        else:
            print(f"DEBUG: {num} is not greater than {max_value}")
    
    print(f"DEBUG: Final maximum = {max_value}")
    return max_value

test_numbers = [5, 2, 9, 1, 7, 3]
print(f"Finding maximum in {test_numbers}:")
result = find_maximum_value(test_numbers)
print(f"Result: {result}")
print()

print("Technique 2: Assert statements")
print()

def calculate_percentage(part, total):
    """Calculate percentage with assertions for validation"""
    # Precondition checks
    assert isinstance(part, (int, float)), "Part must be a number"
    assert isinstance(total, (int, float)), "Total must be a number"
    assert total > 0, "Total must be positive"
    assert part >= 0, "Part must be non-negative"
    assert part <= total, "Part cannot exceed total"
    
    percentage = (part / total) * 100
    
    # Postcondition check
    assert 0 <= percentage <= 100, "Percentage must be between 0 and 100"
    
    return percentage

print("Testing percentage calculation with assertions:")
try:
    print(f"calculate_percentage(25, 100) = {calculate_percentage(25, 100)}%")
    print(f"calculate_percentage(50, 200) = {calculate_percentage(50, 200)}%")
    
    # This will trigger assertion error
    print(f"calculate_percentage(150, 100) = {calculate_percentage(150, 100)}%")
except AssertionError as e:
    print(f"Assertion Error caught: {e}")
print()

print("Technique 3: Logging instead of printing")
print()

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_user_data(username, age):
    """Process user data with proper logging"""
    logging.info(f"Processing user: {username}")
    
    if not username or not username.strip():
        logging.error("Empty username provided")
        return False
    
    if not isinstance(age, int):
        logging.warning(f"Age is not integer: {age} ({type(age).__name__})")
        try:
            age = int(age)
            logging.info(f"Successfully converted age to integer: {age}")
        except ValueError:
            logging.error(f"Cannot convert age to integer: {age}")
            return False
    
    if age < 0 or age > 150:
        logging.error(f"Invalid age value: {age}")
        return False
    
    logging.debug(f"User data validated: {username}, age {age}")
    logging.info("User data processed successfully")
    return True

print("Processing user data with logging:")
process_user_data("Alice", 25)
process_user_data("", 30)
process_user_data("Bob", "invalid")
print()

# -----------------------------------------------------------------------------
# 9. DEBUGGING WITH BREAKPOINT (CONCEPT)
# -----------------------------------------------------------------------------

print("9. Debugging with Breakpoint (Concept)")
print("-" * 39)

print("The breakpoint() function:")
print("- Pauses program execution at specific point")
print("- Opens interactive debugger (pdb)")
print("- Allows inspection of variables")
print("- Enables step-by-step execution")
print()

print("Common debugger commands:")
print("- n (next): Execute next line")
print("- s (step): Step into function")
print("- c (continue): Continue until next breakpoint")
print("- p <var>: Print variable value")
print("- l (list): Show current code location")
print("- q (quit): Exit debugger")
print()

print("Example code with breakpoint (commented out):")
print('''
def complex_calculation(x, y):
    result = x * 2
    # breakpoint()  # Debugger would pause here
    result = result + y
    # breakpoint()  # And here
    return result
''')
print()

print("Note: breakpoint() is commented out to allow script to run")
print("In practice, you would uncomment it to debug interactively")
print()

# Example without actual breakpoint
def complex_calculation_example(x, y):
    """Example calculation with debugging comments"""
    result = x * 2
    print(f"DEBUG: After multiplication: result = {result}")
    # In real debugging, you would use: breakpoint()
    
    result = result + y
    print(f"DEBUG: After addition: result = {result}")
    # In real debugging, you would use: breakpoint()
    
    return result

print("Running calculation with debug prints:")
final_result = complex_calculation_example(5, 10)
print(f"Final result: {final_result}")
print()

# -----------------------------------------------------------------------------
# 10. SYSTEMATIC DEBUGGING APPROACH
# -----------------------------------------------------------------------------

print("10. Systematic Debugging Approach")
print("-" * 33)

print("Step-by-step debugging process:")
print()

print("1. REPRODUCE THE ERROR")
print("   - Create a test case that consistently fails")
print("   - Identify exact conditions that trigger the bug")
print()

print("2. ISOLATE THE PROBLEM")
print("   - Narrow down which part of code has the issue")
print("   - Use binary search approach (comment out half)")
print("   - Check inputs and outputs of each function")
print()

print("3. UNDERSTAND THE ERROR")
print("   - Read error messages completely")
print("   - Identify the error type and location")
print("   - Trace back through the stack trace")
print()

print("4. FORM A HYPOTHESIS")
print("   - What do you think is causing the error?")
print("   - What assumptions might be wrong?")
print("   - Consider edge cases and special conditions")
print()

print("5. TEST YOUR HYPOTHESIS")
print("   - Add print statements or use debugger")
print("   - Check variable values at key points")
print("   - Verify your assumptions about the data")
print()

print("6. FIX THE BUG")
print("   - Implement the fix")
print("   - Test with original failing case")
print("   - Test with additional edge cases")
print()

print("7. DOCUMENT THE FIX")
print("   - Add comments explaining the fix")
print("   - Update documentation if needed")
print("   - Consider if similar bugs exist elsewhere")
print()

# -----------------------------------------------------------------------------
# 11. PRACTICE EXERCISES
# -----------------------------------------------------------------------------

print("11. Practice Exercises")
print("-" * 20)
print("Complete these exercises to master documentation and debugging!")
print()

print("Exercise 1: Write Comprehensive Docstrings")
print("Description: Add proper documentation to functions")
print("Requirements:")
print("  - Write complete docstrings for given functions")
print("  - Include all standard sections (Args, Returns, Examples)")
print("  - Add type hints where appropriate")
print("  - Document any exceptions that might be raised")
print()

# TODO for students
# def validate_email(email):
#     # TODO: Add comprehensive docstring
#     # Check if email contains @ and .
#     # Return True if valid, False otherwise
#     pass

# def calculate_network_subnet(ip, mask):
#     # TODO: Add comprehensive docstring
#     # Calculate network address and broadcast address
#     # Return dict with network details
#     pass

print("Exercise 2: Debug the Age Calculator")
print("Description: Find and fix bugs in age calculation function")
print("Bug: Function returns incorrect average")
print()

# def calculate_class_average_buggy(student_ages):
#     """Calculate average age of students (contains bugs)"""
#     total = 0
#     count = 0
#     
#     for age in student_ages[:-1]:  # BUG: Skips last student
#         total += age
#         count += 1
#     
#     if count = 0:  # BUG: Should be ==
#         return 0
#     
#     return total / len(student_ages)  # BUG: Should use count

# TODO for students: Find and fix the three bugs
# Test with: [20, 22, 21, 23, 24]
# Expected: 22.0

print("Exercise 3: Debug the Password Validator")
print("Description: Fix logical errors in password validation")
print("Bug: Function accepts weak passwords")
print()

# def validate_password_buggy(password):
#     """Validate password strength (contains logic bugs)"""
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special = False
#     
#     if len(password) > 8:  # BUG: Should be >= not >
#         return False
#     
#     for char in password:
#         if char.isupper():
#             has_upper == True  # BUG: Should be = not ==
#         if char.islower():
#             has_lower = True
#         if char.isdigit():
#             has_digit = True
#         if char in '!@#$%':
#             has_special = True
#     
#     return has_upper or has_lower or has_digit or has_special  # BUG: Should be and

# TODO for students: Find and fix the three bugs
# Test with: "Weak1", "StrongP@ss1", "short"

print("Exercise 4: Add Debug Logging")
print("Description: Add comprehensive logging to function")
print("Requirements:")
print("  - Add appropriate log levels (DEBUG, INFO, WARNING, ERROR)")
print("  - Log function entry and exit")
print("  - Log important intermediate values")
print("  - Log any error conditions")
print()

# TODO for students
# def process_security_event(event_type, severity, details):
#     # TODO: Add comprehensive logging
#     # Validate inputs
#     # Process event based on severity
#     # Return processing result
#     pass

print("Exercise 5: Debug List Processing")
print("Description: Fix index and logic errors")
print("Bug: Function crashes with index errors")
print()

# def find_duplicates_buggy(numbers):
#     """Find duplicate numbers in list (contains bugs)"""
#     duplicates = []
#     
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers) + 1):  # BUG: Index out of bounds
#             if numbers[i] = numbers[j]:  # BUG: Should be ==
#                 if numbers[i] not in duplicates:
#                     duplicates.append(numbers[i])
#     
#     return duplicates

# TODO for students: Find and fix the bugs
# Test with: [1, 2, 3, 2, 4, 1, 5]
# Expected: [1, 2]

print("Exercise 6: Write Unit Tests")
print("Description: Create test cases for given function")
print("Requirements:")
print("  - Test normal cases")
print("  - Test edge cases (empty input, single item, etc.)")
print("  - Test error cases (invalid input)")
print("  - Add assertions to verify results")
print()

# TODO for students
# def calculate_discount(price, discount_percent):
#     '''Calculate final price after discount'''
#     if discount_percent < 0 or discount_percent > 100:
#         raise ValueError("Discount must be between 0 and 100")
#     discount_amount = price * (discount_percent / 100)
#     return price - discount_amount

# Write comprehensive tests:
# def test_calculate_discount():
#     # TODO: Add test cases
#     pass

print("Exercise 7: Debug Network Scanner")
print("Description: Fix bugs in network scanning simulation")
print("Bug: Function returns incorrect results")
print()

# def scan_network_buggy(ip_range, timeout):
#     """Scan network for active hosts (contains bugs)"""
#     active_hosts = []
#     
#     for ip in ip_range:
#         # Simulate network check (buggy logic)
#         octets = ip.split('.')
#         if len(octets) != 4:  # BUG: Should continue, not return
#             return []
#         
#         last_octet = int(octets[-1])
#         if last_octet % 2:  # BUG: Should be == 0 for even
#             active_hosts.append(ip)
#     
#     return active_hosts[::-1]  # BUG: Should not reverse

# TODO for students: Find and fix the bugs
# Test with: ['192.168.1.2', '192.168.1.4', '192.168.1.5']
# Expected: ['192.168.1.2', '192.168.1.4']

print("Exercise 8: Comprehensive Debugging Project")
print("Description: Debug complete security log analyzer")
print("Bug: Multiple logical and runtime errors")
print()

# TODO for students: Create and debug complete program
# Requirements:
# - Read security logs from file
# - Parse log entries with error handling
# - Calculate statistics (events per type, severity distribution)
# - Generate report with findings
# - Add comprehensive error handling
# - Include detailed logging
# - Write proper documentation

print()
print("=" * 51)
print("End of Session 13 - Excellent work with documentation!")
print("Good documentation makes code maintainable and professional!")
print("Debugging skills improve with practice - keep at it!")
print()
print("Key takeaways:")
print("- Always write docstrings for functions and classes")
print("- Document WHY, not just WHAT")
print("- Use systematic approach to debugging")
print("- Test edge cases and error conditions")
print("- Use appropriate tools (print, logging, debugger)")
print("- Read error messages carefully")
print("- Practice makes perfect!")
