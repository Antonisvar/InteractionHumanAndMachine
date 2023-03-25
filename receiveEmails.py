import imaplib
import email

# Set up the email parameters
username = "keraynos54@gmail.com"
password = "cdzffymblodhjtug"

# Connect to the IMAP server and select the inbox folder
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)
mail.select('inbox')

# Search for all unread messages
status, response = mail.search(None, 'UNSEEN')

# Get the subject lines of each message
for num in response[0].split():
    status, msg_data = mail.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(msg_data[0][1])
    print("Subject:", msg['Subject'])

# Close the connection
mail.close()
mail.logout()
