import json
import inspect
import opt

print(" _____ _____ ____  _____ ___")
print("|_   _| ____/ ___|| ____/ _ \\")
print("  | | |  _| \\___ \\|  _|| | | |")
print("  | | | |___ ___) | |__| |_| |")
print("  |_| |_____|____/|_____\\___/")
print()




arr=["Ancho del lote              > ", "Largo del lote              > ","Diametro del neumático      > ","Separación entre neumáticos > ", "Separación con el borde     > "]
val=[]
for i in arr:
    s = input(i)
    try:
        s = int(s)
        val.append(s)
    except:
        print("¡LOS VALORES DEBEN SER ENTEROS!")

funciones = [
                func for _ ,func in inspect.getmembers(opt, inspect.isfunction)
                if hasattr(func, "nombre")  # Filtrar solo las que tienen nombre personalizado
            ]

resultados = [[]] * len(funciones)
cont=0
for fun in funciones:
    resultados[cont]=funciones[cont](val[0], val[1], val[2], val[3], val[4])
    cont+=1
btr = []
for i in resultados:
    if len(btr) < len(i):
        btr = i

coordenadas = [{"x": x, "y": y} for x, y in btr]
data = {"num": len(coordenadas), "coordenadas": coordenadas}

# Guardar en un archivo .json
with open("output.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=1)

print("\n")
print("SOLUCIÓN >\n")
print(json.dumps(data))







  
  
  
