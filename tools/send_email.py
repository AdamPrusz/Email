import smtplib
from smtplib import *
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


def send_email(office, password, filename, receiver_email):
    msg = MIMEMultipart()
    sender_email = "adamprusz95@gmail.com"
    msg['Subject'] = f"Potwierdzenie {office} -  MEGAKAM"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    body = "Dokument w załączniku \n \n \n Pozdrawiam, \n Piotr Pruszyński"

    msgText = MIMEText(body)
    msg.attach(msgText)

    with open(filename, 'rb') as attachment:
        pdf = MIMEApplication(attachment.read())
        pdf.add_header('Content-Disposition', 'attachment', filename = f'{office} MEGAKAM.pdf')
        msg.attach(pdf)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_object:
            smtp_object.ehlo()
            smtp_object.starttls()
            smtp_object.login(sender_email, password)
            smtp_object.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception:
        error = "error"
        return error








