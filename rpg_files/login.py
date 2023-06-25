from rpg_files.db import *
from rpg_files.msg import *
from rpg_files.crearpj import *
import getpass


class Login():

    def __init__(self) -> None:
        self.email = None

    def login(self):

        print()

        menu_login = {1:'Tengo cuenta',2:'Crear cuenta',3:'Salir al menu principal'}

        salir = False

        while not salir:

            try:
                for key in menu_login.keys():
                    print(key,'--',menu_login[key])
                print('\n')

                option_menu_login = int(input('Opción: '))
                if option_menu_login == 1:
                    valini = self.iniciar_sesion()
                    if valini == 1:
                        break

                    else:
                        continue
                
                elif option_menu_login == 2:
                    self.crear_cuenta()

                elif option_menu_login == 3:
                    game_close()
                    salir = True
                    return salir

                else:
                    opcion_no_valida()
            
            except ValueError:
                opcion_no_valida()

    def iniciar_sesion(self):

        try:
            volver_atras()
            email = input('Email: ')
            contrasena = getpass.getpass('Contrasena: ')
            print('\n')

            self.email = email

            val = select_user(email,contrasena)
            return val
        
        except:
            print()
        
    def crear_cuenta(self):

        try:
            volver_atras()
            email = input('Email: ')
            contrasena = getpass.getpass('Contrasena: ')
            print('\n')

            insert_values_into_db(email,contrasena)

        except:
            print()

l = Login()