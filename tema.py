import os
os.system('cls')

option = ''
robo_r = 0
robo_c = 0

gmap = [
    ['  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  ']
]

while option != 'x':
    os.system('cls')
    print('-'*12)
    for r in range(5):
        
        print('|', end="")
        for c in range(5):
            print(gmap[r][c], end='')
        print('|')

    print('-'*12)
    print("\n\ncontrols: \na - left,\nd - right,\nw - up,\ns - exit")  

    option = input(">>")

    if option == 'd':
        
        gmap[robo_r][robo_c] = ' '
        robo_c += 1
        gmap[robo_r][robo_c] = 'x'
        
    if option =="s":
        gmap[robo_r][robo_c] = ''
        robo_r += 1
        gmap[robo_r][robo_r] = 'x' 
    elif option == 'w' :
        gmap[robo_r][robo_c] = ' '
        robo_r -= 1
        gmap[robo_r][robo_c] = 'x'
        
    if option == 'a':
        gmap[robo_r][robo_c] = ' '
        robo_c -= 1
        gmap[robo_r][robo_c] = 'x'           
   
