# Beginner-Cybersecurity-Projects-and-Tools
# Suspicious IP Detector

## Overview

Suspicious IP Detector is a beginner-friendly cybersecurity project built with Python.

The project analyzes authentication logs and identifies IP addresses that generate an unusually high number of failed login attempts within a specific time window.

It is designed as a small SOC-style detection tool.

The project demonstrates how security logs can be processed and converted into actionable alerts.

## Features

* Parses authentication log files.
* Extracts timestamps from log entries.
* Extracts IP addresses.
* Detects failed login attempts.
* Groups events by IP address.
* Uses a configurable time window.
* Detects repeated failed login attempts.
* Assigns alert severity levels.
* Displays alerts in the terminal.
* Generates a CSV security report.

## Detection Logic

The detector uses two main conditions.

First, an IP must generate a minimum number of failed login attempts.

Second, those attempts must occur within the configured time window.

The default configuration is:

```text
Failed login threshold: 5 attempts
Time window: 5 minutes
```

For example:

```text
192.168.1.20
7 failed attempts
within 5 minutes
```

This will generate a security alert.

## Severity Levels

The project currently uses three severity levels.

```text
5-6 attempts   → LOW
7-9 attempts   → MEDIUM
10+ attempts   → HIGH
```

These values are configurable and are intended for demonstration purposes.

## Example Log

The detector expects log entries similar to:

```text
2026-09-27 09:04:08 FAILED_LOGIN 192.168.1.20
2026-09-27 09:04:15 FAILED_LOGIN 192.168.1.20
2026-09-27 09:04:21 FAILED_LOGIN 192.168.1.20
```

Each entry contains:

```text
Date
Time
Event Type
IP Address
```

## Project Structure

```text
suspicious_ip_detector/
│
├── suspicious_ip_detector.py
├── sample_logs.txt
├── suspicious_ips.csv
├── README.md
└── requirements.txt
```

## Technologies Used

* Python
* datetime
* collections
* csv
* File handling
* Log analysis

## How It Works

The program first opens the log file.

Each log entry is read individually.

The line is split into separate fields.

The timestamp, event type, and IP address are extracted.

Only `FAILED_LOGIN` events are analyzed.

The timestamps are grouped according to IP address.

The timestamps are sorted chronologically.

The program then examines five-minute time windows.

Failed login attempts inside each window are counted.

If the count reaches the configured threshold, an alert is generated.

The alert contains the IP address, attempt count, timestamps, and severity.

Finally, all detected alerts are exported to a CSV file.

## Example Output

```text
============================================================
             SUSPICIOUS IP DETECTOR
============================================================

Suspicious IPs detected: 1

[MEDIUM] Suspicious IP: 192.168.1.20
    Failed attempts : 7
    Start time      : 2026-09-27 09:04:08
    End time        : 2026-09-27 09:05:23

Report saved as suspicious_ips.csv
```

## Installation

Clone or download the project.

Make sure Python is installed on your system.

Open a terminal inside the project directory.

Run:

```bash
python suspicious_ip_detector.py
```

No external Python packages are required for the current version.

## Configuration

The detection behavior can be changed using:

```python
FAILED_LOGIN_THRESHOLD = 5
TIME_WINDOW_MINUTES = 5
```

For example, changing the threshold to `10` will require ten failed login attempts before generating an alert.

## Security Concept

The project demonstrates a basic form of behavioral detection.

A large number of failed login attempts from one IP can indicate a possible brute-force attack.

However, a detection does not automatically mean that an IP address is malicious.

A legitimate user can also generate multiple failed login attempts.

Therefore, alerts should be investigated before taking defensive action.

## Future Improvements

Possible improvements include:

* Real-time log monitoring.
* IP reputation checking.
* Geographic IP information.
* Reverse DNS lookups.
* Windows Event Log support.
* Sysmon integration.
* Wazuh integration.
* Tkinter dashboard.
* Graphical alert visualization.
* Email notifications.
* More advanced detection rules.
* Multiple authentication event types.

## Disclaimer

This project is intended for educational and defensive cybersecurity purposes.

Use it only with logs and systems that you own or are authorized to monitor.

The detection rules are simplified and should not be considered a replacement for a production SIEM or security monitoring system.

## Author

Built as a beginner cybersecurity and SOC learning project using Python.
