#31 = buzzer
#16 = push button


import picamera
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
#setup the camera such that it closes
#when we are done with it



GPIO.setmode(GPIO.BOARD)

GPIO.setup(16,GPIO.IN)
GPIO.setup(31,GPIO.OUT)
button_state=GPIO.LOW
i=0

while True:
    print(GPIO.input(16))
    if GPIO.input(16)==0:
        GPIO.output(31,0)
    else:
        GPIO.output(31,1)
        time.sleep(0.5)
        GPIO.output(31,0)
        
        print("About to take a picture.")
        
        with picamera.PiCamera() as camera:
            camera.resolution= (1280,720)
#            while i<10:
            camera.capture("/home/pi/Desktop/mabash/image"+str(i)+".jpg")
            i+=1
        print("Picture taken.")
GPIO.cleanup(31)



