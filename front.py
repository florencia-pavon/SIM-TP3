import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from back import *


#Funcion que calcula y realiza la tabla de montecarlo
def simular(probabilidad_1er_tiro, probabilidad_7, probabilidad_8, probabilidad_9, rondas, puntaje_max_1, puntaje_max_2, cantidad_puntos_probabilidad, cantidad_rondas_probabilidad, iteracion_i, iteracion_j):
    # Crear una ventana
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title("Tabla de simulación")

    # Crear la tabla
    tabla = ttk.Treeview(ventana_tabla, columns=("Ronda", "Rnd 1", "Pinos 1ra tirada", "Rnd 2", "Pinos 2da tirada", "Puntos", "Puntos acumulados", "Éxito"), show="headings")
    
    # Configurar encabezados de columnas
    for col in tabla["columns"]:
        tabla.heading(col, text=col)

    # Agregar la tabla a la ventana
    tabla.pack(expand=True, fill="both")
    
    puntos_totales = 0
    puntos_ronda_probabilidad = 0
    puntos_ronda = 0
    exito = 0
    contador = 0
    contador_vector = 1
    vector = [[],[]]
    for r in range(rondas):
        contador += 1 
        contador_vector += 1
        # Alternar entre las posiciones [0] y [1] del vector
        index = contador_vector % 2
        resultado_1, rnd_1 = tirar_bolos_primer_tiro(probabilidad_1er_tiro)
        if resultado_1 != 10:
            resultado_2,rnd_2, puntos = tirar_bolos_segundo_tiro(resultado_1, probabilidad_7, probabilidad_8, probabilidad_9, puntaje_max_2)
            puntos_ronda_probabilidad += puntos
            puntos_totales += puntos
            puntos_ronda = puntos
            
        else:
            resultado_2 = 0
            rnd_2 = 0
            puntos_totales += puntaje_max_1
            puntos_ronda_probabilidad += puntaje_max_1
            puntos_ronda = puntaje_max_1
                  
        if contador == cantidad_rondas_probabilidad:
            contador = 0
            if puntos_ronda_probabilidad > cantidad_puntos_probabilidad:
                exito += 1
                
            puntos_ronda_probabilidad = 0   
                     
        datos = [r+1, round(rnd_1,2), resultado_1, round(rnd_2,2), resultado_2, puntos_ronda, puntos_totales, exito]
        vector[index] = datos
        
        if iteracion_i <= r+1 < iteracion_i + iteracion_j:
            tabla.insert("", "end", values=datos)
            
        if iteracion_i+iteracion_j != rondas:
            if r == rondas-1:
                tabla.insert("", "end", values=datos)
              
    probabilidad = 0
    cantidad_casos_probabilidad = rondas //cantidad_rondas_probabilidad
    if cantidad_casos_probabilidad != 0:
        probabilidad = round(exito/cantidad_casos_probabilidad,2)
        
    boton_probabilidad = tk.Button(ventana_tabla, text="Calcular Probabilidad", command=lambda: mostrar_probabilidad(probabilidad, cantidad_rondas_probabilidad, cantidad_puntos_probabilidad))
    boton_probabilidad.pack()
    
def mostrar_probabilidad(prob, rondas, puntos):
    ventana_probabilidad_exito = tk.Toplevel()
    ventana_probabilidad_exito.title("PROBABILIDAD ÉXITO")

    # Mensaje de la probabilidad
    mensaje = f"Probabilidad de que en {rondas} rondas haga más de {puntos} puntos:"
    etiqueta_mensaje = tk.Label(ventana_probabilidad_exito, text=mensaje)
    etiqueta_mensaje.pack(padx=10, pady=10)

    # Probabilidad
    etiqueta_probabilidad = tk.Label(ventana_probabilidad_exito, text=f"{prob:.2f}")
    etiqueta_probabilidad.pack(padx=10, pady=10)

   
    

