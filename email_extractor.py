"""
CodeAlpha Internship - Task 3: Task Automation with Python Scripts
Goal: Automate a small, real-life repetitive task.
Chosen Idea: Extract all email addresses from a .txt file and save
             them to another file.

Key Concepts Used: os, re, file handling
"""

import os
import re

INPUT_FILE = "sample_input.txt"
OUTPUT_FILE = "extracted_emails.txt"

# Regex pattern to match standard email addresses
EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found. Please make sure it exists in this folder.")
        return

    with open(input_file, "r") as file:
        content = file.read()

    # Find all matches, remove duplicates, keep order
    found_emails = re.findall(EMAIL_PATTERN, content)
    unique_emails = list(dict.fromkeys(found_emails))

    if not unique_emails:
        print("No email addresses were found in the input file.")
        return

    with open(output_file, "w") as file:
        for email in unique_emails:
            file.write(email + "\n")

    print(f"Found {len(unique_emails)} unique email address(es):")
    for email in unique_emails:
        print(f"  - {email}")
    print(f"\nSaved to '{output_file}'.")


if __name__ == "__main__":
    extract_emails(INPUT_FILE, OUTPUT_FILE)
