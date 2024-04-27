import tkinter as tk
import tkinter.messagebox as messagebox
from back import *


#HAY QUE REHACER ESTA FUNCION ESTA HECHA SOLO PARA VERIFICAR
def simular(probabilidad_1er_tiro, probabilidad_7, probabilidad_8, probabilidad_9, rondas):
    for _ in range(rondas):
        resultado_1, resultado_2 = tirar_bolos(probabilidad_1er_tiro, probabilidad_7, probabilidad_8, probabilidad_9)
        if resultado_2 != None:
            print('resultado Primer tiro')
            print(resultado_1)
            print('resultado Segundo tiro')
            print(resultado_2)
        else:
            print('resultado 1')
            print(resultado_1)

def cargar_datos():
    # Crear una ventana
    ventana_probabilidades = tk.Toplevel()
    ventana_probabilidades.title("Ingresar Probabilidades y Puntos")
    
    # Variables para almacenar las probabilidades y puntos
    probabilidades_1er_tiro = [tk.DoubleVar() for _ in range(4)]
    probabilidades_2do_tiro = [tk.DoubleVar() for _ in range(9)]
    puntos_max_1ra_tirada = tk.IntVar()
    puntos_max_2da_tirada = tk.IntVar()
    rondas = tk.IntVar()

    # Etiquetas de las columnas
    primeras_columnas = ["Primera Ronda","Segunda Ronda"]
    for i, columna in enumerate(primeras_columnas):
        tk.Label(ventana_probabilidades, text=columna).grid(row=0, column=i)
    
    segundas_columnas = ["Cantidad de Pinos", "Probabilidad", "Cantidad de Pinos", "Probabilidad", "Puntos"]
    for i, columna in enumerate(segundas_columnas):
        tk.Label(ventana_probabilidades, text=columna).grid(row=1, column=i)
    
    # Posibles cantidades de pinos y probabilidades en el 1er tiro
    tk.Label(ventana_probabilidades, text=7).grid(row=3, column=0)
    tk.Entry(ventana_probabilidades, textvariable=probabilidades_1er_tiro[0]).grid(row=3, column=1)
    tk.Label(ventana_probabilidades, text=8).grid(row=7, column=0)
    tk.Entry(ventana_probabilidades, textvariable=probabilidades_1er_tiro[1]).grid(row=7, column=1)
    tk.Label(ventana_probabilidades, text=9).grid(row=9, column=0)
    tk.Entry(ventana_probabilidades, textvariable=probabilidades_1er_tiro[2]).grid(row=9, column=1)
    tk.Label(ventana_probabilidades, text=10).grid(row=11, column=0)
    tk.Entry(ventana_probabilidades, textvariable=probabilidades_1er_tiro[3]).grid(row=11, column=1)
    
    # Posibles cantidades de pinos y probabilidades en el 2do tiro
    for j, cantidad in enumerate([0, 1, 2, 3, 0, 1, 2, 0, 1], start=2):
        tk.Label(ventana_probabilidades, text=cantidad).grid(row=j, column=2)
        tk.Entry(ventana_probabilidades, textvariable=probabilidades_2do_tiro[j-2]).grid(row=j, column=3)
        
    #Puntos
    for j, puntos in enumerate([7,8,9], start=2):
        tk.Label(ventana_probabilidades, text=puntos).grid(row=j, column=4)
    for j, puntos in enumerate([8,9], start=6):
        tk.Label(ventana_probabilidades, text=puntos).grid(row=j, column=4)
    tk.Label(ventana_probabilidades, text=9).grid(row=9, column=4)
    
    tk.Entry(ventana_probabilidades, textvariable=puntos_max_1ra_tirada).grid(row=11, column=4)
    tk.Entry(ventana_probabilidades, textvariable=puntos_max_2da_tirada).grid(row=5, column=4)
    tk.Entry(ventana_probabilidades, textvariable=puntos_max_2da_tirada).grid(row=8, column=4)
    tk.Entry(ventana_probabilidades, textvariable=puntos_max_2da_tirada).grid(row=10, column=4)
    tk.Label(ventana_probabilidades, text="Cuantas rondas desea simular?").grid(row=1, column=5)
    tk.Entry(ventana_probabilidades, textvariable=rondas).grid(row=2, column=5)


    
    # Botón para validar las probabilidades
    boton_validar = tk.Button(ventana_probabilidades, text="Validar", command=lambda: validar_ingreso(probabilidades_1er_tiro, probabilidades_2do_tiro, puntos_max_1ra_tirada, puntos_max_2da_tirada, rondas))
    boton_validar.grid(row=20, column=20, pady=10)
    
    
def validar_ingreso(probabilidades_1er_tiro, probabilidades_2do_tiro, puntos_max_1ra_tirada, puntos_max_2da_tirada, rondas):
    # Obtener los valores ingresados por el usuario
    valores_probabilidades_1er_tiro = [probabilidad.get() for probabilidad in probabilidades_1er_tiro]
    valores_probabilidades_2do_tiro = [probabilidad.get() for probabilidad in probabilidades_2do_tiro]
    probabilidad_7 = valores_probabilidades_2do_tiro[0:4]
    probabilidad_8 = valores_probabilidades_2do_tiro[4:7]
    probabilidad_9 = valores_probabilidades_2do_tiro[7:]
    puntaje_maximo_1ra_tirada = puntos_max_1ra_tirada.get()
    puntaje_maximo_2da_tirada = puntos_max_2da_tirada.get()
    cantidad_rondas = rondas.get()

    # Validar las probabilidades y puntos
    valido = validar_datos(valores_probabilidades_1er_tiro, probabilidad_7, probabilidad_8, probabilidad_9, puntaje_maximo_1ra_tirada, puntaje_maximo_2da_tirada, cantidad_rondas)

    # Mostrar resultado
    if valido:
        messagebox.showinfo("Éxito", "Datos CORRECTAMENTE cargados.")
        simular(valores_probabilidades_1er_tiro, probabilidad_7, probabilidad_8, probabilidad_9, cantidad_rondas)
    else:
        messagebox.showerror("Error", "Datos ERRONEOS, revisar.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulación de Bowling")

# Crear etiqueta para pedir al usuario que ingrese las probabilidades
etiqueta = tk.Label(ventana, text="Ingrese los datos", font=("Arial", 20))
etiqueta.pack(pady=10, padx=200)

# Crear botón para ingresar las probabilidades
boton_ingresar = tk.Button(ventana, text="Ingresar", command=cargar_datos, font=("Arial", 18))
boton_ingresar.pack(pady=15)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
