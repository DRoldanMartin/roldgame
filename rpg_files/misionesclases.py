from rpg_files.enemies import *

class Misiones():
    def __init__(self,mision_name,experiencia_mision,oro_mision,enemigos,valor_mision) -> None:
        self.mision_name = mision_name
        self.experiencia_mision = experiencia_mision
        self.oro_mision = oro_mision
        self.enemigos = enemigos
        self.valor_mision = valor_mision
        

#Mision 1
class CazaDeVampirosNovatos(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'Caza de vampiros novatos',
        experiencia_mision = 100,
        oro_mision = 100,
        enemigos = [VampiroNovato(),VampiroNovato(),VampiroNovato(),VampiroNovato()],
        valor_mision = 1
        )

#Mision 2
class CazaDeDampirosEnElBosque(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'Caza de vampiros en el bosque',
        experiencia_mision = 150,
        oro_mision = 150,
        enemigos = [VampiroAcechador(),VampiroNovato(),VampiroAcechador(),VampiroNovato()],
        valor_mision = 1
        )

#Mision 3
class CazaDeVampirosEnLasProfundidadesDelBosque(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'Caza de vampiros en las profundidades del bosque',
        experiencia_mision = 200,
        oro_mision = 200,
        enemigos = [EspectroOscuro(),VampiroNovato(),EspectroOscuro(),VampiroAcechador()],
        valor_mision = 1
        )

#Mision 4
class ProtegerLaCiudad(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'Proteger la ciudad',
        experiencia_mision = 300,
        oro_mision = 300,
        enemigos = [VampiroExplorador(),VampiroAterrador(),EspectroDeLaNoche()],
        valor_mision = 1
        )

#Mision 5
class CazaDelVampiroMaestro(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'Caza del vampiro maestro',
        experiencia_mision = 500,
        oro_mision = 500,
        enemigos = [VampiroCazador(),VampiroGuerrero(),VampiroMaestro()],
        valor_mision = 1
        )

#Mision 6
class InfiltraciónEnLaMansiónVampírica(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'Infiltración en la mansión vampírica',
        experiencia_mision = 800,
        oro_mision = 800,
        enemigos = [GuardiaVampiro(),CriptaDeVampiros(),JefeDeSeguridadVampirica(),LiderVampirico()],
        valor_mision = 1
        )

#Mision 7
class DestrucciónDeLaFábricaDeSangre(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'Destrucción de la fábrica de sangre',
        experiencia_mision = 1000,
        oro_mision = 1000,
        enemigos = [TrabajadorVampiro(),GuardianDeLaFabrica(),IngenieroJefeVampiro(),ExperimentoFallido()],
        valor_mision = 1
        )

#Mision 8
class ProtegerALosCiviles(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'Proteger a los civiles',
        experiencia_mision = 1200,
        oro_mision = 1200,
        enemigos = [VampiroCazadorGrande(),VampiroRastreador(),VampiroVolador()],
        valor_mision = 1
        )

#Mision 9
class AtacandoElNidoDeVampiros(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'Atacando el nido de vampiros',
        experiencia_mision = 1500,
        oro_mision = 1500,
        enemigos = [GuardiaVampiroMayor(),VampiroHechicero(),LiderVampiro()],
        valor_mision = 1
        )

#Mision 10
class LaGuaridaDelCondeDrácula(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'La guarida del Conde Drácula',
        experiencia_mision = 3000,
        oro_mision = 3000,
        enemigos = [GuardianDelCastillo(),EspectroDelCastillo(),CondeDracula()],
        valor_mision = 1
        )

#Mision 11
class ElAmuletoDeLaLunaLlena(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'El amuleto de la Luna Llena',
        experiencia_mision = 4000,
        oro_mision = 4000,
        enemigos = [LadronVampiro(),GuerreroVampiro(),LiderVampiroAdulto()],
        valor_mision = 1
        )

#Mision 12
class LaGuaridaDeLosVampiros(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'La guarida de los vampiros',
        experiencia_mision = 4500,
        oro_mision = 4500,
        enemigos = [EsbirroVampiro(),VampiroCazadorAdulto(),VampiroMago(),VampiroNoble()],
        valor_mision = 1
        )

#Mision 13
class LaTumbaDelVampiroAnciano(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'La tumba del vampiro anciano',
        experiencia_mision = 6000,
        oro_mision = 6000,
        enemigos = [EsbirroVampiro(),VampiroGuerreroAnciano(),VampiroSacerdote(),VampiroAnciano()],
        valor_mision = 1
        )

#Mision 14
class ElTemploDelVampiroSupremo(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'El Templo del Vampiro Supremo',
        experiencia_mision = 6000,
        oro_mision = 6000,
        enemigos = [EsbirroVampiro(),VampiroCazadorAdulto(),VampiroMago(),VampiroNoble(),VampiroSupremo()],
        valor_mision = 1
        )

#Mision 15
class ElAbismoDeLasSombras(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'El Abismo de las Sombras',
        experiencia_mision = 5000,
        oro_mision = 5000,
        enemigos = [HorrorDeLasSombras(),MagoOscuro(),EspectroDeLaOscuridad(),DemonioDeLasSombras()],
        valor_mision = 1
        )

#Mision 16
class ElSantuarioDeLaSangre(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'El Santuario de la Sangre',
        experiencia_mision = 6000,
        oro_mision = 6000,
        enemigos = [EsbirroVampiroAdulto(),VampiroAcechador(),VampiroMagoAdulto(),VampiroNobleAdulto(),ElSeñorDeLaSangre()],
        valor_mision = 1
        )

#Mision 17
class LaCriptaDelVampiroOscuro(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'La cripta del vampiro oscuro',
        experiencia_mision = 6000,
        oro_mision = 6000,
        enemigos = [MurcielagoGigante(),Gargola(),Espectro(),VampiroOscuro()],
        valor_mision = 1
        )

#Mision 18
class ElSantuarioDelCondeOscuro(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'El santuario del Conde Oscuro',
        experiencia_mision = 7500,
        oro_mision = 7500,
        enemigos = [EspectroSanguinario(),GolemDeSombra(),DemonioInvocado(),ElCondeOscuro()],
        valor_mision = 1
        )

#Mision 19
class LaFortalezaDelCondeVampiro(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'La Fortaleza del Conde Vampiro',
        experiencia_mision = 6000,
        oro_mision = 6000,
        enemigos = [GargolaAnciana(),MirmidonVampiro(),VampiroSabueso(),CondeVampiroAnciano()],
        valor_mision = 1
        )

#Mision 20
class LaGuaridaDelSeñorDeLosVampiros(Misiones):
    def __init__(self) -> None:
        super().__init__(
        mision_name = 'La guarida del señor de los vampiros',
        experiencia_mision = 10000,
        oro_mision = 10000,
        enemigos = [SeñorDeLosVampiros(),VampiroEspectro(),VampiroDragon(),VampiroEspectro()],
        valor_mision = 1
        )