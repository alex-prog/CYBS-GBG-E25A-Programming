"""
Session 09: File Operations and Data Persistence
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Master file input and output operations
- Understand different file modes and their applications
- Learn proper file handling with context managers
- Work with text files for data storage and retrieval
- Practice Path operations for cross-platform compatibility
- Implement file-based data persistence
- Handle file errors and exceptions gracefully
- Apply file operations to real-world scenarios

Author: Programming Instructor
Date: 04-Oct-2025
"""

# =============================================================================
# FILE OPERATIONS AND DATA PERSISTENCE
# =============================================================================

print("Welcome to Session 09: File Operations and Data Persistence")
print("=" * 59)
print()

# -----------------------------------------------------------------------------
# 1. INTRODUCTION TO FILE OPERATIONS
# -----------------------------------------------------------------------------

print("1. Introduction to File Operations")
print("-" * 33)

print("Why work with files?")
print("- Store data permanently (persistence)")
print("- Share data between programs")
print("- Create logs and reports")
print("- Process large datasets")
print("- Configuration and settings storage")
print()

print("File operation basics:")
print("- Opening files: open() function")
print("- Reading data: read(), readline(), readlines()")
print("- Writing data: write(), writelines()")
print("- Closing files: close() method or context managers")
print()

print("File modes:")
print("- 'r': Read mode (default)")
print("- 'w': Write mode (overwrites existing content)")
print("- 'a': Append mode (adds to end of file)")
print("- 'r+': Read and write mode")
print("- 'x': Exclusive creation (fails if file exists)")
print()

# -----------------------------------------------------------------------------
# 2. READING FILES - BASIC METHODS
# -----------------------------------------------------------------------------

print("2. Reading Files - Basic Methods")
print("-" * 31)

# First, let's create a sample file to work with
print("Creating a sample log file for demonstration...")

sample_log_content = """2025-10-04 09:15:23 INFO User alice logged in successfully
2025-10-04 09:16:45 WARNING Failed login attempt for user bob
2025-10-04 09:17:12 INFO User alice accessed secure document
2025-10-04 09:18:33 ERROR Database connection timeout
2025-10-04 09:19:01 INFO User charlie logged in successfully
2025-10-04 09:20:15 WARNING Multiple failed attempts detected
2025-10-04 09:21:44 CRITICAL Security breach detected - IP: 192.168.1.100"""

# Write sample file
with open('security_log.txt', 'w') as f:
    f.write(sample_log_content)

print("Sample file 'security_log.txt' created.")
print()

# Method 1: Reading entire file at once
print("Method 1: Reading entire file with read()")
with open('security_log.txt', 'r') as file:
    entire_content = file.read()
    print("File content:")
    print(entire_content[:100] + "..." if len(entire_content) > 100 else entire_content)

print()

# Method 2: Reading line by line
print("Method 2: Reading line by line with readline()")
with open('security_log.txt', 'r') as file:
    line_count = 0
    while True:
        line = file.readline()
        if not line:  # End of file
            break
        line_count += 1
        if line_count <= 3:  # Show first 3 lines
            print(f"Line {line_count}: {line.strip()}")
    
    print(f"... (showing first 3 of {line_count} total lines)")

print()

# Method 3: Reading all lines into a list
print("Method 3: Reading all lines with readlines()")
with open('security_log.txt', 'r') as file:
    all_lines = file.readlines()
    print(f"Total lines read: {len(all_lines)}")
    print("First and last lines:")
    print(f"First: {all_lines[0].strip()}")
    print(f"Last:  {all_lines[-1].strip()}")

print()

print("Best practices for reading files:")
print("- Use context managers (with statement) for automatic file closing")
print("- Choose appropriate method based on file size and usage")
print("- strip() removes newline characters from lines")
print("- Handle large files line by line to save memory")
print()

# -----------------------------------------------------------------------------
# 3. PROCESSING FILE CONTENT
# -----------------------------------------------------------------------------

print("3. Processing File Content")
print("-" * 26)

print("Example: Analyzing security log data")

