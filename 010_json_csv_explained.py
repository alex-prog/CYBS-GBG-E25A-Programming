"""
Session 10: JSON and CSV Data Processing
Programming Course 1st Semester (CYBS-GBG-E25A)

Learning objectives:
- Master JSON data format and manipulation
- Understand CSV file processing and data extraction
- Learn to parse and validate structured data
- Work with nested data structures in JSON
- Implement data filtering and transformation
- Handle data format errors and edge cases
- Apply JSON/CSV processing to cybersecurity scenarios
- Create data export and reporting systems

Author: Programming Instructor
Date: 04-Oct-2025
"""

# =============================================================================
# JSON AND CSV DATA PROCESSING
# =============================================================================

print("Welcome to Session 10: JSON and CSV Data Processing")
print("=" * 52)
print()

# -----------------------------------------------------------------------------
# 1. INTRODUCTION TO STRUCTURED DATA
# -----------------------------------------------------------------------------

print("1. Introduction to Structured Data")
print("-" * 33)

print("Why structured data formats?")
print("- Standardized way to store and exchange data")
print("- Human-readable and machine-parseable")
print("- Platform-independent data exchange")
print("- Widely supported across programming languages")
print("- Essential for APIs and data integration")
print()

print("Common structured data formats:")
print("- JSON (JavaScript Object Notation): Web APIs, configuration")
print("- CSV (Comma-Separated Values): Spreadsheet data, reports")
print("- XML: Document markup, complex hierarchical data")
print("- YAML: Configuration files, human-readable format")
print()

print("In cybersecurity, structured data is used for:")
print("- Security alerts and incident reports")
print("- Threat intelligence feeds")
print("- Log analysis and SIEM integration")
print("- Vulnerability databases")
print("- Configuration management")
print()

# -----------------------------------------------------------------------------
# 2. JSON BASICS - STRUCTURE AND SYNTAX
# -----------------------------------------------------------------------------

print("2. JSON Basics - Structure and Syntax")
print("-" * 35)

print("JSON data types:")
print("- Strings: \"text in double quotes\"")
print("- Numbers: 42, 3.14 (integers and floats)")
print("- Booleans: true, false (lowercase)")
print("- null: represents empty/missing value")
print("- Arrays: [item1, item2, item3]")
print("- Objects: {\"key\": \"value\", \"key2\": \"value2\"}")
print()

# Create sample JSON files for demonstration
import json
from pathlib import Path

# Sample security alert JSON
alert_data = {
    "alert_id": "ALT-2025-001234",
    "timestamp": "2025-10-04T14:30:25Z",
    "severity": "high",
    "alert_type": "malware_detection",
    "source_ip": "192.168.1.100",
    "destination_ip": "203.0.113.45",
    "description": "Suspicious executable detected",
    "affected_systems": ["workstation-001", "server-db-01"],
    "indicators": {
        "file_hash": "a1b2c3d4e5f6789012345678901234567890abcd",
        "file_name": "suspicious.exe",
        "file_size": 2048576
    },
    "response_actions": [
        "quarantine_file",
        "isolate_system",
        "notify_security_team"
    ],
    "resolved": False
}

# Create alert.json file
with open('alert.json', 'w') as f:
    json.dump(alert_data, f, indent=4)

print("Sample JSON structure (security alert):")
print(json.dumps(alert_data, indent=2)[:300] + "...")
print()

print("JSON syntax rules:")
print("- Data enclosed in curly braces {}")
print("- Key-value pairs separated by commas")
print("- Keys must be strings in double quotes")
print("- Values can be any valid JSON data type")
print("- No trailing commas allowed")
print("- Case-sensitive (true/false, not True/False)")
print()

# -----------------------------------------------------------------------------
# 3. READING AND PARSING JSON FILES
# -----------------------------------------------------------------------------

print("3. Reading and Parsing JSON Files")
print("-" * 32)

