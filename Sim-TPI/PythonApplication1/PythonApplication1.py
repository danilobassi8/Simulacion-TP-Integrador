import math
import random



def Inicializacion():
    global clock
    global server1,server2,server3,server4,server5
    global cola1,cola2,cola3
    global contadorSistema
    global demoraTotal,util_sv1,util_sv2,util_sv3,util_sv4,util_sv5


    #creo los servidores y las colas.
    server1 = Servidor()
    server2 = Servidor()
    server3 = Servidor()
    server4 = Servidor()
    server5 = Servidor()

    server1.tasa = 7
    server2.tasa = 5
    server3.tasa = 5        #en clientes/unidad de tiempo
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
    demoraTotal = 0
    util_sv1 = 0
    util_sv2 = 0
    util_sv3 = 0
    util_sv4 = 0
    util_sv5 = 0

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
        self.banderaUtilizacion = 0

    def VaciaServer():
        pass

    def MeteEnLaCola(cliente):
        pass

class Cola():
    def __init__(self):
        self.clientes = []
        self.politicaAtencion = "politica no asignada."

    def DameCliente(self):
        if(self.politicaAtencion == "FIFO"):
            retorno = self.clientes[0]
            self.clientes.remove(retorno)
            return retorno
        elif(self.politicaAtencion == "LIFO"):
            retorno = self.clientes[len(clientes) - 1]
            self.clientes.remove(retorno)
            return retorno

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
    # # # # este método solo determina cual va a ser el proximo evento # # #
    return 0

def generarPrioridad(porcentaje):
    r = random.uniform(0,1)
    if(r * 100 <= porcentaje):
        return True
    else:
        return False

def OcurreProximoEvento(nextEvent):
    global clock
    global server1,server2,server3,server4,server5
    global cola1,cola2,cola3
    global demoraTotal,util_sv1,util_sv2,util_sv3,util_sv4,util_sv5

    if(nextEvent == "llegada"): 
        #avanzo el reloj y creo la proxima llegada.
        clock = ListaEventos.llegadaProximoCliente
        ListaEventos.llegadaProximoCliente = generarAleatorioExponencial(1 / 10) + clock

        #creo un cliente con su tiempo de llegada y prioridad.
        clienteNuevo = Cliente()
        clienteNuevo.tiempoArribo = clock
        clienteNuevo.prioridad = generarPrioridad(5)

        #meto el cliente en alguna de las dos colas.
        if(len(cola1.clientes) <= len(cola2.clientes)):
            cola1.clientes.append(clienteNuevo)
        else:
            cola2.clientes.append(clienteNuevo)
                    
    elif(nextEvent == "partida1"):
        #actualizo el clock
        clock = ListaEventos.partida1

        clienteSV1 = server1.cliente
        server1.cliente = 0
        cola3.clientes.append(clienteSV1)
        #calculo el tiempo utilizado del servidor en base a la bandera que se
        #actualiza cuando entra un cliente.
        util_sv1 = util_sv1 + clock - server1.banderaUtilizacion

    elif(nextEvent == "partida2"):
        #actualizo el clock
        clock = ListaEventos.partida2

        clienteSV2 = server2.cliente
        server2.cliente = 0
        cola3.clientes.append(clienteSV2)
        #calculo el tiempo utilizado del servidor en base a la bandera que se
        #actualiza cuando entra un cliente.
        util_sv2 = util_sv2 + clock - server2.banderaUtilizacion

    elif(nextEvent == "partida3"):
        #actualizo el clock
        clock = ListaEventos.partida3

        clienteSV3 = server3.cliente
        server3.cliente = 0
        
        #calculo el tiempo utilizado del servidor en base a la bandera que se
        #actualiza cuando entra un cliente.
        util_sv3 = util_sv3 + clock - server3.banderaUtilizacion

        #sumo a la demora total del sistema (clock - tiempollegada del cliente)
        demoraTotal = demoraTotal + clock - clienteSV3.tiempoArribo

    elif(nextEvent == "partida4"):
        clock = ListaEventos.partida4

        clienteSV4 = server4.cliente
        server4.cliente = 0
        
        #calculo el tiempo utilizado del servidor en base a la bandera que se
        #actualiza cuando entra un cliente.
        util_sv4 = util_sv4 + clock - server4.banderaUtilizacion

        #sumo a la demora total del sistema (clock - tiempollegada del cliente)
        demoraTotal = demoraTotal + clock - clienteSV4.tiempoArribo
    elif(nextEvent == "partida5"):
        clock = ListaEventos.partida5

        clienteSV5 = server5.cliente
        server5.cliente = 0
        
        #calculo el tiempo utilizado del servidor en base a la bandera que se
        #actualiza cuando entra un cliente.
        util_sv5 = util_sv5 + clock - server5.banderaUtilizacion

        #sumo a la demora total del sistema (clock - tiempollegada del cliente)
        demoraTotal = demoraTotal + clock - clienteSV5.tiempoArribo

