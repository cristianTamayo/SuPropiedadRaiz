class Inmueble:
    listaInmuebles = []
    def __init__(self, estrato, direccion, vigilancia, servicios, ascensor, area, cuartos, banos, tipo):
        self._estrato = estrato
        self._direccion = direccion
        self._vigilancia = vigilancia
        self._servicios = servicios
        self._ascensor = ascensor
        self._area = area
        self._banos = banos
        self._cuartos = cuartos
        self._tipo = tipo    #El tipo es para saber ACTUALMENTE si esta en compra-venta o en arriendo
        self._arriendo=[]
        self._compraventa=None
#ooooeee   #kmas   #hahasalu2
    def toString(inmueble):
        printer = "{"+str(inmueble._estrato)+", "+inmueble._tipo+" }"
        return printer
    
    def getEstrato(self):
        return self._estrato
    
    def setEstrato(self, est):
        self._estrato = est
        
    def getDireccion(self):
        return self._direccion
    
    def setDireccion(self,dire):
        self._direccion = dire
    
    def getVigilancia(self):
        return self._vigilancia

    def setVigilancia(self,vi):
        self._vigilancia = vi
    
    def getServicios(self):
        return self._servicios
    
    def setServicios(self,ser):
        self._servicios = ser
    
    def getAscensor(self):
        return self._ascensor

    def setAscensor(self,asc):
        self._ascensor = asc
    
    def getArea(self):
        return self._area

    def setArea(self,ar):
        self._area = ar
    
    def getBanos(self):
        return self._banos

    def setBanos(self, ba):
        self._banos = ba

    def getCuartos(self):
        return self._cuartos

    def setCuartos(self,cu):
        self._cuartos = cu
    
    def getTipo(self):
        return self._tipo

    def setTipo(self,ti):
        self._tipo = ti

    def getArriendo(self):
        return self._arriendo

    def addArriendo(self,contratoArriendo):
        if self._compraventa==None:
            self._arriendo.append(contratoArriendo)
        else:
            print("No se puede arendar,ya esta en venta")

    def getCompraventa(self):
        return self._compraventaS

    def setCompraventa(self, compraventa):
        if self._compraventa==None:
            self._compraventa=compraventa
        else:
            print("Ya se vendio")


     
    @staticmethod
    def buscarInmueblesEnArriendo(lista):
        listaArriendo = []
        for inmuebles in lista:
            if(inmuebles.getTipo() == "arriendo"):
                listaArriendo.append(inmuebles.toString())
        return listaArriendo
        



