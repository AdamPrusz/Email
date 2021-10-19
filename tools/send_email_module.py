import os
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import find_file_module
file = find_file_module.file_path

class Email:
    subject = "Potwierdzenie ZUS - MEGAKAM"
    body = "Dokument w załączniku \n \n \n Piotr Pruszyński"

    def __init__(self,  password, sender_email = "adamprusz95@gmail.com", receiver_email = "adamprusz95@gmail.com"):
        self.password = password
        self.sender_email = sender_email
        self.receiver_email = receiver_email

    def send_email_zus(self, file):
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = self.receiver_email
        message["Subject"] = self.subject

        message.attach(MIMEText(self.body, "plain"))


        with open(file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())


        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {file}",
        )

        message.attach(part)
        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, text)

mail = Email("eisxssoszjffxhvz")

mail.send_email_zus(file)



