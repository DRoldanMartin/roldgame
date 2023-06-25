import random
from rpg_files.msg import *

class Habilidad:
    def __init__(self, nombre, descripcion, objetivo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetivo = objetivo

    def usar(self, atacante, objetivo):
        if random.random() < 0.5:
            dano = atacante.dano_condicion - objetivo.resistencia_condicion
            objetivo.vida -= dano
            #enemigo_habilidad(objetivo.name,atacante.dano_condicion)
            return dano


class Enemies():
    def __init__(self,name,vida,fuerza,defensa,dano_condicion,experiencia,oro) -> None:
        self.name = name
        self.vida = vida
        self.max_vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
        self.dano_condicion = dano_condicion
        self.experiencia = experiencia
        self.oro = oro
        self.habilidad_enemigo = Habilidad("Habilidad Enemigo", "Una habilidad especial del enemigo", "objetivo")
    
    def stats(self, i):

        print("{:<10} {:<30} {:<20} {:<20} {:<6}".format(i+1, self.name, self.vida, self.fuerza, self.defensa))
    
    def usar_habilidad_enemigo(self, personaje):
        return self.habilidad_enemigo.usar(self, personaje)


#Enemigos mision 1
class VampiroNovato(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro novato", 50, 10, 5, 5, 20, 10)

#Enemigos mision 2 // SE REPITE ENEMIGO VampiroNovato
class VampiroAcechador(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro acechador", 80, 20, 10, 10, 40, 20)
    
#Enemigos mision 3 // SE REPITE ENEMIGO VampiroNovato y VampiroAcechador
class EspectroOscuro(Enemies):
    def __init__(self) -> None:
        super().__init__("Espectro oscuro", 120, 30, 20, 15, 60, 30)

#Enemigos mision 4
class VampiroExplorador(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro explorador", 80, 20, 10, 10, 40, 20)

class VampiroAterrador(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro aterrador", 100, 30, 20, 15, 60, 30)

class EspectroDeLaNoche(Enemies):
    def __init__(self) -> None:
        super().__init__("Espectro de la noche", 120, 35, 25, 20, 80, 40)

#Enemigos mision 5
class VampiroCazador(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro cazador", 100, 35, 20, 15, 70, 30)

class VampiroGuerrero(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro guerrero", 120, 40, 25, 20, 100, 40)

class VampiroMaestro(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro maestro", 200, 50, 35, 25, 200, 100)

#Enemigos mision 6
class GuardiaVampiro(Enemies):
    def __init__(self) -> None:
        super().__init__("Guardia vampiro", 150, 45, 30, 20, 120, 50)

class CriptaDeVampiros(Enemies):
    def __init__(self) -> None:
        super().__init__("Cripta de vampiros", 120, 40, 25, 20, 100, 40)

class JefeDeSeguridadVampirica(Enemies):
    def __init__(self) -> None:
        super().__init__("Jefe de seguridad vampírica", 200, 50, 35, 25, 200, 100)

class LiderVampirico(Enemies):
    def __init__(self) -> None:
        super().__init__("Líder vampírico", 300, 65, 50, 35, 500, 250)

#Enemigos mision 7
class TrabajadorVampiro(Enemies):
    def __init__(self) -> None:
        super().__init__("Trabajador vampiro", 180, 40, 30, 20, 140, 60)

class GuardianDeLaFabrica(Enemies):
    def __init__(self) -> None:
        super().__init__("Guardian de la fábrica", 220, 55, 40, 25, 180, 80)

class IngenieroJefeVampiro(Enemies):
    def __init__(self) -> None:
        super().__init__("Ingeniero jefe vampírico", 300, 70, 50, 35, 350, 150)

class ExperimentoFallido(Enemies):
    def __init__(self) -> None:
        super().__init__("Experimento fallido", 400, 85, 60, 45, 600, 300)

#Enemigos mision 8
class VampiroCazadorGrande(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro cazador grande", 250, 60, 40, 30, 200, 80)

class VampiroRastreador(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro rastreador", 180, 50, 35, 20, 160, 60)

class VampiroVolador(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro volador", 200, 45, 30, 25, 180, 70)

#Enemigos mision 9
class GuardiaVampiroMayor(Enemies):
    def __init__(self) -> None:
        super().__init__("Guardia vampiro mayor", 350, 70, 50, 40, 300, 120)

class VampiroHechicero(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro hechicero", 300, 65, 45, 50, 280, 100)

class LiderVampiro(Enemies):
    def __init__(self) -> None:
        super().__init__("Líder vampiro", 500, 80, 70, 60, 400, 150)

#Enemigos mision 10
class GuardianDelCastillo(Enemies):
    def __init__(self) -> None:
        super().__init__("Guardián del castillo", 500, 80, 70, 60, 500, 200)

class EspectroDelCastillo(Enemies):
    def __init__(self) -> None:
        super().__init__("Espectro del castillo", 400, 70, 50, 70, 450, 180)

class CondeDracula(Enemies):
    def __init__(self) -> None:
        super().__init__("Conde Drácula", 1000, 100, 90, 80, 1500, 300)

#Enemigos mision 11
class LadronVampiro(Enemies):
    def __init__(self) -> None:
        super().__init__("Ladrón vampiro", 300, 70, 50, 60, 300, 150)

class GuerreroVampiro(Enemies):
    def __init__(self) -> None:
        super().__init__("Guerrero vampiro", 500, 90, 70, 70, 500, 200)

class LiderVampiroAdulto(Enemies):
    def __init__(self) -> None:
        super().__init__("Líder vampiro adulto", 800, 110, 90, 80, 1000, 350)

#Enemigos mision 12
class EsbirroVampiro(Enemies):
    def __init__(self) -> None:
        super().__init__("Esbirro vampiro", 400, 80, 60, 50, 400, 200)

class VampiroCazadorAdulto(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro cazador adulto", 500, 90, 70, 70, 500, 250)

class VampiroMago(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro mago", 600, 100, 80, 90, 700, 300)

class VampiroNoble(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro noble", 800, 120, 100, 100, 1200, 450)

#Enemigos mision 13 // SE REPITO EsbirroVampiro
class VampiroGuerreroAnciano(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro guerrero anciano", 600, 110, 90, 80, 800, 350)

class VampiroSacerdote(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro sacerdote", 700, 120, 100, 100, 900, 400)

class VampiroAnciano(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro anciano", 1000, 150, 120, 150, 1500, 600)

#Enemigos mision 14 // SE REPITEN ENEMIGOS MISION 12
class VampiroSupremo(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro Supremo", 1500, 150, 130, 150, 2000, 700)

#Enemigos mision 15
class HorrorDeLasSombras(Enemies):
    def __init__(self) -> None:
        super().__init__("Horror de las sombras", 800, 100, 120, 60, 800, 250)

class MagoOscuro(Enemies):
    def __init__(self) -> None:
        super().__init__("Mago oscuro", 600, 120, 80, 140, 900, 300)

class EspectroDeLaOscuridad(Enemies):
    def __init__(self) -> None:
        super().__init__("Espectro de la oscuridad", 500, 80, 60, 150, 500, 200)

class DemonioDeLasSombras(Enemies):
    def __init__(self) -> None:
        super().__init__("Demonio de las sombras", 1000, 150, 140, 200, 1500, 500)

#Enemigos mision 16
class EsbirroVampiroAdulto(Enemies):
    def __init__(self) -> None:
        super().__init__("Esbirro vampiro adulto", 500, 90, 70, 50, 500, 250)

class VampiroAcechador(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro acechador", 600, 100, 80, 70, 600, 300)

class VampiroMagoAdulto(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro mago adulto", 700, 110, 90, 90, 800, 350)

class VampiroNobleAdulto(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro noble adulto", 900, 130, 110, 100, 1400, 500)

class ElSeñorDeLaSangre(Enemies):
    def __init__(self) -> None:
        super().__init__("El señor de la sangre", 1500, 180, 150, 150, 3000, 800)

#Enemigos mision 17
class MurcielagoGigante(Enemies):
    def __init__(self) -> None:
        super().__init__("Murciélago gigante", 400, 100, 60, 50, 500, 200)

class Gargola(Enemies):
    def __init__(self) -> None:
        super().__init__("Gárgola", 800, 150, 100, 100, 1000, 400)

class Espectro(Enemies):
    def __init__(self) -> None:
        super().__init__("Espectro", 600, 120, 80, 80, 700, 300)

class VampiroOscuro(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro oscuro", 1000, 200, 150, 150, 2000, 1000)

#Enemigos mision 18
class EspectroSanguinario(Enemies):
    def __init__(self) -> None:
        super().__init__("Espectro sanguinario", 600, 100, 80, 50, 500, 300)

class GolemDeSombra(Enemies):
    def __init__(self) -> None:
        super().__init__("Golem de sombra", 1200, 150, 120, 80, 800, 400)

class DemonioInvocado(Enemies):
    def __init__(self) -> None:
        super().__init__("Demonio invocado", 1400, 200, 150, 120, 1000, 500)

class ElCondeOscuro(Enemies):
    def __init__(self) -> None:
        super().__init__("El Conde Oscuro", 3000, 300, 250, 200, 2000, 1000)

#Enemigos mision 19
class GargolaAnciana(Enemies):
    def __init__(self) -> None:
        super().__init__("Gárgola anciana", 1200, 150, 100, 80, 1500, 600)

class MirmidonVampiro(Enemies):
    def __init__(self) -> None:
        super().__init__("Mirmidon vampiro", 1500, 180, 120, 100, 2000, 800)

class VampiroSabueso(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro sabueso", 1000, 120, 90, 70, 1200, 500)

class CondeVampiroAnciano(Enemies):
    def __init__(self) -> None:
        super().__init__("Conde Vampiro anciano", 2500, 250, 200, 200, 5000, 2000)

#Enemigos mision 20
class SeñorDeLosVampiros(Enemies):
    def __init__(self) -> None:
        super().__init__('Señor de los vampiros',5000, 400, 300, 400, 5000, 5000)

class VampiroEspectro(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro espectro", 1200, 250, 225, 200, 1200, 225)

class VampiroDragon(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro dragón", 1400, 275, 235, 210, 1400, 235)

class VampiroEspectro(Enemies):
    def __init__(self) -> None:
        super().__init__("Vampiro elemental", 1300, 270, 230, 205, 1300, 230)