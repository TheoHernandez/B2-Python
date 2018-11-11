#!/usr/bin/python36
# 
# 3b-opty : Permet d'effectuer une sauvegarde
# Date : 11/11/2018
# Auteur : Theo HERNANDEZ && Jonathan DINH

import signal
import shutil
import gzip
import os
import sys
import subprocess
import argparse


# Fermer le programme
def closeProgramme(signal, frame):
    exit()

signal.signal(signal.SIGINT, closeProgramme)


# Permet de choisir le chemin du dossier 'Data'
def dataChemin():
    arguments = argparse.ArgumentParser()
    arguments.add_argument("-p", "--path", help="chemin du dossier")
    args = arguments.parse_args()
    if args.path:
        return args.path
    else:
        return '../scripts'


# Creer une archive
def createArchive():
    os.remove(dossierData + '/archive.tar.gz')
    shutil.move(archive + '.tar.gz', dossierData)


# Supprime l'archive
def deleteArchive():
    if os.path.exists(archive + '.tar.gz'):
        os.remove(archive + '.tar.gz')

#
# Variables
#

dossierData = os.path.expanduser(dataChemin()+'/data/')
dossierScripts = os.path.expanduser('../scripts')
archive = os.path.expanduser('./archive')

# Création dossier 'Data'
os.makedirs(dossierData, exist_ok=True)
sys.stdout.write('Le dossier \'data\' vient d\'être créé.\n')

shutil.make_archive(archive, 'gztar', dossierScripts)

# Existance d'une sauvegarde
if os.path.exists(dossierData + '/archive.tar.gz'):

    with gzip.open(dossierData + '/archive.tar.gz', 'rb') as f:
        exist_save = f.read()

    with gzip.open(archive + '.tar.gz', 'rb') as f:
        new_save = f.read()

    if exist_save != new_save:
        createArchive()
        sys.stdout.write('La sauvegarde a été créer dans le dossier \'data\'.\n')

    else:
        deleteArchive()
        sys.stdout.write('La sauvegarde a était supprimer.\n')

else:
    shutil.move(archive + '.tar.gz', dossierData)
    sys.stdout.write('La sauvegarde a été archivé dans le dossier \'data\'.\n')
