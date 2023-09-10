import smtplib
import getpass
import jinja2
import datetime
import threading

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP configuration
HOST = "smtp.gmail.com"
PORT = 25
FROM_EMAIL = "mayank.101120@gmail.com"
TO_EMAIL = "mayankkumarrai_se20b15_62@dtu.ac.in"
PASSWORD = getpass.getpass("Enter password: ")

# Load the Jinja2 template
template_loader = jinja2.FileSystemLoader(searchpath="./templates")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("campaign_template.html")

# Replace with your actual data
subject = "Your Daily Newsletter"
preview_text = "Check out our latest news!"
article_url = "https://example.com/article"
published_date = "September 9, 2023"
html_content = "<p>Click on read more to go to documentation for testing this API.</p>"
plain_text_content = "This is the plain text version of your email."

# Number of parallel threads for sending emails
NUM_THREADS = 3

# Function to send an email
def send_email(to_email):
    try:
        # Render the email content using the template
        email_content = template.render(
            subject=subject,
            preview_text=preview_text,
            article_url=article_url,
            published_date=published_date,
            html_content=html_content,
            plain_text_content=plain_text_content
        )

        # Create the email message
        message = MIMEMultipart("alternative")
        message['Subject'] = subject
        message['From'] = FROM_EMAIL
        message['To'] = to_email

        html_part = MIMEText(email_content, 'html')
        message.attach(html_part)

        # Connect to the SMTP server and send the email
        smtp = smtplib.SMTP(HOST, PORT)

        status_code, response = smtp.ehlo()
        print(f"[*] Echoing the server: {status_code} {response}")

        status_code, response = smtp.starttls()
        print(f"[*] Starting TLS connection: {status_code} {response}")

        status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
        print(f"[*] Logging in: {status_code} {response}")

        smtp.sendmail(FROM_EMAIL, to_email, message.as_string())
        smtp.quit()

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {str(e)}")

# List of recipient email addresses
recipient_emails = ["mayankkumarrai_se20b15_62@dtu.ac.in", "mayank.101120@gmail.com", "msd0104msd@gmail.com","mittalkeshav41@gmail.com","keshavmittal_se20b8_53@dtu.ac.in"]

# Create and start multiple threads for sending emails in parallel
threads = [threading.Thread(target=send_email, args=(email,))for email in recipient_emails ]

    
for thread in threads:
    thread.start()


print("All emails sent.")
