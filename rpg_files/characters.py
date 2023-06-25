from rpg_files.armas import *
import random

class Character():
    
    def __init__(self,name,clase,nivel,vida,resistencia,dano_condicion,fuerza,curacion,resistencia_condicion,experiencia,max_experiencia,arma,habilidades) -> None:
        self.name = name
        self.clase = clase
        self.nivel = nivel
        self.vida = vida
        self.max_vida = vida
        self.resistencia = resistencia
        self.dano_condicion = dano_condicion
        self.fuerza = fuerza
        self.curacion = curacion
        self.resistencia_condicion = resistencia_condicion
        self.experiencia = experiencia
        self.max_experiencia = max_experiencia
        self.arma = arma
        self.habilidades = habilidades


    def stats(self, i):

        print("{:<10} {:<20} {:<20} {:<6} {:<6} {:<14} {:<18} {:<10} {:<10} {:<25} {:<20} {:<20}".format(i+1, self.clase, self.name, self.nivel, self.vida, self.resistencia, self.dano_condicion, self.fuerza, self.curacion, self.resistencia_condicion ,self.experiencia, self.max_experiencia))


class Berserker(Character):
    def __init__(self) -> None:
        super().__init__(None,'Berserker',1,200,25,0,45,0,0,0,1000,HachaRota(),habilidades = [Embestida(),TormentaDeAcero(),GritoDeGuerra(),PorLaSangre()])
    
class Paladin(Character):
    def __init__(self) -> None:
        super().__init__(None,'Paladin',1,400,20,0,20,20,20,0,1000,EspadaRota(),habilidades = [ChoqueDivino(),PurgaCelestial(),BendicionCurativa(),EscudoDivino()])

class Clerigo(Character):
    def __init__(self) -> None:
        super().__init__(None,'Clerigo',1,200,20,0,5,60,10,0,1000,BastonQuebrado(),habilidades = [ManoDeLaDivinidad(),SanacionDivina(),AreaBendita(),ResurreccionDivina()])

class Brujo(Character):
    def __init__(self) -> None:
        super().__init__(None,'Brujo',1,200,10,60,5,0,40,0,1000,Guadaña(),habilidades = [MaldicionDeLasSombras(),PactoDemoniaco(),TormentaDeLasSombras(),SombraPenetrante()])




class Habilidad():

    def __init__(self,nombre,descripcion,tipo) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo

#Berserker
class Embestida(Habilidad):
    def __init__(self) -> None:
        super().__init__('Embestida', 'El guerrero corre hacia su objetivo con gran velocidad y lo golpea con un fuerte golpe.','target')
    
    def usar(self, personaje, enemigo):
        dano = personaje.fuerza + personaje.arma.dano_base
        prob_critico = personaje.arma.prob_critico
        if random.random() < (prob_critico / 100.0):
            dano *= 2
        dano -= enemigo.defensa
        dano = max(dano, 0)
        enemigo.vida -= dano
        return dano

class TormentaDeAcero(Habilidad):
    def __init__(self) -> None:
        super().__init__('Tormenta de Acero', 'El guerrero realiza una serie de golpes rápidos con su arma, infligiendo daño a todos los enemigos en un área alrededor de él.','aoe')

    def usar(self, personaje, enemigo):
        dano = (personaje.fuerza + personaje.arma.dano_base) / 4
        prob_critico = personaje.arma.prob_critico
        if random.random() < (prob_critico / 100.0):
            dano *= 2
        dano = dano
        dano -= enemigo.defensa
        dano = max(dano, 0)
        enemigo.vida -= dano
        return dano

class  GritoDeGuerra(Habilidad):
    def __init__(self) -> None:
        super().__init__('Grito de Guerra', 'El guerrero emite un fuerte grito de guerra, aumentando su fuerza.','bufo')

    def usar(self, personaje):
        fuerza = 10
        personaje.fuerza += fuerza
        return fuerza

class PorLaSangre(Habilidad):
    def __init__(self) -> None:
        super().__init__('Por la Sangre', 'El guerrero imbuye su arma en sangre aumentando su probabilidad critica.','bufo')

    def usar(self, personaje):
        prob_critico = 5
        personaje.arma.prob_critico += prob_critico
        return prob_critico

#Paladin
class ChoqueDivino(Habilidad):
    def __init__(self) -> None:
        super().__init__('Choque Divino', 'El paladín carga hacia sus enemigos con su arma sagrada en alto, infligiendo daño a todos los enemigos en su camino y reduciendo su defensa.','aoe') 

    def usar(self, personaje, enemigo):
        dano = (personaje.fuerza + personaje.arma.dano_base) / 4
        prob_critico = personaje.arma.prob_critico
        if random.random() < (prob_critico / 100.0):
            dano *= 2
        dano -= enemigo.defensa
        dano = max(dano, 0)
        enemigo.vida -= dano
        defensa = 10
        enemigo.defensa -= defensa
        return dano, defensa

