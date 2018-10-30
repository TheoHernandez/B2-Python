#!/bin/python36

# Nom : 1b-dic.py
# Description : liste de prenom trier par ordre alphabetique
# Date : 15/10/2018
# Auteur : Theo HERNANDEZ et Jonathan DINH

liste = [] 	#on déclare notre liste

while 0 < 1: 	
	prenom = input('Saisir un prenom, taper \'q\' pour quitter : ')
	if prenom == 'q': 	
		break
	liste.append(prenom) 

print(sorted(liste)) 	




