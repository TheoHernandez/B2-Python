#!bin/phyton36
# 1d-mol.py est un jeu du plus ou moins
# Date 23/10/2018
# Auteur : Theo HERNANDEZ && Jonathan DINH

import random
import signal
import sys

from random import randint
from time import sleep


nombreRandom = randint(0,100)


def youcant(sig, frame):
	print(' ')
	aurevoir()
	sys.exit(0)

signal.signal(signal.SIGINT, youcant)


def checkIsNumber():
	while 0 < 1:
		try:
			nombre = input('Saisir un nombre, taper \'q\' pour quitter : ')
			if nombre == 'q':
				break
			nombre = int(nombre)
			if nombre > 100  or nombre < 0:
				print('Erreur ce nombre n\'est pas compris entre 0 et 100')
			else: 
				break
		except ValueError:
			print('Erreur ce n\'est pas un nombre')
	return nombre

def aurevoir():
	print('Le nombre etait ' + str(nombreRandom))
	print('Aurevoir')



while 0 < 1:
	nombreUser = checkIsNumber()
	
	if nombreUser == 'q':
		aurevoir()
		break
	if nombreUser == nombreRandom:
		print('Gagner')
		break
	elif nombreUser > nombreRandom:
		print('Plus petit')
	else:
		print('Plus grand')  


