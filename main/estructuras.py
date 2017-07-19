class Estructuras:
	def __init__(self,confPath):
		self.tanquesDeAgua = {}
		self.tanquesDeGas = {}
		self.plantasSeparadoras = {}
		self._tanquesDeAguaEnConstruccion = {}
		self._tanquesDeGasEnConstruccion = {}
		self._plantasSeparadorasEnConstruccion = {}
		archivo = confPath + "estructuras.txt"
		with open(archivo, "r") as file:
            linea = file.readLine()
            lineaParseada = linea.split(" ")
            self.tiempoTanqueAguaPorLitro = lineaParseada[0]
            self.tiempoTanqueGasPorLitro = lineaParseada[2]
            self.tiempoPlantaPorLitro = lineaParseada[4]

	def tanquesDeAguaEnConstruccion(self):
		return set(self._tanquesDeAguaEnConstruccion)

	def tanquesDeGasEnConstruccion(self):
		return set(self._tanquesDeGasEnConstruccion)

	def plantasSeparadorasEnConstruccion(self):
		return set(_plantasSeparadorasEnConstruccion)

	def capacidadMaximaDeTanquesDeAgua(self):
		res = 0
		for tanque in self.tanquesDeAgua:
			res = res + tanque.litrosMaximo()
		return res

	def litrosDeAguaAlmacenado(self):
		res = 0
		for tanque in self.tanquesDeAgua:
			res = res + tanque.litros()
		return res

	def capacidadMaximaDeTanquesDeGas(self):
		res = 0
		for tanque in self.tanquesDeGas:
			res = res + tanque.litrosMaximo()
		return res

	def litrosDeGasAlmacenado(self):
		res = 0
		for tanque in self.tanquesDeGas:
			res = res + tanque.litros()
		return res

	def litrosPorDiaDePlantas(self):
		res = 0
		for planta in self.plantasProcesadoras:
			res = res + planta.litrosPorDia()
		return res

	def cantidadQuePuedeProcesarEnDia(self):
		res = 0
		for planta in self.plantasProcesadoras:
			res = res + planta.cantidadQuePuedeProcesarEnDia()
		return res

	def almacenarAgua(self):
		res = 0
		for planta in self.plantasProcesadoras:
			res = res + planta.cantidadQuePuedeProcesarEnDia()
		return res

    def almacenarGas(self, litrosDeGas):
        for tanq in self.tanquesDeGas:
            cant = min(tanq.cantidadQuePuedeAlmacenar(), litrosDeGas)
            if cant != 0:
                tanq.almacenar(composicionDeCrudo, cant)
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo == 0:
                break

    def almacenarAgua(self, litrosDeAgua):
        for tanq in self.tanquesDeAgua:
            cant = min(tanq.cantidadQuePuedeAlmacenar(), litrosDeAgua)
            if cant != 0:
                tanq.almacenar(composicionDeCrudo, cant)
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo == 0:
                break

    def retirarGas(self, litrosDeGas):
        for tanq in self.tanquesDeGas:
            cant = min(tanq.litrosAlmacenados(), litrosDeGas)
            if cant != 0:
                tanq.retirar(composicionDeCrudo, cant)
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo == 0:
                break

    def retirarAgua(self, litrosDeAgua):
        for tanq in self.tanquesDeAgua:
            cant = min(tanq.litrosAlmacenados(), litrosDeAgua)
            if cant != 0:
                tanq.retirar(composicionDeCrudo, cant)
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo == 0:
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
    		self.tanquesDeAgua.add(TanqueDeAgua(litros))
    	def quitarConstructorTanqueAgua(constructor):
    		self._tanquesDeGasEnConstruccion.discart(constructor)
    	self._tanquesDeAguaEnConstruccion.add(EstructuraConstruccion(litros*self.tiempoTanqueAguaPorLitro,agregarNuevoTanqueAgua,quitarConstructorTanqueAgua))

    def construirTanqueGas(self,litros,log):
    	def agregarNuevoTanqueGas():
    		log.escribirLinea("terminado tanque de gas, litros: " + str(litros) + "\n")
    		self.tanquesDeGas.add(TanqueDeGas(litros))
    	def quitarConstructorTanqueGas(constructor):
    		self._tanquesDeGasEnConstruccion.discart(constructor)
    	self._tanquesDeGasEnConstruccion.add(EstructuraConstruccion(litros*self.tiempoTanqueGasPorLitro,agregarNuevoTanqueGas,quitarConstructorTanqueGas))

    def construirPlantaSeparadora(self,litros,log):
    	def agregarNuevaPlantaProcesadora():
    		log.escribirLinea("terminado planta separadora, litros: " + str(litros) + "\n")
    		self.plantasProcesadoras.add(PlantaProcesadoras(litros))
    	def quitarConstructorPlantaProcesadora(constructor):
    		self.plantasProcesadoras.discart(constructor)
    	self.plantasProcesadoras.add(EstructuraConstruccion(litros*self.tiempoPlantaPorLitro,agregarNuevaPlantaProcesadora,quitarConstructorPlantaProcesadora))

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