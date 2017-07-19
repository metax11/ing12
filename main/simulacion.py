"""
Created on 12 jul. 2017

@author: Luis
"""
import math

from yacimiento import Yacimiento, Pozo


class Simulacion:
    def __init__(self):
        self.log = Log("log")
        self.diaNumero = 0
        self.scheduler = Scheduler()
        self.contexto = Contexto("./config/")

    def comenzar(self):
        self.log.comenzar()

    def simularDia(self):
        self.log.escribirLinea("Comienza el dia " + str(self.diaNumero))
        self.scheduler.ejecutarPoliticas(self.contexto)
        self.diaNumero += 1

class Log:
    def __init__(self, archivo):
        self.miArchivo = archivo
        self.dineroGanado = 0
        self.dineroPerdido = 0

    def comenzar(self):
        with open(self.miArchivo, "w") as file:
            file.write("Comienzo de simulacion \n")

        return "Comienzo de simulacion\n"

    def escribirLinea(self, texto):
        with open(self.miArchivo, "a") as file:
            file.write(texto + "\n")
        return texto + "\n"

    def venta(self, dinero):
        self.dineroGanado += dinero
        self.escribirLinea("Ingreso de dolares: " + str(dinero) + "\n")

    def gasto(self, dinero):
        self.dineroGanado -= dinero
        self.escribirLinea("Gasto de dolares: " + str(dinero) + "\n")

    def ventas(self):
        self.log.escribirLinea("dolares obtenidos hasta la fecha: " + str(self.dineroGanado))

    def gastos(self):
        self.log.escribirLinea("dolares gastados hasta la fecha: " + str(self.dineroPerdido))

    def balance(self):
        self.log.escribirLinea("ganancias hasta la fecha: " + str(self.dineroGanado - self.dineroPerdido))


class Scheduler:
    def __init__(self):
        self.politicas = []

    def ejecutarPoliticas(self, contexto):
        for politica in self.politicas:
            politica.decidir(contexto)

    def agregarPolitica(self, politica):
        self.politicas.append(politica)


class Estructura(object):
    def costo_de_construccion(self):
        pass

    def tiempo_de_construccion(self):
        pass

    def fecha_de_inicio(self):
        pass


def Tanque(Estructura):
    def capacidad(self):
        pass

    def litros(self):
        pass


def TanqueGas(Tanque):
    def __init__(self, capacidad):
        self._capacidad = capacidad
        self._litros = 0

    def capacidad(self):
        return self._capacidad

    def litros(self):
        return self._litros

    def llenar(self, volumen):
        self._litros += volumen

    def tranferir(self, volumen):
        self._litros -= volumen


def TanqueAgua(Tanque):
    def __init__(self, capacidad):
        self._capacidad = capacidad
        self._litros = 0

    def capacidad(self):
        return self._capacidad

    def litros(self):
        return self._litros

    def llenar(self, volumen):
        self._litros += volumen

    def tranferir(self, volumen):
        self._litros -= volumen


class Estructuras(object):
    def __init__(self, estructuras):
        self._estructuras = estructuras


class Contexto:
    def __init__(self, configPath):
        self.yacimiento = Yacimiento(configPath)
        self.administradorDeRigs = AdministradorDeRigs(configPath)
        #self.excavador = Excavador(configPath)
        self.estructuras = Estructuras(configPath)
        #self.constructor = Constructor(configPath)

    def pasarDia(self):
        self.yacimiento.pasarDia()
        self.administradorDeRigs.pasarDia()
        self.estructuras.pasarDia()


class Formulas:
    def __init__(self, alpha1=0.3, alpha2=0.01):
        if 0.1 <= alpha1 <= 0.6:
            self.alpha1 = alpha1
        else:
            raise ValueError
        if 0.005 <= alpha2 <= 0.01:
            self.alpha2 = alpha2
        else:
            raise ValueError

    def potencialVol(self, presion, volumenRi, numPozos):
        sumando1 = self.alpha1 * (presion / numPozos)
        sumando2 = self.alpha2 * ((presion / numPozos) ^ 2)
        return sumando1 + sumando2

    def presionAlSiguienteDia(self, presionAnterior, volumenR, volumenRi, numPozos):
        betaI = self.betaI(volumenR, volumenRi, numPozos)
        return presionAnterior * (math.e ^ -(betaI))

    def betaI(self, volumenR, volumenRi, numPozos):
        return (0.1 * (volumenRi / volumenR)) / ((numPozos) ^ (2 / 3))


class Tanque:
    def __init__(self, capacidadEnLitros):
        self.capacidadEnLitros = capacidadEnLitros
        self._litrosAlmacenados = 0

    def cantidadQuePuedeAlmacenar(self):
        self.capacidadEnLitros - self._litrosAlmacenados

    def almacenar(self, litros):
        if (self._litrosAlmacenados + litros > self.capacidadEnLitros):
            raise ValueError
        else:
            self._litrosAlmacenados = self._litrosAlmacenados + litros

    def retirar(self, litros):
        if (self._litrosAlmacenados < litros):
            raise ValueError
        else:
            self._litrosAlmacenados = self._litrosAlmacenados - litros
    def litrosAlmacenados(self):
        return _litrosAlmacenados


class PlantaProcesadora:
    def __init__(self, litrosPorDia, vendedorDePetroleo):
        self._litrosPorDia = litrosPorDia
        self.litrosProcesadosEnDia = 0
        self.vendedorDePetroleo = vendedorDePetroleo

    def cantidadQuePuedeProcesarEnDia(self):
        return (self._litrosPorDia) - (self.litrosProcesadosEnDia)

    def procesarCrudo(self, composicionDeCrudo, litrosDeCrudo):
        if (litrosDeCrudo > self.cantidadQuePuedeProcesarEnDia()):
            raise ValueError
        litrosDePetroleo = composicionDeCrudo[0] * litrosDeCrudo / 100
        litrosDeAgua = composicionDeCrudo[1] * litrosDeCrudo / 100
        litrosDeGas = composicionDeCrudo[2] * litrosDeCrudo / 100
        self.vendedorDePetroleo.vender(litrosDePetroleo)
        return (litrosDeAgua,litrosDeGas)

    def pasarDia(self):
        self.litrosProcesadosEnDia = 0

    def litrosPorDia(self):
        return self._litrosPorDia

class VendedorDePetroleo:
    def __init__(self, dolarPorLitro, log):
        self.dolarPorLitro = dolarPorLitro
        self.log = log

    def vender(self, litrosDePetroleo):
        self.log.escribirLinea("litros de petroleo destilados: " + str(litrosDePetroleo) + "\n")
        dinero = self.dolarPorLitro * litrosDePetroleo
        self.log.venta(dinero)
