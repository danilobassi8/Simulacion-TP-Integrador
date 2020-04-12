  ![](/iSim-TPI/imagenes/UtnLogo.png)
# Sobre el repositorio! 

Este repositorio fue utilizado por los integrantes del grupo para realizar y modificar un script de simulación en Python el cual debía en primer medida, simular una situación. Luego de eso, se deberán proponer dos alternativas que puedan mejorar el sistema actual y llevarlas a cabo.
Se anexa al final de este README informe final entregado (y aprobado).

Esto fue un trabajo practico para la cátedra de **simulación** en la **Universidad Tecnológica Nacional de Rosario**

# Integrantes del grupo:
|       Miembro         |Legajo                 |Dirección de Correo           					|
|-----------------------|-----------------------|-----------------------------------------------|
|Bassi, Danilo           |43725					|danilo-bassi@hotmail.com                       |
|Campitelli, Gabriel     |43677					|campitelligabriel@hotmail.com                  |
|Moreyra, Sebastián      |43684					|sebastian.j.moreyra@hotmail.com                |


# Esquema inicial.
El esquema inicial a simular era un sistema con las siguientes caracteristicas:
  ![](/Sim-TPI/imagenes/original.png)

# Cambios propuestos.
Los cambios propuestos y en base a los que se sacan las conclusiones que se pueden observar en el informe final fueron los siguientes:
### 1 - Agregado de una cola prioritaria
En este cambio se propone que algunos clientes tengan prioridad. Los clientes que tengan esta propiedad, podrán acceder a un servidor que estará dedicado a ellos. En caso de que no haya clientes con prioridad en la cola 2, el servidor atenderá a los demás clientes de la cola como en el sistema original.

 ![](/Sim-TPI/imagenes/cambio1.png)

### 1 - Modificación de la ubicación de los servidores.
Este cambio se propuso luego de analizar el sistema inicial y el cambio 1. Se observó gran sasturacion de la primer linea de servidores, por lo que se propuso pasar poner todos los servidores con una tasa de atencion de 5 cli/ut en la primer linea, y los dos servidores mas rapidos en la segunda linea. Además, también se unificó la cola en la primer instancia de atención.
 ![](/Sim-TPI/imagenes/cambio2.png)

# Informe final

 <p>Para visualizar el informe final, haga click en:  <a href="https://github.com/elcurco8/Simulacion-TP-Integrador/blob/master/Sim-TPI/imagenes/TP_SIM.pdf">TP Entregado</a>.</p>
