"""
CodeAlpha Internship - Task 3: Task Automation with Python Scripts
Idea Chosen: Extract all CodeAlpha email addresses from a .txt file and save them to another file.

Key Concepts Used: re, file handling
"""

import re

def extract_emails(input_file, output_file, domain_filter="codealpha"):
    # Regex pattern to match standard email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    try:
        # Read the input file
        with open(input_file, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found. Please check the file path.")
        return

    # Find all emails in the content
    all_emails = re.findall(email_pattern, content)

    # Keep only emails whose domain contains the filter word (e.g. "codealpha")
    filtered_emails = [email for email in all_emails if domain_filter.lower() in email.lower()]

    # Remove duplicates while keeping order
    unique_emails = list(dict.fromkeys(filtered_emails))

    if not unique_emails:
        print(f"No '{domain_filter}' email addresses found in the file.")
        return

    # Save extracted emails to the output file
    with open(output_file, "w") as file:
        for email in unique_emails:
            file.write(email + "\n")

    print(f"{len(unique_emails)} '{domain_filter}' email address(es) found and saved to '{output_file}':")
    for email in unique_emails:
        print(f" - {email}")


if __name__ == "__main__":
    input_file = "sample_data.txt"        # File to read from
    output_file = "extracted_emails.txt"  # File to save results to
    domain_filter = "codealpha"           # Only keep emails containing this word

    extract_emails(input_file, output_file, domain_filter)
