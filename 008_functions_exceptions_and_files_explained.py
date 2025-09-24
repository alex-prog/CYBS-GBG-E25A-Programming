"""
Session 08: Functions, Exception Handling, and File Operations
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Master function definition and calling
- Understand parameters, arguments, and return values
- Learn default parameters and flexible argument handling
- Master exception handling with try/except/finally blocks
- Practice defensive programming and error handling
- Understand function scope and variable visibility
- Apply functions to solve modular programming problems
- Learn best practices for code organization

Author: Programming Instructor
Date: 24-Sep-2025
"""

# =============================================================================
# FUNCTIONS, EXCEPTIONS, AND ADVANCED PROGRAMMING CONCEPTS
# =============================================================================

print("Welcome to Session 08: Functions and Exception Handling")
print("=" * 58)
print()

# -----------------------------------------------------------------------------
# 1. FUNCTION BASICS - DEFINITION AND CALLING
# -----------------------------------------------------------------------------

print("1. Function Basics - Definition and Calling")
print("-" * 40)

# Functions are reusable blocks of code that perform specific tasks
print("What are functions?")
print("- Reusable blocks of code")
print("- Take inputs (parameters) and optionally return outputs")
print("- Help organize and structure your programs")
print("- Reduce code duplication")
print()

# Simple function example
def greet_user():
    """Simple function with no parameters"""
    print("Hello, welcome to the security system!")

print("Example 1: Function without parameters")
print("Calling greet_user():")
greet_user()
print()

# Function with parameters
def greet_user_by_name(username):
    """Function with one parameter"""
    print(f"Hello {username}, welcome to the security system!")

print("Example 2: Function with parameters")
print("Calling greet_user_by_name('Alice'):")
greet_user_by_name('Alice')
print()

# Function with multiple parameters
def create_user_account(username, role, department):
    """Function with multiple parameters"""
    print(f"Creating account for: {username}")
    print(f"Role: {role}")
    print(f"Department: {department}")
    print("Account created successfully!")

print("Example 3: Function with multiple parameters")
print("Calling create_user_account('Bob', 'Analyst', 'Cybersecurity'):")
create_user_account('Bob', 'Analyst', 'Cybersecurity')
print()

# -----------------------------------------------------------------------------
# 2. FUNCTIONS WITH RETURN VALUES
# -----------------------------------------------------------------------------

print("2. Functions with Return Values")
print("-" * 30)

def add_numbers(a, b):
    """Function that returns a value"""
    result = a + b
    return result

print("Example: Function that returns a value")
sum_result = add_numbers(10, 20)
print(f"add_numbers(10, 20) returns: {sum_result}")

# You can use the return value directly
print(f"Direct use: add_numbers(5, 3) = {add_numbers(5, 3)}")
print()

# More practical example with return values
def calculate_password_strength(password):
    """Calculate password strength score"""
    score = 0
    
    # Length check
    if len(password) >= 8:
        score += 2
    elif len(password) >= 6:
        score += 1
    
    # Character type checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 2
    
    return score

print("Password strength calculator:")
test_passwords = ["weak", "Stronger1", "VeryStrong123!", "a"]

for pwd in test_passwords:
    strength = calculate_password_strength(pwd)
    print(f"'{pwd}' -> Strength score: {strength}/8")
print()

# -----------------------------------------------------------------------------
# 3. DEFAULT PARAMETERS
# -----------------------------------------------------------------------------

print("3. Default Parameters")
print("-" * 19)

def password_checker(password, min_length=8, max_length=64):
    """Function with default parameters"""
    
    # Validate minimum length parameter
    if min_length < 6:
        return "Error: Minimum length cannot be less than 6"
    
    if max_length > 128:
        return "Error: Maximum length cannot exceed 128"
    
    # Check password length
    if len(password) < min_length:
        return f"Password too short. Minimum {min_length} characters required."
    elif len(password) > max_length:
        return f"Password too long. Maximum {max_length} characters allowed."
    else:
        return "Password length is acceptable."

print("Example: Function with default parameters")
print("password_checker(password, min_length=8, max_length=64)")
print()

# Test with different parameter combinations
test_cases = [
    ("bob123", {}),  # Use all defaults
    ("bob123", {"min_length": 10}),  # Override min_length only
    ("verylongpasswordthatexceedslimits" * 3, {"max_length": 32}),  # Override max_length
    ("good_password_123", {"min_length": 10, "max_length": 20})  # Override both
]

