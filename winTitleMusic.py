# -*- coding: utf-8 -*-

import win32gui
import pygame
import codecs
import sys
w=win32gui


pygame.mixer.init()
rekuiemu = pygame.mixer.Sound("rekuiemu.wav")
jazz = pygame.mixer.Sound("jazz.wav")
street = pygame.mixer.Sound("street.wav")

bgm = pygame.mixer.Channel(0)
bgm.play(jazz,-1,0,0)
bgm.set_volume(0.4)

se = pygame.mixer.Channel(1)




i=0
temp = ""
while i<10000:
    name = w.GetWindowText (w.GetForegroundWindow()) #ウインドウタイトル取得
    b_name = name.encode("utf8")
    if temp!=name:
      temp = name
      print(b_name)
      title = str(b_name,"utf8")
      
   
      if int(title.find("Tweet")) >= 0 or int(title.find("Twitter")) >= 0:
        if se.get_busy() == False:
          se.play(street,-1,0,0)
          se.set_volume(0.2)
          print("Deck="+str(title.find("Tweet"))+"，Twitter="+str(title.find("Twi")))
        else:
          pass  
      else:
          se.stop()
      
      

    else:
      pass