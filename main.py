#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import inspect
import json
import plot
import opt


class Interface:

    ancho_lote = 0
    largo_lote = 0
    diametro_neumatico = 0
    separacion_neumatico = 0
    separacion_bordes = 0
    num_neumaticos = 0
    coordenadas = []

    def __init__(self, master=None):
        self._job = None
        self.appFrame = ttk.Frame(master)
        root.state('zoomed') #iniciar en ventana completa
        width = root.winfo_screenwidth() #obtiene el tamaño de la pantalla
        height = root.winfo_screenheight() 
        self.appFrame.configure(height=height, width=width)
        self.appFrame.pack(side="top")
        self.mainlabel = ttk.Label(self.appFrame)
        self.mainlabel.configure(
            anchor="center", font="{Times New Roman} 36 {bold}", foreground="#003e3e", justify="center", text='TESEO\nOptimización de almacenamiento de cubiertas de camión', wraplength=900)
        self.mainlabel.place(anchor="center", x=width / 2, y=height / 6)

        # Nuevo frame para agrupar los elementos
        self.inputFrame = tk.Frame(self.appFrame, borderwidth=2, relief="ridge", background="lightgray")
        self.inputFrame.place(anchor="center", x=width / 2, y=height / 2, width=450, height=430)  # Ubicación centrada

        # Labels dentro del nuevo frame
        self.label1 = ttk.Label(self.inputFrame, text='Ancho del lote', font=("Times New Roman", 14),
                                background="lightgray")
        self.label1.place(anchor="center", height=30, width=220, x=150, y=50)

        self.label2 = ttk.Label(self.inputFrame, text='Largo del lote', font=("Times New Roman", 14),
                                background="lightgray")
        self.label2.place(anchor="center", height=30, width=220, x=150, y=100)

        self.label3 = ttk.Label(self.inputFrame, text='Diámetro del neumático', font=("Times New Roman", 14),
                                background="lightgray")
        self.label3.place(anchor="center", height=30, width=220, x=150, y=150)

        self.label4 = ttk.Label(self.inputFrame, text='Separación entre neumáticos', font=("Times New Roman", 14),
                                background="lightgray")
        self.label4.place(anchor="center", height=30, width=220, x=150, y=200)

        self.label5 = ttk.Label(self.inputFrame, text='Separación a los bordes', font=("Times New Roman", 14),
                                background="lightgray")
        self.label5.place(anchor="center", height=30, width=220, x=150, y=250)

        # Entradas dentro del nuevo frame
        self.texto1 = ttk.Entry(self.inputFrame)
        self.texto1.place(anchor="center", height=30, width=150, x=350, y=50)

        self.texto2 = ttk.Entry(self.inputFrame)
        self.texto2.place(anchor="center", height=30, width=150, x=350, y=100)

        self.texto3 = ttk.Entry(self.inputFrame)
        self.texto3.place(anchor="center", height=30, width=150, x=350, y=150)

        self.texto4 = ttk.Entry(self.inputFrame)
        self.texto4.place(anchor="center", height=30, width=150, x=350, y=200)

        self.texto5 = ttk.Entry(self.inputFrame)
        self.texto5.place(anchor="center", height=30, width=150, x=350, y=250)

        # Botón dentro del nuevo frame
        self.button2 = ttk.Button(self.inputFrame, text='SOLUCIÓN ÓPTIMA', command=self.optima, cursor="hand2")
        self.button2.place(anchor="s", height=40, width=300, x=225, y=320)

        self.button2 = ttk.Button(self.inputFrame, text='GENERAR JSON', command=self.generar_json, cursor="hand2")
        self.button2.place(anchor="s", height=40, width=300, x=225, y=370)

        self.mainwindow = self.appFrame

    def run(self):
        """
        Run the program, display the GUI
        """
        
        self.mainwindow.mainloop()


    def verificar_datos(self):
        """
        Comprueba que los datos introducidos son correctos.

        Raises:
            ValueError: si alguno de los datos no es correcto.
        """

        self.ancho_lote = abs(int(self.texto1.get()))
        self.largo_lote = abs(int(self.texto2.get()))
        self.diametro_neumatico = abs(int(self.texto3.get()))
        self.separacion_neumatico = abs(int(self.texto4.get()))
        self.separacion_bordes = abs(int(self.texto5.get()))


    def generar_json(self):
        """
        Genera un archivo json con los datos del cálculo de las coordenadas de los neumáticos.
        """

        try:
            #Comprobar si los datos son correctos
            self.verificar_datos()

            self.coordenadas, self.num_neumaticos = self.obtener_datos()

            self.coordenadas = [{"x": x, "y": y} for x, y in self.coordenadas]
            data = {"width": self.ancho_lote, "height": self.largo_lote, "num_cols_neumaticos": self.num_neumaticos,
                    "coordenadas": self.coordenadas}

            # Guardar en un archivo .json
            with open("output.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=1)

        except ValueError:
            print(ValueError)
            messagebox.showinfo('ERROR', 'Valores incorrectos, asegúrese de introducir números enteros')


    def optima(self):
        """
        Obtiene los datos del cálculo de las coordenadas y muestra el gráfico de las coordenadas.
        """

        try:
            #Comprobar si los datos son correctos
            self.verificar_datos()

            self.coordenadas, self.num_neumaticos = self.obtener_datos()

            plot.plot_neumaticos(self.ancho_lote,self.largo_lote,self.diametro_neumatico, self.coordenadas, self.num_neumaticos)
            
        except ValueError:
            print(ValueError)
            messagebox.showinfo('ERROR', 'Valores incorrectos, asegúrese de introducir números enteros')


    def obtener_datos(self):
        """
        Obtiene el mejor conjunto de datos de los cálculos de las coordenadas de los neumáticos.
        """

        funciones = [
            func for _, func in inspect.getmembers(opt, inspect.isfunction)
            if hasattr(func, "nombre")  # Filtrar solo las que tienen nombre personalizado
        ]

        resultados = [[]] * len(funciones)
        cont = 0
        for fun in funciones:
            resultados[cont] = funciones[cont](self.ancho_lote, self.largo_lote, self.diametro_neumatico,
                                               self.separacion_neumatico, self.separacion_bordes)
            cont += 1
        btr = []
        for i in resultados:
            if len(btr) < len(i):
                btr = i

        return btr, len(btr)


global app
root = tk.Tk()
root.title('Teseo')
root.iconbitmap(default="favicon.ico")
app = Interface(root)
app.run()