def load_and_analyze_alert(filename):
    """Load and analyze a security alert from JSON file"""
    
    try:
        with open(filename, 'r') as f:
            alert = json.load(f)
        
        print(f"Alert Analysis for {filename}:")
        print(f"  Alert ID: {alert['alert_id']}")
        print(f"  Severity: {alert['severity'].upper()}")
        print(f"  Type: {alert['alert_type'].replace('_', ' ').title()}")
        print(f"  Source: {alert['source_ip']}")
        print(f"  Timestamp: {alert['timestamp']}")
        
        # Access nested data
        if 'indicators' in alert:
            indicators = alert['indicators']
            print(f"  File Hash: {indicators['file_hash'][:16]}...")
            print(f"  File Name: {indicators['file_name']}")
            print(f"  File Size: {indicators['file_size']:,} bytes")
        
        # Access array data
        if 'affected_systems' in alert:
            systems = alert['affected_systems']
            print(f"  Affected Systems: {', '.join(systems)}")
        
        # Check resolution status
        status = "Resolved" if alert.get('resolved', False) else "Open"
        print(f"  Status: {status}")
        
        return alert
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        return None
    except KeyError as e:
        print(f"Error: Missing required field - {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

print("Example: Loading and analyzing security alert")
alert = load_and_analyze_alert('alert.json')
print()

# Demonstrate accessing different data types
if alert:
    print("Accessing different JSON data types:")
    print(f"String: {type(alert['alert_id']).__name__} - {alert['alert_id']}")
    print(f"Boolean: {type(alert['resolved']).__name__} - {alert['resolved']}")
    print(f"List: {type(alert['affected_systems']).__name__} - {len(alert['affected_systems'])} items")
    print(f"Dict: {type(alert['indicators']).__name__} - {len(alert['indicators'])} keys")
    print()

# -----------------------------------------------------------------------------
# 4. WORKING WITH COMPLEX JSON DATA
# -----------------------------------------------------------------------------

print("4. Working with Complex JSON Data")
print("-" * 33)

# Create complex threat intelligence JSON
threat_intel_data = {
    "feed_info": {
        "provider": "CyberThreat Intelligence Corp",
        "version": "2.1",
        "last_updated": "2025-10-04T12:00:00Z",
        "total_indicators": 1250
    },
    "indicators": [
        {
            "id": "IOC-001",
            "type": "ip_address",
            "value": "198.51.100.42",
            "confidence": 95,
            "severity": "high",
            "first_seen": "2025-09-30T08:15:00Z",
            "last_seen": "2025-10-03T16:22:00Z",
            "tags": ["botnet", "c2_server", "malware"],
            "attribution": {
                "threat_actor": "APT-29",
                "campaign": "Operation StealtthDrop",
                "techniques": ["T1071.001", "T1090"]
            }
        },
        {
            "id": "IOC-002",
            "type": "file_hash",
            "value": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "confidence": 88,
            "severity": "medium",
            "first_seen": "2025-10-01T10:30:00Z",
            "last_seen": "2025-10-04T09:45:00Z",
            "tags": ["trojan", "info_stealer"],
            "attribution": {
                "threat_actor": "Unknown",
                "campaign": "RedTeam Exercise",
                "techniques": ["T1059", "T1055"]
            }
        },
        {
            "id": "IOC-003",
            "type": "domain",
            "value": "malicious-site.example.com",
            "confidence": 76,
            "severity": "high",
            "first_seen": "2025-09-28T14:20:00Z",
            "last_seen": "2025-10-02T11:15:00Z",
            "tags": ["phishing", "credential_theft"],
            "attribution": {
                "threat_actor": "CriminalGroup-X",
                "campaign": "Phishing Campaign 2025-Q4",
                "techniques": ["T1566.002"]
            }
        },
        {
            "id": "IOC-004",
            "type": "ip_address",
            "value": "203.0.113.77",
            "confidence": 65,
            "severity": "low",
            "first_seen": "2025-10-03T06:00:00Z",
            "last_seen": "2025-10-04T07:30:00Z",
            "tags": ["scanning", "reconnaissance"],
            "attribution": {
                "threat_actor": "Unknown",
                "campaign": "Automated Scanning",
                "techniques": ["T1595"]
            }
        }
    ]
}

# Save threat intelligence data
with open('threat_intel.json', 'w') as f:
    json.dump(threat_intel_data, f, indent=4)

print("Created threat intelligence feed with complex nested data")
print(f"Feed contains {len(threat_intel_data['indicators'])} indicators")
print()

def filter_high_confidence_indicators(filename, min_confidence=80, target_severity='high'):
    """Filter threat indicators based on confidence and severity"""
    
    try:
        with open(filename, 'r') as f:
            threat_data = json.load(f)
        
        indicators = threat_data.get('indicators', [])
        filtered_indicators = []
        
        print(f"Filtering indicators with confidence > {min_confidence} and severity '{target_severity}'")
        
        for ioc in indicators:
            confidence = ioc.get('confidence', 0)
            severity = ioc.get('severity', '').lower()
            
            if confidence > min_confidence and severity == target_severity.lower():
                filtered_indicators.append(ioc)
                print(f"  ✓ {ioc['id']}: {ioc['type']} - {ioc['value'][:30]}...")
                print(f"    Confidence: {confidence}%, Severity: {severity}")
                print(f"    Tags: {', '.join(ioc.get('tags', []))}")
                print(f"    Attribution: {ioc.get('attribution', {}).get('threat_actor', 'Unknown')}")
                print()
        
        print(f"Found {len(filtered_indicators)} indicators matching criteria")
        return filtered_indicators
    
    except Exception as e:
        print(f"Error processing threat intelligence: {e}")
        return []

print("Example: Filtering high-confidence, high-severity indicators")
high_priority_iocs = filter_high_confidence_indicators('threat_intel.json', 80, 'high')
print()

# Advanced JSON manipulation
def generate_ioc_summary_report(indicators):
    """Generate summary report from filtered indicators"""
    
    if not indicators:
        return "No indicators to analyze"
    
    # Count by type
    type_counts = {}
    severity_counts = {}
    threat_actors = set()
    all_techniques = set()
    
    for ioc in indicators:
        # Count types
        ioc_type = ioc.get('type', 'unknown')
        type_counts[ioc_type] = type_counts.get(ioc_type, 0) + 1
        
        # Count severities
        severity = ioc.get('severity', 'unknown')
        severity_counts[severity] = severity_counts.get(severity, 0) + 1
        
        # Collect threat actors
        attribution = ioc.get('attribution', {})
        actor = attribution.get('threat_actor')
        if actor and actor != 'Unknown':
            threat_actors.add(actor)
        
        # Collect techniques
        techniques = attribution.get('techniques', [])
        all_techniques.update(techniques)
    
    # Generate report
    report = []
    report.append("=" * 50)
    report.append("THREAT INTELLIGENCE SUMMARY REPORT")
    report.append("=" * 50)
    report.append(f"Total Indicators Analyzed: {len(indicators)}")
    report.append("")
    
    report.append("Indicator Types:")
    for ioc_type, count in sorted(type_counts.items()):
        report.append(f"  {ioc_type.replace('_', ' ').title()}: {count}")
    report.append("")
    
    report.append("Severity Distribution:")
    for severity, count in sorted(severity_counts.items()):
        report.append(f"  {severity.title()}: {count}")
    report.append("")
    
    if threat_actors:
        report.append("Known Threat Actors:")
        for actor in sorted(threat_actors):
            report.append(f"  - {actor}")
        report.append("")
    
    if all_techniques:
        report.append(f"MITRE ATT&CK Techniques ({len(all_techniques)} total):")
        techniques_list = sorted(list(all_techniques))
        for i in range(0, len(techniques_list), 5):  # Show 5 per line
            line_techniques = techniques_list[i:i+5]
            report.append(f"  {', '.join(line_techniques)}")
    
    return "\n".join(report)

if high_priority_iocs:
    summary_report = generate_ioc_summary_report(high_priority_iocs)
    print("Generated Summary Report:")
    print(summary_report)
    print()

# -----------------------------------------------------------------------------
# 5. WRITING AND CREATING JSON FILES
# -----------------------------------------------------------------------------

print("5. Writing and Creating JSON Files")
print("-" * 33)

def create_incident_report(incident_id, severity, description, affected_assets):
    """Create a structured incident report in JSON format"""
    
    from datetime import datetime
    
    incident_report = {
        "incident_id": incident_id,
        "created_timestamp": datetime.now().isoformat() + "Z",
        "severity": severity.lower(),
        "status": "open",
        "description": description,
        "affected_assets": affected_assets,
        "timeline": [
            {
                "timestamp": datetime.now().isoformat() + "Z",
                "action": "incident_created",
                "description": "Initial incident report created",
                "user": "security_analyst"
            }
        ],
        "evidence": [],
        "response_actions": [],
        "resolution": None,
        "lessons_learned": None
    }
    
    return incident_report

def save_incident_report(incident_data, filename):
    """Save incident report to JSON file with proper formatting"""
    
    try:
        with open(filename, 'w') as f:
            json.dump(incident_data, f, indent=4, ensure_ascii=False)
        
        print(f"Incident report saved to '{filename}'")
        return True
    
    except Exception as e:
        print(f"Error saving incident report: {e}")
        return False

def add_timeline_entry(incident_file, action, description, user="system"):
    """Add a new timeline entry to existing incident report"""
    
    from datetime import datetime
    
    try:
        # Load existing report
        with open(incident_file, 'r') as f:
            incident = json.load(f)
        
        # Add new timeline entry
        new_entry = {
            "timestamp": datetime.now().isoformat() + "Z",
            "action": action,
            "description": description,
            "user": user
        }
        
        incident['timeline'].append(new_entry)
        
        # Save updated report
        with open(incident_file, 'w') as f:
            json.dump(incident, f, indent=4)
        
        print(f"Timeline entry added: {action}")
        return True
    
    except Exception as e:
        print(f"Error updating timeline: {e}")
        return False

print("Example: Creating and managing incident reports")

# Create new incident
incident = create_incident_report(
    "INC-2025-0187",
    "HIGH",
    "Suspicious network activity detected from external IP address",
    ["web-server-01", "database-server", "user-workstation-045"]
)

# Save incident report
incident_file = "incident_INC-2025-0187.json"
if save_incident_report(incident, incident_file):
    print(f"Created incident report: {incident['incident_id']}")
    print(f"Severity: {incident['severity'].upper()}")
    print(f"Affected assets: {len(incident['affected_assets'])}")

# Add timeline entries
add_timeline_entry(incident_file, "investigation_started", "Security team began investigation", "analyst_smith")
add_timeline_entry(incident_file, "evidence_collected", "Network logs collected for analysis", "analyst_jones")
add_timeline_entry(incident_file, "containment_initiated", "Blocked suspicious IP at firewall", "analyst_smith")

print()

# Read and display updated incident
print("Updated incident report timeline:")
with open(incident_file, 'r') as f:
    updated_incident = json.load(f)
    for i, entry in enumerate(updated_incident['timeline'], 1):
        print(f"  {i}. {entry['timestamp'][:19]} - {entry['action']}")
        print(f"     {entry['description']} (by {entry['user']})")

print()

# -----------------------------------------------------------------------------
# 6. INTRODUCTION TO CSV FORMAT
# -----------------------------------------------------------------------------

print("6. Introduction to CSV Format")
print("-" * 27)

print("CSV (Comma-Separated Values) characteristics:")
print("- Simple, widely-supported format")
print("- Each line represents one record")
print("- Fields separated by commas (or other delimiters)")
print("- First line often contains column headers")
print("- Human-readable and spreadsheet-compatible")
print()

print("CSV in cybersecurity:")
print("- Log exports from SIEM systems")
print("- Vulnerability scan results")
print("- User access reports")
print("- Network traffic summaries")
print("- Threat intelligence feeds")
print()

# Create sample CSV data
import csv

# Sample network traffic log data
network_logs = [
    ["timestamp", "source_ip", "dest_ip", "port", "protocol", "bytes_sent", "bytes_received", "status"],
    ["2025-10-04 14:30:15", "192.168.1.100", "203.0.113.45", "443", "HTTPS", "1024", "2048", "established"],
    ["2025-10-04 14:30:16", "192.168.1.101", "198.51.100.42", "80", "HTTP", "512", "1536", "established"],
    ["2025-10-04 14:30:17", "10.0.0.50", "203.0.113.45", "22", "SSH", "256", "128", "failed"],
    ["2025-10-04 14:30:18", "192.168.1.102", "8.8.8.8", "53", "DNS", "64", "128", "completed"],
    ["2025-10-04 14:30:19", "172.16.0.10", "198.51.100.42", "443", "HTTPS", "2048", "4096", "established"]
]

# Write CSV file
with open('network_traffic.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(network_logs)

print("Created sample network traffic CSV file")
print("Sample CSV content:")
for i, row in enumerate(network_logs[:4]):  # Show first 4 rows
    if i == 0:
        print(f"  Header: {','.join(row)}")
    else:
        print(f"  Row {i}: {','.join(row)}")
if len(network_logs) > 4:
    print(f"  ... and {len(network_logs) - 4} more data rows")
print()

# -----------------------------------------------------------------------------
# 7. READING AND PROCESSING CSV FILES
# -----------------------------------------------------------------------------

print("7. Reading and Processing CSV Files")
print("-" * 33)

def analyze_network_traffic(csv_file):
    """Analyze network traffic from CSV file"""
    
    traffic_stats = {
        'total_connections': 0,
        'protocols': {},
        'status_counts': {},
        'top_sources': {},
        'top_destinations': {},
        'total_bytes_sent': 0,
        'total_bytes_received': 0,
        'failed_connections': []
    }
    
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)  # Automatically uses first row as headers
            
            for row in reader:
                traffic_stats['total_connections'] += 1
                
                # Count protocols
                protocol = row['protocol']
                traffic_stats['protocols'][protocol] = traffic_stats['protocols'].get(protocol, 0) + 1
                
                # Count connection status
                status = row['status']
                traffic_stats['status_counts'][status] = traffic_stats['status_counts'].get(status, 0) + 1
                
                # Track source IPs
                source_ip = row['source_ip']
                traffic_stats['top_sources'][source_ip] = traffic_stats['top_sources'].get(source_ip, 0) + 1
                
                # Track destination IPs
                dest_ip = row['dest_ip']
                traffic_stats['top_destinations'][dest_ip] = traffic_stats['top_destinations'].get(dest_ip, 0) + 1
                
                # Sum bytes
                try:
                    bytes_sent = int(row['bytes_sent'])
                    bytes_received = int(row['bytes_received'])
                    traffic_stats['total_bytes_sent'] += bytes_sent
                    traffic_stats['total_bytes_received'] += bytes_received
                except ValueError:
                    pass  # Skip invalid byte counts
                
                # Track failed connections
                if status == 'failed':
                    traffic_stats['failed_connections'].append({
                        'timestamp': row['timestamp'],
                        'source': source_ip,
                        'destination': dest_ip,
                        'port': row['port']
                    })
    
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found")
        return None
    except Exception as e:
        print(f"Error processing CSV file: {e}")
        return None
    
    return traffic_stats

def display_traffic_analysis(stats):
    """Display formatted traffic analysis results"""
    
    if not stats:
        print("No data to display")
        return
    
    print("Network Traffic Analysis Results:")
    print("=" * 40)
    
    print(f"Total Connections: {stats['total_connections']}")
    print(f"Total Data Sent: {stats['total_bytes_sent']:,} bytes")
    print(f"Total Data Received: {stats['total_bytes_received']:,} bytes")
    print()
    
    print("Protocol Distribution:")
    for protocol, count in sorted(stats['protocols'].items()):
        percentage = (count / stats['total_connections']) * 100
        print(f"  {protocol}: {count} ({percentage:.1f}%)")
    print()
    
    print("Connection Status:")
    for status, count in sorted(stats['status_counts'].items()):
        percentage = (count / stats['total_connections']) * 100
        print(f"  {status.title()}: {count} ({percentage:.1f}%)")
    print()
    
    if stats['failed_connections']:
        print(f"Failed Connections ({len(stats['failed_connections'])}):")
        for failure in stats['failed_connections']:
            print(f"  {failure['timestamp']} - {failure['source']} -> {failure['destination']}:{failure['port']}")
        print()
    
    print("Top Source IPs:")
    sorted_sources = sorted(stats['top_sources'].items(), key=lambda x: x[1], reverse=True)
    for ip, count in sorted_sources[:5]:  # Top 5
        print(f"  {ip}: {count} connections")

print("Example: Analyzing network traffic CSV")
traffic_analysis = analyze_network_traffic('network_traffic.csv')
if traffic_analysis:
    display_traffic_analysis(traffic_analysis)
print()

# -----------------------------------------------------------------------------
# 8. WRITING CSV FILES
# -----------------------------------------------------------------------------

print("8. Writing CSV Files")
print("-" * 17)

def generate_security_report_csv(incidents_data, output_file):
    """Generate security incident report in CSV format"""
    
    # Define CSV headers
    headers = [
        'incident_id', 'date', 'severity', 'category', 'description',
        'affected_systems', 'status', 'analyst_assigned', 'resolution_time'
    ]
    
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            
            # Write header row
            writer.writeheader()
            
            # Write incident data
            for incident in incidents_data:
                writer.writerow(incident)
        
        print(f"Security report written to '{output_file}'")
        return True
    
    except Exception as e:
        print(f"Error writing CSV report: {e}")
        return False

# Sample incident data for CSV export
sample_incidents = [
    {
        'incident_id': 'INC-2025-0185',
        'date': '2025-10-01',
        'severity': 'HIGH',
        'category': 'Malware Detection',
        'description': 'Trojan detected on user workstation',
        'affected_systems': 'WS-USER-042',
        'status': 'Resolved',
        'analyst_assigned': 'Smith, John',
        'resolution_time': '4.5 hours'
    },
    {
        'incident_id': 'INC-2025-0186',
        'date': '2025-10-02',
        'severity': 'MEDIUM',
        'category': 'Unauthorized Access',
        'description': 'Failed login attempts detected',
        'affected_systems': 'SERVER-WEB-01',
        'status': 'In Progress',
        'analyst_assigned': 'Jones, Alice',
        'resolution_time': 'Pending'
    },
    {
        'incident_id': 'INC-2025-0187',
        'date': '2025-10-03',
        'severity': 'LOW',
        'category': 'Policy Violation',
        'description': 'USB device usage without approval',
        'affected_systems': 'WS-USER-018',
        'status': 'Resolved',
        'analyst_assigned': 'Brown, Mike',
        'resolution_time': '1.2 hours'
    }
]

print("Example: Generating security incident report CSV")
if generate_security_report_csv(sample_incidents, 'security_incidents.csv'):
    print(f"Generated report with {len(sample_incidents)} incidents")
    
    # Read back and display first few rows
    print("\nGenerated CSV content (first 2 rows):")
    with open('security_incidents.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                print(f"  Headers: {', '.join(row)}")
            elif i <= 2:
                print(f"  Row {i}: {row[0]} | {row[2]} | {row[3]} | {row[6]}")
            if i >= 2:
                break

print()

# -----------------------------------------------------------------------------
# 9. DATA CONVERSION BETWEEN FORMATS
# -----------------------------------------------------------------------------

print("9. Data Conversion Between Formats")
print("-" * 33)

def csv_to_json_converter(csv_file, json_file):
    """Convert CSV data to JSON format"""
    
    try:
        data_records = []
        
        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                # Convert numeric fields
                if 'bytes_sent' in row:
                    try:
                        row['bytes_sent'] = int(row['bytes_sent'])
                    except ValueError:
                        pass
                
                if 'bytes_received' in row:
                    try:
                        row['bytes_received'] = int(row['bytes_received'])
                    except ValueError:
                        pass
                
                data_records.append(row)
        
        # Create JSON structure
        json_data = {
            "data_source": csv_file,
            "conversion_timestamp": "2025-10-04T14:30:00Z",
            "total_records": len(data_records),
            "records": data_records
        }
        
        # Write JSON file
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2)
        
        print(f"Converted {len(data_records)} records from CSV to JSON")
        print(f"Output saved to '{json_file}'")
        return True
    
    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")
        return False

def json_to_csv_converter(json_file, csv_file, records_key='records'):
    """Convert JSON data to CSV format"""
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        records = json_data.get(records_key, [])
        if not records:
            print(f"No records found in JSON file (looking for key '{records_key}')")
            return False
        
        # Get all unique keys from all records (for headers)
        all_keys = set()
        for record in records:
            all_keys.update(record.keys())
        
        headers = sorted(list(all_keys))
        
        # Write CSV file
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            
            for record in records:
                # Ensure all fields are present (fill missing with empty string)
                complete_record = {key: record.get(key, '') for key in headers}
                writer.writerow(complete_record)
        
        print(f"Converted {len(records)} records from JSON to CSV")
        print(f"Output saved to '{csv_file}'")
        return True
    
    except Exception as e:
        print(f"Error converting JSON to CSV: {e}")
        return False

print("Example: Converting between CSV and JSON formats")

# Convert CSV to JSON
if csv_to_json_converter('network_traffic.csv', 'network_traffic.json'):
    # Read and display JSON structure
    with open('network_traffic.json', 'r') as f:
        converted_data = json.load(f)
        print(f"JSON structure created with {converted_data['total_records']} records")
        print(f"First record: {converted_data['records'][0]}")

print()

# Convert JSON back to CSV
if json_to_csv_converter('network_traffic.json', 'converted_traffic.csv'):
    print("Successfully converted JSON back to CSV format")

print()

# -----------------------------------------------------------------------------
# 10. EXERCISES FOR PRACTICE
# -----------------------------------------------------------------------------

print("10. Try It Yourself!")
print("-" * 22)
print("Practice exercises to master JSON and CSV processing:")
print()

print("Exercise 1: Threat Intelligence Aggregator")
print("- Read multiple JSON threat feeds")
print("- Merge and deduplicate indicators")
print("- Filter by confidence scores and dates")
print("- Export results to both JSON and CSV formats")
print()

print("Exercise 2: Log Analysis Dashboard")
print("- Parse CSV log files from different sources")
print("- Normalize timestamps and field names")
print("- Calculate statistics and trends")
print("- Generate JSON summary reports")
print()

print("Exercise 3: Incident Response Tracker")
print("- Create JSON schema for incident records")
print("- Import incidents from CSV spreadsheets")
print("- Track status changes and timeline")
print("- Export reports in multiple formats")
print()

print("Exercise 4: Vulnerability Management System")
print("- Process JSON vulnerability scan results")
print("- Parse CSV asset inventories")
print("- Match vulnerabilities to assets")
print("- Generate prioritized remediation reports")
print()

# TODO for students: Uncomment and complete these exercises

# # Exercise 1: Threat Intelligence Aggregator
# print("\n--- Exercise 1: Threat Intelligence Aggregator ---")
# 
# def merge_threat_feeds(feed_files):
#     # TODO: Read multiple JSON threat intelligence files
#     # - Load each feed and extract indicators
#     # - Merge indicators and remove duplicates
#     # - Sort by confidence and severity
#     # - Return aggregated feed structure
#     pass
# 
# def export_threat_data(indicators, json_file, csv_file):
#     # TODO: Export threat indicators to both formats
#     # - Create structured JSON with metadata
#     # - Generate CSV with flattened indicator data
#     # - Include conversion timestamp and source info
#     pass

# # Exercise 2: Log Analysis Dashboard
# print("\n--- Exercise 2: Log Analysis Dashboard ---")
# 
# def normalize_log_data(csv_files):
#     # TODO: Read and normalize multiple CSV log files
#     # - Handle different timestamp formats
#     # - Standardize field names and values
#     # - Detect and handle malformed records
#     # - Return unified data structure
#     pass
# 
# def generate_dashboard_data(normalized_logs):
#     # TODO: Calculate dashboard statistics
#     # - Time-based trends and patterns
#     # - Top sources, destinations, protocols
#     # - Anomaly detection and alerts
#     # - Export as JSON for web dashboard
#     pass

# # Exercise 3: Incident Response Tracker
# print("\n--- Exercise 3: Incident Response Tracker ---")
# 
# class IncidentTracker:
#     def __init__(self, data_file):
#         # TODO: Initialize incident tracking system
#         pass
#     
#     def import_incidents_from_csv(self, csv_file):
#         # TODO: Import incidents from CSV spreadsheet
#         pass
#     
#     def update_incident_status(self, incident_id, new_status, notes):
#         # TODO: Update incident status and add timeline entry
#         pass
#     
#     def export_status_report(self, output_format='json'):
#         # TODO: Generate status report in requested format
#         pass

# # Exercise 4: Vulnerability Management System
# print("\n--- Exercise 4: Vulnerability Management System ---")
# 
# def process_vulnerability_scan(json_scan_file):
#     # TODO: Parse JSON vulnerability scan results
#     # - Extract vulnerability details
#     # - Normalize CVSS scores and severity
#     # - Group by affected systems
#     # - Return structured vulnerability data
#     pass
# 
# def match_vulnerabilities_to_assets(vuln_data, asset_csv):
#     # TODO: Match vulnerabilities to asset inventory
#     # - Load asset information from CSV
#     # - Match by IP addresses, hostnames, etc.
#     # - Calculate risk scores based on asset criticality
#     # - Generate prioritized remediation list
#     pass

print("\n" + "=" * 52)
print("End of Session 10 - Outstanding work with structured data!")
print("JSON and CSV are fundamental for data exchange and analysis!")
print("These skills are essential for cybersecurity data processing!")