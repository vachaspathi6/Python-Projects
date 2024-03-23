## This code won't work if 2 factor authentication is enabled on your Google account

import imaplib
import email

def check_inbox(email_address, password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_address, password)
    mail.select("inbox")
    _, data = mail.search(None, "ALL")
    mail_ids = data[0]
    id_list = mail_ids.split()
    latest_email_id = id_list[-1]
    _, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)
    print("From:", email_message["From"])
    print("Subject:", email_message["Subject"])
    print("Body:")
    print(email_message.get_payload())

def main():
    email_address = input("Enter email address: ")
    password = input("Enter email password: ")
    check_inbox(email_address, password)

if __name__ == "__main__":
    main()
