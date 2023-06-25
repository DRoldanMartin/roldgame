class Weapons():
    def __init__(self,name,dano_base,prob_critico) -> None:
        self.name = name
        self.dano_base = dano_base
        self.prob_critico = prob_critico


    def stats(self):
        weapon_stats = {'Nombre:\t\t ':self.name,
                    'Daño base:\t ':self.dano_base,
                    'Prob. critico:\t ':self.prob_critico}
        
        for key in weapon_stats:
            print(key,weapon_stats[key])
        print('\n')

class HachaRota(Weapons):
    def __init__(self) -> None:
        super().__init__('Hacha Rota',450,15)

class BastonQuebrado(Weapons):
    def __init__(self) -> None:
        super().__init__('Baston Quebrado',200,30)

class EspadaRota(Weapons):
    def __init__(self) -> None:
        super().__init__('Espada Rota',350,20)

class Guadaña(Weapons):
    def __init__(self) -> None:
        super().__init__('Guadaña',300,25)

class EspadaDelRey(Weapons):
    def __init__(self) -> None:
        super().__init__('Espada del Rey',1500,30)    

class CetroDeLaTempestad(Weapons):
    def __init__(self) -> None:
        super().__init__('Cetro de la Tempestad',1000,25)

class MartilloDivino(Weapons):
    def __init__(self) -> None:
        super().__init__('Martillo Divino',1200,20)

class DagaDelViento(Weapons):
    def __init__(self) -> None:
        super().__init__('Daga del Viento',800,40)