#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
servo = GPIO.PWM(14,50)
servo.start(0.0)
        
print('Content-type: text/html; charset=UTF-8\r\n')
print('Web SERVO<br><br>')
print('Rotate:<br>')

print('<form action="" method="post">')
print('<input type="submit" name="angle" value=-90>')
print('<input type="submit" name="angle" value=-45>')
print('<input type="submit" name="angle" value=0>')
print('<input type="submit" name="angle" value=45>')
print('<input type="submit" name="angle" value=90>')
print('</form>')

form = cgi.FieldStorage()
duty = (1.44 + float(form.getvalue("angle")) * (0.95/90)) / 20 * 100
servo.ChangeDutyCycle(duty)
time.sleep(0.25)
if(form.getvalue("angle")!=None):
    print('servo fan at '+form.getvalue("angle")+' digree from origin')
