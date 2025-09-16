"""
Session 05: Variables and Data Types - Part 3 (Tuples and Dictionaries)
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Understand tuples and their immutable nature
- Learn tuple-to-list and list-to-tuple conversion
- Master dictionary creation and manipulation
- Work with dictionary keys and values
- Practice with tuple concatenation
- Explore practical applications of tuples and dictionaries

Author: Programming Instructor
Date: 16-Sep-2025
"""

# =============================================================================
# TUPLES AND DICTIONARIES
# =============================================================================

print("Welcome to Session 05: Tuples and Dictionaries")
print("=" * 50)
print()

# -----------------------------------------------------------------------------
# 1. INTRODUCTION TO TUPLES
# -----------------------------------------------------------------------------

print("1. Introduction to Tuples")
print("-" * 25)

# Tuples are like lists, but they are IMMUTABLE (cannot be changed)
x = (1, 2, 3, 4, 5, "Sebastian")
print(f"Original tuple: {x}")
print(f"Type: {type(x)}")

print()
print("Key differences between tuples and lists:")
print("- Tuples use parentheses: (1, 2, 3)")
print("- Lists use square brackets: [1, 2, 3]")
print("- Tuples are immutable (cannot be changed after creation)")
print("- Lists are mutable (can be modified)")
print()

# You can access tuple elements just like lists
print("Accessing tuple elements:")
print(f"First element: {x[0]}")
print(f"Last element: {x[-1]}")
print(f"Length of tuple: {len(x)}")
print()

# -----------------------------------------------------------------------------
# 2. TUPLE IMMUTABILITY AND WORKAROUNDS
# -----------------------------------------------------------------------------

print("2. Tuple Immutability and Workarounds")
print("-" * 38)

print("Problem: We cannot directly modify a tuple")
print("For example, x.append('alex') would cause an error")
print()

print("Solution: Convert to list, modify, then convert back to tuple")
print()

# Method 1: Step by step conversion
print("Method 1: Step by step conversion")
x = (1, 2, 3, 4, 5, "Sebastian")
print(f"Original tuple: {x}")

# Convert tuple to list
y = list(x)
print(f"Converted to list: {y}")
print(f"Type: {type(y)}")

# Now we can modify the list
y.append('alex')
print(f"After appending 'alex': {y}")

# Convert back to tuple
x = tuple(y)
print(f"Converted back to tuple: {x}")
print()

# Method 2: One-line conversion
print("Method 2: One-line conversion")
x = (1, 2, 3, 4, 5, "Sebastian")
y = tuple(list(x) + ['alex'])
print(f"Original: {x}")
print(f"Modified in one line: {y}")
print()

# Method 3: Tuple concatenation (most elegant for tuples)
print("Method 3: Tuple concatenation (recommended)")
x = (1, 2, 3, 4, 5, "Sebastian")
x = x + ('alex',)  # Note: ('alex',) is a tuple with one element
print(f"Using tuple concatenation: {x}")
print()

print("Important note about single-element tuples:")
print("- ('alex',) with comma creates a tuple")
print("- ('alex') without comma is just a string with parentheses")
single_tuple = ('alex',)
not_tuple = ('alex')
print(f"With comma: {single_tuple}, type: {type(single_tuple)}")
print(f"Without comma: {not_tuple}, type: {type(not_tuple)}")
print()

# -----------------------------------------------------------------------------
# 3. WHEN TO USE TUPLES VS LISTS
# -----------------------------------------------------------------------------

print("3. When to Use Tuples vs Lists")
print("-" * 30)

print("Use TUPLES when:")
print("- Data should not change (coordinates, RGB colors, database records)")
print("- You want to prevent accidental modification")
print("- You need to use the data as a dictionary key")
print("- You want slightly better performance for read-only data")
print()

print("Use LISTS when:")
print("- You need to add, remove, or change elements")
print("- The size of your data will vary")
print("- You need list methods like append(), remove(), sort()")
print()

# Example: Coordinates (good use of tuple)
point = (10, 20)
print(f"Point coordinates: {point}")
print("Coordinates shouldn't change once set - perfect for tuple!")
print()

