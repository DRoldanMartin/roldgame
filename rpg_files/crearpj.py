from rpg_files.db import *
from rpg_files.characters import *
from rpg_files.login import *
from rpg_files.misionesclases import *


class CreatePJ():
    def __init__(self,email) -> None:
        self.personajes = [Berserker(),Paladin(),Brujo(),Clerigo()]
        self.char_list = []
        self.email = email
        self.arma = None
        self.nombre_equipo = None
    
    
    def menuEQUIPO(self):

        print('\n')

        menu_crearpj = {1:'Seleccionar equipo',2:'Crear equipo',3:'Salir al menu principal'}
        print('Wellcome: ', self.email)

        salir = False

        while not salir:

            try:
                print('\n')
                for key in menu_crearpj.keys():
                    print(key,'--',menu_crearpj[key])
                print('\n')
                
                option_menu_create = int(input('Opción: '))
                
                if option_menu_create == 1:
                    self.listar_equipo()
                    break
                
                elif option_menu_create == 2:
                    self.setup()
                    self.crear_equipo()
                    break

                elif option_menu_create == 3:
                    game_close()
                    salir = True
                    return salir

                else:
                    opcion_no_valida()
            
            except ValueError:
                opcion_no_valida()

    def print_all_characters(self,cls):
        return cls.__subclasses__()
    
    def setup(self):

        print('\n')

        print("{:<4} {:<20} {:<6} {:<6} {:<12} {:<14} {:<8} {:<10} {:<18}".format("", "Clase", "Nivel", "Vida", "Resistencia", "Daño condicion", "Fuerza", "Curacion", "Resistencia condicion"))

        i = 0
        for char in self.print_all_characters(Character):
            self.char_list.append(char())
            char_instance = char()
            char_values = [i+1, char_instance.__class__.__name__, char_instance.nivel, char_instance.vida, char_instance.resistencia, char_instance.dano_condicion, char_instance.fuerza, char_instance.curacion, char_instance.resistencia_condicion]
            print("{:<4} {:<20} {:<6} {:<6} {:<12} {:<14} {:<8} {:<10} {:<18}".format(*char_values))
            i += 1

        print('\n')
    
    def crear_equipo(self):

        self.nombre_equipo = input('Nombre para el quipo: ')

        for i in range(len(self.personajes)): 

            nombres_del_equipo = []

            nombre_personaje = input(f'Nombre del {self.personajes[i].clase}: ')
            self.personajes[i].name = nombre_personaje

            nombres_del_equipo.append(self.personajes[i].name)

        insert__equipo_into_db(self.email,self.nombre_equipo,self.personajes[0].clase,self.personajes[0].name,self.personajes[1].clase,self.personajes[1].name,self.personajes[2].clase,self.personajes[2].name,self.personajes[3].clase,self.personajes[3].name)
        insert_items_into_db(self.nombre_equipo,'moneda','oro',0)
        insert_items_into_db(self.nombre_equipo,'poti','Pocion Pequeña',0)
        insert_items_into_db(self.nombre_equipo,'poti','Pocion Mediana',0)
        insert_items_into_db(self.nombre_equipo,'poti','Pocion Grande',0)
        
        for i in range(len(self.personajes)):
            insert_personajes_into_db(self.nombre_equipo,self.personajes[i].name,self.personajes[i].clase,self.personajes[i].nivel,self.personajes[i].vida,self.personajes[i].resistencia,self.personajes[i].dano_condicion,self.personajes[i].fuerza,self.personajes[i].curacion,self.personajes[i].resistencia_condicion,self.personajes[i].experiencia,self.personajes[i].max_experiencia)

        self.setup_misiones()
        
    def print_all_misions(self, cls):
        return cls.__subclasses__()

    def setup_misiones(self):

        for m in self.print_all_misions(Misiones):
            m_instance = m()
            insert_into_misiones(self.nombre_equipo,m_instance.mision_name,m_instance.valor_mision)

    def listar_equipo(self):
        equipos = listar_equipos(self.email)
        personajes = listar_personajes_totales()

        print('\n')

        a = 1
        for equipo in equipos:
            
            print(f"{a} Equipo: {equipo}")
            a += 1
            print("{:<20} {:<20} {:<6} {:<6} {:<14} {:<18} {:<10} {:<10} {:<25} {:<20} {:<20}".format("Clase", "Nombre", "Nivel", "Vida", "Resistencia", "Daño condicion", "Fuerza", "Curacion", "Resistencia condicion" ,"Experiencia", "Experiencia Necesaria"))

            for i, personaje in enumerate(personajes):
                if personaje[0] == equipo:
                    print("{:<20} {:<20} {:<6} {:<6} {:<14} {:<18} {:<10} {:<10} {:<25} {:<20} {:<20}".format(personaje[2], personaje[1], personaje[3], personaje[4], personaje[5], personaje[6], personaje[7], personaje[8], personaje[9], personaje[10], personaje[11]))

            print('\n')
        print('\n')

        opcion_valida = False

        while not opcion_valida:

            char_select = int(input('\nSeleccion del equipo (1-{}): '.format(len(equipos))))
        
            if char_select in range(1, len(equipos) + 1):
                opcion_valida = True
            
            else:
                opcion_no_valida()
            
        print('\n')

        if char_select in range(1, len(equipos)+1):
            equipo_seleccionado(equipos[char_select-1])
            
            self.nombre_equipo = equipos[char_select-1]

            personajes = listar_personajes_equipo(self.nombre_equipo)

            for i in range(len(personajes)):
                if personajes[i][0] == self.nombre_equipo:
                    if personajes[i][2] == 'Berserker':
                        self.personajes[i] = Berserker()

                    if personajes[i][2] == 'Paladin':
                        self.personajes[i] = Paladin()

                    if personajes[i][2] == 'Brujo':
                        self.personajes[i] = Brujo()

                    if personajes[i][2] == 'Clerigo':
                        self.personajes[i] = Clerigo()
                
                    if i < len(self.personajes):
                        self.personajes[i].clase = personajes[i][2]
                        self.personajes[i].name = personajes[i][1]
                        self.personajes[i].nivel = personajes[i][3]
                        self.personajes[i].vida = personajes[i][4]
                        self.personajes[i].resistencia = personajes[i][5]
                        self.personajes[i].dano_condicion = personajes[i][6]
                        self.personajes[i].fuerza = personajes[i][7]
                        self.personajes[i].curacion = personajes[i][8]
                        self.personajes[i].resistencia_condicion = personajes[i][9]
                        self.personajes[i].experiencia = personajes[i][10]
                        self.personajes[i].max_experiencia = personajes[i][11]