for password, kwargs in test_cases:
    result = password_checker(password, **kwargs)
    params_used = f"min_length={kwargs.get('min_length', 8)}, max_length={kwargs.get('max_length', 64)}"
    print(f"'{password[:15]}...' [{params_used}]")
    print(f"  -> {result}")
print()

print("Default parameter benefits:")
print("- Make functions more flexible")
print("- Reduce the need for multiple similar functions")
print("- Allow backward compatibility when adding new parameters")
print("- Provide sensible defaults for common use cases")
print()

# -----------------------------------------------------------------------------
# 4. ADVANCED FUNCTION FEATURES
# -----------------------------------------------------------------------------

print("4. Advanced Function Features")
print("-" * 28)

# Type hints (good practice for documentation)
def secure_add(a: int, b: int) -> int:
    """Add two numbers with type hints"""
    total = a + b
    return total

print("Type hints help document expected types:")
print("def secure_add(a: int, b: int) -> int:")
result = secure_add(15, 25)
print(f"secure_add(15, 25) = {result}")
print()

# Multiple return values using tuples
def analyze_log_entry(log_line):
    """Analyze a log entry and return multiple values"""
    parts = log_line.split(" ")
    if len(parts) >= 4:
        timestamp = parts[0]
        level = parts[1]
        source = parts[2]
        message = " ".join(parts[3:])
        
        # Determine severity
        if level in ["ERROR", "CRITICAL"]:
            severity = "HIGH"
        elif level == "WARNING":
            severity = "MEDIUM"
        else:
            severity = "LOW"
        
        return timestamp, level, source, message, severity
    else:
        return None, None, None, "Invalid log format", "UNKNOWN"

print("Multiple return values example:")
sample_log = "2025-09-24 ERROR firewall Connection blocked from suspicious IP"
timestamp, level, source, message, severity = analyze_log_entry(sample_log)

print(f"Log analysis results:")
print(f"  Timestamp: {timestamp}")
print(f"  Level: {level}")
print(f"  Source: {source}")
print(f"  Message: {message}")
print(f"  Severity: {severity}")
print()

# -----------------------------------------------------------------------------
# 5. EXCEPTION HANDLING BASICS
# -----------------------------------------------------------------------------

print("5. Exception Handling Basics")
print("-" * 27)

print("What are exceptions?")
print("- Errors that occur during program execution")
print("- Can crash your program if not handled")
print("- Python provides try/except blocks to handle them gracefully")
print()

