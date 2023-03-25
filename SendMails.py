import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders

# Set up the email parameters
sender_email = "keraynos54@gmail.com"
recipient_email = "cs171214@uniwa.gr"
subject = "Test email with attachment"
message = "Hello, this is a test email with an attachment from Python!"

# Create the message object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = COMMASPACE.join([recipient_email])
msg['Subject'] = subject
msg.attach(MIMEText(message))

# Add the attachment
attachment_file = "D://recordings/InteractionHumanAndMachine/Magic.pdf"
with open(attachment_file, "rb") as f:
    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(f.read())
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment_file)}")
    msg.attach(attachment)

# Send the email using SMTP
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, 'cdzffymblodhjtug')
    smtp.sendmail(sender_email, recipient_email, msg.as_string())
