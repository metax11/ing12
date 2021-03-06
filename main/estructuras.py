from estructuraEnConstruccion import EstructuraConstruccion

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
        return (litrosDeAgua, litrosDeGas)

    def pasarDia(self):
        self.litrosProcesadosEnDia = 0

    def litrosPorDia(self):
        return self._litrosPorDia


class Tanque:
    def capacidad(self):
        pass

    def litros(self):
        pass

    def llenar(self, volumen):
        pass

    def retirar(self, volumen):
        pass


class TanqueGas(Tanque):
    def __init__(self, capacidad):
        self._capacidad = capacidad
        self._litros = 0

    def capacidad(self):
        return self._capacidad

    def litros(self):
        return self._litros

    def llenar(self, volumen):
        self._litros += volumen

    def retirar(self, volumen):
        self._litros -= volumen


class TanqueAgua(Tanque):
    def __init__(self, capacidad):
        self._capacidad = capacidad
        self._litros = 0

    def capacidad(self):
        return self._capacidad

    def litros(self):
        return self._litros

    def llenar(self, volumen):
        self._litros += volumen

    def retirar(self, volumen):
        self._litros -= volumen

class Estructuras:
    def __init__(self,confPath,vendedorDePetroleo):
        self.tanquesDeAgua = set()
        self.tanquesDeGas = set()
        self.plantasSeparadoras = set()
        self._tanquesDeAguaEnConstruccion = set()
        self._tanquesDeGasEnConstruccion = set()
        self._plantasSeparadorasEnConstruccion = set()
        self.vendedorDePetroleo = vendedorDePetroleo
        archivo = confPath + "estructuras.txt"
        with open(archivo, "r") as as_file:
            linea = as_file.readline()
            lineaParseada = linea.split(" ")
            self.tiempoTanqueAguaPorLitro = int(lineaParseada[0])
            self.tiempoTanqueGasPorLitro = int(lineaParseada[2])
            self.tiempoPlantaPorLitro = int(lineaParseada[4])

    def pasarDia(self):
        for planta in set(self.plantasSeparadoras):
            planta.pasarDia()
        for tanqAg in set(self._tanquesDeAguaEnConstruccion):
            tanqAg.pasarDia()
        for tanqG in set(self._tanquesDeGasEnConstruccion):
            tanqG.pasarDia()
        for planta in set(self._plantasSeparadorasEnConstruccion):
            planta.pasarDia()


    def tanquesDeAguaEnConstruccion(self):
        return set(self._tanquesDeAguaEnConstruccion)

    def tanquesDeGasEnConstruccion(self):
        return set(self._tanquesDeGasEnConstruccion)

    def plantasSeparadorasEnConstruccion(self):
        return set(self._plantasSeparadorasEnConstruccion)

    def capacidadMaximaDeTanquesDeAgua(self):
        res = 0
        for tanque in self.tanquesDeAgua:
            res = res + tanque.litros()
        return res

    def litrosDeAguaAlmacenada(self):
        res = 0
        for tanque in self.tanquesDeAgua:
            res = res + tanque.litros()
        return res

    def capacidadMaximaDeTanquesDeGas(self):
        res = 0
        for tanque in self.tanquesDeGas:
            res = res + tanque.litros()
        return res

    def litrosDeGasAlmacenado(self):
        res = 0
        for tanque in self.tanquesDeGas:
            res = res + tanque.litros()
        return res

    def litrosPorDiaDePlantas(self):
        res = 0
        for planta in self.plantasSeparadoras:
            res = res + planta.litrosPorDia()
        return res

    def cantidadQuePuedeProcesarEnDia(self):
        res = 0
        for planta in self.plantasSeparadoras:
            res = res + planta.cantidadQuePuedeProcesarEnDia()
        return res

    def almacenarGas(self, litrosDeGas):
        for tanq in self.tanquesDeGas:
            cant = min(tanq.cantidadQuePuedeAlmacenar(), litrosDeGas)
            if cant != 0:
                tanq.almacenar(cant)
                litrosDeGas = litrosDeGas - cant
            if litrosDeGas == 0:
                break

    def almacenarAgua(self, litrosDeAgua):
        for tanq in self.tanquesDeAgua:
            cant = min(tanq.cantidadQuePuedeAlmacenar(), litrosDeAgua)
            if cant != 0:
                tanq.almacenar(cant)
                litrosDeAgua = litrosDeAgua - cant
            if litrosDeAgua == 0:
                break

    def retirarGas(self, litrosDeGas):
        for tanq in self.tanquesDeGas:
            cant = min(tanq.litrosAlmacenados(), litrosDeGas)
            if cant != 0:
                tanq.retirar(cant)
                litrosDeGas = litrosDeGas - cant
            if litrosDeGas == 0:
                break

    def retirarAgua(self, litrosDeAgua):
        for tanq in self.tanquesDeAgua:
            cant = min(tanq.litrosAlmacenados(), litrosDeAgua)
            if cant != 0:
                tanq.retirar(cant)
                litrosDeAgua = litrosDeAgua - cant
            if litrosDeAgua == 0:
                break


    def procesarCrudo(self, composicionDeCrudo, litrosDeCrudo):
        materialesSeparados = (0, 0)

        for planta in (self.plantasSeparadoras):
            cant = min(planta.cantidadQuePuedeProcesarEnDia(), litrosDeCrudo)
            if cant != 0:
                materialesSeparadosEnPlanta = planta.procesar(composicionDeCrudo, cant)
                materialesSeparados[0] = materialesSeparados[0] + materialesSeparadosEnPlanta[0]
                materialesSeparados[1] = materialesSeparados[1] + materialesSeparadosEnPlanta[1]
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo == 0:
                break
        return materialesSeparados


    def construirTanqueAgua(self,litros,log):
        def agregarNuevoTanqueAgua():
            log.escribirLinea("terminado tanque de agua, litros: " + str(litros) + "\n")
            self.tanquesDeAgua.add(TanqueAgua(litros))
        def quitarConstructorTanqueAgua(constructor):
            self._tanquesDeGasEnConstruccion.discard(constructor)
        self._tanquesDeAguaEnConstruccion.add(EstructuraConstruccion(litros*self.tiempoTanqueAguaPorLitro,litros,agregarNuevoTanqueAgua,quitarConstructorTanqueAgua))

    def construirTanqueGas(self,litros,log):
        def agregarNuevoTanqueGas():
            log.escribirLinea("terminado tanque de gas, litros: " + str(litros) + "\n")
            self.tanquesDeGas.add(TanqueGas(litros))
        def quitarConstructorTanqueGas(constructor):
            self._tanquesDeGasEnConstruccion.discard(constructor)
        self._tanquesDeGasEnConstruccion.add(EstructuraConstruccion(litros*self.tiempoTanqueGasPorLitro,litros,agregarNuevoTanqueGas,quitarConstructorTanqueGas))

    def construirPlantaSeparadora(self,litros,log):
        def agregarNuevaPlantaProcesadora():
            log.escribirLinea("terminado planta separadora, litros: " + str(litros) + "\n")
            self.plantasSeparadoras.add(PlantaProcesadora(litros,self.vendedorDePetroleo))
        def quitarConstructorPlantaProcesadora(constructor):
            self._plantasSeparadorasEnConstruccion.discard(constructor)
        self._plantasSeparadorasEnConstruccion.add(EstructuraConstruccion(litros*self.tiempoPlantaPorLitro,litros,agregarNuevaPlantaProcesadora,quitarConstructorPlantaProcesadora))

    def capacidadMaximaDeTanquesDeAguaAFuturo(self):
        res = 0
        for tanque in self._tanquesDeAguaEnConstruccion:
            res = res + tanque.litros()
        return res + self.capacidadMaximaDeTanquesDeAgua()

    def capacidadMaximaDeTanquesDeGasAFuturo(self):
        res = 0
        for tanque in self._tanquesDeGasEnConstruccion:
            res = res + tanque.litros()
        return res + self.capacidadMaximaDeTanquesDeGas()

    def cantidadQuePuedeProcesarEnDiaAFuturo(self):
        res = 0
        for planta in self._plantasSeparadorasEnConstruccion:
            res = res + planta.litros()
        return res + self.cantidadQuePuedeProcesarEnDia()