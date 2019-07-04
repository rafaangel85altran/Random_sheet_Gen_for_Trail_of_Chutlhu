'''
Created on Jun 17, 2018

@author: joanrafaelangelperez
'''

Health      =   1
Stability   =   1
Sanity      =   1

def printMainStats ():
    print("Health ", Health)
    print("Stability ", Stability)
    print("Sanity ", Sanity)
    
def incrementStat(stat, quantity):
    stat += quantity
    return  stat

    