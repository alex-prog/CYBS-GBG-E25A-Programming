"""
Session 12: Course Recap and Integration
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Review fundamental programming concepts covered in the course
- Practice integrating multiple concepts in single programs
- Reinforce data types, control flow, and functions
- Master file operations and data processing
- Apply all learned concepts to solve practical problems
- Build confidence through comprehensive exercises
- Prepare for more advanced programming topics
- Demonstrate understanding through mini-projects

Author: Programming Instructor
Date: 04-Nov-2025
"""

# =============================================================================
# COURSE RECAP AND INTEGRATION
# =============================================================================

print("Welcome to Session 12: Course Recap and Integration")
print("=" * 52)
print()

print("This session reviews all major topics from the course:")
print("- Variables and data types")
print("- Lists, tuples, and dictionaries")
print("- Control flow (if/elif/else, loops)")
print("- Functions and error handling")
print("- File operations")
print("- Data processing and manipulation")
print()

# -----------------------------------------------------------------------------
# 1. VARIABLES AND DATA TYPES RECAP
# -----------------------------------------------------------------------------

print("1. Variables and Data Types Recap")
print("-" * 32)

print("Basic variable operations:")

# Variable assignment and arithmetic
bob_age = 11
print(f"Bob's initial age: {bob_age}")
print(f"Type: {type(bob_age)}")

# Incrementing values
bob_age = bob_age + 1  # Method 1: explicit addition
bob_age += 1           # Method 2: compound assignment (same result)
print(f"Bob's age after two increments: {bob_age}")
print()

alice_age = 12
print(f"Alice's age: {alice_age}")
print()

print("Key concepts:")
print("- Variables store data and can be reassigned")
print("- Python is dynamically typed (type can change)")
print("- Compound operators (+=, -=, *=, /=) modify in place")
print("- Use descriptive variable names for readability")
print()

# Data type examples
print("Common data types:")
name = "Alice"                    # String
age = 25                          # Integer
height = 1.75                     # Float
is_active = True                  # Boolean
skills = ["Python", "SQL", "Git"] # List
coordinates = (10.5, 20.3)        # Tuple
user_info = {"name": "Bob", "role": "analyst"}  # Dictionary

print(f"String:     {name} ({type(name).__name__})")
print(f"Integer:    {age} ({type(age).__name__})")
print(f"Float:      {height} ({type(height).__name__})")
print(f"Boolean:    {is_active} ({type(is_active).__name__})")
print(f"List:       {skills} ({type(skills).__name__})")
print(f"Tuple:      {coordinates} ({type(coordinates).__name__})")
print(f"Dictionary: {user_info} ({type(user_info).__name__})")
print()

# -----------------------------------------------------------------------------
# 2. LISTS AND LIST OPERATIONS RECAP
# -----------------------------------------------------------------------------

print("2. Lists and List Operations Recap")
print("-" * 33)

# Creating and using lists
ages = [bob_age, alice_age]
print(f"Ages list: {ages}")

# Accessing list elements
print(f"First age: {ages[0]}")
print(f"Second age: {ages[1]}")

# List operations
sum_ages_manual = ages[0] + ages[1]
sum_ages_builtin = sum(ages)
print(f"Sum of ages (manual): {sum_ages_manual}")
print(f"Sum of ages (built-in): {sum_ages_builtin}")
print()

