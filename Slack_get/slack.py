import requests
import json
import pprint
import time
import pygame
pygame.mixer.init()
pygame.mixer.music.load("./test.mp3")


number_of_messages=0

while True:
    headers = ./secrets
    messages=r.get('messages')
    i=0
    for message in messages:
        i=i+1
        print(i)
    if (number_of_messages < i) and (number_of_messages !=0):
        print("alarm")
        pygame.mixer.music.play()
        alarm=True
    else:
        alarm=False
    number_of_messages=i
    time.sleep(1)
