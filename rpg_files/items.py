class Items():
    def __init__(self,name,curacion,precio) -> None:
        self.name = name
        self.curacion = curacion
        self.precio = precio


    def stats(self):
        potis_stats = {'Nombre:\t\t ':self.name,
                    'Curacion:\t ':self.curacion,
                    'Precio:\t ':self.precio}
        
        for key in potis_stats:
            print(key,potis_stats[key])
        print('\n')


class PocionPequena(Items):
    def __init__(self) -> None:
        super().__init__('Pocion Pequeña',50,20)

class PocionMediana(Items):
    def __init__(self) -> None:
        super().__init__('Pocion Mediana',100,100)

class PocionGrande(Items):
    def __init__(self) -> None:
        super().__init__('Pocion Grande',150,200)