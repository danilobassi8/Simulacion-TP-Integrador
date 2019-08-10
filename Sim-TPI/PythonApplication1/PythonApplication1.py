import math
import random



def Inicializacion():
    global clock
    global server1,server2,server3,server4,server5
    global cola1,cola2,cola3
    global contadorSistema


    #creo los servidores y las colas.
    server1 = Servidor()
    server2 = Servidor()
    server3 = Servidor()
    server4 = Servidor()
    server5 = Servidor()

    server1.tasa = 7
    server2.tasa = 5
    server3.tasa = 5
    server4.tasa = 5
    server5.tasa = 6

    cola1 = Cola()
    cola2 = Cola()
    cola3 = Cola()
    
    cola1.politicaAtencion = "FIFO"
    cola2.politicaAtencion = "FIFO"
    cola3.politicaAtencion = "FIFO"    
    
    #seteo demas variables de interes.
    contadorSistema = 0
    clock = 0

    #como es la primera vez, voy a generar el primer tiempo de arribo.
    ListaEventos.llegadaProximoCliente = generarAleatorioExponencial(10)


#ejemplo para recordar como se usan las propiedades.
class Clase():
    VariablesDeClase = 1                            #esto es una variable de clase.
    def __init__(self, atributo=0):
        self.atributo = atributo                    #esto es una propiedad.
        pass


class Servidor():
    def __init__(self):
        self.tasa = 0
        self.cliente = 0
        self.colaAsociada = 0

    def VaciaServer():
        pass

    def MeteEnLaCola(cliente):
        pass

class Cola():
    def __init__(self):
        self.clientes = []
        self.politicaAtencion = "politica no asignada."

    def DameCliente():
        pass

class Cliente():
    def __init__(self):
        self.tiempoArribo = 0
        self.prioridad = 1

class ListaEventos():
    #variables de clase.
    llegadaProximoCliente = 0
    partida1 = 99999999999999999999999 * 99999999999999999999999
    partida2 = 99999999999999999999999 * 99999999999999999999999
    partida3 = 99999999999999999999999 * 99999999999999999999999       #para que no salgan nunca.
    partida4 = 99999999999999999999999 * 99999999999999999999999
    partida5 = 99999999999999999999999 * 99999999999999999999999


def generarAleatorioExponencial(media):
    r = random.uniform(0,1)
    numeroGenerado = -media * math.log(r,math.e)
    return numeroGenerado

def proximoEvento():
    #veo cual es el menor numero.
    numeroMinimo = min([ListaEventos.llegadaProximoCliente,ListaEventos.partida1,ListaEventos.partida2,ListaEventos.partida3,ListaEventos.partida4,ListaEventos.partida5]) 
    #veo a quien corresponde.
    if(ListaEventos.llegadaProximoCliente == numeroMinimo):
        return "llegada"
    elif(ListaEventos.partida1 == numeroMinimo):
        return "partida1"
    elif(ListaEventos.partida2 == numeroMinimo):
        return "partida2"
    elif(ListaEventos.partida3 == numeroMinimo):
        return "partida3"
    elif(ListaEventos.partida4 == numeroMinimo):
        return "partida4"
    elif(ListaEventos.partida5 == numeroMinimo):
        return "partida5"


def OcurreProximoEvento(nextEvent):
    if(nextEvent == "llegada"): 
        pass
    elif(nextEvent == "partida1"):
        pass
    elif(nextEvent == "partida2"):
        pass
    elif(nextEvent == "partida3"):
        pass
    elif(nextEvent == "partida4"):
        pass
    elif(nextEvent == "partida5"):
        pass



Inicializacion()
sigueSimulacion = True
while(sigueSimulacion):
    nextEvent = proximoEvento() #basicamente se fija en cual es el evento mas proximo y lo devuelve.
    
    OcurreProximoEvento(nextEvent)
    
   



