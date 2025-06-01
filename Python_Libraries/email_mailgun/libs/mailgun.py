import requests


class Mailgun:
    MAILGUN_API_URL = 'https://api.mailgun.net/v3/sandboxc53dc6a6c03e4f7e8050790fdc10ec1d.mailgun.org/messages'
    MAILGUN_API_KEY = 'Mailgun Sandbox <postmaster@sandboxc53dc6a6c03e4f7e8050790fdc10ec1d.mailgun.org>'

    FROM_NAME = 'Javier'
    FROM_EMAIL = 'javierito.rojas.ramirez@gmail.com'

    @classmethod
    def send_email(cls, to_emails, subject, content):
        requests.post(
            cls.MAILGUN_API_URL,
            auth=('api', cls.MAILGUN_API_KEY),
            data={
                'from': f'{cls.FROM_NAME} <{cls.FROM_EMAIL}>',
                'to': to_emails,
                'subject': subject,
                'text': content
            }
        )
