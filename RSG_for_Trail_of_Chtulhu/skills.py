'''
Created on Jun 17, 2018

@author: joanrafaelangelperez
'''
from healthStabilitySanity import incrementStat

skills = [
    
    #ACADEMIC SKILLS
    {'type': "Academica",       'name': 'Antropologia',         'value': 0},
    {'type': 'Academica',       'name': 'Arqueologia',          'value': 0},
    {'type': 'Academica',       'name': 'Arquitectura',         'value': 0},
    {'type': 'Academica',       'name': 'Biologia',             'value': 0},
    {'type': 'Academica',       'name': 'Buscar libros',        'value': 0},
    {'type': 'Academica',       'name': 'Ciencias ocultas',     'value': 0},
    {'type': 'Academica',       'name': 'Contabilidad',         'value': 0},
    {'type': 'Academica',       'name': 'Criptografia',         'value': 0},
    {'type': 'Academica',       'name': 'Derecho',              'value': 0},
    {'type': 'Academica',       'name': 'Fisica',               'value': 0},
    {'type': 'Academica',       'name': 'Geologia',             'value': 0},
    {'type': 'Academica',       'name': 'Historia',             'value': 0},
    {'type': 'Academica',       'name': 'Historia del arte',    'value': 0},
    {'type': 'Academica',       'name': 'Ingles',               'value': 0},
    {'type': 'Academica',       'name': 'Latin',                'value': 0},
    {'type': 'Academica',       'name': 'Griego',               'value': 0},
    {'type': 'Academica',       'name': 'Frances',              'value': 0},
    {'type': 'Academica',       'name': 'Hebreo',               'value': 0},
    {'type': 'Academica',       'name': 'Castellano',           'value': 0},
    
    #INTERPERSONAL SKILLS
    {'type': "Interpersonal",   'name': 'Adulacion',            'value': 0},
    {'type': "Interpersonal",   'name': 'Bajos fondos',         'value': 0},
    {'type': "Interpersonal",   'name': 'Burocracia',           'value': 0},
    {'type': "Interpersonal",   'name': 'Consuelo',             'value': 0},
    {'type': "Interpersonal",   'name': 'Credito',              'value': 0},
    {'type': "Interpersonal",   'name': 'Credito',              'value': 0},
    {'type': "Interpersonal",   'name': 'Evaluar sinceridad',   'value': 0},
    {'type': "Interpersonal",   'name': 'Historia oral',        'value': 0},
    {'type': "Interpersonal",   'name': 'Interrogatorio',       'value': 0},
    {'type': "Interpersonal",   'name': 'Intimidacion',         'value': 0},
    {'type': "Interpersonal",   'name': 'Jerga policial',       'value': 0},
    {'type': "Interpersonal",   'name': 'Regatear',             'value': 0},
    
    #TECHNICAL SKILLS
    {'type': "Tecnica",         'name': 'Astronomia',            'value': 0},
    {'type': "Tecnica",         'name': 'Cerrajeria',            'value': 0},
    {'type': "Tecnica",         'name': 'Farmacologia',          'value': 0},
    {'type': "Tecnica",         'name': 'Fotografia',            'value': 0},
    {'type': "Tecnica",         'name': 'Habilidad artesanal',   'value': 0},
    {'type': "Tecnica",         'name': 'Habilidad artistica',   'value': 0},
    {'type': "Tecnica",         'name': 'Medicina forense',      'value': 0},
    {'type': "Tecnica",         'name': 'Quimica',               'value': 0},
    {'type': "Tecnica",         'name': 'Recogida de pruebas',   'value': 0},
    {'type': "Tecnica",         'name': 'Supervivencia',         'value': 0},
    
    #GENERAL SKILLS
    {'type': "General",         'name': 'Armas',                  'value': 0},
    {'type': "General",         'name': 'Armas de fuego',         'value': 0},
    {'type': "General",         'name': 'Atletismo',              'value': 0},
    {'type': "General",         'name': 'Birlar',                 'value': 0},
    {'type': "General",         'name': 'Conduccion',             'value': 0},
    {'type': "General",         'name': 'Cordura',                'value': 0},
    {'type': "General",         'name': 'Disfraz',                'value': 0},
    {'type': "General",         'name': 'Electricidad',           'value': 0},
    {'type': "General",         'name': 'Escaramuza',             'value': 0},
    {'type': "General",         'name': 'Estabilidad',            'value': 0},
    {'type': "General",         'name': 'Explosivos',             'value': 0},
    {'type': "General",         'name': 'Hipnosis',               'value': 0},
    {'type': "General",         'name': 'Huida',                  'value': 0},
    {'type': "General",         'name': 'Mecanica',               'value': 0},
    {'type': "General",         'name': 'Monta',                  'value': 0},
    {'type': "General",         'name': 'Ocultar',                'value': 0},
    {'type': "General",         'name': 'Pilotaje',               'value': 0},
    {'type': "General",         'name': 'Preparacion',            'value': 0},
    {'type': "General",         'name': 'Primeros auxilios',      'value': 0},
    {'type': "General",         'name': 'Psicoanalisis',          'value': 0},
    {'type': "General",         'name': 'Salud',                  'value': 0},
    {'type': "General",         'name': 'Seguir',                 'value': 0},
    {'type': "General",         'name': 'Sentir el peligro',      'value': 0},
    {'type': "General",         'name': 'Sigilo',                 'value': 0},   
]


#print(incrementStat(skills[0].get('value'),2))
#print(skills[0].get('type'), skills[0].get('name'), skills[0].get('value'))

def printSkills():
    print("Habilidades Academicas")
    for dicts in skills:
        if 'Academica' in dicts.get('type'):
            print('    ',dicts.get('name'), dicts.get('value'))
            
    print("Habilidades Interpersonales")
    
    for dicts in skills:
        if 'Interpersonal' in dicts.get('type'):
            print('    ',dicts.get('name'), dicts.get('value'))
            
    print("Habilidades Tecnicas")
    
    for dicts in skills:
        if 'Tecnica' in dicts.get('type'):
            print('    ',dicts.get('name'), dicts.get('value'))
            
    print("Habilidades Generales")
    for dicts in skills:
        if 'General' in dicts.get('type'):
            print('    ',dicts.get('name'), dicts.get('value'))
                                   
printSkills()
