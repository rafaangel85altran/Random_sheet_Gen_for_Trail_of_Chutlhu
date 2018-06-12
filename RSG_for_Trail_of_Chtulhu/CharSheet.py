'''
Created on 12 jun. 2018

@author: win7
'''

investigators = []

class CharSheet:
    
    def __init__(self, name, surname):
        investigator = {"name": name, "surname": surname}
        investigators.append(investigator)
        
    def __str__(self):
        return "charsheet class"   
    
    
random1 = CharSheet("Willy", "Mondongo")
print(random1)