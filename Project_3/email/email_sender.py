import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = ''
email['to'] = ''
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.meta.ua', port=465) as smtp:
  smtp.starttls()
  smtp.ehlo()
  smtp.login('', '')
  smtp.send_message(email)
  print('all good boss!')
