#!/usr/bin/env python
# -*- coding: utf-8 -*-
##!C:\Python\Python27
#qpy:console
#
#
# TO.DO:
# os.system('clear') est OS specifique
# encodage a specifier
#
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
    menu['1']=u"Déterminer signe Zodiaque"
    menu['2']=u"Déterminer jour de la semaine"
    menu['3']=u"Déterminer si année bissextile"
    menu['4']=u"Déterminer numéro de semaine"
    menu['5']=u"Afficher calendrier"
    menu['6']=u"Sortir"
    while True:
        options=menu.keys()
        options.sort()
        print
        for entry in options:
            print entry, menu[entry]
        selection=raw_input(u"Choisissez une action:")
        if selection =='1':
            print
            print u"SIGNE DU ZODIAQUE:"
            jour=int(raw_input(u"Quel jour? "))
            mois=int(raw_input(u"Quel mois? "))
            m=fmt[mois-1]
            print "Le", jour, m, u"correspond à", getAstroSigne(jour,mois)
            print
            s=raw_input()
        elif selection == '2':
            print
            print u"JOUR DE LA SEMAINE:"
            jour=int(raw_input(u"Quel jour? "))
            mois=int(raw_input(u"Quel mois? "))
            aaaa=int(raw_input("Quelle année? "))
            m=fmt[mois-1]
            day=datetime.date(aaaa,mois,jour)
            wday=day.weekday()
            print joursemaine(wday), jour, m, aaaa
            print
            s=raw_input()
        elif selection == '3':
            print
            print u"ANNEE BISSEXTILE:"
            aaaa=int(raw_input("Quelle année? "))
            print getBiss(aaaa)
            print
            s=raw_input()
        elif selection == '4':
            print
            print u"NUMERO DE LA SEMAINE:"
            jour=int(raw_input(u"Quel jour? "))
            mois=int(raw_input(u"Quel mois? "))
            aaaa=int(raw_input("Quelle année? "))
            m=fmt[mois-1]
            print u"Le",jour,m,aaaa,u"est en semaine:",numsemaine(aaaa, mois, jour)
            print
            s=raw_input()
        elif selection == '5':
            print
            print u"CALENDRIER MENSUEL:"
            mois=int(raw_input(u"Quel mois? "))
            aaaa=int(raw_input("Quelle année? "))
            print
            getCalendar(aaaa, mois)
            print
            s=raw_input()
        elif selection == '6':
            break

        else:
           print u"Unknown Option Selected!"
#
def getAstroSigne(day,month):
    signs = [u"Capricorne",u"Verseau",u"Poisson",u"Bélier",u"Taureau",u"Gémeaux",u"Cancer",u"Lion",u"Vierge",u"Balance",u"Scorpion",u"Sagitaire"];
    dayTransition = [20,18,20,19,20,21,22,22,22,23,22,21];
    index = (month-1)%12 if day <= dayTransition[month-1] else month%12;
    return signs[index];
#
def getBiss(yyyy):
    b = calendar.isleap(yyyy)
    if b == 1:
        leap = str(yyyy)+u" est bissextile"
    else:
        leap = str(yyyy)+u" n'est pas bissextile"
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
    # OS specific: to be change accordingly: clear for NIX like,
    #os.system('clear')
    if (os.name == 'posix'):
        cmd = 'clear'
    else:
        cmd = 'cls'
    os.system(cmd)
#
def joursemaine(code_joursem):
    # code_joursem: lundi= 0 to dimanche= 6
    fwd = [u'lundi', u'mardi', u'mercredi', u'jeudi', u'vendredi', u'samedi', u'dimanche']
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
yearday = x[7] # nb jour depuis debut annee
#
#
## DEBUT ##
efface()
fmt = [u'janvier', u'février', u'mars', u'avril', u'mai', u'juin', u'juillet', u'août', u'septembre', u'octobre', u'novembre', u'décembre']
mt = fmt[month-1]
print u"Aujourd'hui c'est le:"
print joursemaine(weekday), day, mt, year, u", semaine ", numsemaine(year, month, day)
print getBiss(year)
print getDebToDate(year, month, day), u"jours depuis le 1er janvier"
print getFinToDate(year, month, day), u"jours jusqu'a la fin de l'année"
print u"Periode zodiacale:",getAstroSigne(day,month)
print
#getCalendar(year, month)
menu()