def analyze_security_log(filename):
    """Analyze security log file and return statistics"""
    
    log_stats = {
        'total_entries': 0,
        'info_count': 0,
        'warning_count': 0,
        'error_count': 0,
        'critical_count': 0,
        'users': set(),
        'suspicious_ips': []
    }
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                
                log_stats['total_entries'] += 1
                
                # Count log levels
                if 'INFO' in line:
                    log_stats['info_count'] += 1
                elif 'WARNING' in line:
                    log_stats['warning_count'] += 1
                elif 'ERROR' in line:
                    log_stats['error_count'] += 1
                elif 'CRITICAL' in line:
                    log_stats['critical_count'] += 1
                
                # Extract usernames
                if 'user ' in line.lower():
                    words = line.split()
                    for i, word in enumerate(words):
                        if word.lower() == 'user' and i + 1 < len(words):
                            username = words[i + 1]
                            log_stats['users'].add(username)
                
                # Extract suspicious IPs
                if 'IP:' in line:
                    parts = line.split('IP:')
                    if len(parts) > 1:
                        ip = parts[1].strip()
                        log_stats['suspicious_ips'].append(ip)
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
    return log_stats

# Analyze our sample log
stats = analyze_security_log('security_log.txt')

if stats:
    print("Security Log Analysis Results:")
    print(f"Total entries: {stats['total_entries']}")
    print(f"INFO messages: {stats['info_count']}")
    print(f"WARNING messages: {stats['warning_count']}")
    print(f"ERROR messages: {stats['error_count']}")
    print(f"CRITICAL messages: {stats['critical_count']}")
    print(f"Unique users: {', '.join(sorted(stats['users']))}")
    print(f"Suspicious IPs: {', '.join(stats['suspicious_ips'])}")

print()

# -----------------------------------------------------------------------------
# 4. WRITING FILES - DIFFERENT MODES
# -----------------------------------------------------------------------------

print("4. Writing Files - Different Modes")
print("-" * 33)

# Write mode ('w') - overwrites existing content
print("Write mode ('w') - creates new file or overwrites existing")
with open('user_report.txt', 'w') as f:
    f.write("Security Report - Generated on 2025-10-04\n")
    f.write("=" * 40 + "\n")
    f.write("Active users today: alice, bob, charlie\n")
    f.write("Failed login attempts: 3\n")

print("File 'user_report.txt' created with initial content.")

# Read back to verify
with open('user_report.txt', 'r') as f:
    content = f.read()
    print("Initial content:")
    print(content)

print()

# Append mode ('a') - adds to end of existing file
print("Append mode ('a') - adds content to end of file")
with open('user_report.txt', 'a') as f:
    f.write("Security alerts: 1 critical\n")
    f.write("Recommended actions: Review access logs\n")

print("Content appended to 'user_report.txt'.")

# Read updated content
with open('user_report.txt', 'r') as f:
    updated_content = f.read()
    print("Updated content:")
    print(updated_content)

print()

# -----------------------------------------------------------------------------
# 5. ADVANCED FILE OPERATIONS WITH PATH
# -----------------------------------------------------------------------------

print("5. Advanced File Operations with Path")
print("-" * 36)

from pathlib import Path

print("Why use pathlib.Path?")
print("- Cross-platform compatibility (Windows, Mac, Linux)")
print("- Object-oriented approach to file paths")
print("- Built-in methods for path manipulation")
print("- More readable and maintainable code")
print()

# Working with Path objects
print("Path operations example:")

# Get current working directory
current_dir = Path.cwd()
print(f"Current directory: {current_dir}")

# Create path to a file
log_file_path = current_dir / 'security_log.txt'
print(f"Log file path: {log_file_path}")

# Check if file exists
if log_file_path.exists():
    print(f"File exists: {log_file_path.name}")
    print(f"File size: {log_file_path.stat().st_size} bytes")
    
    # Get file information
    file_info = log_file_path.stat()
    print(f"Last modified: {file_info.st_mtime}")
else:
    print("File does not exist")

print()

# Create directory structure
print("Creating directory structure:")
data_dir = current_dir / 'security_data'
reports_dir = data_dir / 'reports'
logs_dir = data_dir / 'logs'

# Create directories if they don't exist
reports_dir.mkdir(parents=True, exist_ok=True)
logs_dir.mkdir(parents=True, exist_ok=True)

print(f"Created directory structure:")
print(f"  {data_dir}")
print(f"  ├── {reports_dir.name}/")
print(f"  └── {logs_dir.name}/")

# Move our log file to the logs directory
source_path = current_dir / 'security_log.txt'
target_path = logs_dir / 'security_log.txt'

