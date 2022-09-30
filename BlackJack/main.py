from email.mime import image
from fileinput import filename
import tkinter
from tkinter import ttk
from tracemalloc import stop
from turtle import back
from typing import Container
import tk
import imghdr
from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
import numpy as np 
import pygame
from PIL import Image,ImageTk
import os
import time
import pyautogui
from PIL import Image, ImageTk

lst=["assets\doi.png","assets\Trei.png","assets\patru.png","assets\cinci.png","assets\sase.png","assets\sapte.png","assets\opt.png","assets\moua.png","assets\zece.png","assets\As.png"]
m=0
n=0
hscore=0
pygame.font.init()
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED=200
score=0
z=random.randint(0,9)
score+=z
score+=2
w=random.randint(0,9)
score+=w
score+=2
hscore=0
o=random.randint(0,9)
hscore+=o
hscore+=2
p=random.randint(0,9)
hscore+=p
hscore+=2

ok=1
def fold():
   global hscore
   global ok
   ok=0
   if hscore>=score and hscore<=21:
        game_over()
        ok=1
   if hscore>21:
        won()
        ok=1
   B["state"] = DISABLED
   img3=PhotoImage(file="assets\plyed.png")
   my_image=canvas.create_image(50,250,anchor=NW,image=img3)
   label2.config(text="House Score:{}".format(hscore))
   if hscore<score:
      global n
      canvas.delete(ALL)
      n=random.randint(0,9)
      print(n)
      hscore+=n
      hscore+=2
      img0=PhotoImage(file=lst[n])
      my_image=canvas.create_image(450,250,anchor=NW,image=img0)
      imgi=PhotoImage(file="assets\Bara.png")
      my_image=canvas.create_image(350,0,anchor=NW,image=imgi)
      img3=PhotoImage(file="assets\plyed.png")
      my_image=canvas.create_image(50,250,anchor=NW,image=img3)
      label2.config(text="House Score:{}".format(hscore))
      time()
      time.sleep(2)
      if hscore>=score and hscore<=21:
        game_over()
      if hscore>21:
        won()
      
def invoke_button(self, event):
    event.widget.config(relief = "sunken")
    self.root.update_idletasks()
    event.widget.invoke()
    time.sleep(0.1)
    event.widget.config(relief = "raised")

def card():
    global score 
    global m
    canvas.delete(ALL)
    m=random.randint(0,9)
    score+=m
    score+=2
    if score>21:
        game_over()
    else:
        img8=PhotoImage(file=lst[m])
        my_image=canvas.create_image(150,250,anchor=NW,image=img8)
        imgi=PhotoImage(file="assets\Bara.png")
        my_image=canvas.create_image(350,0,anchor=NW,image=imgi)
        img3=PhotoImage(file=lst[p])
        img4=PhotoImage(file=lst[o])
        my_image=canvas.create_image(450,50,anchor=NW,image=img3)
        my_image2=canvas.create_image(450,350,anchor=NW,image=img4)
    label.config(text="Your Score:{}".format(score))
    time()


def game_over():
    canvas.delete(ALL)
    B["state"] = DISABLED
    F["state"] = DISABLED
    canvas.config(background='black')
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="You LOST",fill="red",tag="You LOST")
    canvas.pack()

def won():
    canvas.delete(ALL)
    B["state"] = DISABLED 
    F["state"] = DISABLED 
    canvas.config(background='black')
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="You WON",fill="white",tag="You WON")
    canvas.pack()


window=Tk()
window.title("BlackJack")
window.resizable(False,False)

label= Label(window, text="Your Score:" ,font=('consolas',30))
label.config(text="Your Score:{}".format(score))
label2= Label(window, text="Your Score:" ,font=('consolas',30))
label2.config(text="House Score:{}".format(hscore))
canvas=Canvas(window, bg='green',height=GAME_HEIGHT,width=GAME_WIDTH)
img=PhotoImage(file=lst[z])
img2=PhotoImage(file=lst[w])
imgi=PhotoImage(file="assets\Bara.png")
my_image=canvas.create_image(150,50,anchor=NW,image=img)
my_image=canvas.create_image(350,0,anchor=NW,image=imgi)
my_image2=canvas.create_image(150,350,anchor=NW,image=img2)
img3=PhotoImage(file=lst[p])
img4=PhotoImage(file=lst[o])
my_image=canvas.create_image(450,50,anchor=NW,image=img3)
my_image2=canvas.create_image(450,350,anchor=NW,image=img4)
B = tkinter.Button(window, text ="New card", command = card)
F = tkinter.Button(window, text ="Fold", command = fold)
if score>21:
     game_over()
label.pack()
label2.pack()
B.pack()
F.pack()
canvas.pack()
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.mainloop()