# Example: Shopping list (good use of list)
shopping = ['apples', 'bread', 'milk']
shopping.append('eggs')  # Easy to modify
print(f"Shopping list: {shopping}")
print("Shopping list changes often - perfect for list!")
print()

# -----------------------------------------------------------------------------
# 4. INTRODUCTION TO DICTIONARIES
# -----------------------------------------------------------------------------

print("4. Introduction to Dictionaries")
print("-" * 30)

# Dictionaries store key-value pairs
print("Creating and using dictionaries:")

# Method 1: Create empty dictionary and add items
d = dict()  # or d = {}
print(f"Empty dictionary: {d}")

# Adding key-value pairs
d['name'] = 'Alice'
print(f"After adding name: {d}")

# Keys must be unique - new value overwrites old value
d['name'] = 'Bob'
print(f"After changing name to Bob: {d}")

# Add more key-value pairs
d['name2'] = 'Alice'
d['age'] = 25
d['city'] = 'Copenhagen'
print(f"Complete dictionary: {d}")
print(f"Dictionary length: {len(d)}")
print()

print("Key dictionary concepts:")
print("- Keys must be unique (duplicates overwrite)")
print("- Values can be duplicated")
print("- Keys can be strings, numbers, or tuples")
print("- Values can be any data type")
print()

# -----------------------------------------------------------------------------
# 5. DICTIONARY OPERATIONS AND METHODS
# -----------------------------------------------------------------------------

print("5. Dictionary Operations and Methods")
print("-" * 35)

# Create a sample dictionary
person = {
    'first_name': 'Anna',
    'last_name': 'Hansen',
    'age': 22,
    'city': 'Aarhus',
    'hobbies': ['reading', 'cycling', 'coding']
}

print(f"Sample dictionary: {person}")
print()

print("Accessing dictionary values:")
print(f"First name: {person['first_name']}")
print(f"Age: {person['age']}")
print(f"Hobbies: {person['hobbies']}")
print()

print("Dictionary methods:")
# Get all keys
keys = person.keys()
print(f"All keys: {list(keys)}")

# Get all values
values = person.values()
print(f"All values: {list(values)}")

# Get all key-value pairs
items = person.items()
print(f"All items: {list(items)}")
print()

# Safe way to get values (won't crash if key doesn't exist)
print("Safe value access:")
email = person.get('email', 'No email provided')
print(f"Email: {email}")

# Check if key exists
if 'phone' in person:
    print(f"Phone: {person['phone']}")
else:
    print("Phone number not available")
print()

# -----------------------------------------------------------------------------
# 6. MODIFYING DICTIONARIES
# -----------------------------------------------------------------------------

print("6. Modifying Dictionaries")
print("-" * 23)

student = {'name': 'Erik', 'grade': 85}
print(f"Original: {student}")

# Update existing value
student['grade'] = 92
print(f"Updated grade: {student}")

# Add new key-value pair
student['subject'] = 'Programming'
print(f"Added subject: {student}")

# Remove a key-value pair
removed_grade = student.pop('grade')
print(f"Removed grade {removed_grade}: {student}")

# Add multiple items at once
student.update({'age': 19, 'semester': 1})
print(f"Added multiple items: {student}")
print()

# -----------------------------------------------------------------------------
# 7. NESTED DATA STRUCTURES
# -----------------------------------------------------------------------------

print("7. Nested Data Structures")
print("-" * 25)

# Dictionaries can contain lists, and lists can contain dictionaries
students = {
    'class_1A': ['Alice', 'Bob', 'Charlie'],
    'class_1B': ['Diana', 'Erik', 'Fiona'],
    'teachers': ('Mr. Smith', 'Ms. Johnson')  # Using tuple for teachers
}

print("Nested dictionary with lists and tuple:")
print(f"Students data: {students}")
print()

print("Accessing nested data:")
print(f"Class 1A students: {students['class_1A']}")
print(f"First student in class 1A: {students['class_1A'][0]}")
print(f"All teachers: {students['teachers']}")
print(f"First teacher: {students['teachers'][0]}")
print()

# More complex example
course_data = {
    'course_name': 'CYBS-GBG-E25A Programming',
    'instructors': ('Alex', 'Sebastian'),
    'sessions': [
        {'number': 1, 'topic': 'Introduction', 'completed': True},
        {'number': 2, 'topic': 'Variables', 'completed': True},
        {'number': 3, 'topic': 'Data Types', 'completed': False}
    ]
}

