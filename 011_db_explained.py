"""
Session 11: Database Operations and HTTP Requests
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Master SQLite database operations in Python
- Understand SQL basics for CRUD operations
- Learn to create and manage database tables
- Practice safe database queries and data insertion
- Work with HTTP requests using the requests library
- Understand HTTP methods and status codes
- Handle web API interactions and responses
- Apply databases and HTTP to cybersecurity scenarios

Author: Programming Instructor
Date: 29-Oct-2025
"""

# =============================================================================
# DATABASE OPERATIONS AND HTTP REQUESTS
# =============================================================================

print("Welcome to Session 11: Database Operations and HTTP Requests")
print("=" * 61)
print()

# -----------------------------------------------------------------------------
# 1. INTRODUCTION TO DATABASES
# -----------------------------------------------------------------------------

print("1. Introduction to Databases")
print("-" * 27)

print("What is a database?")
print("- Organized collection of structured data")
print("- Persistent storage (data survives program restarts)")
print("- Efficient data retrieval and management")
print("- Supports concurrent access and data integrity")
print()

print("Why use databases?")
print("- Store large amounts of data efficiently")
print("- Query and filter data quickly")
print("- Maintain data relationships and consistency")
print("- Support multi-user access")
print("- Provide data backup and recovery")
print()

print("SQLite characteristics:")
print("- Lightweight, serverless database")
print("- Stored in a single file")
print("- No configuration required")
print("- Perfect for small to medium applications")
print("- Built into Python (no installation needed)")
print()

print("Databases in cybersecurity:")
print("- Store security events and logs")
print("- Track user accounts and permissions")
print("- Maintain threat intelligence databases")
print("- Record incident response activities")
print("- Manage vulnerability assessments")
print()

# -----------------------------------------------------------------------------
# 2. SQLITE BASICS - CREATING A DATABASE
# -----------------------------------------------------------------------------

print("2. SQLite Basics - Creating a Database")
print("-" * 37)

import sqlite3

# Create or connect to a database
print("Creating/connecting to a database file...")
conn = sqlite3.connect('security_system.db')
cursor = conn.cursor()

print("Database connection established!")
print("- Connection object: manages database connection")
print("- Cursor object: executes SQL commands")
print()

# Create a simple table
print("Creating a 'users' table...")

create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        role TEXT NOT NULL,
        created_date TEXT NOT NULL,
        active INTEGER DEFAULT 1
    )
