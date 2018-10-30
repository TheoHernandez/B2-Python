
m : 1a-add.py
# 1a-add.py Additionne 2 chiffre
# Date : 15/10/2018
# Auteur : Theo HERNANDEZ && Jonathan DINH

def addition(): #fonction addition
	while 0 < 1:  
		try: #on test input est un nombre si c'est vrai on casse la boucle
			int1 = int(input('Nombre 1 ? : '))
			break
		except ValueError: #sinon on affiche une erreur
			print("Erreur")
	
	while 0 < 1: 
		try:
			int2 = int(input('Nombre 2 ? : '))
			break
		except ValueError:
			print("Erreur")
	
	return int1 + int2 

print('Le résultat est : ' + str(addition())) #affiche le résultat
