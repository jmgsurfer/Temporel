#!/usr/bin/env python
#-*- coding: Latin-1 -*-
#qpy:console
#
#
# TO.DO:
# def ephemeride
# def vac.scolaires
# def capture.saisies
# def check.locales
# def diffdate, result sec, min, heure, jour
# def conversions
# menu
# efface ecran
#
#
import os
import time
import datetime
import calendar
#
#
def menu():
    menu = {}
    menu['1']="Determiner signe Zodiaque" 
    menu['2']="Determiner jour de la semaine"
    menu['3']="Determiner si annee bissextile"
    menu['4']="Determiner numero de semaine"
    menu['5']="Afficher calendrier"
    menu['6']="Sortir"
    while True: 
        options=menu.keys()
        options.sort()
        print
        for entry in options: 
            print entry, menu[entry]
        selection=raw_input("Choisissez une action:") 
        if selection =='1': 
            print
            print "SIGNE DU ZODIAQUE:"
            jour=int(raw_input("Quel jour? "))
            mois=int(raw_input("Quel mois? "))
            m=fmt[mois-1]
            print "Le", jour, m, "correspond a", getAstroSigne(jour,mois)
            print
            s=raw_input()
        elif selection == '2': 
            print
            print "JOUR DE LA SEMAINE:"
            jour=int(raw_input("Quel jour? "))
            mois=int(raw_input("Quel mois? "))
            aaaa=int(raw_input("Quelle annee? "))
            m=fmt[mois-1]
            day=datetime.date(aaaa,mois,jour)
            wday=day.weekday()
            print joursemaine(wday), jour, m, aaaa
            print
            s=raw_input()
        elif selection == '3':
            print
            print "ANNEE BISSEXTILE:"
            aaaa=int(raw_input("Quelle annee? "))
            print getBiss(aaaa)
            print
            s=raw_input()
        elif selection == '4': 
            print
            print "NUMERO DE LA SEMAINE:"
            jour=int(raw_input("Quel jour? "))
            mois=int(raw_input("Quel mois? "))           
            aaaa=int(raw_input("Quelle annee? "))
            m=fmt[mois-1]
            print "Le",jour,m,aaaa,"est en semaine:",numsemaine(aaaa, mois, jour)
            print
            s=raw_input()
        elif selection == '5':
            print
            print "CALENDRIER MENSUEL:"
            mois=int(raw_input("Quel mois? "))           
            aaaa=int(raw_input("Quelle annee? "))
            print
            getCalendar(aaaa, mois)
            print
            s=raw_input()
        elif selection == '6':
            break
    
        else: 
           print "Unknown Option Selected!"
#
def getAstroSigne(day,month):
    signs = ["Capricorne","Verseau","Poisson","Belier","Taureau","Gemeaux","Cancer","Lion","Vierge","Balance","Scorpion","Sagitaire"];
    dayTransition = [20,18,20,19,20,21,22,22,22,23,22,21];
    index = (month-1)%12 if day <= dayTransition[month-1] else month%12;
    return signs[index];
#
def getBiss(yyyy):
    b = calendar.isleap(yyyy)
    if b == 1:
        leap = str(yyyy)+" est bissextile"
    else:
        leap = str(yyyy)+" n'est pas bissextile"
    return leap
#
def getDebToDate(yyyy, mm, dd):
    day = datetime.date(yyyy, mm, dd)
    debAn = datetime.date(yyyy, 1, 1)
    yd = day - debAn
    yd = yd.days + 1
    return yd
#    
def getFinToDate(yyyy, mm, dd):
    day = datetime.date(yyyy, mm, dd)
    finAn = datetime.date(yyyy, 12, 31)
    yf = finAn - day
    yf = yf.days
    return yf
#
def getCalendar(yyyy, mm):
    clo = calendar.LocaleTextCalendar(calendar.MONDAY, 'fr_FR.utf8')
    return clo.prmonth(yyyy, mm)    
#
def efface():
    os.system('clear')
#
def joursemaine(code_joursem):
    # code_joursem: lundi= 0 � dimanche= 6
    fwd = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
    wd = fwd[code_joursem]
    return wd
#
def numsemaine(yyyy, mm, dd):
    temp=datetime.date(yyyy, mm, dd)
    weeknumber=temp.isocalendar()[1]
    return weeknumber
#
#def today():
#
# variables
x = time.localtime()
year = x[0]
month = x[1]
day = x[2]
weekday = x[6] # 0 = lundi
yearday = x[7] # nb jour depuis d�but ann�e 
#
#
## DEBUT ##
efface()
fmt = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre']
mt = fmt[month-1]
print "Aujourd'hui c'est le:"
print joursemaine(weekday), day, mt, year, ", semaine ", numsemaine(year, month, day)
print getBiss(year)
print getDebToDate(year, month, day), "jours depuis le 1er janvier"
print getFinToDate(year, month, day), "jours jusqu'à la fin de l'annee"
print "Periode zodiacale:",getAstroSigne(day,month)
print
#getCalendar(year, month)
menu()