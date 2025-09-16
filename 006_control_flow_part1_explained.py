"""
Session 06: Control Flow - Part 1 (Conditional Statements)
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Understand boolean values and logical operations
- Master if, elif, and else statements
- Learn comparison operators and their usage
- Practice with nested conditional statements
- Work with logical operators (and, or, not)
- Apply conditional logic to real-world problems

Author: Programming Instructor
Date: 16-Sep-2025
"""

# =============================================================================
# CONTROL FLOW - CONDITIONAL STATEMENTS
# =============================================================================

print("Welcome to Session 06: Control Flow - Conditional Statements")
print("=" * 60)
print()

# -----------------------------------------------------------------------------
# 1. INTRODUCTION TO BOOLEAN VALUES
# -----------------------------------------------------------------------------

print("1. Introduction to Boolean Values")
print("-" * 32)

# Boolean values are True or False
print("Boolean values in Python:")
print(f"True: {True}, type: {type(True)}")
print(f"False: {False}, type: {type(False)}")
print()

# Boolean values from comparisons
age = 20
print(f"age = {age}")
print(f"age >= 18: {age >= 18}")
print(f"age < 18: {age < 18}")
print(f"age == 20: {age == 20}")
print(f"age != 20: {age != 20}")
print()

print("Important notes about booleans:")
print("- True and False must be capitalized")
print("- Comparison operators return boolean values")
print("- Boolean values can be stored in variables")
print()

# -----------------------------------------------------------------------------
# 2. COMPARISON OPERATORS
# -----------------------------------------------------------------------------

print("2. Comparison Operators")
print("-" * 22)

a = 10
b = 20
c = 10

print(f"Variables: a = {a}, b = {b}, c = {c}")
print()

print("Equality and inequality:")
print(f"a == b: {a == b}")  # Equal to
print(f"a == c: {a == c}")  # Equal to
print(f"a != b: {a != b}")  # Not equal to
print()

print("Comparison operators:")
print(f"a < b: {a < b}")   # Less than
print(f"a > b: {a > b}")   # Greater than
print(f"a <= c: {a <= c}") # Less than or equal to
print(f"b >= a: {b >= a}") # Greater than or equal to
print()

print("String comparisons:")
name1 = "Alice"
name2 = "Bob"
print(f"name1 = '{name1}', name2 = '{name2}'")
print(f"name1 == name2: {name1 == name2}")
print(f"name1 < name2: {name1 < name2}")  # Alphabetical order
print()

# -----------------------------------------------------------------------------
# 3. BASIC IF STATEMENTS
# -----------------------------------------------------------------------------

print("3. Basic If Statements")
print("-" * 20)

print("Example 1: Simple age check")
age = 25
print(f"Age: {age}")

if age >= 18:
    print("You are an adult")
    print("You can vote")

print("This line always executes")
print()

print("Example 2: Grade evaluation")
grade = 85
print(f"Grade: {grade}")

if grade >= 90:
    print("Excellent work!")

if grade >= 80:
    print("Good job!")

if grade >= 70:
    print("You passed")
print()

print("Key points about if statements:")
print("- Use colon (:) after the condition")
print("- Indent the code block that runs when condition is True")
print("- Python uses 4 spaces for indentation")
print("- Code after the if block always runs")
print()

# -----------------------------------------------------------------------------
# 4. IF-ELSE STATEMENTS
# -----------------------------------------------------------------------------

print("4. If-Else Statements")
print("-" * 19)

print("Example 1: Adult or minor check")
age = 16
print(f"Age: {age}")

if age >= 18:
    print("You are an adult")
    print("You have full rights")
else:
    print("You are a minor")
    print("Some restrictions apply")

print("Check completed")
print()

print("Example 2: Pass or fail")
score = 65
print(f"Score: {score}")

if score >= 70:
    print("Congratulations! You passed the exam")
    status = "PASS"
else:
    print("Sorry, you did not pass the exam")
    status = "FAIL"

print(f"Final status: {status}")
print()

# -----------------------------------------------------------------------------
# 5. IF-ELIF-ELSE STATEMENTS
# -----------------------------------------------------------------------------