"""

cursor.execute(create_table_query)
conn.commit()

print("Table created successfully!")
print()

print("SQL table structure explanation:")
print("- user_id: Unique identifier (auto-increments)")
print("- username: User's login name (must be unique)")
print("- email: User's email address")
print("- role: User's security role (admin, analyst, viewer)")
print("- created_date: When account was created")
print("- active: Boolean flag (1=active, 0=inactive)")
print()

print("SQL data types in SQLite:")
print("- INTEGER: Whole numbers")
print("- TEXT: String/text data")
print("- REAL: Floating-point numbers")
print("- BLOB: Binary data")
print("- NULL: Missing/empty value")
print()

print("Table constraints:")
print("- PRIMARY KEY: Unique identifier for each row")
print("- NOT NULL: Field cannot be empty")
print("- UNIQUE: No duplicate values allowed")
print("- DEFAULT: Default value if none provided")
print("- AUTOINCREMENT: Automatically generates next number")
print()

# -----------------------------------------------------------------------------
# 3. INSERTING DATA INTO DATABASE
# -----------------------------------------------------------------------------

print("3. Inserting Data Into Database")
print("-" * 30)

from datetime import datetime

def insert_user(username, email, role):
    """Insert a new user into the database"""
    
    created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    insert_query = """
        INSERT INTO users (username, email, role, created_date)
        VALUES (?, ?, ?, ?)
    """
    
    try:
        cursor.execute(insert_query, (username, email, role, created_date))
        conn.commit()
        print(f"User '{username}' added successfully!")
        return True
    except sqlite3.IntegrityError as e:
        print(f"Error: {e} (username might already exist)")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

print("Method 1: Using parameterized queries (SAFE)")
print("Benefits: Prevents SQL injection attacks")
print()

# Insert some sample users
print("Inserting sample users:")
insert_user("alice_admin", "alice@company.com", "admin")
insert_user("bob_analyst", "bob@company.com", "analyst")
insert_user("charlie_viewer", "charlie@company.com", "viewer")
insert_user("diana_analyst", "diana@company.com", "analyst")

print()

print("Why use parameterized queries?")
print("- Prevents SQL injection attacks")
print("- Automatically handles special characters")
print("- More secure and reliable")
print("- Uses ? as placeholders for values")
print()

print("DANGER: Never use string formatting for SQL!")
print("BAD:  f\"INSERT INTO users VALUES ('{username}')\"")
print("GOOD: cursor.execute(query, (username,))")
print()

# -----------------------------------------------------------------------------
# 4. QUERYING DATA - SELECT STATEMENTS
# -----------------------------------------------------------------------------

print("4. Querying Data - SELECT Statements")
print("-" * 35)

def display_all_users():
    """Display all users in the database"""
    
    query = "SELECT user_id, username, email, role, active FROM users"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        print(f"Total users in database: {len(results)}")
        print("-" * 80)
        print(f"{'ID':<5} {'Username':<20} {'Email':<25} {'Role':<15} {'Active':<6}")
        print("-" * 80)
        
        for user_id, username, email, role, active in results:
            status = "Yes" if active == 1 else "No"
            print(f"{user_id:<5} {username:<20} {email:<25} {role:<15} {status:<6}")
        
        print("-" * 80)
        return results
    
    except Exception as e:
        print(f"Error querying users: {e}")
        return []

print("Example: Fetching all users from database")
all_users = display_all_users()
print()

print("Fetch methods:")
print("- fetchall(): Returns all rows as list of tuples")
print("- fetchone(): Returns next single row")
print("- fetchmany(n): Returns n rows")
print()

# Filtering queries
def get_users_by_role(role):
    """Get all users with a specific role"""
    
    query = "SELECT username, email FROM users WHERE role = ? AND active = 1"
    
    try:
        cursor.execute(query, (role,))
        results = cursor.fetchall()
        
        print(f"Active users with role '{role}':")
        for username, email in results:
            print(f"  - {username} ({email})")
        
        return results
    
    except Exception as e:
        print(f"Error querying by role: {e}")
        return []

print("Example: Filtering users by role")
analysts = get_users_by_role("analyst")
print()

# Sorting and ordering
def get_users_sorted(order_by="username", ascending=True):
    """Get users sorted by specified column"""
    
    order = "ASC" if ascending else "DESC"
    query = f"SELECT username, role, created_date FROM users ORDER BY {order_by} {order}"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        print(f"Users sorted by {order_by} ({'ascending' if ascending else 'descending'}):")
        for username, role, created_date in results:
            print(f"  {username:<20} {role:<15} {created_date}")
        
        return results
    
    except Exception as e:
        print(f"Error sorting users: {e}")
        return []

print("Example: Sorting users")
sorted_users = get_users_sorted("role", ascending=True)
print()

# -----------------------------------------------------------------------------
# 5. UPDATING DATA IN DATABASE
# -----------------------------------------------------------------------------

print("5. Updating Data in Database")
print("-" * 27)

def update_user_role(username, new_role):
    """Update a user's role"""
    
    update_query = "UPDATE users SET role = ? WHERE username = ?"
    
    try:
        cursor.execute(update_query, (new_role, username))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Updated {username}'s role to '{new_role}'")
            return True
        else:
            print(f"User '{username}' not found")
            return False
    
    except Exception as e:
        print(f"Error updating user: {e}")
        return False

