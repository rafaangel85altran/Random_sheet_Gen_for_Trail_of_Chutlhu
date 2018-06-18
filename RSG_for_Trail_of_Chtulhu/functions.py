'''
Created on 12 jun. 2018

@author: win7
'''

import random

jobSuitedForMotiv = [
        {"motivation": "Arrogancia", "suitedJobs": "Alienista"},
        {"motivation": "Aventura", "suitedJobs": "Criminal  Militar Parapsicologo Piloto"},
        {"motivation": "Coleccionar Antiguedades", "suitedjobs": "Anticuario Arqueologo Miembro del Clero Profesor"}
    ]

def getRandomFromFile(fileName):
    try:
        lines = open(fileName).read().splitlines()
        lineChoiced = random.choice(lines)
        return lineChoiced
    except Exception:
        print("file with choices could not be readed")
    
#Name Generation
name = getRandomFromFile("firstNames.txt")
name += " "
name += getRandomFromFile("LastNames.txt")

#Motivation Generator
motivation = getRandomFromFile("motivations.txt")

#Job Generation
suitedJob = next(item for item in jobSuitedForMotiv if item["motivation"] == "Arrogancia")
#job = getRandomFromFile("jobs.txt")
job = "Alienista"

if job in suitedJob.values():
    print(job)
