# GitHub Copilot Instructions for CYBS-GBG-E25A Programming Course

## Course Context
This repository contains code examples and exercises for Programming Course 1st Semester (CYBS-GBG-E25A). The course focuses on fundamental programming concepts using Python as the primary language.

## Coding Standards and Style

### Python Code Standards
- Use Python 3.8+ compatible syntax
- Follow PEP 8 style guidelines
- Use descriptive variable names (e.g., `student_name` instead of `sn`)
- Include type hints where appropriate for educational clarity
- Keep functions small and focused on a single responsibility

### Code Documentation
- Include docstrings for all functions and classes
- Add inline comments to explain complex logic
- Use clear, educational comments that help students understand concepts
- Include examples in docstrings when helpful

### File Naming Convention
- Use descriptive filenames that indicate the session and topic
- Format: `XXX_topic_description.py` (e.g., `001_variables_and_input.py`)
- Use lowercase with underscores for separation

## Educational Guidelines

### Code Complexity
- Start with simple, clear examples
- Gradually increase complexity throughout the course
- Avoid advanced concepts unless they're being specifically taught
- Prefer explicit code over clever shortcuts for clarity

### Error Handling
- Include basic error handling in examples when appropriate
- Show both correct and incorrect examples to illustrate common mistakes
- Use try/except blocks with clear error messages

### Comments and Documentation
- Explain WHY something is done, not just WHAT is done
- Include expected output as comments when helpful
- Add "TODO" comments for exercises students should complete
- Use `# Example:` to show sample usage

### Variable and Function Names
- Use meaningful names that describe the purpose
- Avoid abbreviations unless they're commonly understood
- Use full words (e.g., `calculate_average` not `calc_avg`)

## Code Examples Format

### Beginning of Each File
```python
"""
Session XX: Topic Name
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Objective 1
- Objective 2
- Objective 3

Author: [Instructor Name]
Date: [Date]
"""
```

### Function Template
```python
def function_name(parameter: type) -> return_type:
    """
    Brief description of what the function does.
    
    Args:
        parameter: Description of the parameter
        
    Returns:
        Description of what is returned
        
    Example:
        >>> function_name(example_input)
        expected_output
    """
    # Implementation here
    pass
```

## Exercise Guidelines

### Creating Exercises
- Include clear instructions as comments
- Provide starter code when appropriate
- Include expected output examples
- Add difficulty indicators (Easy/Medium/Hard)
- Provide hints for complex problems

### Exercise Format
```python
# Exercise X.X: Title
# Difficulty: Easy/Medium/Hard
# 
# Instructions:
# Write a function that...
#
# Expected output:
# function_call() should return: expected_result
#
# Hint: Remember to...

def exercise_function():
    # TODO: Implement this function
    pass
```

## Common Programming Concepts to Emphasize

### For Beginners
- Variables and data types
- Input/output operations
- Basic operators
- Conditional statements
- Loops (for and while)
- Lists and basic data structures
- Functions and scope

### Intermediate Topics
- File handling
- Exception handling
- Object-oriented programming basics
- Modules and imports
- String manipulation
- Basic algorithms

## Code Safety and Best Practices

### Security Considerations
- Always validate user input
- Avoid using `eval()` or `exec()` in examples
- Show secure coding practices
- Demonstrate input sanitization

### Performance Tips
- Show efficient vs inefficient approaches
- Explain time complexity for algorithms
- Demonstrate when to use different data structures

## Testing and Validation

### Include Test Cases
- Provide simple test cases for functions
- Show how to validate input
- Include edge case examples
- Demonstrate debugging techniques

### Example Test Structure
```python
def test_function_name():
    """Test cases for function_name"""
    assert function_name(input1) == expected1
    assert function_name(input2) == expected2
    print("All tests passed!")
```

## Repository Organization

### Session Files
- Each session should have its own numbered file
- Include both complete examples and exercises
- Separate complex topics into multiple files if needed

### Supporting Materials
- Include README.md with course overview
- Add requirements.txt for any dependencies
- Include solution files in a separate directory (if sharing solutions)

## Interactive Learning

### Encourage Experimentation
- Include prompts for students to modify code
- Suggest variations and extensions
- Add "Try this:" sections with challenges
- Include reflection questions as comments

### Real-World Applications
- Connect examples to practical uses
- Include mini-projects that combine multiple concepts
- Show how concepts apply to different domains

## Code Generation Preferences

When generating code for this course:
1. Prioritize clarity over cleverness
2. Include educational comments
3. Use standard library functions when possible
4. Avoid external dependencies unless necessary
5. Make code readable for beginners
6. Include error handling examples
7. Provide complete, runnable examples
8. Add suggestions for further exploration

## Common Patterns to Follow

### Input Validation
```python
def get_user_input(prompt: str) -> str:
    """Get and validate user input"""
    while True:
        user_input = input(prompt).strip()
        if user_input:  # Basic validation
            return user_input
        print("Please enter a valid input.")
```

### Main Function Pattern
```python
def main():
    """Main function to run the program"""
    # Program logic here
    pass

if __name__ == "__main__":
    main()
```

Remember: The goal is to create code that teaches effectively while demonstrating good programming practices that students can build upon throughout their programming journey.
