"""
Session 04: Variables and Data Types - Part 2
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Work with user input and type conversion
- Master f-string formatting with expressions
- Understand list indexing and slicing
- Learn list methods and operations
- Practice with negative indexing
- Explore list manipulation techniques

Author: Programming Instructor  
Date: 08-Sep-2025
"""

# =============================================================================
# VARIABLES AND DATA TYPES - PART 2
# =============================================================================

print("Welcome to Session 04: Variables and Data Types - Part 2")
print("=" * 60)
print()

# -----------------------------------------------------------------------------
# 1. USER INPUT AND TYPE CONVERSION
# -----------------------------------------------------------------------------

print("1. User Input and Type Conversion")
print("-" * 35)

# Remember: input() always returns a string
# We need to convert it to the appropriate type

print("Example: Age calculator")
print("Note: We're using example values instead of input() for demonstration")

# Simulating user input
age_input = "25"  # This would be: input('How old are you? ')
age = int(age_input)  # Convert string to integer

future_age = age + 100
print(f"Current age: {age}")
print(f"Your age in 100 years: {future_age}")

# Calculate what year they'll turn 100
current_year = 2025
future_year = current_year + (100 - age)
print(f"You will turn 100 in year {future_year}")

print()
print("Key Points:")
print("- input() returns a string, even if user types numbers")
print("- Use int() to convert string to integer")
print("- Use float() to convert string to decimal number")
print("- Always convert before doing math operations")
print()

# -----------------------------------------------------------------------------
# 2. F-STRING FORMATTING WITH EXPRESSIONS
# -----------------------------------------------------------------------------

print("2. F-String Formatting with Expressions")
print("-" * 40)

# f-strings can contain variables AND expressions
name = 'Amira'
age = 19

print("F-string with variables and expressions:")
print(f"Hi {name}. Today is Monday. You are {age} years old. And 2+3 is {2+3}")

print()
print("Comparison with traditional print using comma separation:")
print("Hi", name, '. Today is Monday. You are', age, ' years old. And 2+3 is ', (2+3), sep='')

print()
print("Why f-strings are better:")
print("- More readable and easier to write")
print("- Can include calculations directly: {2+3}")
print("- Can include function calls: {len(name)}")
print("- Can include complex expressions: {age * 2}")
print()

# -----------------------------------------------------------------------------
# 3. LIST BASICS AND INDEXING
# -----------------------------------------------------------------------------

print("3. List Basics and Indexing")
print("-" * 30)

# Lists are ordered collections of items
x = ["first", "second", "third", "fourth"]
print(f"Original list: {x}")

# Basic indexing
print(f"First item (index 0): {x[0]}")
print(f"Last item (index -1): {x[-1]}")

# List slicing - getting portions of a list
print(f"First three items: {x[:3]}")
print(f"Last two items: {x[-2:]}")

print()
print("List indexing rules:")
print("- Indexing starts at 0")
print("- Negative indexing starts at -1 (last item)")
print("- Slicing: [start:end] (end is not included)")
print("- [:n] means 'from beginning to position n'")
print("- [n:] means 'from position n to end'")
print()

# -----------------------------------------------------------------------------
# 4. ADVANCED LIST SLICING
# -----------------------------------------------------------------------------

print("4. Advanced List Slicing")
print("-" * 25)

# Working with a larger list to demonstrate slicing
#    0  1  2   3    4   5   6    <- positive indices
#   -7 -6 -5  -4   -3  -2  -1    <- negative indices
l = [4, 5, 8 , 12 , 45, 42, 16]

print("List with index positions:")
print("Values: ", l)
print("Positive:", [0, 1, 2, 3, 4, 5, 6])
print("Negative:", [-7, -6, -5, -4, -3, -2, -1])
print()

print("Slicing with step (reverse order):")
# [start:end:step] - step of -1 means go backwards
print(f"l[4:0:-1] = {l[4:0:-1]}")  # From index 4 to 1 (backwards)
print(f"l[-3:-7:-1] = {l[-3:-7:-1]}")  # Same slice using negative indices

print()
print("Standard slicing examples:")
print(f"Full list: {l}")
print(f"First 4 items [0:4]: {l[0:4]}")
print(f"First 4 items [:4]: {l[:4]}")  # Same as above
print(f"Using negative indices [-7:-3]: {l[-7:-3]}")
print(f"Middle section [2:4]: {l[2:4]}")

print()
print("Slicing with step:")
print(f"Every 2nd item [::2]: {l[::2]}")    # Start at 0, step by 2
print(f"Every 2nd item starting from 1 [1::2]: {l[1::2]}")  # Start at 1, step by 2
print(f"Reverse entire list [::-1]: {l[::-1]}")  # Reverse the whole list

print()

# -----------------------------------------------------------------------------
# 5. PRACTICAL LIST SLICING EXERCISE
# -----------------------------------------------------------------------------

print("5. Practical List Slicing Exercise")
print("-" * 35)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(f"Working with list: {my_list}")

print("Basic operations:")
print(f"First element: {my_list[0]}")
print(f"Last element: {my_list[-1]}")
print(f"First 4 elements: {my_list[0:4]}")

# Getting last 3 elements in reverse order
second_list = my_list[-1:-4:-1]  # Last 3 in reverse
print(f"Last 3 elements reversed: {second_list}")

print()

# -----------------------------------------------------------------------------
# 6. LIST METHODS AND OPERATIONS
# -----------------------------------------------------------------------------

print("6. List Methods and Operations")
print("-" * 30)

# Start with a list containing duplicates
my_list = [0, 1, 0, 0, 0, 2, 3, 4, 5, 6, 7, 8]
print(f"Starting list: {my_list}")

