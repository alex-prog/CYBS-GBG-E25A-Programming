"""
Session 03: Variables and Data Types
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Understand different data types in Python (int, float, str, NoneType)
- Learn about dynamic typing and type conversion
- Master string manipulation techniques
- Work with string methods and operations
- Understand variable assignment and reassignment
- Practice with lists and string splitting/joining

Author: Programming Instructor  
Date: 03-Sep-2025
"""

# =============================================================================
# VARIABLES AND DATA TYPES IN PYTHON
# =============================================================================

print("Welcome to Session 03: Variables and Data Types")
print("=" * 55)
print()

# -----------------------------------------------------------------------------
# 1. DYNAMIC TYPING IN PYTHON
# -----------------------------------------------------------------------------

print("1. Dynamic Typing - Variables Can Change Type")
print("-" * 45)

# Python is dynamically typed - variables can hold different types of data
# and change type during program execution

print("Example: One variable, different types")

# Start with a float (decimal number)
x = 4.0
print(f"x = {x}, type: {type(x)}")

# Change to string
x = "Cyber"
print(f"x = {x}, type: {type(x)}")

# Change to integer
x = 500
print(f"x = {x}, type: {type(x)}")

# What happens when we assign print() result to a variable?
print(f"Before assignment: x = {x}")
x = print("From line above:", x)  # print() returns None
print(f"After assignment: x = {x}, type: {type(x)}")

print("📝 Key Point: print() function returns None (no value)")
print("   Variables can hold None, which represents 'no value'")
print()

# -----------------------------------------------------------------------------
# 2. STRING DATA TYPE AND ESCAPE CHARACTERS
# -----------------------------------------------------------------------------

print("2. Working with Strings and Escape Characters")
print("-" * 45)

# Strings can contain special characters using escape sequences
print("Basic string with newline (\\n):")
text = "Alice is good.\nBob is bad."
print(f"Text: {repr(text)}")  # repr() shows the actual escape characters
print("Displayed as:")
print(text)
print()

print("String with apostrophe - using escape (\\'):")
text = 'Alice is good.\nBob is bad. It\'s monday.'
print(f"Text: {repr(text)}")
print("Displayed as:")
print(text)
print()

print("Multi-line string using triple quotes:")
text = '''Alice is good.
Bob is bad. 
It's monday.'''
print(f"Text: {repr(text)}")
print("Displayed as:")
print(text)
print()

print("💡 Tip: Use triple quotes (''' or \"\"\") for multi-line strings")
print("💡 Tip: Use \\' to include apostrophes in single-quoted strings")
print()

# -----------------------------------------------------------------------------
# 3. STRING OPERATIONS AND METHODS
# -----------------------------------------------------------------------------

print("3. String Operations and Methods")
print("-" * 35)

# String concatenation and basic operations
first_name = 'Bob'
last_name = 'Sponge'
full_name = first_name + ' ' + last_name

print("String concatenation:")
print(f"first_name = '{first_name}'")
print(f"last_name = '{last_name}'")
print(f"full_name = first_name + ' ' + last_name")
print(f"Result: '{full_name}'")
print()

# String length and repetition
print("String properties and operations:")
print(f"Length of full name: {len(full_name)} characters")
print(f"Full name repeated 3 times: '{full_name * 3}'")
print()

# String indexing (accessing individual characters)
print("String indexing (accessing individual characters):")
print(f"Full name: '{full_name}'")
print(f"Length: {len(full_name)}")

last_index = len(full_name) - 1
print(f"Last index: {last_index}")
print(f"Character at last index [index {last_index}]: '{full_name[last_index]}'")
print(f"Character at index [-1] (negative indexing): '{full_name[-1]}'")

print()
print("📝 Key Points about string indexing:")
print("   - Indexing starts at 0 (first character is index 0)")
print("   - Last index is always length - 1")
print("   - Negative indexing: -1 is last character, -2 is second-to-last, etc.")
print()

# -----------------------------------------------------------------------------
# 4. STRING SPLITTING AND JOINING
# -----------------------------------------------------------------------------

print("4. String Splitting and Joining")
print("-" * 35)

# Working with multi-line text and splitting
print("Example: Processing log data")
log = '''192.0.0.3 - - GET /index.html 200
4.45.40.3 - - GET /admin.html 200'''

print("Original log:")
print(log)
print()

print("Splitting log into lines:")
lines = log.split('\n')  # Split on newline character
print(f"Lines: {lines}")
print(f"Number of lines: {len(lines)}")
print()

print("Extracting IP addresses from each line:")
print(f"First line IP: {lines[0].split()[0]}")
print(f"Second line IP: {lines[1].split()[0]}")
print()

print("💡 How split() works:")
print("   - split('\\n') splits on newline characters")
print("   - split() with no argument splits on any whitespace")
print("   - Returns a list of strings")
print()

# Joining strings
print("String joining example:")
connection_parts = ['11.12.3.4', '80']
connection_string = ':'.join(connection_parts)
print(f"Parts: {connection_parts}")
print(f"Joined with ':': {connection_string}")
print()

# -----------------------------------------------------------------------------
# 5. LISTS VS STRINGS - UNDERSTANDING THE DIFFERENCE
# -----------------------------------------------------------------------------

