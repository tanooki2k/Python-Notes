from libs.mailgun import Mailgun

TO_EMAILS = ['javierito.rojas.ramirez@gmail.com']
SUBJECT = 'Test e-mail with Python'
CONTENT = 'Hello, this is a test e-mail.'

Mailgun.send_email(TO_EMAILS, SUBJECT, CONTENT)