def GestionDeServidores():
    global clock
    global server1,server2,server3,server4,server5
    global cola1,cola2,cola3

    if(server1.cliente == 0):
        if(len(cola1.clientes) > 0):
            server1.cliente = cola1.DameCliente()
            server1.banderaUtilizacion = clock
            ListaEventos.partida1 = generarAleatorioExponencial(1 / server1.tasa) + clock
        else:
            ListaEventos.partida1 = 99999999999999999999999 * 99999999999999999999999
     #de aca para abajo es copy paste con su correspondiente cola y servidor.
    if(server2.cliente == 0):
        if(len(cola2.clientes) > 0):
            server2.cliente = cola2.DameCliente()
            server2.banderaUtilizacion = clock
            ListaEventos.partida2 = generarAleatorioExponencial(1 / server2.tasa) + clock
        else:
            ListaEventos.partida2 = 99999999999999999999999 * 99999999999999999999999
    if(server3.cliente == 0):
        if(len(cola3.clientes) > 0):
            server3.cliente = cola3.DameCliente()
            server3.banderaUtilizacion = clock
            ListaEventos.partida3 = generarAleatorioExponencial(1 / server3.tasa) + clock
        else:
            ListaEventos.partida3 = 99999999999999999999999 * 99999999999999999999999
    if(server4.cliente == 0):
        if(len(cola3.clientes) > 0):
            server4.cliente = cola3.DameCliente()
            server4.banderaUtilizacion = clock
            ListaEventos.partida4 = generarAleatorioExponencial(1 / server4.tasa) + clock
        else:
            ListaEventos.partida4 = 99999999999999999999999 * 99999999999999999999999
    if(server5.cliente == 0):
        if(len(cola3.clientes) > 0):
            server5.cliente = cola3.DameCliente()
            server5.banderaUtilizacion = clock
            ListaEventos.partida5 = generarAleatorioExponencial(1 / server5.tasa) + clock
        else:
            ListaEventos.partida5 = 99999999999999999999999 * 99999999999999999999999
    return 0


def Graficar():
    global clock
    global server1,server2,server3,server4,server5
    global cola1,cola2,cola3
    global contadorSistema
    global demoraTotal,util_sv1,util_sv2,util_sv3,util_sv4,util_sv5

    print("--------------  " + str(contadorSistema) + "  ---------------")
    print()
    print("cola1: ", end = '')
    print(cola1.clientes)
    print("                                                  server1: " , end = '')
    print([server1.cliente])
    print("cola2: ", end = '')
    print(cola2.clientes)
    print("                                                  server2: " , end = '')
    print([server2.cliente])





Inicializacion()
sigueSimulacion = True
Graficar()
contadorSistema = 0
while(sigueSimulacion):
    nextEvent = proximoEvento() #basicamente se fija en cual es el evento mas proximo y lo devuelve.
    OcurreProximoEvento(nextEvent)
    Graficar()
    GestionDeServidores()
    Graficar()
    contadorSistema = contadorSistema + 1
    
   



