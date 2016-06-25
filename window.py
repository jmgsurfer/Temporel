#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Module
from Tkinter import *
import time
import datetime
import calendar
#
# Functions
#
def getAstroSigne(day,month):
    signs = [u"Capricorne",u"Verseau",u"Poisson",u"Bélier",u"Taureau",u"Gémeaux",u"Cancer",u"Lion",u"Vierge",u"Balance",u"Scorpion",u"Sagitaire"];
    dayTransition = [20,18,20,19,20,21,22,22,22,23,22,21];
    index = (month-1)%12 if day <= dayTransition[month-1] else month%12;
    return signs[index];
#
def joursemaine(code_joursem):
    # code_joursem: lundi= 0 to dimanche= 6
    fwd = [u'lundi', u'mardi', u'mercredi', u'jeudi', u'vendredi',u'samedi', u'dimanche']
    wd = fwd[code_joursem]
    return wd
#
def getBiss(yyyy):
    b = calendar.isleap(yyyy)
    if b == 1:
        leap = str(yyyy)+u" est bissextile"
    else:
        leap = str(yyyy)+u" n'est pas bissextile"
    return leap
#
def numsemaine(yyyy, mm, dd):
    temp=datetime.date(yyyy, mm, dd)
    weeknumber=temp.isocalendar()[1]
    return weeknumber

# Global var
#
x = time.localtime()
Today_Year = x[0]
Today_Month = x[1]
Today_Day = x[2]
Today_Weekday = x[6] # 0 = lundi
Today_Yearday = x[7] # nb jour depuis debut annee
#
Window = Tk()
Window.title('=== Temporel ===')
#
#Frames
#
LFrame1 = LabelFrame(Window, text="Menu", padx=20, pady=20)
LFrame1.grid(row=0,column=0, rowspan=2,padx=2, pady=2)
#
Frame2 = Frame(Window)
Frame2.grid(row=0,column=1,sticky='n', padx=2, pady=2)
#
LFrame2 = LabelFrame(Frame2, text="Interface")
LFrame2.grid(row=0,column=0)
Label1= Label(LFrame2, text="Texte")
Label1.grid()
#
LFrame3 = LabelFrame(Frame2, text="Résultat")
LFrame3.grid(row=1,column=0, sticky='nesw',padx=2, pady=2)
Label2= Label(LFrame3, text="Texte")
Label2.grid()
#
#
#RadioButtons
#
Rbutton1 = Radiobutton(LFrame1, text="Zodiaque", value=1)
Rbutton1.grid(sticky='w')
Rbutton1.select() #Rb1 first selected
Rbutton2 = Radiobutton(LFrame1, text="Jour semaine", value=2)
Rbutton2.grid(sticky='w')
Rbutton3 = Radiobutton(LFrame1, text="Bissextile", value=3)
Rbutton3.grid(sticky='w')
Rbutton4 = Radiobutton(LFrame1, text="Numéro semaine", value=4)
Rbutton4.grid(sticky='w')
Rbutton5 = Radiobutton(LFrame1, text="Calendrier", value=5)
Rbutton5.grid(sticky='w')
#
#
# Spinbox date
#
var = StringVar(Window)
var.set("15")
Spinbox1 = Spinbox(LFrame2, width=2, from_=1, to=31, textvariable=var).grid(row=0, column=0)
Spinbox2 = Spinbox(LFrame2, width=2, from_=1, to=12, textvariable="2").grid(row=0, column=1)
Spinbox3 = Spinbox(LFrame2, width=4, from_=0, to=2020, textvariable="1970").grid(row=0, column=2)


Window.mainloop()