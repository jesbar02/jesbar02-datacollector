from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average_height, count):
    from_email = "jesbar02@gmail.com"
    from_password = "plokiju*89"
    to_email = email

    subject = "height data"
    message = "Hey there, your height is <strong>%s</strong>.  <br> Average height of all is <strong>%s</strong> and is calculated out of <strong>%s</strong> people. <br> Thanks!! " % (height, average_height, count)

    msg = MIMEText(message, "html")
    msg['subject'] = subject
    msg['To'] = to_email
    msg['from'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
