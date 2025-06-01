"""
If  you get an STMPAuthenticationError even when your password is correct,
it's possible that you have 2-factor authentication enabled.
You'll need to use an App Password to log in instead of your normal password.

If you don't have 2-FA enabled, you'll have to allow access by
less secure apps in your Gmail security preferences-though remember to deactivate
it once you've finished learning about sending e-mails with Python!
"""

import smtplib
from email.message import EmailMessage

email_content = """Hello,

I am sending you an e-mail with Python. I hope you like it!

Kind regards,
JRR
"""

email = EmailMessage()

email['Subject'] = 'Test email with Python'
email['From'] = 'you@gmail.com'
email['To'] = 'someone@gmail.com'

email.set_content(email_content)

with smtplib.SMTP(host='stmp.gmail.com', port=587) as smtp_connector:
    smtp_connector.starttls()
    smtp_connector.login('you@gmail.com', 'Password')
    smtp_connector.send_message(email)
