from colorama import Fore

def game_close():
    print('\n')
    print(Fore.RED,'Se ha cerrado el juego',Fore.RESET)
    print('\n')

def volver_atras():
    print('\n')
    print(Fore.RED,'CTRL + C para volver al menú de inicio',Fore.RESET)
    print('\n')

def opcion_no_valida():
    print('\n')
    print(Fore.RED,'Opcion no valida',Fore.RESET)
    print('\n')

def credenciales_correctas():
    print('\n')
    print(Fore.GREEN,'CREDENCIALES CORRECTAS',Fore.RESET)
    print('\n')

def credenciales_incorrectas():
    print('\n')
    print(Fore.RED,'CREDENCIALES INCORRECTAS',Fore.RESET)
    print('\n')

def enemigo_eliminado(enemigo):
    print('\n')
    print('Enemigo eliminado: ',Fore.RED,enemigo.name,Fore.RESET)
    print('\n')

def has_muerto():
    print('\n')
    print(Fore.RED,'HAS MUERTO',Fore.RESET)
    print('\n')

def personaje_eliminado(personaje):
    print('\n')
    print('Personaje eliminado: ',Fore.YELLOW,personaje.name,Fore.RESET)
    print('\n')

def equipo_seleccionado(equipo):
    print('\n')
    print('Equipo seleccionado: ',Fore.YELLOW,equipo,Fore.RESET)
    print('\n')

def mision_seleccionada(mision_name):
    print('\n')
    print('Mision seleccionada: ',Fore.YELLOW,mision_name,Fore.RESET)
    print('\n')

def nombre_personaje(clase_personaje,nombre_personaje):
    print(clase_personaje,'-->',Fore.YELLOW,nombre_personaje,Fore.RESET)

def personaje_ataca_a_enemigo(personaje,enemigo):
    print(Fore.YELLOW,personaje,Fore.RESET,' ataca a ',Fore.RED,enemigo,Fore.RESET)

def enemigo_ataca_a_personaje(personaje,enemigo):
    print(Fore.RED,enemigo,Fore.RESET,' ataca a ',Fore.YELLOW,personaje,Fore.RESET)

def enemigo_recibe_daño(enemigo,vida):
    print(Fore.RED,enemigo,Fore.RESET,' ha recibido un daño de ',Fore.RED,vida,Fore.RESET)

def personaje_recibe_daño(personaje,vida):
    print(Fore.YELLOW,personaje,Fore.RESET,' ha recibido un daño de ',Fore.RED,vida,Fore.RESET)

def vida_restante_enemigo(enemigo,vida):
    print('Vida restante de ',Fore.RED,enemigo,Fore.RESET,Fore.BLUE,vida,Fore.RESET)
    print('\n')

def vida_restante_personaje(personaje,vida):
    print('Vida restante de ',Fore.YELLOW,personaje,Fore.RESET,Fore.BLUE,vida,Fore.RESET)
    print('\n')

def maldicion_de_las_sombras(enemigo,dano_condicion):
    print(Fore.RED,enemigo,Fore.RESET,' ha recibido un daño de maldicion de sombra de ',Fore.RED,dano_condicion,Fore.RESET)

def tormenta_de_las_sombras(enemigo,dano_condicion):
    print(Fore.RED,enemigo,Fore.RESET,' ha recibido un daño de tormenta de sombra de ',Fore.RED,dano_condicion,Fore.RESET)

def enemigo_habilidad(personaje,dano_condicion):
    print(Fore.YELLOW,personaje,Fore.RESET,' ha recibido un daño de condicion de ',Fore.RED,dano_condicion,Fore.RESET)