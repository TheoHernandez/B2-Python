#!/bin/python36
#
# 2a-mol.py Plus ou moins en demon
# Date : 23/10/2018
# Auteur : Theo HERNANDEZ && Jonathan DINH

#
# Imports
#

import random
import time
import sys
import signal

#
# Variables
#

nbrauto = 50
msg = 'Jeu plus ou moins, rentrer un nombre entre 0 et 100'
win = 'Gagner'
pluspetit = 'Plus petit'
plusgrand = 'Plus grand'

#
#Fonctions
#

def end(sig, frame):
	bye()
	sys.exit(0)

def ecrire():
	fichier = open("jeu.txt", "w")
	fichier.write(nbrauto)
	fichier.close()

def lecture():
	fichier = open("jeu.txt", "r")
	return fichier.read()
	fichier.close()

def bye():
	print('\nLe nombre etait ' + str(nbrRandom))

#
# Scripts
#

signal.signal(signal.SIGINT, end)
signal.signal(signal.SIGTERM, end)

while True:
		if lecture() == msg:
			ecrire()
		elif lecture() == win:
			break
		elif lecture() == pluspetit:
			nbrauto = nbrauto%2
			ecrire()
		elif lecture() == plusgrand:
			nbrauto += nbrauto%2
			ecrire()
		
