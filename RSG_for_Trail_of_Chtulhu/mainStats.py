'''
Created on Jun 17, 2018

@author: joanrafaelangelperez
'''

from sheet_functions import incrementStat

Health      =   1
Stability   =   1
Sanity      =   1

incrementStat(Health, 1)

def printMainStats ():
    print("Health ", Health)
    print("Stability ", Stability)
    print("Sanity ", Sanity)
    