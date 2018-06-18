'''
Created on 12 jun. 2018

@author: win7
'''

import random

def getCompleteName():

    try:
        lines = open('firstNames.txt').read().splitlines()
        name = random.choice(lines)
        lines = open('lastNames.txt').read().splitlines()
        name += " "
        name += random.choice(lines)
        return name
    except Exception:
        print("File could not be readed, check it firstNamesComplete.txt is inside the folder ")

def getJob():
    try:
        lines = open('jobs.txt').read().splitlines()
        job = random.choice(lines)
        return job
    except Exception:
        print("File could not be readed, check it jobs.txt is inside the folder ")

print("Nombre Personaje :", getCompleteName())
print("Profesion: ", getJob())