print("5. If-Elif-Else Statements")
print("-" * 26)

print("Example 1: Grade letter assignment")
score = 78
print(f"Score: {score}")

if score >= 90:
    letter_grade = "A"
    print("Outstanding performance!")
elif score >= 80:
    letter_grade = "B"
    print("Good work!")
elif score >= 70:
    letter_grade = "C"
    print("Satisfactory performance")
elif score >= 60:
    letter_grade = "D"
    print("You need improvement")
else:
    letter_grade = "F"
    print("You must retake the exam")

print(f"Your letter grade: {letter_grade}")
print()

print("Example 2: Weather-based activity suggestion")
weather = "sunny"
print(f"Weather: {weather}")

if weather == "sunny":
    print("Great day for a picnic!")
    activity = "outdoor sports"
elif weather == "rainy":
    print("Perfect time to read a book")
    activity = "indoor activities"
elif weather == "snowy":
    print("Time for winter sports!")
    activity = "skiing or snowball fight"
else:
    print("Let's see what the day brings")
    activity = "flexible planning"

print(f"Recommended activity: {activity}")
print()

print("Important about elif:")
print("- elif means 'else if'")
print("- Only the first True condition executes")
print("- Once a condition is True, remaining conditions are skipped")
print("- You can have multiple elif statements")
print("- else is optional and runs if no condition is True")
print()

# -----------------------------------------------------------------------------
# 6. LOGICAL OPERATORS
# -----------------------------------------------------------------------------

print("6. Logical Operators (and, or, not)")
print("-" * 34)

print("Example 1: Using 'and' operator")
age = 25
has_license = True
print(f"Age: {age}, Has driver's license: {has_license}")

if age >= 18 and has_license:
    print("You can rent a car")
else:
    print("You cannot rent a car")
print()

print("Example 2: Using 'or' operator")
day = "Saturday"
is_holiday = False
print(f"Day: {day}, Is holiday: {is_holiday}")

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("You don't have to work today!")
else:
    print("It's a working day")
print()

print("Example 3: Using 'not' operator")
is_raining = False
print(f"Is raining: {is_raining}")

if not is_raining:
    print("You don't need an umbrella")
else:
    print("Take an umbrella with you")
print()

print("Logical operator truth tables:")
print("AND operator:")
print("True and True = True")
print("True and False = False") 
print("False and True = False")
print("False and False = False")
print()

print("OR operator:")
print("True or True = True")
print("True or False = True")
print("False or True = True") 
print("False or False = False")
print()

print("NOT operator:")
print("not True = False")
print("not False = True")
print()

# -----------------------------------------------------------------------------
# 7. NESTED IF STATEMENTS
# -----------------------------------------------------------------------------

print("7. Nested If Statements")
print("-" * 22)

print("Example: University admission system")
grade = 85
age = 19
has_diploma = True

print(f"Grade: {grade}, Age: {age}, Has diploma: {has_diploma}")

if has_diploma:
    print("Diploma verified")
    if age >= 18:
        print("Age requirement met")
        if grade >= 80:
            print("ACCEPTED: You meet all requirements!")
            status = "ACCEPTED"
        else:
            print("REJECTED: Grade too low (minimum 80)")
            status = "REJECTED - LOW GRADE"
    else:
        print("REJECTED: You must be at least 18 years old")
        status = "REJECTED - TOO YOUNG"
else:
    print("REJECTED: High school diploma required")
    status = "REJECTED - NO DIPLOMA"

print(f"Application status: {status}")
print()

print("Alternative approach using logical operators:")
if has_diploma and age >= 18 and grade >= 80:
    print("ACCEPTED: All requirements met!")
else:
    print("REJECTED: One or more requirements not met")
print()

# -----------------------------------------------------------------------------
# 8. PRACTICAL APPLICATIONS
# -----------------------------------------------------------------------------

print("8. Practical Applications")
print("-" * 24)

print("Application 1: Login system")
username = "student123"
password = "secure_pass"
input_username = "student123"
input_password = "secure_pass"

print(f"Attempting login with: {input_username}")

if input_username == username and input_password == password:
    print("Login successful! Welcome back!")
    access_granted = True