def deactivate_user(username):
    """Deactivate a user account"""
    
    update_query = "UPDATE users SET active = 0 WHERE username = ?"
    
    try:
        cursor.execute(update_query, (username,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"User '{username}' has been deactivated")
            return True
        else:
            print(f"User '{username}' not found")
            return False
    
    except Exception as e:
        print(f"Error deactivating user: {e}")
        return False

print("Example: Updating user data")
update_user_role("bob_analyst", "senior_analyst")
deactivate_user("charlie_viewer")
print()

print("UPDATE statement components:")
print("- UPDATE table_name: Specifies which table to update")
print("- SET column = value: Specifies what to change")
print("- WHERE condition: Specifies which rows to update")
print("- Important: Always use WHERE to avoid updating all rows!")
print()

# Show updated data
print("Updated user list:")
display_all_users()
print()

# -----------------------------------------------------------------------------
# 6. DELETING DATA FROM DATABASE
# -----------------------------------------------------------------------------

print("6. Deleting Data from Database")
print("-" * 29)

def delete_user(username):
    """Delete a user from the database"""
    
    delete_query = "DELETE FROM users WHERE username = ?"
    
    try:
        # First, check if user exists
        cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
        if cursor.fetchone() is None:
            print(f"User '{username}' not found")
            return False
        
        # Delete the user
        cursor.execute(delete_query, (username,))
        conn.commit()
        
        print(f"User '{username}' has been deleted from database")
        return True
    
    except Exception as e:
        print(f"Error deleting user: {e}")
        return False

def delete_inactive_users():
    """Delete all inactive users"""
    
    delete_query = "DELETE FROM users WHERE active = 0"
    
    try:
        cursor.execute(delete_query)
        conn.commit()
        
        deleted_count = cursor.rowcount
        print(f"Deleted {deleted_count} inactive user(s)")
        return deleted_count
    
    except Exception as e:
        print(f"Error deleting inactive users: {e}")
        return 0

print("Example: Deleting users")
delete_inactive_users()
print()

print("DELETE statement warning:")
print("- DELETE without WHERE deletes ALL rows!")
print("- Always double-check your WHERE clause")
print("- Consider using soft deletes (setting active=0) instead")
print("- No undo - deleted data is gone permanently")
print()

# -----------------------------------------------------------------------------
# 7. PRACTICAL DATABASE APPLICATION
# -----------------------------------------------------------------------------

print("7. Practical Database Application")
print("-" * 32)

# Create a security events table
create_events_table = """
    CREATE TABLE IF NOT EXISTS security_events (
        event_id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_type TEXT NOT NULL,
        severity TEXT NOT NULL,
        source_ip TEXT,
        target_system TEXT,
        description TEXT,
        timestamp TEXT NOT NULL,
        resolved INTEGER DEFAULT 0
    )
"""

cursor.execute(create_events_table)
conn.commit()

print("Created 'security_events' table for logging security incidents")
print()

def log_security_event(event_type, severity, source_ip, target_system, description):
    """Log a security event to the database"""
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    insert_query = """
        INSERT INTO security_events 
        (event_type, severity, source_ip, target_system, description, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    
    try:
        cursor.execute(insert_query, (event_type, severity, source_ip, target_system, description, timestamp))
        conn.commit()
        print(f"Logged {severity} {event_type} event")
        return cursor.lastrowid
    
    except Exception as e:
        print(f"Error logging event: {e}")
        return None

def get_unresolved_events(min_severity="MEDIUM"):
    """Get all unresolved security events above a minimum severity"""
    
    severity_order = {"LOW": 1, "MEDIUM": 2, "HIGH": 3, "CRITICAL": 4}
    
    query = """
        SELECT event_id, event_type, severity, source_ip, target_system, timestamp
        FROM security_events
        WHERE resolved = 0
        ORDER BY 
            CASE severity
                WHEN 'CRITICAL' THEN 4
                WHEN 'HIGH' THEN 3
                WHEN 'MEDIUM' THEN 2
                WHEN 'LOW' THEN 1
            END DESC,
            timestamp DESC
    """
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        min_severity_level = severity_order.get(min_severity.upper(), 1)
        
        filtered_results = [
            event for event in results 
            if severity_order.get(event[2], 0) >= min_severity_level
        ]
        
        print(f"Unresolved events (severity >= {min_severity}):")
        print("-" * 90)
        
        for event_id, event_type, severity, source_ip, target_system, timestamp in filtered_results:
            print(f"[{event_id}] {timestamp} | {severity:8} | {event_type:20} | {source_ip:15} -> {target_system}")
        
        return filtered_results
    
    except Exception as e:
        print(f"Error retrieving events: {e}")
        return []

def resolve_event(event_id):
    """Mark a security event as resolved"""
    
    update_query = "UPDATE security_events SET resolved = 1 WHERE event_id = ?"
    
    try:
        cursor.execute(update_query, (event_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Event {event_id} marked as resolved")
            return True
        else:
            print(f"Event {event_id} not found")
            return False
    
    except Exception as e:
        print(f"Error resolving event: {e}")
        return False

print("Example: Security event logging system")

# Log some sample events
log_security_event("FAILED_LOGIN", "MEDIUM", "203.0.113.45", "auth-server", "Multiple failed login attempts")
log_security_event("MALWARE_DETECTED", "HIGH", "192.168.1.100", "workstation-042", "Trojan detected and quarantined")
log_security_event("PORT_SCAN", "LOW", "198.51.100.23", "firewall", "Port scanning activity detected")
log_security_event("DATA_EXFILTRATION", "CRITICAL", "10.0.0.55", "file-server", "Unauthorized large data transfer")
log_security_event("PRIVILEGE_ESCALATION", "HIGH", "192.168.1.88", "domain-controller", "Suspicious privilege escalation attempt")

print()

# Display unresolved events
unresolved = get_unresolved_events("MEDIUM")
print()

# Resolve some events
if unresolved:
    print("Resolving some events...")
    resolve_event(unresolved[0][0])  # Resolve first event
    print()

# -----------------------------------------------------------------------------
# 8. INTERACTIVE DATABASE OPERATIONS
# -----------------------------------------------------------------------------

print("8. Interactive Database Operations")
print("-" * 33)

def interactive_student_entry():
    """Interactive system to add students to database"""
    
    # Create students table
    create_students_table = """
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            grade INTEGER,
            enrollment_date TEXT
        )
    """
    
    cursor.execute(create_students_table)
    conn.commit()
    
    print("Student Entry System")
    print("Enter student information (type 'exit' to finish)")
    print()
    
    students_added = 0
    
    # Simulated input for demonstration (normally would use input())
    sample_students = [
        "Alice Johnson 10",
        "Bob Smith 12",
        "Charlie Brown 11"
    ]
    
    for entry in sample_students:
        print(f"Enter name and grade: {entry}")
        
        if entry.lower() == 'exit' or entry.lower() == 'e':
            break
        
        parts = entry.split()
        
        if len(parts) >= 3:
            first_name = parts[0]
            last_name = parts[1]
            try:
                grade = int(parts[2])
            except ValueError:
                print("Invalid grade - must be a number")
                continue
            
            enrollment_date = datetime.now().strftime("%Y-%m-%d")
            
            insert_query = """
                INSERT INTO students (first_name, last_name, grade, enrollment_date)
                VALUES (?, ?, ?, ?)
            """
            
            try:
                cursor.execute(insert_query, (first_name, last_name, grade, enrollment_date))
                conn.commit()
                print(f"  Added: {first_name} {last_name} (Grade {grade})")
                students_added += 1
            except Exception as e:
                print(f"  Error adding student: {e}")
        else:
            print("Invalid format. Use: FirstName LastName Grade")
    
    print(f"\nTotal students added: {students_added}")
    return students_added

def display_students_sorted():
    """Display all students sorted by grade"""
    
    query = """
        SELECT first_name, last_name, grade, enrollment_date
        FROM students
        ORDER BY grade DESC, last_name ASC
    """
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        print("\nStudent List (sorted by grade):")
        print("-" * 60)
        print(f"{'Name':<25} {'Grade':<10} {'Enrolled':<20}")
        print("-" * 60)
        
        for first_name, last_name, grade, enrollment_date in results:
            full_name = f"{first_name} {last_name}"
            print(f"{full_name:<25} {grade:<10} {enrollment_date:<20}")
        
        print("-" * 60)
        return results
    
    except Exception as e:
        print(f"Error displaying students: {e}")
        return []

print("Example: Interactive student database")
interactive_student_entry()
display_students_sorted()
print()

# -----------------------------------------------------------------------------
# 9. INTRODUCTION TO HTTP REQUESTS
# -----------------------------------------------------------------------------

print("9. Introduction to HTTP Requests")
print("-" * 31)

print("What are HTTP requests?")
print("- HTTP: HyperText Transfer Protocol")
print("- Standard protocol for web communication")
print("- Client sends request, server sends response")
print("- Foundation of web APIs and services")
print()

print("HTTP methods (verbs):")
print("- GET: Retrieve data from server")
print("- POST: Send data to server")
print("- PUT: Update existing data")
print("- DELETE: Remove data")
print("- PATCH: Partial update of data")
print()

print("HTTP status codes:")
print("- 200: OK - Request successful")
print("- 201: Created - Resource created successfully")
print("- 400: Bad Request - Invalid request")
print("- 401: Unauthorized - Authentication required")
print("- 403: Forbidden - Access denied")
print("- 404: Not Found - Resource doesn't exist")
print("- 500: Internal Server Error - Server error")
print()

print("HTTP in cybersecurity:")
print("- Interact with security APIs")
print("- Fetch threat intelligence feeds")
print("- Submit samples to malware analysis services")
print("- Query vulnerability databases")
print("- Automate security tool interactions")
print()

# -----------------------------------------------------------------------------
# 10. WORKING WITH REQUESTS LIBRARY
# -----------------------------------------------------------------------------

print("10. Working with Requests Library")
print("-" * 32)

print("The requests library makes HTTP easy:")
print("- Simple, intuitive API")
print("- Handles encoding, headers automatically")
print("- Supports sessions and authentication")
print("- Built-in JSON support")
print()

try:
    import requests
    
    print("Example: Making a simple HTTP GET request")
    print()
    
    # Example 1: Simple GET request
    print("Request 1: Checking a website status")
    url = "https://httpbin.org/status/200"
    
    try:
        response = requests.get(url, timeout=5)
        
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Status: {'Success' if response.status_code == 200 else 'Failed'}")
        print()
    
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.ConnectionError:
        print("Connection error")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: GET request with response data
    print("Request 2: Fetching JSON data from API")
    api_url = "https://httpbin.org/json"
    
    try:
        response = requests.get(api_url, timeout=5)
        
        if response.status_code == 200:
            print(f"Status Code: {response.status_code}")
            
            # Get response as JSON
            data = response.json()
            print(f"Response Type: JSON")
            print(f"Data Keys: {list(data.keys())}")
            print(f"Sample Data: {str(data)[:100]}...")
        else:
            print(f"Request failed with status code: {response.status_code}")
        
        print()
    
    except Exception as e:
        print(f"Error: {e}")
        print()
    
    # Example 3: Response properties
    print("Request 3: Examining response properties")
    url = "https://httpbin.org/get"
    
    try:
        response = requests.get(url, timeout=5)
        
        print(f"URL: {response.url}")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(list(response.headers.items())[:3])}...")
        print(f"Encoding: {response.encoding}")
        print(f"Content Type: {response.headers.get('content-type')}")
        
        # Response content
        print(f"\nResponse text (first 200 chars):")
        print(response.text[:200] + "...")
        
        print(f"\nResponse content (bytes, first 100 bytes):")
        print(str(response.content[:100]) + "...")
        
        print()
    
    except Exception as e:
        print(f"Error: {e}")
        print()
    
    # Example 4: Custom headers and parameters
    print("Request 4: Using custom headers and parameters")
    url = "https://httpbin.org/get"
    
    # Custom headers
    headers = {
        "User-Agent": "SecurityScanner/1.0",
        "Accept": "application/json"
    }
    
    # Query parameters
    params = {
        "source": "security_tool",
        "version": "1.0",
        "scan_type": "vulnerability"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print(f"Request URL: {response.url}")
            print(f"Sent Headers: {headers}")
            print(f"Sent Parameters: {params}")
            print(f"Status: Success ({response.status_code})")
        
        print()
    
    except Exception as e:
        print(f"Error: {e}")
        print()
    
    print("Best practices for HTTP requests:")
    print("- Always set a timeout to prevent hanging")
    print("- Handle exceptions (timeouts, connection errors)")
    print("- Check status codes before processing response")
    print("- Use appropriate headers for your application")
    print("- Respect rate limits and API terms of service")
    print()

except ImportError:
    print("Note: 'requests' library not installed")
    print("Install with: pip install requests")
    print()
    print("HTTP request concepts still apply!")
    print()

# -----------------------------------------------------------------------------
# CLEANUP AND BEST PRACTICES
# -----------------------------------------------------------------------------

print("Database Best Practices:")
print("- Always close connections when done")
print("- Use parameterized queries to prevent SQL injection")
print("- Create indexes for frequently queried columns")
print("- Use transactions for multiple related operations")
print("- Regularly backup your database files")
print("- Handle exceptions appropriately")
print()

# Close the database connection
conn.close()
print("Database connection closed")
print()

print("=" * 61)
print("End of Session 11 - Excellent work with databases and HTTP!")
print("Databases are essential for data persistence and management!")
print("HTTP requests enable integration with external services and APIs!")
print("These skills are fundamental for cybersecurity automation!")
