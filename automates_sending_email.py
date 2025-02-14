# -*- coding: utf-8 -*-
"""automates sending email.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/163HL6B33SHi5IczQou_N_A4olOZkcJr0
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email credentials
email_address = "your_email@example.com"
email_password = "your_password"

# SMTP server configuration
smtp_server = "smtp.example.com"  # e.g., smtp.gmail.com
smtp_port = 587  # For SSL, use 465

# Function to send an email
def send_email(to_address, subject, body, attachment_path=None):
    # Set up the email details
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Attach a file (optional)
    if attachment_path:
        attachment = open(attachment_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {attachment_path}')
        msg.attach(part)

    # Set up the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(email_address, email_password)

    # Send the email
    text = msg.as_string()
    server.sendmail(email_address, to_address, text)

    # Close the SMTP server connection
    server.quit()

    print(f"Email sent to {to_address}")

# Main function to send emails to multiple recipients
def send_bulk_emails(recipient_list, subject, body_template, attachment_path=None):
    for recipient in recipient_list:
        personalized_body = body_template.format(name=recipient['name'])
        send_email(recipient['email'], subject, personalized_body, attachment_path)

if __name__ == "__main__":
    # List of recipients
    recipients = [
        {"name": "John Doe", "email": "john.doe@example.com"},
        {"name": "Jane Smith", "email": "jane.smith@example.com"},
        # Add more recipients as needed
    ]

    # Email subject and body template
    subject = "Your Subject Here"
    body_template = """
    Hi {name},

    This is a personalized message for you.

    Best regards,
    Your Name
    """

    # Optional: Path to an attachment
    attachment = None  # e.g., "path/to/your/file.pdf"

    # Send the emails
    send_bulk_emails(recipients, subject, body_template, attachment)