def cargar_datos():
    # Crear una ventana
    ventana_probabilidades = tk.Toplevel()
    ventana_probabilidades.title("Ingresar Probabilidades y Puntos")
    
    # Variables para almacenar las probabilidades y puntos
    probabilidades_1er_tiro = [tk.DoubleVar() for _ in range(4)]
    probabilidad_7 = [tk.DoubleVar() for _ in range(4)]
    probabilidad_8 = [tk.DoubleVar() for _ in range(3)]
    probabilidad_9 = [tk.DoubleVar() for _ in range(2)]
    puntos_max_1ra_tirada = tk.IntVar()
    puntos_max_2da_tirada = tk.IntVar()
    rondas = tk.IntVar()
    rondas_probabilidad = tk.IntVar()
    puntos_probabilidad = tk.IntVar()
    valor_i = tk.IntVar()
    valor_j = tk.IntVar()
    
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
    tk.Label(ventana_probabilidades, text=9).grid(row=11, column=0)
    tk.Entry(ventana_probabilidades, textvariable=probabilidades_1er_tiro[2]).grid(row=11, column=1)
    tk.Label(ventana_probabilidades, text=10).grid(row=14, column=0)
    tk.Entry(ventana_probabilidades, textvariable=probabilidades_1er_tiro[3]).grid(row=14, column=1)
    
    # Posibles cantidades de pinos y probabilidades en el 2do tiro
    #Probabilidad del 7
    for j, cantidad in enumerate([0, 1, 2, 3], start=2):
        tk.Label(ventana_probabilidades, text=cantidad).grid(row=j, column=2)
        tk.Entry(ventana_probabilidades, textvariable=probabilidad_7[j-2]).grid(row=j, column=3)
    tk.Label(ventana_probabilidades, text=' ').grid(row=6, column=2)
    tk.Label(ventana_probabilidades, text=' ').grid(row=6, column=3)
    #Probabilidad del 8
    for j, cantidad in enumerate([0, 1, 2], start=7):
        tk.Label(ventana_probabilidades, text=cantidad).grid(row=j, column=2)
        tk.Entry(ventana_probabilidades, textvariable=probabilidad_8[j-7]).grid(row=j, column=3)
    tk.Label(ventana_probabilidades, text=' ').grid(row=10, column=2)
    tk.Label(ventana_probabilidades, text=' ').grid(row=10, column=3)
    #Probabilidad del 9
    for j, cantidad in enumerate([0, 1], start=11):
        tk.Label(ventana_probabilidades, text=cantidad).grid(row=j, column=2)
        tk.Entry(ventana_probabilidades, textvariable=probabilidad_9[j-11]).grid(row=j, column=3)
    tk.Label(ventana_probabilidades, text=' ').grid(row=13, column=2)
    tk.Label(ventana_probabilidades, text=' ').grid(row=13, column=3)

        
        
    #Puntos
    for j, puntos in enumerate([7,8,9], start=2):
        tk.Label(ventana_probabilidades, text=puntos).grid(row=j, column=4)
    for j, puntos in enumerate([8,9], start=7):
        tk.Label(ventana_probabilidades, text=puntos).grid(row=j, column=4)
    tk.Label(ventana_probabilidades, text=9).grid(row=11, column=4)
    
    tk.Entry(ventana_probabilidades, textvariable=puntos_max_1ra_tirada).grid(row=14, column=4)
    tk.Entry(ventana_probabilidades, textvariable=puntos_max_2da_tirada).grid(row=5, column=4)
    tk.Entry(ventana_probabilidades, textvariable=puntos_max_2da_tirada).grid(row=9, column=4)
    tk.Entry(ventana_probabilidades, textvariable=puntos_max_2da_tirada).grid(row=12, column=4)
    tk.Label(ventana_probabilidades, text="Cantidad de Rondas").grid(row=1, column=6)
    tk.Entry(ventana_probabilidades, textvariable=rondas).grid(row=2, column=6)
    tk.Label(ventana_probabilidades, text="Para calcular la PROBABILIDAD").grid(row=5, column=6)
    tk.Label(ventana_probabilidades, text="RONDAS").grid(row=6, column=5)
    tk.Entry(ventana_probabilidades, textvariable=rondas_probabilidad).grid(row=6, column=6)
    tk.Label(ventana_probabilidades, text="PUNTOS").grid(row=7, column=5)
    tk.Entry(ventana_probabilidades, textvariable=puntos_probabilidad).grid(row=7, column=6)
    tk.Label(ventana_probabilidades, text="Valor de i").grid(row=10, column=5)
    tk.Entry(ventana_probabilidades, textvariable=valor_i).grid(row=10, column=6)
    tk.Label(ventana_probabilidades, text="Valor de j").grid(row=11, column=5)
    tk.Entry(ventana_probabilidades, textvariable=valor_j).grid(row=11, column=6)


    
    # Botón para validar las probabilidades
    boton_validar = tk.Button(ventana_probabilidades, text="Validar", command=lambda: validar_ingreso(probabilidades_1er_tiro, probabilidad_7, probabilidad_8, probabilidad_9, puntos_max_1ra_tirada, puntos_max_2da_tirada, rondas, puntos_probabilidad, rondas_probabilidad, valor_i, valor_j))
    boton_validar.grid(row=20, column=20, pady=10)
    
    
def validar_ingreso(probabilidades_1er_tiro, prob_7, prob_8, prob_9, puntos_max_1ra_tirada, puntos_max_2da_tirada, rondas, puntos_probabilidad, rondas_probabilidad, valor_i, valor_j):
    # Obtener los valores ingresados por el usuario
    valores_probabilidades_1er_tiro = [probabilidad.get() for probabilidad in probabilidades_1er_tiro]
    probabilidad_7 = [probabilidad.get() for probabilidad in prob_7]
    probabilidad_8 = [probabilidad.get() for probabilidad in prob_8]
    probabilidad_9 = [probabilidad.get() for probabilidad in prob_9]
    puntaje_maximo_1ra_tirada = puntos_max_1ra_tirada.get()
    puntaje_maximo_2da_tirada = puntos_max_2da_tirada.get()
    cantidad_rondas = rondas.get()
    cantidad_puntos_probabilidad = puntos_probabilidad.get()
    cantidad_rondas_probabilidad = rondas_probabilidad.get()
    iteracion_i = valor_i.get()
    iteracion_j = valor_j.get()

    # Validar las probabilidades y puntos
    valido = validar_datos(valores_probabilidades_1er_tiro, probabilidad_7, probabilidad_8, probabilidad_9, puntaje_maximo_1ra_tirada, puntaje_maximo_2da_tirada, cantidad_rondas, cantidad_puntos_probabilidad, cantidad_rondas_probabilidad, iteracion_i, iteracion_j)

    # Mostrar resultado
    if valido:
        messagebox.showinfo("Éxito", "Datos CORRECTAMENTE cargados.")
        simular(valores_probabilidades_1er_tiro, probabilidad_7, probabilidad_8, probabilidad_9, cantidad_rondas, puntaje_maximo_1ra_tirada, puntaje_maximo_2da_tirada, cantidad_puntos_probabilidad, cantidad_rondas_probabilidad, iteracion_i, iteracion_j)
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
