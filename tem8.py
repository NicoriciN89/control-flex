import os
from os import system
from time import sleep

ads = [
    "cumpara",                         #0
    "apa de 15 lei ",                  #1  
    "recomand de 2l minimu pe ziua"    #2
]

ads_duration =[
    3.0,
    3.5,
    5.0
    
    
]   



index = 0
os.system('cls')

while True:
    system("clear")
    ad = ads.pop(0)
    duration =ads_duration.pop(0)
    
    print(">", ad, "<<")
    sleep(duration)
    
   
    ads.append(ad)
    ads_duration.append(duration)
   
        
     