'''
Created on 12 jun. 2018
@author: win7
'''
import mainStats
from nameJobMotiv import printNameJobMotiv
from skills import printSkills
from mainStats import printMainStats
from sheet_functions import incrementStat

incrementStat(mainStats.Health, 6)

print("#####################################################################")
#printNameJobMotiv()
print("                                                                     ")
printMainStats()
print("                                                                     ")
#printSkills()
print("#####################################################################")