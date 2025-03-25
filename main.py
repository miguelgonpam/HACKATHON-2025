#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, simpledialog
import time

from pyparsing import results

import plot
import matplotlib.pyplot as plt
import opt



class Interface:

    def __init__(self, master=None):
        self._job = None
        self.appFrame = ttk.Frame(master)
        root.state('zoomed') #iniciar en ventana completa
        width = root.winfo_screenwidth() #obtiene el tamaño de la pantalla
        height = root.winfo_screenheight() 
        self.appFrame.configure(height=900, width=1000)
        self.appFrame.pack(side="top")
        self.mainlabel = ttk.Label(self.appFrame)
        self.mainlabel.configure(
            anchor="center", font="{Times New Roman} 36 {bold}", foreground="#003e3e", justify="center", text='TESEO\nOptimización de almacenamiento de cubiertas de camión', wraplength=900)
        self.mainlabel.place(anchor="center", x=500, y=100)

        self.label1= ttk.Label(self.appFrame)
        self.label1.place(anchor="center", height=50, width=220, x=int(width/4), y=int(height/3)+50)
        self.label1.configure(anchor="center",
                             font="{Times New Roman} 14 {}", justify="left", text='Ancho del lote')
        self.label2= ttk.Label(self.appFrame)
        self.label2.place(anchor="center", height=50, width=220, x=int(width/4), y=int(height/3)+105)
        self.label2.configure(anchor="center",
                             font="{Times New Roman} 14 {}", justify="left", text='Largo del lote')
        self.label3= ttk.Label(self.appFrame)
        self.label3.place(anchor="center", height=50, width=220, x=int(width/4), y=int(height/3)+160)
        self.label3.configure(anchor="center",
                             font="{Times New Roman} 14 {}", justify="left", text='Diámetro del neumático')
        self.label4= ttk.Label(self.appFrame)
        self.label4.place(anchor="center", height=50, width=220, x=int(width/4), y=int(height/3)+215)
        self.label4.configure(anchor="center",
                             font="{Times New Roman} 14 {}", justify="left", text='Separación entre neumáticos')
        self.label5= ttk.Label(self.appFrame)
        self.label5.place(anchor="center", height=50, width=220, x=int(width/4), y=int(height/3)+270)
        self.label5.configure(anchor="center",
                             font="{Times New Roman} 14 {}", justify="left", text='Separación a los bordes')


        self.texto1 = ttk.Entry(self.appFrame)
        self.texto1.place(anchor="center", height=50, width=150, x=int(width/4)+200, y=int(height/3)+50 )
        self.texto2 = ttk.Entry(self.appFrame)
        self.texto2.place(anchor="center", height=50, width=150, x=int(width/4)+200, y=int(height/3)+105 )
        self.texto3 = ttk.Entry(self.appFrame)
        self.texto3.place(anchor="center", height=50, width=150, x=int(width/4)+200, y=int(height/3)+160 )
        self.texto4 = ttk.Entry(self.appFrame)
        self.texto4.place(anchor="center", height=50, width=150, x=int(width/4)+200, y=int(height/3)+215 )
        self.texto5 = ttk.Entry(self.appFrame)
        self.texto5.place(anchor="center", height=50, width=150, x=int(width/4)+200, y=int(height/3)+270 )

        self.button1 = ttk.Button(self.appFrame, command=self.voraz)
        self.button1.configure(cursor="hand2", text='SOLUCIÓN RÁPIDA', compound="top")
        self.button1.place(anchor="s", height=50, width=190, x=int(width/4), y=int(height/3)+350)

        self.button2 = ttk.Button(self.appFrame, command=self.backtracking)
        self.button2.configure(cursor="hand2", text='SOLUCIÓN ÓPTIMA', compound="top")
        self.button2.place(anchor="s", height=50, width=190, x=int(width/4)+195, y=int(height/3)+350)
        #self.solvebutton.bind("<ButtonPress>", self.comprobar)

        
        

        self.mainwindow = self.appFrame

    def run(self):
        """
        Run the program, display the GUI
        """
        #app.displayStateOnGrid('000000000')
        #app.gif_loading.place_forget()
        #self.refreshFrame()
        #self.mainwindow.after(0, app.refreshGIF, 0)
        self.mainwindow.mainloop()
        #str= self.texto1.get()
        #print(str)

    def voraz(self):
        try:
            X=int(self.texto1.get())
            Y=int(self.texto2.get())
            D=int(self.texto3.get())
            E=int(self.texto4.get())
            S=int(self.texto5.get())
            vor=opt.voraz(X,Y,D,E,S)
            #print(vor)
            plot.plot_neumaticos(X,Y,D, vor)
        except:
            messagebox.showinfo('ERROR', 'Valores incorrectos, asegúrese de introducir números enteros')


    def backtracking(self):
        try:
            X=int(self.texto1.get())
            Y=int(self.texto2.get())
            D=int(self.texto3.get())
            E=int(self.texto4.get())
            S=int(self.texto5.get())
            resultados = [None] * 3
            resultados[0] = opt.distribucion_hexagonal_neumaticos(X, Y, D, E, S)
            resultados[1] = opt.distribucion_maxima_densidad(X,Y,D,E,S)
            resultados[2] = opt.optimizar_distribucion_neumaticos(X,Y,D,E,S)
            btr = []
            for i in resultados:
                if len(btr) < len(i):
                    btr = i
            print(btr)
            plot.plot_neumaticos(X,Y,D, btr)
        except ValueError:
            print(ValueError)
            messagebox.showinfo('ERROR', 'Valores incorrectos, asegúrese de introducir números enteros')

    def comprobar(self):
        val=self.texto1.get()
        self.texto1.delete(0,100)
        if val != "":
            if  val in self.valores:
                messagebox.showinfo('Echa el freno madaleno!', f'El número {val} ya está registrado')
            else:
                self.valores.append(val) 


global app
root = tk.Tk()
root.title('Teseo')
    
root.iconbitmap(default="favicon.ico")
app = Interface(root)
app.run()