import smtplib
from email.mime.text import MIMEText


# build message
def build_message(sender_email, recipient_email, subject, email_body_content):
    msg = MIMEText(email_body_content)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    return msg


# The below method will send email
# required parameters are:
# sender_email_id, sender_password,
# recipient_email_id, email_subject,
# email_body, smtp_server, port
def send_email(msg,
               sender_password,
               server_name,
               port):
    server = smtplib.SMTP_SSL(server_name, port)
    server.login(msg['From'], sender_password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

