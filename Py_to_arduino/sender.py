import serial
import time
import psutil
import os


#while 1:
arduino = serial.Serial('/dev/ttyUSB0')
time.sleep(2)
print(arduino.readline())
while 1:
        arduino.write((str(int(psutil.cpu_percent()))).encode())
        #print(arduino.readline())
        time.sleep(2)
        arduino.write((str(int((psutil.virtual_memory().available)/1048576))).encode())
        #print(arduino.readline())
        time.sleep(2)
        # print(arduino.readline())


     # i=i+1
     # print(i)
     # if (i%2==1):
     #     arduino.write(f"{(str(int(psutil.cpu_percent())))} \r".encode())
     #     print(arduino.readline())
     # else:
     #     arduino.write(f"{(str(int((psutil.virtual_memory().used)/1048576)))} \r".encode())
     #     print(arduino.readline())
     # if (i>1000): i=0
     # time.sleep(2)
