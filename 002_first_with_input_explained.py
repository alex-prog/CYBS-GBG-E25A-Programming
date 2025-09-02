"""
Session 02: User Input and String Formatting
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Understand how to get input from users
- Learn different ways to format and display text
- Practice working with variables and strings
- Explore various string formatting methods in Python

Author: Programming Instructor
Date: 01-Sep-2025
"""

# =============================================================================
# USER INPUT AND STRING FORMATTING EXAMPLES
# =============================================================================

print("Welcome to Session 02: User Input and String Formatting")
print("=" * 55)
print()

# -----------------------------------------------------------------------------
# 1. GETTING USER INPUT
# -----------------------------------------------------------------------------

print("1. Getting User Input")
print("-" * 25)

# The input() function displays a message to the user and waits for them to type something
# Whatever the user types is returned as a string
name = input("Enter your name: ")

# At this point, the variable 'name' contains whatever the user typed
# Note: input() always returns a string, even if the user types numbers
print(f"You entered: '{name}' (type: {type(name)})")
print()

# -----------------------------------------------------------------------------
# 2. STRING FORMATTING METHODS
# -----------------------------------------------------------------------------

print("2. Different Ways to Format Strings")
print("-" * 35)

# Method 1: Using print() with multiple arguments and 'sep' parameter
print("Method 1 - Using print() with sep parameter:")
print("Hello,", name, "!", sep='')  # sep='' means no space between arguments
print("Explanation: The sep='' removes spaces between the printed items")
print()

# Method 2: String concatenation with the + operator
print("Method 2 - String concatenation with + operator:")
print("Hello, " + name + "!")
print("Explanation: We manually add spaces and combine strings with +")
print()

# Method 3: f-strings (formatted string literals) - RECOMMENDED for Python 3.6+
print("Method 3 - f-strings (formatted string literals):")
print(f"Hello, {name}!")
print("Explanation: f-strings are modern, readable, and efficient")
print("The {name} gets replaced with the value of the variable 'name'")
print()

# Method 4: .format() method - older but still useful
print("Method 4 - .format() method:")
print("Hello, {0}! {1} {2}".format(name, 78, "bob"))
print("Explanation: {0} refers to first argument, {1} to second, etc.")
print("This method allows for more complex formatting")
print()

# -----------------------------------------------------------------------------
# 3. ADDITIONAL STRING FORMATTING EXAMPLES
# -----------------------------------------------------------------------------

print("3. More String Formatting Examples")
print("-" * 35)

# Getting multiple inputs
age = input("Enter your age: ")  # Remember: input() returns a string!
city = input("Enter your city: ")

# Converting string to integer for age (we'll learn more about this later)
try:
    age_number = int(age)  # Convert string to integer
    print(f"\nUsing f-strings for multiple variables:")
    print(f"Hi {name}! You are {age_number} years old and live in {city}.")
    
    # Demonstrating f-string expressions
    print(f"Next year you will be {age_number + 1} years old!")
    
except ValueError:
    print(f"\nNote: '{age}' is not a valid number, so we'll treat it as text.")
    print(f"Hi {name}! You entered '{age}' as your age and live in {city}.")

print()

# -----------------------------------------------------------------------------
# 4. FORMATTING WITH DIFFERENT DATA TYPES
# -----------------------------------------------------------------------------

print("4. Working with Different Data Types")
print("-" * 40)

# Numbers and formatting
price = 19.99
quantity = 3

print("Using f-strings with numbers and calculations:")
print(f"Item price: ${price}")
print(f"Quantity: {quantity}")
print(f"Total cost: ${price * quantity}")
print(f"Total cost (rounded): ${price * quantity:.2f}")  # .2f = 2 decimal places
print()

# -----------------------------------------------------------------------------
# 5. COMMON BEGINNER MISTAKES AND SOLUTIONS
# -----------------------------------------------------------------------------

print("5. Common Mistakes to Avoid")
print("-" * 30)

print("❌ MISTAKE: Forgetting that input() returns a string")
print("   age = input('Age: ')  # This is a string!")
print("   next_year = age + 1   # ERROR! Can't add number to string")
print()

print("✅ SOLUTION: Convert to the right type first")
print("   age = int(input('Age: '))  # Convert to integer")
print("   next_year = age + 1        # Now this works!")
print()

print("❌ MISTAKE: Mixing up string concatenation and f-strings")
print("   print('Hello, {name}!')   # This prints {name} literally")
print()

print("✅ SOLUTION: Use f-string prefix or proper concatenation")
print("   print(f'Hello, {name}!')  # f-string: variable gets substituted")
print("   print('Hello, ' + name + '!')  # Concatenation: strings joined")
print()

# -----------------------------------------------------------------------------
# 6. TRY IT YOURSELF EXERCISES
# -----------------------------------------------------------------------------

print("6. Try It Yourself!")
print("-" * 20)
print("Now it's your turn to practice! Try these exercises:")
print()

print("Exercise 1: Create a simple calculator")
print("- Ask user for two numbers")
print("- Add them together and display the result")
print("- Hint: Remember to convert strings to numbers!")
print()

print("Exercise 2: Personal information formatter")
print("- Ask for: name, favorite color, favorite number")
print("- Display a nicely formatted message using f-strings")
print("- Example: 'Hi Alice! Your favorite color is blue and your lucky number is 7.'")
print()

print("Exercise 3: Experiment with string formatting")
print("- Try all four methods shown above with your own text")
print("- See which one you find easiest to read and understand")
print()

# TODO for students: Uncomment and complete these exercises

# # Exercise 1: Simple Calculator
# print("\n--- Exercise 1: Simple Calculator ---")
# # Your code here:
# # first_number = ?
# # second_number = ?
# # result = ?
# # print(f"Result: ...")

# # Exercise 2: Personal Information
# print("\n--- Exercise 2: Personal Information ---")
# # Your code here:
# # favorite_color = ?
# # favorite_number = ?
# # print(f"...")

# # Exercise 3: String Formatting Practice
# print("\n--- Exercise 3: String Formatting Practice ---")
# # Try all different formatting methods with your own example

print("\n" + "=" * 55)
print("End of Session 02 - Great job learning about input and formatting!")
print("Remember: Practice makes perfect. Try the exercises above!")