else:
    print("Invalid credentials. Access denied.")
    access_granted = False

print(f"Access granted: {access_granted}")
print()

print("Application 2: Shopping discount calculator")
purchase_amount = 150
is_member = True
is_student = False

print(f"Purchase: ${purchase_amount}, Member: {is_member}, Student: {is_student}")

discount = 0
if purchase_amount >= 100:
    discount = 10  # 10% for purchases over $100
    print("Qualified for bulk purchase discount (10%)")

if is_member:
    discount += 5  # Additional 5% for members
    print("Member discount applied (5%)")

if is_student:
    discount += 3  # Additional 3% for students
    print("Student discount applied (3%)")

if discount > 0:
    savings = purchase_amount * (discount / 100)
    final_amount = purchase_amount - savings
    print(f"Total discount: {discount}%")
    print(f"You save: ${savings:.2f}")
    print(f"Final amount: ${final_amount:.2f}")
else:
    print("No discounts applied")
    print(f"Final amount: ${purchase_amount:.2f}")
print()

# -----------------------------------------------------------------------------
# 9. COMMON PATTERNS AND BEST PRACTICES
# -----------------------------------------------------------------------------

print("9. Common Patterns and Best Practices")
print("-" * 37)

print("Best practices for conditional statements:")
print("- Use clear, descriptive variable names")
print("- Keep conditions simple and readable")
print("- Use logical operators to combine simple conditions")
print("- Consider using elif instead of multiple separate if statements")
print("- Indent consistently (4 spaces in Python)")
print()

print("Common patterns:")
print()

print("Pattern 1: Range checking")
temperature = 22
print(f"Temperature: {temperature}°C")

if temperature < 0:
    print("Freezing")
elif temperature < 20:
    print("Cold")
elif temperature < 30:
    print("Comfortable")
else:
    print("Hot")
print()

print("Pattern 2: Input validation")
user_input = "25"
print(f"User input: '{user_input}'")

if user_input.isdigit():
    number = int(user_input)
    if 1 <= number <= 100:
        print(f"Valid number: {number}")
    else:
        print("Number must be between 1 and 100")
else:
    print("Input must be a number")
print()

# -----------------------------------------------------------------------------
# 10. EXERCISES FOR PRACTICE
# -----------------------------------------------------------------------------

print("10. Try It Yourself!")
print("-" * 22)
print("Practice exercises to master conditional statements:")
print()

print("Exercise 1: Age categorizer")
print("- Take an age value")
print("- Categorize as: child (0-12), teenager (13-19), adult (20-64), senior (65+)")
print("- Print appropriate message for each category")
print()

print("Exercise 2: Grade calculator")
print("- Take a numerical score")
print("- Convert to letter grade (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)")
print("- Include appropriate messages")
print()

print("Exercise 3: Password strength checker")
print("- Check if password meets criteria:")
print("  * At least 8 characters long")
print("  * Contains both letters and numbers")
print("- Provide feedback on password strength")
print()

print("Exercise 4: Shipping cost calculator")
print("- Calculate shipping based on weight and destination")
print("- Local: free if over $50, otherwise $5")
print("- International: $10 + $2 per kg")
print("- Express option: double the cost")
print()

# TODO for students: Uncomment and complete these exercises

# # Exercise 1: Age categorizer
# print("\n--- Exercise 1: Age categorizer ---")
# age = 25  # Try different ages
# # Write if-elif-else statements to categorize age

# # Exercise 2: Grade calculator  
# print("\n--- Exercise 2: Grade calculator ---")
# score = 87  # Try different scores
# # Convert numerical score to letter grade

# # Exercise 3: Password strength checker
# print("\n--- Exercise 3: Password strength checker ---")
# password = "mypass123"  # Try different passwords
# # Check length and content requirements

# # Exercise 4: Shipping calculator
# print("\n--- Exercise 4: Shipping calculator ---")
# weight = 2.5  # kg
# destination = "local"  # or "international"
# express = False
# order_total = 45.00
# # Calculate shipping cost based on conditions

print("\n" + "=" * 60)
print("End of Session 06 - Excellent work with conditional statements!")
print("Control flow is fundamental to programming logic - keep practicing!")