print("Complex nested structure:")
print(f"Course: {course_data['course_name']}")
print(f"Instructors: {course_data['instructors']}")
print(f"First session topic: {course_data['sessions'][0]['topic']}")
print()

# -----------------------------------------------------------------------------
# 8. PRACTICAL EXAMPLES
# -----------------------------------------------------------------------------

print("8. Practical Examples")
print("-" * 20)

# Example 1: Student gradebook
print("Example 1: Student Gradebook")
gradebook = {}
gradebook['Alice'] = [85, 92, 78, 88]
gradebook['Bob'] = [76, 81, 85, 79]
gradebook['Charlie'] = [92, 89, 94, 91]

for student, grades in gradebook.items():
    average = sum(grades) / len(grades)
    print(f"{student}: grades {grades}, average: {average:.1f}")
print()

# Example 2: Configuration settings
print("Example 2: Application Configuration")
config = {
    'app_name': 'Student Portal',
    'version': (1, 2, 0),  # Using tuple for version number
    'settings': {
        'theme': 'dark',
        'language': 'english',
        'notifications': True
    }
}

print(f"App: {config['app_name']} v{'.'.join(map(str, config['version']))}")
print(f"Theme: {config['settings']['theme']}")
print()

# -----------------------------------------------------------------------------
# 9. COMMON PATTERNS AND BEST PRACTICES
# -----------------------------------------------------------------------------

print("9. Common Patterns and Best Practices")
print("-" * 37)

print("Dictionary best practices:")
print("- Use descriptive key names")
print("- Use get() method for safe access")
print("- Check if keys exist before accessing")
print("- Use update() for adding multiple items")
print()

print("Tuple best practices:")
print("- Use for data that shouldn't change")
print("- Don't forget comma for single-element tuples")
print("- Convert to list for modifications, then back to tuple")
print("- Use tuple concatenation for adding elements")
print()

# -----------------------------------------------------------------------------
# 10. EXERCISES FOR PRACTICE
# -----------------------------------------------------------------------------

print("10. Try It Yourself!")
print("-" * 22)
print("Practice exercises to master tuples and dictionaries:")
print()

print("Exercise 1: Tuple manipulation")
print("- Create a tuple with your favorite colors")
print("- Add a new color using tuple concatenation")
print("- Convert to list, add another color, convert back")
print()

print("Exercise 2: Personal dictionary")
print("- Create a dictionary with your personal information")
print("- Include: name, age, hobbies (as a list), hometown")
print("- Practice accessing and updating values")
print()

print("Exercise 3: Grade calculator")
print("- Create a dictionary with student names as keys")
print("- Store lists of grades as values")
print("- Calculate and print average grade for each student")
print()

print("Exercise 4: Data conversion practice")
print("- Start with a list of tuples: [('Alice', 85), ('Bob', 92)]")
print("- Convert to a dictionary")
print("- Add new students")
print("- Convert back to list of tuples")
print()

# TODO for students: Uncomment and complete these exercises

# # Exercise 1: Tuple manipulation
# print("\n--- Exercise 1: Tuple manipulation ---")
# colors = ('red', 'blue', 'green')
# # Add 'yellow' using concatenation
# # Convert to list, add 'purple', convert back

# # Exercise 2: Personal dictionary
# print("\n--- Exercise 2: Personal dictionary ---")
# my_info = {
#     'name': 'Your Name',
#     # Add more fields
# }
# # Practice accessing and updating

# # Exercise 3: Grade calculator
# print("\n--- Exercise 3: Grade calculator ---")
# grades = {
#     'Alice': [85, 90, 78],
#     'Bob': [92, 88, 85]
# }
# # Calculate averages

# # Exercise 4: Data conversion
# print("\n--- Exercise 4: Data conversion ---")
# student_tuples = [('Alice', 85), ('Bob', 92)]
# # Convert to dictionary
# # Add students
# # Convert back to tuples

print("\n" + "=" * 50)
print("End of Session 05 - Great work with tuples and dictionaries!")
print("These data structures are essential for organizing complex data!")