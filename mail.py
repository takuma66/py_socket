from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

def createMIMEText (from_addr, to_addr, message, subject):
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg['Date'] = formatdate()
    return msg

def send_Mail(msg):
    host = "localhost"
    port = 25
    server = SMTP(host, port)
    server.send_message(msg)
    server.quit()
