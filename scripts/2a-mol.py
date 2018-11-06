#!/bin/python36
#
# 2a-mol.py : Plus ou moins avec lecture dans un fichier
# Date : 23/10/2018
# Auteur : Theo HERNANDEZ && Jonathan DINH

#
# IMPORTS 
#

import random
import time
import sys
import signal

#
# VARIABLES
#

nbrRandom = random.randint(0,100)
msg = "Jeu du plus ou moins ! Nombre compris entre 0 et 100"
plusgrand = "C'est plus grand !"
pluspetit = "C'est plus petit !"
error = "Veuillez ecrire un nombre entre 0 et 100 !"
win = "Tu as gagne"

#
# FONCTIONS
#

def end(sig, frame):
	bye()
	sys.exit(0)

def ecrire():
	fichier = open("jeu.txt", "w")
	fichier.write(msg)
	fichier.close()

def lecture():
	fichier = open("jeu.txt", "r")
	return fichier.read()
	fichier.close()

def plusPetit():
	fichier = open("jeu.txt", "w")
	fichier.write(pluspetit)
	fichier.close()

def plusGrand():
	fichier = open("jeu.txt", "w")
	fichier.write(plusgrand)
	fichier.close()

def Victoire():
	fichier = open("jeu.txt", "w")
	fichier.write(win)
	fichier.close()

def bye():
	print('\nLe nombre etait ' + str(nbrRandom))

#
# SCRIPT 
#

signal.signal(signal.SIGINT, end)
signal.signal(signal.SIGTERM, end)
ecrire()

while True:
	nbr = lecture()
	try:
		nbr = int(nbr)
		if nbr == nbrRandom:
			Victoire()
			break
		elif nbr > nbrRandom:
			plusPetit()
			time.sleep(1)
		else:
			plusGrand()
			time.sleep(1)
	except ValueError:
		time.sleep(1)
