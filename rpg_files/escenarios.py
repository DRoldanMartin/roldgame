from rpg_files.characters import *
from rpg_files.enemies import *
from rpg_files.msg import *
from rpg_files.db import *
from rpg_files.misionesclases import *
from rpg_files.items import *
from random import randint
from time import sleep


class Escenario():
    def __init__(self,personajes,email,nombre_equipo) -> None:
        self.personajes = personajes
        self.email = email
        self.nombre_equipo = nombre_equipo
        self.pj_turno = None
        self.enemigo_turno = None
        self.ultimo_enemigo_atacado = None
        self.inventario = []
        self.personajes_eliminados = []
        self.enemigos_eliminados = []
        self.misiones_por_hacer = []
        self.enemigos = []
        self.experiencia_mision = None
        self.oro_mision = None
        self.oro_enemigo = None
        self.oro_total = 0
        self.mision_name = None
        self.habilidad_seleccionada = None
        self.berserker_fuerza = None
        self.berserker_fuerza_usada = False
        self.resistencia_condicion_personaje = None
        self.personaje_resistencia_condicion_aumentada = False
        self.perosonajes_aumentados_resistencia_condicion = []
        self.berserker_pro_crit = None
        self.berserker_pro_crit_usado = False
        self.clerigo_resucitar = True
        self.brujo_maldicion_de_las_sombras = False
        self.enemigo_afectado_maldicion_de_las_sombras = []
        self.brujo_tormenta_de_las_sombras = False
        self.enemigo_afectado_tormenta_de_las_sombras = []
        self.personajes_afectados_por_condicion = []
        self.potis_pequenas_hp = 0
        self.potis_medianas_hp = 0
        self.potis_grandes_hp = 0


    def update_all_items(self):
        items_from_db = select_items_into_db(self.nombre_equipo)
        for item_data in items_from_db:
            item_type = item_data['tipo_item']
            item_name = item_data['nombre_item']
            item_quantity = item_data['cantidad_item']

            if item_type == 'poti' and item_name == 'Pocion Pequeña':
                self.potis_pequenas_hp = item_quantity
            elif item_type == 'poti' and item_name == 'Pocion Mediana':
                self.potis_medianas_hp = item_quantity
            elif item_type == 'poti' and item_name == 'Pocion Grande':
                self.potis_grandes_hp = item_quantity
            elif item_name == 'oro':
                self.oro_total = item_quantity

    def ciudad(self):

        self.update_all_items()

        menu = {1:'Equipo',2:'Inventario',3:'Misiones',4:'Stats',5:'Mercader',6:'Salir al menu principal'}

        salir = False

        while not salir:
            print('\n')
            for key in menu.keys():
                print(key,'--',menu[key])
            print('\n')

            try:
                option_menu = int(input('Opción: '))
                if option_menu == 1:
                    self.equipo()
                    continue

                elif option_menu == 2:
                    self.inventariado()
                    continue

                elif option_menu == 3:
                    self.setup_misiones()
                    mision_seleccionada(self.mision_name)
                    if self.enemigos:
                        self.combate()
                    break
                    
                elif option_menu == 4:
                    self.estadisticas()
                    continue

                elif option_menu == 5:
                    self.mercader()
                    continue
                    

                elif option_menu == 6:
                    game_close()
                    salir = True
                    return salir

                else:
                    opcion_no_valida()
            
            except ValueError:
                opcion_no_valida()

    def equipo(self):
        print('\n')
        for i in range(len(self.personajes)):
            nombre_personaje(self.personajes[i].clase ,self.personajes[i].name)
            Weapons.stats(self.personajes[i].arma)

    def estadisticas(self):
        print('\n')
        print("{:<10} {:<20} {:<20} {:<6} {:<6} {:<14} {:<18} {:<10} {:<10} {:<25} {:<20} {:<20}".format("","Clase", "Nombre", "Nivel", "Vida", "Resistencia", "Daño condicion", "Fuerza", "Curacion", "Resistencia condicion" ,"Experiencia", "Experiencia Necesaria"))
        for i in range(len(self.personajes)):
            Character.stats(self.personajes[i], i)
        print('\n')

    def enemigo_estadisticas(self):
        print("{:<10} {:<30} {:<20} {:<20} {:<6}".format("", "Nombre", "Vida", "Fuerza", "Defensa"))
        for i in range(len(self.enemigos)):
            Enemies.stats(self.enemigos[i], i)
        print('\n')

    def combate(self):
        menu_combate = {1:'Atacar',2:'Usar objeto'}

        i = 0
        while len(self.personajes) > 0 and len(self.enemigos) > 0:

            self.check_condiciones_a_enemigos()
            self.check_condicion_a_personajes()

            if i >= len(self.personajes):
                i = 0

            self.pj_turno = self.personajes[i]
            i += 1

            print('\n')
            if self.pj_turno.clase == 'Berserker':
                print(f'Turno del {self.pj_turno.name}')
            elif self.pj_turno.clase == 'Paladin':
                print(f'Turno del {self.pj_turno.name}')
            elif self.pj_turno.clase == 'Brujo':
                print(f'Turno del {self.pj_turno.name}')
            elif self.pj_turno.clase == 'Clerigo':
                print(f'Turno del {self.pj_turno.name}')
            print('\n')
                            
            self.estadisticas()
            
            self.enemigo_estadisticas()
        
            print('\n')
            for key in menu_combate.keys():
                print(key,'--',menu_combate[key])
            print('\n')

            try:
                option_combate = int(input('Opción: '))
                if option_combate == 1:
                    
                    habilidades_disponibles = self.pj_turno.habilidades

                    print('\n')
                    for a, habilidad in enumerate(habilidades_disponibles):
                        print(f"{a + 1}: {habilidad.nombre} -- {habilidad.descripcion}")
                    print('\n')

                    self.habilidad_seleccionada = int(input('Opción: '))
                    self.habilidad_seleccionada = habilidades_disponibles[self.habilidad_seleccionada - 1]

                    if self.habilidad_seleccionada.tipo == 'target':

                        enemigo_atacado = int(input('Selecciona el enemigo al que quieres atacar: '))

                        if enemigo_atacado < 1 or enemigo_atacado > len(self.enemigos):
                            print('Enemigo no valido')
                            continue

                        enemigo_atacado = self.enemigos[enemigo_atacado - 1]

                        if self.pj_turno and enemigo_atacado:
                            print('\n')
                            if isinstance(self.habilidad_seleccionada, Embestida):
                                self.habilidad_seleccionada.usar(self.pj_turno, enemigo_atacado)

                            if isinstance(self.habilidad_seleccionada, ManoDeLaDivinidad):
                                self.habilidad_seleccionada.usar(self.pj_turno, enemigo_atacado)

                            if isinstance(self.habilidad_seleccionada, MaldicionDeLasSombras):
                                self.habilidad_seleccionada.usar(self.pj_turno, enemigo_atacado)
                                self.enemigo_afectado_maldicion_de_las_sombras.append(enemigo_atacado)
                                self.brujo_maldicion_de_las_sombras = True

                            if isinstance(self.habilidad_seleccionada, PactoDemoniaco):
                                self.habilidad_seleccionada.usar(self.pj_turno, enemigo_atacado)

                        vida_ini = enemigo_atacado.max_vida
                        self.personaje_ataca(self.pj_turno,enemigo_atacado,vida_ini)
                        self.check_enemigo_vida(self.pj_turno, enemigo_atacado)
                        personaje_atacado = self.enemigo_ataca(self.pj_turno)
                        if personaje_atacado:
                            self.check_personaje_vida(personaje_atacado)
                        else:
                            break

                    elif self.habilidad_seleccionada.tipo == 'aoe':
                        if isinstance(self.habilidad_seleccionada, TormentaDeAcero):
                            for enemigo in self.enemigos:
                                self.habilidad_seleccionada.usar(self.pj_turno, enemigo)
                                vida_ini = enemigo.max_vida
                                self.personaje_ataca(self.pj_turno,enemigo,vida_ini)
                                self.check_enemigo_vida(self.pj_turno, enemigo)

                        if isinstance(self.habilidad_seleccionada, ChoqueDivino):
                            for enemigo in self.enemigos:
                                self.habilidad_seleccionada.usar(self.pj_turno, enemigo)
                                vida_ini = enemigo.max_vida
                                self.personaje_ataca(self.pj_turno,enemigo,vida_ini)
                                self.check_enemigo_vida(self.pj_turno, enemigo)

                        if isinstance(self.habilidad_seleccionada, TormentaDeLasSombras):
                            for enemigo in range(len(self.enemigos)):
                                self.habilidad_seleccionada.usar(self.pj_turno, self.enemigos[enemigo])
                                self.enemigo_afectado_tormenta_de_las_sombras.append(self.enemigos[enemigo])
                                vida_ini = self.enemigos[enemigo].max_vida
                                self.personaje_ataca(self.pj_turno,self.enemigos[enemigo],vida_ini)
                                self.check_enemigo_vida(self.pj_turno, self.enemigos[enemigo])
                            self.brujo_tormenta_de_las_sombras = True

                        personaje_atacado = self.enemigo_ataca(self.pj_turno)
                        if personaje_atacado:
                            self.check_personaje_vida(personaje_atacado)
                        else:
                            break

                    elif self.habilidad_seleccionada.tipo == 'bufo':
                        if isinstance(self.habilidad_seleccionada, GritoDeGuerra):
                            fuerza = self.habilidad_seleccionada.usar(self.pj_turno)
                            self.berserker_fuerza_usada = True
                            self.berserker_fuerza = fuerza

                        if isinstance(self.habilidad_seleccionada, PorLaSangre):
                            prob_crit = self.habilidad_seleccionada.usar(self.pj_turno)
                            self.berserker_pro_crit_usado = True
                            self.berserker_pro_crit = prob_crit

                        if isinstance(self.habilidad_seleccionada, AreaBendita):
                            for i in range(len(self.personajes)):
                                aumento_vida = self.habilidad_seleccionada.usar(self.pj_turno,self.personajes[i])
                                print(f"{self.personajes[i].name} ha sido curado por {aumento_vida} puntos de vida.")
                        
                        if isinstance(self.habilidad_seleccionada, PurgaCelestial):
                            for i in range(len(self.personajes)):
                                aumento_vida = self.habilidad_seleccionada.usar(self.pj_turno,self.personajes[i])
                                print(f"{self.personajes[i].name} ha sido curado por {aumento_vida} puntos de vida.")
                            self.personajes_afectados_por_condicion.clear()

                        personaje_atacado = self.enemigo_ataca(self.pj_turno)
                        if personaje_atacado:
                            self.check_personaje_vida(personaje_atacado)
                        else:
                            break
                 
                    elif self.habilidad_seleccionada.tipo == 'bufo_aliado':
                        if isinstance(self.habilidad_seleccionada, SanacionDivina):
                            print('\n')
                            for pj in range(len(self.personajes)):
                                print(f"{pj + 1}. {self.personajes[pj].name}")
                            opcion = int(input('Opción: '))
                            personaje = self.personajes[opcion - 1]
                            aumento_vida = self.habilidad_seleccionada.usar(self.pj_turno,personaje)
                            print(f"{personaje.name} ha sido curado por {aumento_vida} puntos de vida.")

                        if isinstance(self.habilidad_seleccionada, ResurreccionDivina):
                            print('\n')
                            if self.clerigo_resucitar == True:
                                for pj_eliminado in range(len(self.personajes_eliminados)):
                                    print(f"{pj_eliminado + 1}. {self.personajes_eliminados[pj_eliminado].name}")
                                opcion = int(input('Opción: '))
                                personaje = self.personajes_eliminados[opcion - 1]
                                self.personajes_eliminados.remove(personaje)
                                self.personajes.append(personaje)
                                self.habilidad_seleccionada.usar(personaje)
                                print(f"{personaje.name} ha sido reanimado.")
                                self.clerigo_resucitar = False
                            else:
                                print(f'{self.pj_turno.name} no es capaz de canalizar tanta energía.')

                        if isinstance(self.habilidad_seleccionada, BendicionCurativa):
                            print('\n')
                            if len(self.personajes_afectados_por_condicion) != 0:
                                for pj in range(len(self.personajes_afectados_por_condicion)):
                                    print(f"{pj + 1}. {self.personajes_afectados_por_condicion[pj].name}")
                                opcion = int(input('Opción: '))
                                personaje = self.personajes_afectados_por_condicion[opcion - 1]
                                aumento_vida = self.habilidad_seleccionada.usar(personaje)
                                print(f"{personaje.name} ha sido curado con {aumento_vida} puntos de vida.")
                                if personaje in self.personajes_afectados_por_condicion:
                                    self.personajes_afectados_por_condicion.remove(personaje)
                            else:
                                print('\n')
                                print('No hay aliados afectados')
                                print('\n')
                        
                        if isinstance(self.habilidad_seleccionada, EscudoDivino):
                            print('\n')
                            for pj in range(len(self.personajes)):
                                print(f"{pj + 1}. {self.personajes[pj].name}")
                            opcion = int(input('Opción: '))
                            personaje = self.personajes[opcion - 1]
                            resistencia_condicion = self.habilidad_seleccionada.usar(personaje)
                            self.personaje_resistencia_condicion_aumentada = True
                            self.resistencia_condicion_personaje = resistencia_condicion
                            self.perosonajes_aumentados_resistencia_condicion.append(personaje)
                            

                        personaje_atacado = self.enemigo_ataca(self.pj_turno)
                        if personaje_atacado:
                            self.check_personaje_vida(personaje_atacado)
                        else:
                            break

                elif option_combate == 2:
                    pociones_disponibles = []
                    items_from_db = select_items_into_db(self.nombre_equipo)
                    for item_data in items_from_db:
                        item_type = item_data['tipo_item']
                        if item_type == 'poti':
                            item_name = item_data['nombre_item']
                            item_quantity = item_data['cantidad_item']
                            if item_name == 'Pocion Pequeña':
                                pocion = PocionPequena()
                            elif item_name == 'Pocion Mediana':
                                pocion = PocionMediana()
                            elif item_name == 'Pocion Grande':
                                pocion = PocionGrande()
                            pociones_disponibles.append((pocion, item_quantity))

                    if any(quantity > 0 for _, quantity in pociones_disponibles):
                        self.usar_objeto()
                    else:
                        print("No tienes pociones disponibles.")
                    
                    personaje_atacado = self.enemigo_ataca(self.pj_turno)
                    if personaje_atacado:
                        self.check_personaje_vida(personaje_atacado)
                    else:
                        break

                else:
                    print('')

            except(ValueError):
                KeyboardInterrupt
    
    def check_condiciones_a_enemigos(self):
        habilidades_seleccionadas = []

        if self.brujo_maldicion_de_las_sombras:
            habilidades_seleccionadas.append(MaldicionDeLasSombras())
        
        if self.brujo_tormenta_de_las_sombras:
            habilidades_seleccionadas.append(TormentaDeLasSombras())
        
        for habilidad in habilidades_seleccionadas:
            for enemigo_maldicion in range(len(self.enemigo_afectado_maldicion_de_las_sombras)):
                if hasattr(habilidad, 'aplicar_condicion'):
                    dano_condicion = habilidad.aplicar_condicion(self.pj_turno, self.enemigo_afectado_maldicion_de_las_sombras[enemigo_maldicion])
                    maldicion_de_las_sombras(self.enemigo_afectado_maldicion_de_las_sombras[enemigo_maldicion].name, dano_condicion)
            
            for enemigo_tormenta in range(len(self.enemigo_afectado_tormenta_de_las_sombras)):
                if hasattr(habilidad, 'aplicar_condicion'):
                    dano_condicion = habilidad.aplicar_condicion(self.pj_turno, self.enemigo_afectado_tormenta_de_las_sombras[enemigo_tormenta])
                    tormenta_de_las_sombras(self.enemigo_afectado_tormenta_de_las_sombras[enemigo_tormenta].name, dano_condicion)
    
    def check_condicion_a_personajes(self):
        for personaje in self.personajes_afectados_por_condicion:
            dano_condicion = self.enemigo_turno.habilidad_enemigo.usar(self.enemigo_turno, personaje)
            if dano_condicion is None:
                dano_condicion = 0
            enemigo_habilidad(personaje.name,dano_condicion)
            

    def enemigo_ataca(self, personaje_atacado):
        enemigo_turno = random.choice(self.enemigos)
        personaje_atacado = random.choice(self.personajes)
        enemigo_ataca_a_personaje(personaje_atacado.name,enemigo_turno.name)
        vida_ini = personaje_atacado.vida
        daño = randint(enemigo_turno.fuerza - (enemigo_turno.fuerza * 0.8), enemigo_turno.fuerza)
        personaje_atacado.vida = personaje_atacado.vida - (daño)
        vida_fin = personaje_atacado.vida
        personaje_recibe_daño(personaje_atacado.name,vida_fin-vida_ini)
        if personaje_atacado.vida >= 0:
            vida_restante_personaje(personaje_atacado.name,vida_fin)
        afectado = enemigo_turno.usar_habilidad_enemigo(personaje_atacado)
        if afectado and personaje_atacado.name not in self.personajes_afectados_por_condicion:
            self.personajes_afectados_por_condicion.append(personaje_atacado)
        self.enemigo_turno = enemigo_turno
        return personaje_atacado

    def personaje_ataca(self, personaje, enemigo, vida_ini):
        personaje_ataca_a_enemigo(personaje.name,enemigo.name)
        vida_fin = enemigo.vida
        enemigo_recibe_daño(enemigo.name,vida_fin-vida_ini)
        if enemigo.vida >= 0:
            vida_restante_enemigo(enemigo.name,vida_fin)
        return enemigo
    
    def check_enemigo_vida(self, personaje, enemigo_atacado):
        if enemigo_atacado:
            if enemigo_atacado.vida <= 0:
                enemigo_eliminado(enemigo_atacado)
                personaje.experiencia += enemigo_atacado.experiencia
                self.oro_total += enemigo_atacado.oro
                self.enemigos_eliminados.append(enemigo_atacado)
                self.enemigos.remove(enemigo_atacado)
                if enemigo_atacado in self.enemigo_afectado_maldicion_de_las_sombras:
                    self.enemigo_afectado_maldicion_de_las_sombras.remove(enemigo_atacado)
                elif enemigo_atacado in self.enemigo_afectado_tormenta_de_las_sombras:
                    self.enemigo_afectado_tormenta_de_las_sombras.remove(enemigo_atacado)

        if len(self.enemigos) == 0:
            update_misiones(self.nombre_equipo,self.mision_name,0)
            self.misiones_por_hacer.clear()
            self.personajes_afectados_por_condicion.clear()
            self.agregar_personajes()
            self.termina_juego()
            self.check_experiencia()
            self.check_nivel()
            self.ciudad()

    def check_personaje_vida(self, personaje_atacado):
        if personaje_atacado:
            if personaje_atacado.vida <= 0:
                personaje_eliminado(personaje_atacado)
                self.personajes_eliminados.append(personaje_atacado)
                self.personajes.remove(personaje_atacado)
                if personaje_atacado in range(len(self.personajes_afectados_por_condicion)):
                    self.personajes.remove(self.personajes_afectados_por_condicion[personaje_atacado])
            
        if len(self.personajes) == 0:
            self.personajes_afectados_por_condicion.clear()
            has_muerto()
            self.agregar_personajes()
            self.termina_juego()
            self.agregar_enemigos()
            self.restaurar_vidas()
            self.ciudad()
    
    def termina_juego(self):
        for i in range(len(self.personajes)):
            if self.personajes[i].clase == 'Berserker':
                if self.berserker_fuerza_usada == True:
                    self.personajes[i].fuerza -= self.berserker_fuerza
                    self.berserker_fuerza_usada = False
                if self.berserker_pro_crit_usado == True:
                    self.personajes[i].arma.prob_critico -= self.berserker_pro_crit
                    self.berserker_pro_crit_usado = False
        for a in range(len(self.perosonajes_aumentados_resistencia_condicion)):
            if self.personaje_resistencia_condicion_aumentada == True:
                self.perosonajes_aumentados_resistencia_condicion[a].resistencia_condicion -= self.resistencia_condicion_personaje
                self.perosonajes_aumentados_resistencia_condicion.remove(self.perosonajes_aumentados_resistencia_condicion[a])
                self.personaje_resistencia_condicion_aumentada = False

        self.clerigo_resucitar = True
    
    def agregar_enemigos(self):
        for enemigo in self.enemigos_eliminados:
            self.enemigos.append(enemigo)
        self.enemigos_eliminados.clear()
        
    def agregar_personajes(self):
        for personaje in self.personajes_eliminados:
            if personaje.clase == 'Berserker':
                self.personajes.insert(0, personaje)
            elif personaje.clase == 'Paladin':
                self.personajes.insert(1, personaje)
            elif personaje.clase == 'Brujo':
                self.personajes.insert(2, personaje)
            elif personaje.clase == 'Clerigo':
                self.personajes.insert(3, personaje)
        self.personajes_eliminados.clear()
    
    def restaurar_vidas(self):
        for p in range(len(self.personajes)):
            self.personajes[p].vida = self.personajes[p].max_vida
        
        for e in range(len(self.enemigos)):
            self.enemigos[e].vida = self.enemigos[e].max_vida
    
    def check_experiencia(self):
        for i in range(len(self.personajes)):
            self.personajes[i].experiencia += self.experiencia_mision
        self.oro_total += self.oro_mision
        update_items(self.nombre_equipo,'moneda','oro',self.oro_total) 
    
    def check_nivel(self):
        for i in range(len(self.personajes)):
            while self.personajes[i].experiencia >= self.personajes[i].max_experiencia:
                self.personajes[i].nivel += 1
                self.personajes[i].experiencia -= self.personajes[i].max_experiencia
                self.personajes[i].max_experiencia += self.personajes[i].max_experiencia
                self.lvl_up(self.personajes[i])
            
                self.actualizar_personajes()
    
    def lvl_up(self, personaje):

        puntos_restantes = 5

        while puntos_restantes > 0:

            def lvl_option_berserker(puntos_restantes):
                try:
                    lvl_up_option = int(input('Opción: '))
                    if lvl_up_option == 1:
                        personaje.max_vida += 10
                        puntos_restantes -= 1

                    elif lvl_up_option == 2:
                        personaje.resistencia += 1
                        puntos_restantes -= 1

                    elif lvl_up_option == 3:
                        personaje.fuerza += 1
                        puntos_restantes -= 1

                    else:
                        print('')
                    
                    return puntos_restantes
                
                except(ValueError):
                    KeyboardInterrupt

            def lvl_option_paladin(puntos_restantes):
                try:
                    lvl_up_option = int(input('Opción: '))
                    if lvl_up_option == 1:
                        personaje.max_vida += 10
                        puntos_restantes -= 1

                    elif lvl_up_option == 2:
                        personaje.resistencia += 1
                        puntos_restantes -= 1

                    elif lvl_up_option == 3:
                        personaje.fuerza += 1
                        puntos_restantes -= 1

                    elif lvl_up_option == 4:
                        personaje.curacion += 1
                        puntos_restantes -= 1

                    elif lvl_up_option == 5:
                        personaje.resistencia_condicion += 1
                        puntos_restantes -= 1

                    else:
                        print('')
                    
                    return puntos_restantes
                
                except(ValueError):
                    KeyboardInterrupt

            def lvl_option_clerigo(puntos_restantes):
                try:
                    lvl_up_option = int(input('Opción: '))
                    if lvl_up_option == 1:
                        personaje.max_vida += 10
                        puntos_restantes -= 1

                    elif lvl_up_option == 2:
                        personaje.resistencia += 1
                        puntos_restantes -= 1

                    elif lvl_up_option == 3:
                        personaje.fuerza += 1
                        puntos_restantes -= 1

                    elif lvl_up_option == 4:
                        personaje.curacion += 1
                        puntos_restantes -= 1

                    elif lvl_up_option == 5:
                        personaje.resistencia_condicion += 1
                        puntos_restantes -= 1

                    else:
                        print('')

                    return puntos_restantes
                
                except(ValueError):
                    KeyboardInterrupt

            def lvl_option_brujo(puntos_restantes):
                try:
                    lvl_up_option = int(input('Opción: '))
                    if lvl_up_option == 1:
                        personaje.max_vida += 10
                        puntos_restantes -= 1

                    elif lvl_up_option == 2:
                        personaje.resistencia += 1
                        puntos_restantes -= 1

                    elif lvl_up_option == 3:
                        personaje.dano_condicion += 1
                        puntos_restantes -= 1

                    elif lvl_up_option == 4:
                        personaje.curacion += 1
                        puntos_restantes -= 1

                    elif lvl_up_option == 5:
                        personaje.resistencia_condicion += 1
                        puntos_restantes -= 1

                    else:
                        print('')

                    return puntos_restantes
                
                except(ValueError):
                    KeyboardInterrupt
            
            print(f'{personaje.name} puede subir de nivel')
            lvl_up_berserker = {1:'Vida',2:'Resistencia',3:'Fuerza'}
            lvl_up_paladin = {1:'Vida',2:'Resistencia',3:'Fuerza',4:'Curacion',5:'Resistencia condicion'}
            lvl_up_clerigo = {1:'Vida',2:'Resistencia',3:'Fuerza',4:'Curacion',5:'Resistencia condicion'}
            lvl_up_brujo = {1:'Vida',2:'Resistencia',3:'Daño condicion',4:'Fuerza',5:'Resistencia condicion'}
            
            
            print(f'Tienes {puntos_restantes} por incrementar.')

            if personaje.clase == 'Berserker':
                print('\n')
                for key in lvl_up_berserker.keys():
                    print(key,'--',lvl_up_berserker[key])
                print('\n')
                puntos_restantes = lvl_option_berserker(puntos_restantes)

            elif personaje.clase == 'Paladin':
                print('\n')
                for key in lvl_up_paladin.keys():
                    print(key,'--',lvl_up_paladin[key])
                print('\n')
                puntos_restantes = lvl_option_paladin(puntos_restantes)

            elif personaje.clase == 'Clerigo':
                print('\n')
                for key in lvl_up_clerigo.keys():
                    print(key,'--',lvl_up_clerigo[key])
                print('\n')
                puntos_restantes = lvl_option_clerigo(puntos_restantes)

            elif personaje.clase == 'Brujo':
                print('\n')
                for key in lvl_up_brujo.keys():
                    print(key,'--',lvl_up_brujo[key])
                print('\n')
                puntos_restantes = lvl_option_brujo(puntos_restantes)
        
        self.actualizar_personajes()
    
    def actualizar_personajes(self):

        self.restaurar_vidas()
 
        for i in range(len(self.personajes)):
            update_stats_in_db(self.nombre_equipo,self.personajes[i].clase,self.personajes[i].name,
                        self.personajes[i].nivel,self.personajes[i].vida,self.personajes[i].resistencia, self.personajes[i].dano_condicion,
                        self.personajes[i].fuerza,self.personajes[i].curacion,self.personajes[i].resistencia_condicion,self.personajes[i].experiencia,self.personajes[i].max_experiencia)


    def print_all_items(self,cls):
        return cls.__subclasses__()

    def mercader(self):
        print('\n')

        i = 0
        print("{:<4} {:<20} {:<15} {:<6}".format("", "Nombre", "Curacion", "Precio"))
        items_list = []
        for items in self.print_all_items(Items):
            items_list.append(items)
            items_instance = items()
            items_values = [i+1, items_instance.name, "+{} hp".format(items_instance.curacion), "{} oro".format(items_instance.precio)]
            print("{:<4} {:<20} {:<15} {:<6}".format(*items_values))
            i += 1
        
        print('\n')
        comprar = input("¿Quieres comprar un item? (y/n): ")
        print('\n')
        while comprar.lower() == 'y':
            item_comprado = int(input("Selecciona el item (1-{}): ".format(len(items_list))))
            if item_comprado >= 1 and item_comprado <= len(items_list):
                selected_item = items_list[item_comprado - 1]
                item_instance = selected_item()
                if self.oro_total >= item_instance.precio:
                    self.oro_total -= item_instance.precio
                    print("Has comprado el item: {}".format(item_instance.name))
                    print("Oro restante: {}".format(self.oro_total))
                    if item_comprado == 1:
                        self.potis_pequenas_hp += 1
                        update_items(self.nombre_equipo, 'poti', item_instance.name, self.potis_pequenas_hp)
                    if item_comprado == 2:
                        self.potis_medianas_hp += 1
                        update_items(self.nombre_equipo, 'poti', item_instance.name, self.potis_medianas_hp)
                    if item_comprado == 3:
                        self.potis_grandes_hp += 1
                        update_items(self.nombre_equipo, 'poti', item_instance.name, self.potis_grandes_hp)
                    update_items(self.nombre_equipo,'moneda','oro',self.oro_total)
                else:
                    print("No tienes suficiente oro para comprar este item.")
            else:
                print("Opción inválida.")
            

            comprar = input("¿Quieres comprar otro item? (y/n): ")

        print("No has comprado ningún item.")

    
    def inventariado(self):
        items = select_items_into_db(self.nombre_equipo)
        print('\n')

        if len(items) == 0:
            print("No hay items en el inventario.")
        else:
            print("{:<20} {:<10} {:<10}".format("Nombre", "Tipo", "Cantidad"))
            for item in items:
                nombre_item = item['nombre_item']
                tipo_item = item['tipo_item']
                cantidad_item = item['cantidad_item']
                print("{:<20} {:<10} {:<10}".format(nombre_item, tipo_item, cantidad_item))


    def print_all_misions(self, cls, valor_mision):
        return [m for m in cls.__subclasses__() if m().valor_mision == valor_mision]

    def setup_misiones(self):
        print('\n')
        print("{:<4} {:<50} {:<20} {:<20}".format("", "Mision", "Experiencia", "Oro"))

        misiones = select_misiones(self.nombre_equipo)
        misiones_lista = [r[0] for r in misiones]
        misiones_disponibles = self.print_all_misions(Misiones, 1)

        num_mision = 1

        for m in misiones_disponibles:
            m_instance = m()
            if m_instance.mision_name in misiones_lista:
                m_values = [num_mision, m_instance.mision_name, m_instance.experiencia_mision, m_instance.oro_mision]
                print("{:<4} {:<50} {:<20} {:<20}".format(*m_values))
                self.misiones_por_hacer.append(m_instance)
                num_mision += 1

        print('\n')

        while True:
            try:
                opcion = int(input("Opcion: "))
                if opcion < 1 or opcion > len(self.misiones_por_hacer):
                    raise ValueError
                break
            except ValueError:
                print("Debes ingresar un número válido para seleccionar la misión.")

        selected_mision = self.misiones_por_hacer[opcion-1]
        self.mision_name = selected_mision.mision_name
        self.enemigos = selected_mision.enemigos
        self.experiencia_mision = selected_mision.experiencia_mision
        self.oro_mision = selected_mision.oro_mision

    def usar_objeto(self):
        print('\n')
        pociones_disponibles = []
        items_from_db = select_items_into_db(self.nombre_equipo)
        for item_data in items_from_db:
            item_type = item_data['tipo_item']
            if item_type == 'poti':
                item_name = item_data['nombre_item']
                item_quantity = item_data['cantidad_item']
                if item_name == 'Pocion Pequeña':
                    pocion = PocionPequena()
                elif item_name == 'Pocion Mediana':
                    pocion = PocionMediana()
                elif item_name == 'Pocion Grande':
                    pocion = PocionGrande()
                if item_quantity > 0:
                    pociones_disponibles.append((pocion, item_quantity))

        if len(pociones_disponibles) == 0:
            print("No tienes pociones disponibles.")
            return
        else:
            print("Pociones disponibles:")
            print('\n')
            for i, (item_name, item_quantity) in enumerate(pociones_disponibles, start=1):
                print(f"{i}. {item_name.name} - Cantidad: {item_quantity}")

            print('\n')
            choice = input("Selecciona una poción para usar: ")
            print('\n')
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(pociones_disponibles):
                    selected_potion = pociones_disponibles[choice - 1]
                    selected_potion_object, potion_quantity = selected_potion

                    for i, personaje in enumerate(self.personajes, start=1):
                        print(f"{i}. {personaje.name}")
                    
                    print('\n')
                    choice = input("Selecciona un personaje para aplicar la poción: ")
                    print('\n')
                    if choice.isdigit():
                        choice = int(choice)
                        if 1 <= choice <= len(self.personajes):
                            selected_personaje = self.personajes[choice - 1]

                            if selected_personaje.max_vida < (selected_personaje.vida + selected_potion_object.curacion):
                                selected_personaje.vida = selected_personaje.max_vida
                            else:
                                selected_personaje.vida += selected_potion_object.curacion
                            
                            nueva_cantidad = potion_quantity - 1
                            if nueva_cantidad < 0:
                                nueva_cantidad = 0
                            update_items(self.nombre_equipo, 'poti', selected_potion_object.name, nueva_cantidad)
                            print(f"Has usado una poción {selected_potion_object.name} y aumentado la vida de {selected_personaje.name} en {selected_personaje.vida}.")

                        else:
                            print("Opción inválida. Inténtalo de nuevo.")
                    else:
                        print("Opción inválida. Inténtalo de nuevo.")
                else:
                    print("Opción inválida. Inténtalo de nuevo.")
            else:
                print("Opción inválida. Inténtalo de nuevo.")