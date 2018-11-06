#!bin/bash
# Description : Résout 2a-mol
# Date : 06/11/2018
# Auteur : Theo HERNANDEZ && Jonathan DINH

##### IMPORTS #####

import random
import sys
import signal
import time

##### VARIABLES #####

borneMin = 0
borneMax = 100
saisieBot = 50
welcomeMsg = "Bienvenue au jeu du plus ou moins ! Trouvez un nombre compris entre 0 et 100. Vous devez ecrire dans fichier un nombre !"
victoryMsg = 'Bravo, tu as gagne. La solution etait '
lessMsg = "C'est plus petit !"
moreMsg = "C'est plus grand !"

##### FUNCTIONS #####

def youcant(sig, frame):
	goodbye()
	sys.exit(0)

def lireFichier():
	fichier = open("./jeu.txt", "r")
	return fichier.read()
	fichier.close()

def ecrireFichier(text):
	text = str(text)
	fichier = open("./jeu.txt", "w")
	fichier.write(text)
	fichier.close()

def goodbye():
	print('\nLa solution était ' + str(saisieBot))
	print('***Goodbye !***')

##### SCRIPT #####

signal.signal(signal.SIGINT, youcant)
if lireFichier() != welcomeMsg:
	print("***** Le script doit etre lancee au meme endroit ou on lance 2a-mol.py *****")
	sys.exit(0)
ecrireFichier(saisieBot)
time.sleep(1)
while True:
	if lireFichier() == victoryMsg + str(saisieBot):
		goodbye()
		break
	elif lireFichier() == lessMsg:
		borneMax = saisieBot
		saisieBot = borneMin + int((borneMax - borneMin)/2)
		ecrireFichier(saisieBot)
		time.sleep(1)
	elif lireFichier() == moreMsg:
		borneMin = saisieBot
		saisieBot = borneMin + int((borneMax - borneMin)/2)
		ecrireFichier(saisieBot)
		time.sleep(1)
	else:
		time.sleep(1)