if source_path.exists():
    # Read content and write to new location
    content = source_path.read_text()
    target_path.write_text(content)
    print(f"Copied log file to: {target_path}")

print()

# -----------------------------------------------------------------------------
# 6. READ AND WRITE MODE (r+)
# -----------------------------------------------------------------------------

print("6. Read and Write Mode (r+)")
print("-" * 27)

print("Creating a counter file for demonstration...")

# First, create a counter file
counter_path = current_dir / 'access_counter.txt'
with open(counter_path, 'w') as f:
    f.write('0\n')  # Start with counter at 0

print("Counter file created with initial value: 0")
print()

def increment_access_counter(filename):
    """Increment access counter in file using r+ mode"""
    
    try:
        with open(filename, 'r+') as f:
            # Read current value
            lines = f.readlines()
            if lines:
                current_count = int(lines[-1].strip())
            else:
                current_count = 0
            
            # Increment counter
            new_count = current_count + 1
            
            # Write new value (append to end)
            f.write(f'{new_count}\n')
            
            return new_count
    
    except FileNotFoundError:
        print(f"Counter file not found: {filename}")
        return None
    except ValueError:
        print("Invalid counter value in file")
        return None
    except Exception as e:
        print(f"Error updating counter: {e}")
        return None

print("Simulating multiple access counter increments:")
for i in range(5):
    count = increment_access_counter(counter_path)
    if count:
        print(f"Access #{i+1}: Counter = {count}")