print("5. Lists vs Strings - Understanding the Difference")
print("-" * 50)

full_name = 'Alice Allan'
name_list = full_name.split()  # This creates a list
name_string = "['Bob', 'Sponge']"  # This is just a string that looks like a list

print("Comparing actual list vs string representation:")
print(f"name_list = {name_list}")
print(f"name_string = {name_string}")
print(f"Type of name_list: {type(name_list)}")
print(f"Type of name_string: {type(name_string)}")
print()

print("Working with split() on different characters:")
print(f"Original: '{full_name}'")
split_on_space = full_name.split()  # Default: split on whitespace
split_on_a = full_name.split('a')   # Split on letter 'a'

print(f"Split on space: {split_on_space}")
print(f"Split on 'a': {split_on_a}")
print()

# Joining back together
restored_name = 'a'.join(split_on_a)
print(f"Restored by joining with 'a': '{restored_name}'")
print()

# -----------------------------------------------------------------------------
# 6. VARIABLE ASSIGNMENT AND FUNCTION REFERENCES
# -----------------------------------------------------------------------------

print("6. Variable Assignment and Function References")
print("-" * 45)

print("Variables can hold different types of data, including functions!")

# Storing a string in a variable
message = 'Today is sunny'
print(f"message = '{message}'")

# Storing a function in a variable (advanced concept)
print_function = print  # Store the print function in a variable
print(f"print_function now refers to the print function")

# Using the stored function
print_function("Hello from stored function!")

print()
print("⚠️  Advanced Example: What happens if we reassign 'print'?")
# This is generally NOT recommended, but shows how Python works
original_print = print  # Save the original print function
print = 'Bob Sponge'    # Now 'print' is just a string!

print(f"print is now: {print}")  # This won't work because print is now a string!
# original_print("We can still use the original print function")

# Let's restore print for the rest of the program
print = original_print
print("✅ Print function restored!")
print()

# -----------------------------------------------------------------------------
# 7. COMMON DATA TYPE OPERATIONS SUMMARY
# -----------------------------------------------------------------------------

print("7. Summary of Common Data Type Operations")
print("-" * 40)

print("🔢 Numbers (int, float):")
print("   - Arithmetic: +, -, *, /, //, %, **")
print("   - Type conversion: int(), float()")
print()

print("📝 Strings (str):")
print("   - Concatenation: + operator")
print("   - Repetition: * operator")
print("   - Length: len()")
print("   - Indexing: string[index]")
print("   - Splitting: .split()")
print("   - Joining: 'separator'.join(list)")
print()

print("📋 Lists:")
print("   - Created by: .split() or [item1, item2, ...]")
print("   - Access items: list[index]")
print("   - Length: len()")
print()

print("❓ None type:")
print("   - Represents 'no value'")
print("   - Returned by functions that don't return anything")
print()

# -----------------------------------------------------------------------------
# 8. EXERCISES FOR PRACTICE
# -----------------------------------------------------------------------------

print("8. Try It Yourself!")
print("-" * 20)
print("Practice exercises to reinforce your learning:")
print()

print("Exercise 1: String manipulation")
print("- Create variables for your first and last name")
print("- Combine them into a full name")
print("- Print the length and the last character")
print()

print("Exercise 2: Data type exploration")
print("- Create a variable and assign it different types of values")
print("- Print the variable and its type each time")
print("- Try: number, string, result of print()")
print()

print("Exercise 3: String processing")
print("- Create a sentence with at least 5 words")
print("- Split it into words and print the list")
print("- Join the words back with '-' instead of spaces")
print()

print("Exercise 4: Text analysis")
print("- Take a multi-line string")
print("- Split it into lines")
print("- Count and print the number of lines")
print("- Print the first word of each line")
print()

# TODO for students: Uncomment and complete these exercises

# # Exercise 1: String manipulation
# print("\n--- Exercise 1: String manipulation ---")
# # first_name = ?
# # last_name = ?
# # full_name = ?
# # print(f"Full name: {full_name}")
# # print(f"Length: {len(full_name)}")
# # print(f"Last character: {full_name[-1]}")

# # Exercise 2: Data type exploration
# print("\n--- Exercise 2: Data type exploration ---")
# # my_var = 42
# # print(f"Value: {my_var}, Type: {type(my_var)}")
# # my_var = ?  # Try different values
# # print(f"Value: {my_var}, Type: {type(my_var)}")

# # Exercise 3: String processing
# print("\n--- Exercise 3: String processing ---")
# # sentence = ?
# # words = ?
# # rejoined = ?
# # print(f"Original: {sentence}")
# # print(f"Words: {words}")
# # print(f"Rejoined: {rejoined}")

# # Exercise 4: Text analysis
# print("\n--- Exercise 4: Text analysis ---")
# # text = """Line 1
# # Line 2
# # Line 3"""
# # lines = ?
# # print(f"Number of lines: {len(lines)}")
# # for line in lines:
# #     first_word = ?
# #     print(f"First word: {first_word}")

print("\n" + "=" * 55)
print("End of Session 03 - Excellent work with variables and data types!")
print("Remember: Practice these concepts - they're fundamental to programming!")
