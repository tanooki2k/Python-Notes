import requests

MAILGUN_API_URL = 'https://api.mailgun.net/v3/sandboxc53dc6a6c03e4f7e8050790fdc10ec1d.mailgun.org/messages'
MAILGUN_API_KEY = 'Mailgun Sandbox <postmaster@sandboxc53dc6a6c03e4f7e8050790fdc10ec1d.mailgun.org>'

FROM_NAME = 'Javier'
FROM_EMAIL = 'javierito.rojas.ramirez@gmail.com'

TO_EMAILS = ['javierito.rojas.ramirez@gmail.com']
SUBJECT = 'Test e-mail with Python'
CONTENT = 'Hello, this is a test e-mail.'

requests.post(
    MAILGUN_API_URL,
    auth=('api', MAILGUN_API_KEY),
    data={
        'from': f'{FROM_NAME} <{FROM_EMAIL}>',
        'to': TO_EMAILS,
        'subject': SUBJECT,
        'text': CONTENT
    }
)
