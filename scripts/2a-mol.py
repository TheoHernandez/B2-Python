#!/usr/bin/python36
# Description: jeu plus ou moins en demon
# Date: 04/11/2018
# Auteur : Theo HERNANDEZ && Jonathan DINH

#
#Import
#
from random import randint
import re
import signal

#
#Variable
#
min = 0
max = 100
nbr = randint(min,max) 
gagner = False

#
#Fonction pour le message de fin
#
def end(*args):
  read("Désoler c' était: " + str(n))
  exit()

signal.signal(signal.SIGINT, end)
signal.signal(signal.SIGTERM, end)

#
#Ecrire dans jeu.txt
#
def read(msg):
  jeu = open("jeu.txt", "w")
  jeu.write(msg)
  jeu.close()

#
#Lire dans jeu.txt
#
def lire_fichier():
  jeu = open("jeu.txt", "r")
  msg = jeu.read()
  jeu.close()
  return msg
 

read("Jeu du plus ou moins! Saisissez un nombre entre 0 et 100")


#
#Script du jeu
#
while gagner is False:
  nbr = lire_fichier()
  if re.match(r"^[0-9]+$", nbr):
    nbr = int(nbr)
    if nbr > 100:
      continue
    if nbr > n:
      read("Plus petit")
    elif nbr < n:
      read("Plus grand")
    elif nbr == n:
      read("Tu as Gagner")
      gagner = True
    else :
      end()
