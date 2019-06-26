import smtplib
from email.mime.text import MIMEText


# The below method will send email
# required parameters are:
# sender_email_id, sender_password,
# recipient_email_id, email_subject,
# email_body, smtp_server, port
def send_email(sender_email,
               sender_password,
               recipient_email,
               subject,
               email_body_content,
               server_name,
               port):
    msg = MIMEText(email_body_content)
    msg['Subject'] = subject

    server = smtplib.SMTP_SSL(server_name,port)
    server.login(send_email,sender_password)
    server.sendmail(sender_email,recipient_email,msg.as_string())
    server.quit()


