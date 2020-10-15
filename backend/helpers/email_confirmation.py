import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Falta implementar en el proyecto
class EmailConfirmation():
    # Credentials
    provider = 'smtp-mail.outlook.com'
    sender = 'drhealth.jnn@hotmail.com'
    password = 'password1'
    server = smtplib.SMTP(provider, 587)

    def send_msg(self, user_mail):
        # Server connection
        EmailConfirmation.server.starttls()
        EmailConfirmation.server.ehlo()
        # Authentication
        EmailConfirmation.server.login(
            EmailConfirmation.sender, EmailConfirmation.password)
        # message
        message = 'Gracias por elegirnos, su registro ha sido exitoso'
        msg = MIMEMultipart()
        msg.attach(MIMEText(message, 'html'))
        msg['From'] = EmailConfirmation.sender
        msg['To'] = user_mail
        msg['Subject'] = 'Prueba'
        EmailConfirmation.server.sendmail(
            msg['From'], msg['To'], msg.as_string())
