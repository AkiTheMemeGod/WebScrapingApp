import smtplib as sm
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def send_mail(message, To):

    msg = MIMEMultipart()
    msg['Subject'] = 'Music Tour Alert !'
    msg['From'] = 'Your WebScraper'
    msg['To'] = 'only you wink ;'

    text = MIMEText(f"New Music Tour Alert ! \n{message}")
    msg.attach(text)

    s = sm.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("akis.pwdchecker@gmail.com", password=os.getenv("mailpwd"))
    s.sendmail("akis.pwdchecker@gmail.com", To, msg.as_string())
    s.quit()
    print("Email Successfully sent!")
