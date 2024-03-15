import sendgrid
from sendgrid.helpers.mail import Mail

from django.conf import settings

# A Sendgrid Email Utility Function
# Sender defaults to admin@example.com (don't forget to replace this with your Sendgrid email)
def send_email(to, subject, content, sender='admin@example.com'):
    sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)
    mail = Mail(
        from_email = sender,
        to_emails = to,
        subject = subject,
        html_content = content
    )
    return sg.send(mail)

