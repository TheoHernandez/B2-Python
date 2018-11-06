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
 
nbrRandom = random.randint(0,100)
msg = "Jeu du plus ou moins, écrire un nombre entre 0 et 100"
pluspetit = "Plus grand "
plusgrand = "Plus petit !"
error = "Ecrire un nombre entre 0 et 100 !"
victoire = 'Tu as gagne'
 
#
#Fonctions
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

def gagner():
	fichier = open("jeu.txt", "w")
	fichier.write(victoire)
	fichier.close()

def bye():
	print('\nLe nombre etait ' + str(nbrRandom))

#
# Scripts
#

signal.signal(signal.SIGINT, end)
signal.signal(signal.SIGTERM, end)
ecrire()

while True:
	nbr = lecture()
	try:
		nbr = int(nbr)
		if nbr == nbrRandom:
			gagner()
			break
		elif nbr > nbrRandom:
			plusPetit()
			time.sleep(1)
		else:
			plusGrand()
			time.sleep(1)
	except ValueError:
		time.sleep(1)
