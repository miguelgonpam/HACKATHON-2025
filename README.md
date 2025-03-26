# HACKATHON - Michelin x Universidad de Burgos 2025

El fichero `opt.py` incluye los algoritmos de resolución del problema. Los parámetros deben ser pasados en orden, `X`, `Y`, `D`, `E`, `S`.
Siendo: \
`X` el ancho del lote\
`Y` el largo del lote\
`D` el diámetro de los neumáticos\
`E` la separación entre neumáticos\
`S` la separación de los neumáticos con los bordes <br/>
Para las funciones que resuelvan el problema de los neumáticos (las funciones auxiliares no), se les debe añadir un atributo `nombre`. Esto hace que puedan ser indexadas y utilizadas por el programa principal y que el código sea más escalable. Por ejemplo:
```
def func (X,Y,D,E,S):
  ...
  #codigo
  ...
  return ...

func.nombre = 'Nombre de la estrategia'
```

El fichero `plot.py`contiene lo necesario para mostrar la solución gráficamente. <br/>
El fichero `main.py`contiene la interfaz de usuario que solicita los datos y permite elegir el algoritmo (de los que están en `opt.py`) para resolver el problema.
