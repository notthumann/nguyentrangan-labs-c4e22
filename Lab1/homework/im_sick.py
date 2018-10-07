from gmail import GMail, Message
import datetime
now = datetime.datetime.now()

gmail = GMail('notthumann96@gmail.com','minhngoc1996')
msg = Message('I am sick', to='mihngoc19@gmail.com',text = 'Hello, Im so sick right now so I can t go with you. Please take care. ')
if now.hour >= 7:
    gmail.send(msg)

