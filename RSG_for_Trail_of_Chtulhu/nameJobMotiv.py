'''
Created on Jun 17, 2018

@author: joanrafaelangelperez
'''
import random        
        
def getRandomFromFile(fileName):        
    try:
        lines = open(fileName).read().splitlines()
        lineChoiced = random.choice(lines)
        return lineChoiced
    except Exception:
        print("file with choices could not be readed")

def getRandomJob(motivation):
    
    jobSuitedForMotiv = {
    'Arrogancia':               ['Alienista', 'Cientifico'],
    'Aventura':                 ['Criminal', 'Militar', 'Parapsicologo', 'Piloto'],
    'Coleccionar Antiguedades': ['Aticuario', 'Arqueologo', 'Miembro del Clero', 'Profesor'],
    'Curiosidad':               ['Cienfitico', 'Detective de policia', 
                                 'Investigador privado', 'Parapsicologo', 'Periodista'],
    'Deber':                    ['Miembro del Clero', 'Detective de policia', 'Medico', 'Militar'],
    'En la sangre':             ['Anticuario', 'Diletante'],
    'Erudicion':                ['Arqueologo', 'Cientifico', 'Profesor'],
    'Hastio':                   ['Artista', 'Diletante', 'Militar'],
    'Impacto subito':           ['Alienista','Anticuario', 'Arqueologo', 'Artista', 'Cientifico', 'Criminal', 
                                 'Detective de policia', 'Diletante', 'Enfermero', 'Escritor', 'Investigador privado', 
                                 'Medico', 'Miembro del Clero', 'Militar', 'Parapsicologo', 'Periodista', 'Piloto', 
                                 'Profesor', 'Vagabundo'],
    'Mala suerte':              ['Criminal', 'Vagabundo'],
    'Sed de conocimientos':     ['Arqueologo', 'Parapsicologo', 'Profesor'],
    'Seguidor':                 ['Detective de policia', 'Medico', 'Militar'],
    'Sensibilidad Artistica':   ['Artista', 'Diletante', 'Escritor'],
    'Venganza':                 ['Criminal', 'Investigador privado']
    }
    
    if motivation in jobSuitedForMotiv:
        job = random.choice(jobSuitedForMotiv[motivation])
        return job
    
def printNameJobMotiv():
    #Name Generation
    name = getRandomFromFile("firstNames.txt")
    name += " "
    name += getRandomFromFile("LastNames.txt")
    
    #Motivation Generator
    motivation = getRandomFromFile("motivations.txt") 
    
    #Job Generation
    job = getRandomJob(motivation)
    
    print(name)
    print(job)
    print(motivation)

