from rpg_files.characters import *
from rpg_files.escenarios import *
from rpg_files.msg import *
from rpg_files.login import *
from rpg_files.db import *
from rpg_files.crearpj import *
from rpg_files.misionesclases import *


menu_game = {1:'Juega con 1 personaje',2:'Juega con un equipo de 4 personajes',3:'Salir del juego'}

while True:

    try:

        print('\n')
        for key in menu_game.keys():
            print(key,'--',menu_game[key])
        print('\n')

        option_menu_game = int(input('Opción: '))

        if option_menu_game == 1:
            print('Estamos trabando para implementar este modo de juego')

        elif option_menu_game == 2:
            try:
                l = Login()
                salir = l.login()
                if salir:
                    continue

                c = CreatePJ(l.email)
                salir = c.menuEQUIPO()
                if salir:
                    continue
                
                e = Escenario(c.personajes,l.email,c.nombre_equipo)
                salir = e.ciudad()
                if salir:
                    continue

            except KeyboardInterrupt:
                game_close()
        
        elif option_menu_game == 3:
            game_close()
            break

        else:
            opcion_no_valida()
    
    except ValueError:
        opcion_no_valida()
    
    except KeyboardInterrupt:
        game_close()
        break