# Adding elements
my_list.append('bob')  # Add single item to end
print(f"After append('bob'): {my_list}")

my_list.append(['bob', 'alice'])  # Add a list as single item
print(f"After append(['bob', 'alice']): {my_list}")

# Removing elements
my_list.remove(['bob', 'alice'])  # Remove specific item
print(f"After remove(['bob', 'alice']): {my_list}")

my_list.remove(0)  # Remove first occurrence of 0
print(f"After remove(0): {my_list}")

# Clear all elements
original_list = my_list.copy()  # Save a copy first
my_list.clear()  # Remove all elements
print(f"After clear(): {my_list}")

print()
print("Important list methods:")
print("- append(item): Add item to end of list")
print("- remove(item): Remove first occurrence of item")
print("- clear(): Remove all items from list")
print("- copy(): Create a copy of the list")
print()

# -----------------------------------------------------------------------------
# 7. MIN AND MAX FUNCTIONS
# -----------------------------------------------------------------------------

print("7. Finding Minimum and Maximum Values")
print("-" * 40)

# With numbers
l = [4, 6, 15, 17, -3]
print(f"Number list: {l}")
print(f"Minimum value: {min(l)}")
print(f"Maximum value: {max(l)}")

print()

# With strings (alphabetical order)
l = ['a', 'f', 'A']
print(f"String list: {l}")
print(f"Minimum (alphabetically): {min(l)}")
print(f"Maximum (alphabetically): {max(l)}")

print()
print("Note about string comparison:")
print("- Uppercase letters come before lowercase in ASCII")
print("- 'A' < 'a' because ASCII value of 'A' is 65, 'a' is 97")
print()

# -----------------------------------------------------------------------------
# 8. EXTENDING AND BUILDING LISTS
# -----------------------------------------------------------------------------

print("8. Different Ways to Add Multiple Items to Lists")
print("-" * 50)

my_list = []
print(f"Starting with empty list: {my_list}")

# Method 1: Using += operator
my_list += [2, 1, 3]
print(f"After += [2, 1, 3]: {my_list}")

# Method 2: Using + operator (creates new list)
my_list = my_list + [2, 1, 3]
print(f"After = my_list + [2, 1, 3]: {my_list}")

# Method 3: Using extend() method
my_list.extend([2, 1, 3])
print(f"After extend([2, 1, 3]): {my_list}")

# Adding a single item
my_list.append('cyber')
print(f"After append('cyber'): {my_list}")

print()

# Finding and manipulating items
print("Finding and manipulating specific items:")
cyber_index = my_list.index('cyber')
print(f"Index of 'cyber': {cyber_index}")

my_list.remove('cyber')
print(f"After remove('cyber'): {my_list}")

# Sorting the list
my_list.sort()
print(f"After sort(): {my_list}")

print()
print("Comparison of list addition methods:")
print("- += modifies the original list")
print("- + creates a new list")
print("- extend() adds all items from another list")
print("- append() adds one item (even if it's a list)")
print()

# -----------------------------------------------------------------------------
# 9. SUMMARY OF LIST OPERATIONS
# -----------------------------------------------------------------------------

print("9. Summary of List Operations")
print("-" * 30)

print("INDEXING:")
print("- list[0] = first item")
print("- list[-1] = last item")
print("- list[i] = item at position i")
print()

print("SLICING:")
print("- list[start:end] = items from start to end-1")
print("- list[:n] = first n items")
print("- list[n:] = items from position n to end")
print("- list[::step] = every step-th item")
print("- list[::-1] = reverse the list")
print()

print("METHODS:")
print("- append(item) = add item to end")
print("- extend(list) = add all items from another list")
print("- remove(item) = remove first occurrence")
print("- index(item) = find position of item")
print("- sort() = sort the list")
print("- clear() = remove all items")
print()

print("FUNCTIONS:")
print("- len(list) = number of items")
print("- min(list) = smallest item")
print("- max(list) = largest item")
print()

# -----------------------------------------------------------------------------
# 10. EXERCISES FOR PRACTICE
# -----------------------------------------------------------------------------

print("10. Try It Yourself!")
print("-" * 21)
print("Practice exercises to master lists:")
print()

print("Exercise 1: List slicing practice")
print("- Create a list with 10 numbers")
print("- Get the first 5 items")
print("- Get the last 3 items")
print("- Get every 2nd item")
print("- Reverse the entire list")
print()

print("Exercise 2: List manipulation")
print("- Start with an empty list")
print("- Add some numbers using different methods")
print("- Find the min and max values")
print("- Sort the list")
print()

print("Exercise 3: Age calculator improvement")
print("- Ask for current age (use a variable instead of input)")
print("- Calculate age in 10, 20, and 50 years")
print("- Store results in a list")
print("- Print the list")
print()

# TODO for students: Uncomment and complete these exercises

# # Exercise 1: List slicing practice
# print("\n--- Exercise 1: List slicing practice ---")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # first_five = ?
# # last_three = ?
# # every_second = ?
# # reversed_list = ?

# # Exercise 2: List manipulation
# print("\n--- Exercise 2: List manipulation ---")
# my_numbers = []
# # Add numbers using +=, extend(), and append()
# # Find min, max, and sort

# # Exercise 3: Age calculator with lists
# print("\n--- Exercise 3: Age calculator improvement ---")
# current_age = 20  # Use your age here
# # Calculate future ages and store in list
# # Print results

print("\n" + "=" * 60)
print("End of Session 04 - Great work with advanced list operations!")
print("Lists are fundamental in Python - practice these concepts well!")
