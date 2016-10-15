import time
import random
import datetime
import telepot
from RaspyCam.py import RaspyCam

"""
After **inserting token** in the source code, run it:
'''
$ python RaspyCam.py
'''
This simple bot does nothing but accepts two commands:
- '/roll' - reply with a random integer between 1 and 6, like rolling a dice.
- '/time' - reply with the current time, like a clock.
- '/snap' - reply with a photo from PiCamera
"""

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == 'snap':
        raspyCam = RaspyCam()
        filename = raspyCam.capture()
        bot.sendPhoto(chat_id, open(filename, 'rb'))

bot = telepot.Bot('*** INSERT TOKEN ***')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)
