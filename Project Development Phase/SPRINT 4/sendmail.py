from sendgrid import SendGridAPIClient
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = SendGridAPIClient('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')
from_email = Email("nutricounter.cc@gmail.com")  # Change to your verified sender
to_email = To("nutricounter.cc@gmail.com")  # Change to your recipient
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)