# List methods and operations
print("Common list operations:")
numbers = [1, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {numbers}")

# Slicing
print(f"Every second element: {numbers[::2]}")
print(f"First three elements: {numbers[:3]}")
print(f"Last three elements: {numbers[-3:]}")

# List methods
numbers.append(10)
print(f"After append(10): {numbers}")

numbers.extend([11, 12])
print(f"After extend([11, 12]): {numbers}")

numbers.insert(0, 0)
print(f"After insert(0, 0): {numbers}")
print()

print("Key list concepts:")
print("- Lists are mutable (can be changed)")
print("- Zero-based indexing (first element is index 0)")
print("- Negative indices count from the end")
print("- Slicing creates new lists without modifying original")
print("- Many built-in methods for list manipulation")
print()

# -----------------------------------------------------------------------------
# 3. TUPLES AND IMMUTABILITY RECAP
# -----------------------------------------------------------------------------

print("3. Tuples and Immutability Recap")
print("-" * 31)

# Creating tuples
connection = ('127.0.0.1', 80)
print(f"Connection tuple: {connection}")
print(f"Type: {type(connection)}")
print(f"IP address: {connection[0]}")
print(f"Port: {connection[1]}")
print()

# Demonstrating immutability
print("Tuples are immutable - cannot change elements directly")
print("This would cause an error: connection[1] = 8080")
print()

# Converting to modify
print("To modify, convert to list, change, then back to tuple:")
connection_list = list(connection)
print(f"Converted to list: {connection_list}")

connection_list[1] = 8080
print(f"Modified port: {connection_list}")

connection = tuple(connection_list)
print(f"Converted back to tuple: {connection}")
print()

print("When to use tuples vs lists:")
print("- Tuples: Fixed data that shouldn't change (coordinates, config)")
print("- Lists: Dynamic data that needs modification")
print("- Tuples are slightly faster and use less memory")
print("- Tuples can be dictionary keys, lists cannot")
print()

# -----------------------------------------------------------------------------
# 4. DICTIONARIES AND KEY-VALUE PAIRS RECAP
# -----------------------------------------------------------------------------

print("4. Dictionaries and Key-Value Pairs Recap")
print("-" * 40)

# Creating and populating dictionaries
grades = dict()  # or grades = {}
grades['bob'] = 10
grades['alice'] = 7
grades['hasan'] = 12

print(f"Grades dictionary: {grades}")
print()

# Accessing dictionary values
print("Accessing specific grades:")
print(f"Bob's grade: {grades['bob']}")
print(f"Alice's grade: {grades['alice']}")
print()

# Calculating statistics
sum_grades = 0
for student in grades:
    sum_grades += grades[student]

average_grade = sum_grades / len(grades)
print(f"Sum of grades: {sum_grades}")
print(f"Number of students: {len(grades)}")
print(f"Average grade: {average_grade:.2f}")
print()

# Using statistics module
import statistics
avg_with_module = statistics.mean(grades.values())
print(f"Average using statistics.mean(): {avg_with_module:.2f}")
print()

# Dictionary methods
print("Dictionary methods:")
print(f"Keys: {list(grades.keys())}")
print(f"Values: {list(grades.values())}")
print(f"Items: {list(grades.items())}")
print()

# Adding new entries
grades['julius'] = 12
print(f"After adding Julius: {grades}")
print()

# Iterating over dictionaries
print("Iterating over dictionary items:")
for name, grade in grades.items():
    print(f"  {name}: {grade}")
print()

print("Dictionary key concepts:")
print("- Store data as key-value pairs")
print("- Keys must be unique and immutable")
print("- Values can be any data type")
print("- Fast lookup by key")
print("- Useful for structured data and mappings")
print()

# -----------------------------------------------------------------------------
# 5. CONTROL FLOW RECAP
# -----------------------------------------------------------------------------

print("5. Control Flow Recap")
print("-" * 20)

# Conditional statements
print("Conditional statements (if/elif/else):")

def analyze_port(port):
    """Analyze network port number"""
    port_num = int(port)
    
    if port_num > 1023:
        category = "User/Dynamic Port"
        risk = "Low"
    elif port_num >= 1:
        category = "Well-Known System Port"
        risk = "Medium"
    else:
        category = "Invalid Port"
        risk = "High"
    
    print(f"Port {port_num}: {category} (Risk: {risk})")
    return category, risk

# Test different ports
analyze_port(80)
analyze_port(8080)
analyze_port(22)
print()

# Magic number example
def check_magic_number(x):
    """Check if number has special meaning"""
    if x > 42:
        print(f"{x} is bigger than 42")
    elif x == 42:
        print(f"{x} is the MAGIC number 42!")
    else:
        print(f"{x} is less than 42")

print("Magic number checker:")
check_magic_number(43)
check_magic_number(42)
check_magic_number(30)
print()

# Loop examples
print("For loop with list:")
numbers = [1, 3, 4, 5, 6, 7, 8, 9]
print("Even-indexed elements:")
for num in numbers[::2]:
    print(f"  {num}")
print()

print("For loop with range:")
print("Countdown from 5:")
for i in range(5, 0, -1):
    print(f"  {i}...")
print("  Blast off!")
print()

# While loop example
print("While loop example:")
counter = 0
print("Counting to 3:")
while counter < 3:
    counter += 1
    print(f"  Count: {counter}")
print()

# -----------------------------------------------------------------------------
# 6. FUNCTIONS AND ERROR HANDLING RECAP
# -----------------------------------------------------------------------------

print("6. Functions and Error Handling Recap")
print("-" * 38)

def safe_sum(x, y):
    """Safely add two values with error handling"""
    try:
        result = int(x) + int(y)
        return result
    except ValueError:
        print(f"ERROR: Cannot convert '{x}' or '{y}' to integer")
        return 0
    except TypeError:
        print("ERROR: Invalid data types for addition")
        return 0

print("Function with error handling:")
result1 = safe_sum(3, 5)
print(f"safe_sum(3, 5) = {result1}")

result2 = safe_sum(3, 'bob')
print(f"safe_sum(3, 'bob') = {result2}")

result3 = safe_sum('10', '20')
print(f"safe_sum('10', '20') = {result3}")
print()

print("Function benefits:")
print("- Reusable code blocks")
print("- Better organization and readability")
print("- Easier testing and debugging")
print("- Error handling in one place")
print()

# Function with multiple return values
def analyze_student(name, grade):
    """Analyze student performance"""
    if grade >= 10:
        performance = "Excellent"
        pass_status = True
    elif grade >= 7:
        performance = "Good"
        pass_status = True
    else:
        performance = "Needs Improvement"
        pass_status = False
    
    return performance, pass_status

print("Student analysis:")
perf, passed = analyze_student("Alice", 12)
print(f"Alice (grade 12): {perf}, Passed: {passed}")

perf, passed = analyze_student("Bob", 5)
print(f"Bob (grade 5): {perf}, Passed: {passed}")
print()

# -----------------------------------------------------------------------------
# 7. FILE OPERATIONS RECAP
# -----------------------------------------------------------------------------

print("7. File Operations Recap")
print("-" * 23)

# Create sample file for demonstration
print("Creating sample student data file...")
sample_data = """Alice alice@school.com 12
Bob bob@school.com 10
Charlie charlie@school.com 7
Diana diana@school.com 11
Eve eve@school.com 9
"""

with open('students_data.txt', 'w') as f:
    f.write(sample_data)

print("File created: students_data.txt")
print()

# Reading and processing file
print("Reading and processing file data:")
students = []

with open('students_data.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        
        student = {
            'name': parts[0],
            'email': parts[1],
            'grade': int(parts[2])
        }
        students.append(student)

print(f"Loaded {len(students)} students from file")
print()

# Display student information
print("Student roster:")
print("-" * 50)
print(f"{'Name':<15} {'Email':<25} {'Grade':<5}")
print("-" * 50)
for student in students:
    print(f"{student['name']:<15} {student['email']:<25} {student['grade']:<5}")
print("-" * 50)
print()

# Extract specific data
student_emails = []
for student in students:
    student_emails.append(student['email'])

print("Student email list:")
print(", ".join(student_emails))
print()

# Alternative: using list comprehension (advanced)
emails_comprehension = [s['email'] for s in students]
print("Email list (using list comprehension):")
print(", ".join(emails_comprehension))
print()

print("File operation concepts:")
print("- Use 'with' statement for automatic file closing")
print("- 'r' mode for reading, 'w' for writing, 'a' for appending")
print("- strip() removes whitespace from lines")
print("- split() breaks strings into lists")
print("- Process files line by line for efficiency")
print()

# -----------------------------------------------------------------------------
# 8. INTEGRATED EXAMPLE - STUDENT MANAGEMENT SYSTEM
# -----------------------------------------------------------------------------

print("8. Integrated Example - Student Management System")
print("-" * 48)

def calculate_statistics(students):
    """Calculate various statistics for student grades"""
    
    if not students:
        return None
    
    grades = [s['grade'] for s in students]
    
    stats = {
        'total_students': len(students),
        'average_grade': sum(grades) / len(grades),
        'highest_grade': max(grades),
        'lowest_grade': min(grades),
        'passing_count': len([g for g in grades if g >= 7])
    }
    
    return stats

def generate_report(students, stats):
    """Generate a formatted report"""
    
    report_lines = []
    report_lines.append("=" * 60)
    report_lines.append("STUDENT PERFORMANCE REPORT")
    report_lines.append("=" * 60)
    report_lines.append("")
    
    report_lines.append(f"Total Students: {stats['total_students']}")
    report_lines.append(f"Average Grade: {stats['average_grade']:.2f}")
    report_lines.append(f"Highest Grade: {stats['highest_grade']}")
    report_lines.append(f"Lowest Grade: {stats['lowest_grade']}")
    report_lines.append(f"Passing Students: {stats['passing_count']} ({stats['passing_count']/stats['total_students']*100:.1f}%)")
    report_lines.append("")
    
    report_lines.append("Top Performers (Grade >= 10):")
    top_students = [s for s in students if s['grade'] >= 10]
    for student in sorted(top_students, key=lambda x: x['grade'], reverse=True):
        report_lines.append(f"  {student['name']}: {student['grade']}")
    
    report_lines.append("")
    report_lines.append("Students Needing Support (Grade < 7):")
    struggling_students = [s for s in students if s['grade'] < 7]
    if struggling_students:
        for student in struggling_students:
            report_lines.append(f"  {student['name']}: {student['grade']}")
    else:
        report_lines.append("  None - all students passing!")
    
    report_lines.append("")
    report_lines.append("=" * 60)
    
    return "\\n".join(report_lines)

print("Generating comprehensive student report...")
print()

stats = calculate_statistics(students)
report = generate_report(students, stats)
print(report)
print()

# Save report to file
with open('student_report.txt', 'w') as f:
    f.write(report)

print("Report saved to: student_report.txt")
print()

# -----------------------------------------------------------------------------
# 9. PRACTICE EXERCISES
# -----------------------------------------------------------------------------

print("9. Practice Exercises")
print("-" * 19)
print("Complete these exercises to reinforce your learning!")
print()

print("Exercise 1: Grade Calculator")
print("Description: Create a function that calculates letter grades")
print("Requirements:")
print("  - Accept a numeric grade (0-100)")
print("  - Return letter grade (A, B, C, D, F)")
print("  - Handle invalid inputs gracefully")
print("  - A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59")
print()

# TODO for students
# def calculate_letter_grade(numeric_grade):
#     # TODO: Implement grade calculation
#     pass
# 
# Test cases:
# print(calculate_letter_grade(95))  # Should return 'A'
# print(calculate_letter_grade(82))  # Should return 'B'
# print(calculate_letter_grade(58))  # Should return 'F'

print("Exercise 2: Data Validator")
print("Description: Validate user registration data")
print("Requirements:")
print("  - Check username length (3-20 characters)")
print("  - Validate email format (contains @ and .)")
print("  - Check password strength (min 8 chars, has digit)")
print("  - Return list of validation errors or 'Valid'")
print()

# TODO for students
# def validate_registration(username, email, password):
#     # TODO: Implement validation logic
#     errors = []
#     # Check username length
#     # Check email format
#     # Check password strength
#     # Return errors list or 'Valid'
#     pass
# 
# Test cases:
# print(validate_registration("ab", "invalid", "weak"))
# print(validate_registration("alice", "alice@example.com", "Strong123"))

print("Exercise 3: Log File Analyzer")
print("Description: Analyze security log files")
print("Requirements:")
print("  - Read log file with format: timestamp level message")
print("  - Count occurrences of each log level")
print("  - Find most common error messages")
print("  - Generate summary statistics")
print()

# Create sample log file
sample_log = """2025-11-04 10:00:00 INFO User login successful
2025-11-04 10:01:15 WARNING Failed login attempt
2025-11-04 10:02:30 ERROR Database connection failed
2025-11-04 10:03:45 INFO Data backup completed
2025-11-04 10:05:00 ERROR Database connection failed
2025-11-04 10:06:15 WARNING Disk space low
2025-11-04 10:07:30 INFO User logout
2025-11-04 10:08:45 ERROR File not found
"""

with open('security_log.txt', 'w') as f:
    f.write(sample_log)

print("Sample log file created: security_log.txt")
print()

# TODO for students
# def analyze_log_file(filename):
#     # TODO: Implement log analysis
#     log_stats = {
#         'total_entries': 0,
#         'level_counts': {},
#         'error_messages': []
#     }
#     # Read file and count log levels
#     # Extract error messages
#     # Return statistics
#     pass
# 
# stats = analyze_log_file('security_log.txt')
# print(f"Total log entries: {stats['total_entries']}")
# print(f"Log level distribution: {stats['level_counts']}")

print("Exercise 4: Student Grade Manager")
print("Description: Complete student management system")
print("Requirements:")
print("  - Load students from CSV file")
print("  - Add new students to file")
print("  - Calculate class statistics")
print("  - Generate grade distribution report")
print("  - Export data to different formats")
print()

# TODO for students
# class StudentManager:
#     def __init__(self, filename):
#         # TODO: Initialize with filename
#         self.students = []
#         pass
#     
#     def load_students(self):
#         # TODO: Load from file
#         pass
#     
#     def add_student(self, name, email, grade):
#         # TODO: Add student to list and file
#         pass
#     
#     def get_statistics(self):
#         # TODO: Calculate statistics
#         pass
#     
#     def generate_grade_distribution(self):
#         # TODO: Create grade distribution (A, B, C, D, F counts)
#         pass

print("Exercise 5: Network Connection Analyzer")
print("Description: Analyze network connection logs")
print("Requirements:")
print("  - Parse connection data (IP, port, protocol, status)")
print("  - Identify suspicious connections")
print("  - Generate security alerts")
print("  - Create summary report with recommendations")
print()

# TODO for students
# def analyze_connections(connections):
#     # connections = [
#     #     ('192.168.1.100', 22, 'SSH', 'success'),
#     #     ('203.0.113.45', 23, 'TELNET', 'blocked'),
#     #     ('10.0.0.50', 80, 'HTTP', 'success'),
#     # ]
#     # TODO: Analyze connections
#     # Check for insecure protocols (telnet, ftp)
#     # Identify unusual ports
#     # Generate security recommendations
#     pass

print("Exercise 6: Data Format Converter")
print("Description: Convert between different data formats")
print("Requirements:")
print("  - Read data from JSON file")
print("  - Convert to CSV format")
print("  - Convert CSV back to JSON")
print("  - Handle nested data structures")
print("  - Validate data integrity after conversion")
print()

# TODO for students
# import json
# import csv
# 
# def json_to_csv(json_file, csv_file):
#     # TODO: Convert JSON to CSV
#     pass
# 
# def csv_to_json(csv_file, json_file):
#     # TODO: Convert CSV to JSON
#     pass

print("Exercise 7: Password Strength Checker")
print("Description: Comprehensive password validation")
print("Requirements:")
print("  - Check length (minimum 8 characters)")
print("  - Require uppercase and lowercase letters")
print("  - Require at least one digit")
print("  - Require at least one special character")
print("  - Check against common passwords list")
print("  - Return strength score (0-100)")
print()

# TODO for students
# def check_password_strength(password):
#     common_passwords = ['password', '123456', 'qwerty', 'admin']
#     strength_score = 0
#     feedback = []
#     
#     # TODO: Implement comprehensive password checking
#     # Add points for meeting each requirement
#     # Deduct points for common passwords
#     # Provide specific feedback
#     
#     return strength_score, feedback

print("Exercise 8: Mini Project - Security Event Dashboard")
print("Description: Create a complete security monitoring system")
print("Requirements:")
print("  - Read security events from database or file")
print("  - Filter events by severity and type")
print("  - Calculate statistics (events per hour, top sources)")
print("  - Generate visual report with charts (ASCII art)")
print("  - Export results to multiple formats")
print("  - Include error handling and logging")
print()

# TODO for students - This is a larger project combining all skills
# def create_security_dashboard(events_file):
#     # TODO: Build complete dashboard system
#     # Load and parse events
#     # Apply filters
#     # Calculate statistics
#     # Generate visualizations
#     # Export reports
#     pass

print()
print("=" * 52)
print("End of Session 12 - Excellent work reviewing concepts!")
print("You've covered a lot of material this semester!")
print()
print("Key takeaways:")
print("- Master the fundamentals before moving to advanced topics")
print("- Practice combining multiple concepts in single programs")
print("- Always handle errors and edge cases")
print("- Write clean, readable code with good variable names")
print("- Test your code with different inputs")
print("- Keep learning and building projects!")
print()
print("Congratulations on completing the programming course!")
print("Keep practicing and building your programming skills!")