# Basic exception handling
def safe_division(a, b):
    """Safely divide two numbers"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Both values must be numbers!")
        return None

print("Example: Safe division function")
test_cases = [(10, 2), (10, 0), (10, "invalid")]

for a, b in test_cases:
    print(f"safe_division({a}, {b}):")
    result = safe_division(a, b)
    if result is not None:
        print(f"  Result: {result}")
    print()

# -----------------------------------------------------------------------------
# 6. ADVANCED EXCEPTION HANDLING
# -----------------------------------------------------------------------------

print("6. Advanced Exception Handling")
print("-" * 30)

def validate_and_convert_input(user_input):
    """Validate user input and convert to integer"""
    try:
        # Attempt to convert to integer
        number = int(user_input)
        
        # Additional validation
        if number < 0:
            raise ValueError("Number must be positive")
        
        return number
        
    except ValueError as e:
        # Handle conversion errors and custom validation
        if "invalid literal" in str(e):
            raise Exception(f"'{user_input}' is not a valid number")
        else:
            raise Exception(str(e))
    except Exception as e:
        # Catch any other unexpected errors
        raise Exception(f"Unexpected error: {e}")

# Demonstrate exception handling with try/except/finally
def process_user_input():
    """Process user input with comprehensive error handling"""
    print("User input processing simulation:")
    
    # Simulate different user inputs
    test_inputs = ["42", "-5", "abc", "123"]
    
    for user_input in test_inputs:
        print(f"Processing input: '{user_input}'")
        
        try:
            number = validate_and_convert_input(user_input)
            print(f"  Success: Valid number {number}")
            
        except Exception as error:
            print(f"  Error: {error}")
            
        finally:
            print("  Processing complete for this input")
        
        print()

process_user_input()

print("Exception handling best practices:")
print("- Use specific exception types when possible")
print("- Provide meaningful error messages")
print("- Use finally blocks for cleanup code")
print("- Don't catch exceptions you can't handle properly")
print("- Log errors for debugging purposes")
print()

# -----------------------------------------------------------------------------
# 7. CREATING CUSTOM EXCEPTIONS
# -----------------------------------------------------------------------------

print("7. Creating Custom Exceptions")
print("-" * 29)

# Custom exception classes
class PasswordTooShortError(Exception):
    """Custom exception for passwords that are too short"""
    pass

class PasswordTooCommonError(Exception):
    """Custom exception for commonly used passwords"""
    pass

class InvalidCharacterError(Exception):
    """Custom exception for invalid characters in password"""
    pass

def advanced_password_validator(password):
    """Advanced password validation with custom exceptions"""
    
    # Common passwords to avoid
    common_passwords = ["password", "123456", "admin", "qwerty", "letmein"]
    
    # Check minimum length
    if len(password) < 8:
        raise PasswordTooShortError(f"Password must be at least 8 characters (got {len(password)})")
    
    # Check for common passwords
    if password.lower() in common_passwords:
        raise PasswordTooCommonError(f"'{password}' is a commonly used password")
    
    # Check for invalid characters (for this example, no spaces allowed)
    if ' ' in password:
        raise InvalidCharacterError("Password cannot contain spaces")
    
    # If we reach here, password is valid
    return True

print("Custom exception handling example:")
test_passwords = ["secure123", "short", "password", "has spaces", "ValidPass123"]

for pwd in test_passwords:
    print(f"Testing password: '{pwd}'")
    
    try:
        if advanced_password_validator(pwd):
            print("  Password is valid!")
    
    except PasswordTooShortError as e:
        print(f"  Length Error: {e}")
    
    except PasswordTooCommonError as e:
        print(f"  Security Error: {e}")
    
    except InvalidCharacterError as e:
        print(f"  Character Error: {e}")
    
    except Exception as e:
        print(f"  Unexpected Error: {e}")
    
    print()

# -----------------------------------------------------------------------------
# 8. FUNCTION SCOPE AND VARIABLES
# -----------------------------------------------------------------------------

print("8. Function Scope and Variables")
print("-" * 30)

# Global variables
security_level = "HIGH"
login_attempts = 0

def check_security_clearance(user_role):
    """Demonstrate local vs global variable scope"""
    
    # Local variables
    clearance_levels = ["LOW", "MEDIUM", "HIGH", "CLASSIFIED"]
    user_clearance = "MEDIUM"  # This is local to this function
    
    # Access global variable (read-only)
    print(f"Current system security level: {security_level}")
    
    # Modify global variable using 'global' keyword
    global login_attempts
    login_attempts += 1
    print(f"Login attempts so far: {login_attempts}")
    
    # Local logic
    if user_role == "admin":
        user_clearance = "CLASSIFIED"
    elif user_role == "manager":
        user_clearance = "HIGH"
    
    return user_clearance

print("Variable scope demonstration:")
print("Global variables: security_level, login_attempts")

user_clearance_1 = check_security_clearance("admin")
print(f"Admin clearance: {user_clearance_1}")

user_clearance_2 = check_security_clearance("user")
print(f"User clearance: {user_clearance_2}")

print(f"Final login attempts: {login_attempts}")
print()

print("Scope rules:")
print("- Variables defined in functions are local to that function")
print("- Global variables can be read from anywhere")
print("- Use 'global' keyword to modify global variables in functions")
print("- Local variables 'shadow' global variables with the same name")
print()

# -----------------------------------------------------------------------------
# 9. PRACTICAL FUNCTION EXAMPLES
# -----------------------------------------------------------------------------

print("9. Practical Function Examples")
print("-" * 29)

def log_security_event(event_type, user, details, severity="INFO"):
    """Log a security event with timestamp"""
    from datetime import datetime
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {severity}: {event_type} - User: {user} - {details}"
    
    # In a real application, this would write to a file
    print(f"LOG: {log_entry}")
    
    return log_entry

def validate_ip_address(ip):
    """Validate if a string is a valid IP address"""
    parts = ip.split('.')
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        try:
            num = int(part)
            if not (0 <= num <= 255):
                return False
        except ValueError:
            return False
    
    return True

def calculate_network_range(base_ip, subnet_mask):
    """Calculate network range (simplified example)"""
    if not validate_ip_address(base_ip):
        raise ValueError(f"Invalid IP address: {base_ip}")
    
    # Simplified calculation for demonstration
    ip_parts = [int(x) for x in base_ip.split('.')]
    
    if subnet_mask == 24:  # /24 network
        network = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0"
        broadcast = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.255"
        hosts = 254
    elif subnet_mask == 16:  # /16 network
        network = f"{ip_parts[0]}.{ip_parts[1]}.0.0"
        broadcast = f"{ip_parts[0]}.{ip_parts[1]}.255.255"
        hosts = 65534
    else:
        raise ValueError(f"Subnet mask /{subnet_mask} not supported in this example")
    
    return {
        'network': network,
        'broadcast': broadcast,
        'available_hosts': hosts,
        'subnet_mask': f"/{subnet_mask}"
    }

print("Practical examples in action:")

# Logging example
log_security_event("LOGIN", "alice", "Successful authentication")
log_security_event("FAILED_LOGIN", "unknown", "Multiple failed attempts", "WARNING")

print()

# IP validation example
test_ips = ["192.168.1.1", "256.1.1.1", "192.168.1", "10.0.0.1"]
for ip in test_ips:
    is_valid = validate_ip_address(ip)
    print(f"IP '{ip}': {'Valid' if is_valid else 'Invalid'}")

print()

# Network calculation example
try:
    network_info = calculate_network_range("192.168.1.100", 24)
    print("Network calculation results:")
    for key, value in network_info.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
except ValueError as e:
    print(f"Network calculation error: {e}")

print()

# -----------------------------------------------------------------------------
# 10. EXERCISES FOR PRACTICE
# -----------------------------------------------------------------------------

print("10. Try It Yourself!")
print("-" * 22)
print("Practice exercises to master functions and exception handling:")
print()

print("Exercise 1: User Management System")
print("- Create functions for: add_user(), remove_user(), list_users()")
print("- Use exception handling for invalid operations")
print("- Implement user role validation")
print("- Add logging for all operations")
print()

print("Exercise 2: File Security Scanner")
print("- Create function to check file permissions")
print("- Handle file not found errors gracefully")
print("- Return security recommendations")
print("- Use custom exceptions for different security levels")
print()

print("Exercise 3: Password Policy Enforcer")
print("- Implement comprehensive password validation")
print("- Check multiple criteria: length, complexity, history")
print("- Provide specific feedback for each failure")
print("- Generate strong password suggestions")
print()

print("Exercise 4: Network Utility Functions")
print("- Create ping simulation function")
print("- Implement port scanner function")
print("- Add error handling for network timeouts")
print("- Return structured results with status codes")
print()

# TODO for students: Uncomment and complete these exercises

# # Exercise 1: User Management System
# print("\n--- Exercise 1: User Management System ---")
# users = {}  # Dictionary to store users
# 
# def add_user(username, role, department):
#     # TODO: Implement user addition with validation
#     pass
# 
# def remove_user(username):
#     # TODO: Implement user removal with error handling
#     pass
# 
# def list_users():
#     # TODO: Display all users in a formatted way
#     pass

# # Exercise 2: File Security Scanner
# print("\n--- Exercise 2: File Security Scanner ---")
# 
# def check_file_permissions(filepath):
#     # TODO: Check file permissions and return security status
#     pass
# 
# def scan_directory_security(directory_path):
#     # TODO: Scan entire directory for security issues
#     pass

# # Exercise 3: Password Policy Enforcer
# print("\n--- Exercise 3: Password Policy Enforcer ---")
# 
# def enforce_password_policy(password):
#     # TODO: Implement comprehensive password validation
#     pass
# 
# def generate_secure_password(length=12):
#     # TODO: Generate a secure password meeting all criteria
#     pass

# # Exercise 4: Network Utility Functions
# print("\n--- Exercise 4: Network Utility Functions ---")
# 
# def simulate_ping(host, timeout=5):
#     # TODO: Simulate ping operation with timeout handling
#     pass
# 
# def scan_port(host, port, timeout=3):
#     # TODO: Check if a port is open on a host
#     pass

print("\n" + "=" * 58)
print("End of Session 08 - Great work with functions and error handling!")
print("Functions are the building blocks of larger programs!")
print("Exception handling makes your code robust and user-friendly!")