# Show final counter file content
print("\nFinal counter file content:")
with open(counter_path, 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        print(f"Line {i+1}: {line.strip()}")

print()

print("r+ mode characteristics:")
print("- File must already exist")
print("- Can read from and write to the same file")
print("- File pointer starts at beginning")
print("- Useful for updating existing files")
print()

# -----------------------------------------------------------------------------
# 7. ERROR HANDLING WITH FILES
# -----------------------------------------------------------------------------

print("7. Error Handling with Files")
print("-" * 27)

def safe_file_operations(filename, operation, content=None):
    """Demonstrate proper error handling with file operations"""
    
    try:
        if operation == 'read':
            with open(filename, 'r') as f:
                return f.read()
        
        elif operation == 'write':
            if content is None:
                raise ValueError("Content is required for write operation")
            
            with open(filename, 'w') as f:
                f.write(content)
                return f"Successfully wrote to {filename}"
        
        elif operation == 'append':
            if content is None:
                raise ValueError("Content is required for append operation")
            
            with open(filename, 'a') as f:
                f.write(content)
                return f"Successfully appended to {filename}"
        
        else:
            raise ValueError(f"Unknown operation: {operation}")
    
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    
    except PermissionError:
        return f"Error: Permission denied for file '{filename}'"
    
    except IsADirectoryError:
        return f"Error: '{filename}' is a directory, not a file"
    
    except ValueError as e:
        return f"Error: {e}"
    
    except Exception as e:
        return f"Unexpected error: {e}"

print("Testing error handling with various scenarios:")

# Test cases
test_cases = [
    ('user_report.txt', 'read', None),
    ('nonexistent_file.txt', 'read', None),
    ('test_write.txt', 'write', 'Hello, World!\n'),
    ('invalid_operation.txt', 'delete', 'content'),
    ('.', 'read', None)  # Try to read a directory
]

for filename, operation, content in test_cases:
    result = safe_file_operations(filename, operation, content)
    print(f"{operation.capitalize()} '{filename}': {result}")

print()

# -----------------------------------------------------------------------------
# 8. PRACTICAL FILE APPLICATIONS
# -----------------------------------------------------------------------------

print("8. Practical File Applications")
print("-" * 30)

# Application 1: Configuration file manager
def create_config_file():
    """Create a simple configuration file"""
    
    config_content = """# Security System Configuration
# Generated on 2025-10-04

[SECURITY]
max_login_attempts=3
session_timeout=1800
password_min_length=8
enable_2fa=true

[LOGGING]
log_level=INFO
log_file=security.log
rotate_logs=daily

[NETWORK]
allowed_ips=192.168.1.0/24,10.0.0.0/8
blocked_ports=23,135,139
firewall_enabled=true
"""
    
    config_path = current_dir / 'security_config.txt'
    with open(config_path, 'w') as f:
        f.write(config_content)
    
    return config_path

def read_config_file(config_path):
    """Read and parse configuration file"""
    
    config = {}
    current_section = None
    
    try:
        with open(config_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                
                # Section headers
                if line.startswith('[') and line.endswith(']'):
                    current_section = line[1:-1]
                    config[current_section] = {}
                
                # Key-value pairs
                elif '=' in line and current_section:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Convert boolean values
                    if value.lower() in ['true', 'false']:
                        value = value.lower() == 'true'
                    # Convert numeric values
                    elif value.isdigit():
                        value = int(value)
                    
                    config[current_section][key] = value
    
    except Exception as e:
        print(f"Error reading config file: {e}")
        return None
    
    return config

print("Configuration file management example:")
config_file = create_config_file()
print(f"Created config file: {config_file.name}")

config_data = read_config_file(config_file)
if config_data:
    print("Configuration loaded successfully:")
    for section, settings in config_data.items():
        print(f"  [{section}]")
        for key, value in settings.items():
            print(f"    {key} = {value} ({type(value).__name__})")

print()

# Application 2: Simple data logging
def log_user_activity(username, action, details=""):
    """Log user activity to a file"""
    
    from datetime import datetime
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | {username} | {action}"
    
    if details:
        log_entry += f" | {details}"
    
    log_entry += "\n"
    
    activity_log_path = current_dir / 'user_activity.log'
    
    try:
        with open(activity_log_path, 'a') as f:
            f.write(log_entry)
        return True
    except Exception as e:
        print(f"Failed to log activity: {e}")
        return False

print("User activity logging example:")
activities = [
    ("alice", "LOGIN", "Successful authentication"),
    ("alice", "FILE_ACCESS", "Opened confidential_report.pdf"),
    ("bob", "LOGIN_FAILED", "Incorrect password"),
    ("alice", "LOGOUT", "Session ended normally"),
    ("charlie", "LOGIN", "First login today")
]

for username, action, details in activities:
    if log_user_activity(username, action, details):
        print(f"Logged: {username} - {action}")

print("\nActivity log contents:")
activity_log_path = current_dir / 'user_activity.log'
if activity_log_path.exists():
    with open(activity_log_path, 'r') as f:
        lines = f.readlines()
        for line in lines[-3:]:
            print(f"  {line.strip()}")
        if len(lines) > 3:
            print(f"  ... and {len(lines) - 3} more entries")

print()

# -----------------------------------------------------------------------------
# 9. FILE PROCESSING PATTERNS
# -----------------------------------------------------------------------------

print("9. File Processing Patterns")
print("-" * 26)

print("Common file processing patterns:")
print()

# Pattern 1: Line-by-line processing for large files
def process_large_log_file(filename):
    """Process large log files line by line"""
    
    error_count = 0
    warning_count = 0
    processed_lines = 0
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                processed_lines += 1
                
                # Process each line without loading entire file into memory
                if 'ERROR' in line:
                    error_count += 1
                elif 'WARNING' in line:
                    warning_count += 1
                
                # Simulate processing (in real scenario, you might
                # parse timestamps, extract data, etc.)
    
    except FileNotFoundError:
        return None
    
    return {
        'processed_lines': processed_lines,
        'errors': error_count,
        'warnings': warning_count
    }

# Pattern 2: Batch processing with progress tracking
def process_file_batch(filenames):
    """Process multiple files with progress tracking"""
    
    results = []
    total_files = len(filenames)
    
    for i, filename in enumerate(filenames, 1):
        print(f"Processing file {i}/{total_files}: {filename}")
        
        result = process_large_log_file(filename)
        if result:
            result['filename'] = filename
            results.append(result)
        else:
            print(f"  Failed to process {filename}")
    
    return results

# Pattern 3: File backup before modification
def safe_file_update(filename, new_content):
    """Safely update file with backup"""
    
    file_path = Path(filename)
    backup_path = file_path.with_suffix(file_path.suffix + '.backup')
    
    try:
        # Create backup if original file exists
        if file_path.exists():
            original_content = file_path.read_text()
            backup_path.write_text(original_content)
            print(f"Backup created: {backup_path.name}")
        
        # Write new content
        file_path.write_text(new_content)
        print(f"File updated successfully: {filename}")
        
        return True
    
    except Exception as e:
        print(f"Error updating file: {e}")
        
        # Restore from backup if something went wrong
        if backup_path.exists():
            try:
                backup_content = backup_path.read_text()
                file_path.write_text(backup_content)
                print("File restored from backup")
            except:
                print("Failed to restore from backup")
        
        return False

print("Demonstrating file processing patterns:")
print()

# Test large file processing
log_files_path = logs_dir / 'security_log.txt'
if log_files_path.exists():
    result = process_large_log_file(log_files_path)
    if result:
        print("Large file processing result:")
        print(f"  Lines processed: {result['processed_lines']}")
        print(f"  Errors found: {result['errors']}")
        print(f"  Warnings found: {result['warnings']}")

print()

# Test safe file update
test_file = current_dir / 'test_update.txt'
original_content = "Original content\nLine 2\nLine 3\n"
new_content = "Updated content\nNew line 2\nNew line 3\nAdded line 4\n"

test_file.write_text(original_content)
print("Testing safe file update:")
safe_file_update(test_file, new_content)

print()

# -----------------------------------------------------------------------------
# 10. EXERCISES FOR PRACTICE
# -----------------------------------------------------------------------------

print("10. Try It Yourself!")
print("-" * 22)
print("Practice exercises to master file operations:")
print()

print("Exercise 1: Log File Analyzer")
print("- Read a log file and extract specific information")
print("- Count different types of events")
print("- Generate a summary report")
print("- Handle file errors gracefully")
print()

print("Exercise 2: Configuration Manager")
print("- Create a system to read/write config files")
print("- Support different data types (strings, numbers, booleans)")
print("- Validate configuration values")
print("- Provide default values for missing settings")
print()

print("Exercise 3: Data Backup System")
print("- Create automatic file backups with timestamps")
print("- Implement rotation (keep only last N backups)")
print("- Add compression for large files")
print("- Create restore functionality")
print()

print("Exercise 4: CSV Data Processor")
print("- Read CSV files line by line")
print("- Process and transform data")
print("- Write results to new files")
print("- Handle malformed data gracefully")
print()

# TODO for students: Uncomment and complete these exercises

# # Exercise 1: Log File Analyzer
# print("\n--- Exercise 1: Log File Analyzer ---")
# 
# def analyze_log_file(filename):
#     # TODO: Implement comprehensive log analysis
#     # - Count different log levels
#     # - Extract timestamps and calculate time ranges
#     # - Identify most active users
#     # - Find potential security issues
#     pass
# 
# def generate_log_report(analysis_results, output_filename):
#     # TODO: Generate formatted report file
#     pass

# # Exercise 2: Configuration Manager
# print("\n--- Exercise 2: Configuration Manager ---")
# 
# class ConfigManager:
#     def __init__(self, config_file):
#         # TODO: Initialize config manager
#         pass
#     
#     def load_config(self):
#         # TODO: Load configuration from file
#         pass
#     
#     def save_config(self):
#         # TODO: Save current configuration to file
#         pass
#     
#     def get_setting(self, section, key, default=None):
#         # TODO: Get configuration value with default
#         pass
#     
#     def set_setting(self, section, key, value):
#         # TODO: Set configuration value
#         pass

# # Exercise 3: Data Backup System
# print("\n--- Exercise 3: Data Backup System ---")
# 
# def create_backup(source_file, backup_dir, max_backups=5):
#     # TODO: Create timestamped backup
#     # - Add timestamp to backup filename
#     # - Ensure backup directory exists
#     # - Remove old backups if exceeding max_backups
#     pass
# 
# def restore_from_backup(backup_file, restore_location):
#     # TODO: Restore file from backup
#     pass

# # Exercise 4: CSV Data Processor
# print("\n--- Exercise 4: CSV Data Processor ---")
# 
# def process_csv_file(input_file, output_file, transform_function):
#     # TODO: Process CSV file with custom transformation
#     # - Read CSV line by line
#     # - Apply transformation function to each row
#     # - Write transformed data to output file
#     # - Handle malformed rows gracefully
#     pass
# 
# def validate_csv_row(row, expected_columns):
#     # TODO: Validate CSV row format
#     pass

print("\n" + "=" * 59)
print("End of Session 09 - Excellent work with file operations!")
print("File handling is essential for data persistence and processing!")
print("Remember to always use proper error handling and context managers!")