class PurgaCelestial(Habilidad):
    def __init__(self) -> None:
        super().__init__('Purga Celestial', 'El paladín invoca una purga celestial que limpia todas las condiciones negativas en un área.','bufo') 
    
    def usar(self, paladin ,personaje):
        aumento = int(paladin.curacion * 1.5)
        if personaje.vida + aumento > personaje.max_vida:
            aumento = personaje.max_vida - personaje.vida
        personaje.vida += aumento
        return aumento

class BendicionCurativa(Habilidad):
    def __init__(self) -> None:
        super().__init__('Bendicion Curativa', 'El paladín bendice a un aliado con energías curativas, eliminando todas las condiciones negativas que lo afectan y restaurando su vitalidad.','bufo_aliado') 

    def usar(self, personaje):
        personaje.vida = personaje.max_vida
        return personaje.vida
    
class EscudoDivino(Habilidad):
    def __init__(self) -> None:
        super().__init__('Escudo Divino', 'El paladín infunde un escudo divino en un aliado, fortaleciendo su resistencia a las condiciones negativas.','bufo_aliado') 
    
    def usar(self, personaje):
        resistencia_condicion = 20
        personaje.resistencia_condicion += resistencia_condicion
        return resistencia_condicion

    
#Clerigo
class ManoDeLaDivinidad(Habilidad):
    def __init__(self) -> None:
        super().__init__('Mano de la Divinidad', 'El clérigo canaliza la energía sagrada a través de sus manos, liberando una explosión de luz purificadora que causa un daño significativo a los enemigos.','target')
    
    def usar(self, personaje, enemigo):
        dano = personaje.fuerza + personaje.arma.dano_base
        prob_critico = personaje.arma.prob_critico
        if random.random() < (prob_critico / 100.0):
            dano *= 2
        dano -= enemigo.defensa
        dano = max(dano, 0)
        enemigo.vida -= dano
        return dano

class SanacionDivina(Habilidad):
    def __init__(self) -> None:
        super().__init__('Sanacion Divina', 'El clérigo canaliza energía sagrada para curar a un aliado herido.','bufo_aliado')

    def usar(self, clerigo ,personaje):
        aumento = int(clerigo.curacion * 2.5)
        if personaje.vida + aumento > personaje.max_vida:
            aumento = personaje.max_vida - personaje.vida
        personaje.vida += aumento
        return aumento

class AreaBendita(Habilidad):
    def __init__(self) -> None:
        super().__init__('Area Bendita', 'El clérigo canaliza energía creando un area bajo los personajes para curarles.','bufo')

    def usar(self, clerigo ,personaje):
        aumento = int(clerigo.curacion * 1.5)
        if personaje.vida + aumento > personaje.max_vida:
            aumento = personaje.max_vida - personaje.vida
        personaje.vida += aumento
        return aumento

class ResurreccionDivina(Habilidad):
    def __init__(self) -> None:
        super().__init__('Resurreccion Divina', 'El clérigo convoca el poder divino para revivir a un aliado caído en combate.','bufo_aliado')

    def usar(self, personaje_eliminado):
        personaje_eliminado.vida = personaje_eliminado.max_vida

#Brujo
class MaldicionDeLasSombras(Habilidad):
    def __init__(self) -> None:
        super().__init__('Maldicion de las Sombras', 'El brujo maldice a un enemigo con una sombra oscura, infligiendo daño de sombras por cada turno.','target')

    def usar(self, personaje, enemigo):
        dano_inicial = personaje.fuerza + personaje.dano_condicion
        dano_inicial -= enemigo.defensa
        dano_inicial = max(dano_inicial, 0)
        enemigo.vida -= dano_inicial
        return dano_inicial

    def aplicar_condicion(self, personaje, enemigo):
        personaje = Brujo()
        dano_condicion = personaje.dano_condicion
        enemigo.vida -= dano_condicion
        return dano_condicion

class PactoDemoniaco(Habilidad):
    def __init__(self) -> None:
        super().__init__('Pacto Demoniaco', 'El brujo invoca a un demonio aliado que ataca a los enemigos y drena su vida.','target')

    def usar(self, personaje, enemigo):
        dano_inicial = personaje.fuerza + personaje.dano_condicion
        dano_inicial -= enemigo.defensa
        dano_inicial = max(dano_inicial, 0)
        enemigo.vida -= dano_inicial
        personaje.vida += dano_inicial
        return dano_inicial

class TormentaDeLasSombras(Habilidad):
    def __init__(self) -> None:
        super().__init__('Tormenta de las Sombras', 'El brujo desata una oscura tormenta de sombras que afecta a todos los enemigos cercanos.','aoe')

    def usar(self, personaje, enemigo):
        dano_inicial = personaje.fuerza + personaje.dano_condicion
        dano_inicial -= enemigo.defensa
        dano_inicial = max(dano_inicial, 0)
        enemigo.vida -= dano_inicial
        return dano_inicial

    def aplicar_condicion(self, personaje, enemigo):
        personaje = Brujo()
        dano_condicion = personaje.dano_condicion
        enemigo.vida -= dano_condicion
        return dano_condicion

class SombraPenetrante(Habilidad):
    def __init__(self) -> None:
        super().__init__('Sombra Penetrante', 'El brujo concentra su energía sombría en su arma y realiza un poderoso golpe que aprovecha su habilidad crítica.','target')