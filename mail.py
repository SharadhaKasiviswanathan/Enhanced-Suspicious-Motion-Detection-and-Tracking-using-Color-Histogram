import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

gmail_user = "21sharadha@gmail.com"
gmail_pwd = "kasinagappan"
toaddr = '21sharadha@gmail.com'
me = '21sharadha@gmail.com'
Subject = 'security alert'


def mail(subject, text, attach):
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = "21sharadha@gmail.com"
    msg['Subject'] = subject
    to = "21sharadha@gmail.com"
    msg.attach(MIMEText(text))

    part = MIMEBase('application', 'octet-stream')

    part.set_payload(open(attach, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()


c = 0
i = 0

print("code mail")

mail(
    "New Scripts",
    "You have a new xll file",
    "saved_img.jpg")
# break
##########################################################################################time.sleep(1)
