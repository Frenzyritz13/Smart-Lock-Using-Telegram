import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 50) # GPIO 17 for PWM with 50Hz
p.start(5) # Initialization


#LED
def on(pin):
	p.ChangeDutyCycle(20)
	return
def off(pin):
	p.ChangeDutyCycle(20)
	return

# set up GPIO output channel
GPIO.setup(11, GPIO.IN)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s' % command)

    if command == 'Hey':
       bot.sendMessage(chat_id, "hey there")
    elif command =='Unlock':
       off(17)
       bot.sendMessage(chat_id, "Unlocked")
    elif GPIO.input(11) == 1:
       bot.sendMessage(chat_id, "Somebody at the door")
    elif command == 'Lock':
       on(17)
       bot.sendMessage(chat_id, "Locked")

bot = telepot.Bot('1212253230:AAHMVxFTecnDXduCNVVQiaBKXvSyLW0XqeI')
bot.message_loop(handle)
print ('I am listening...')

while 1:
     time.sleep(10)
