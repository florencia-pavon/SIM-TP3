
#Funcion que recibe un vector con probabilidades y devuelve 2 vectores
# el primero con los limites inferiores
# y el segundo con los limites superiores
def calcular_limites(probabilidades):
    cantidad = len(probabilidades)
    limites_inferiores = [0]
    limites_superiores = [probabilidades[0]]
    for i in range(cantidad-1):
        probabilidad_actual = limites_superiores[i]
        probabilidad_siguiente = probabilidades[i+1]
        limites_superiores.append(probabilidad_actual+probabilidad_siguiente)
        limites_inferiores.append(probabilidad_actual)
    return limites_inferiores, limites_superiores
        


#Funcion que revisa cada dato que cargo el usuario devuelve True si esta todo ok o False si algo no esta bien
def validar_datos(probabilidades_1, probabilidades_2, puntos_max_1, puntos_max_2, cantidad_rondas):
    probabilidades = probabilidades_1 + probabilidades_2
    probabilidad_7 = probabilidades_2[0:4]
    probabilidad_8 = probabilidades_2[4:7]
    probabilidad_9 = probabilidades_2[7:]
    
    # Verificar que todas las probabilidades estén entre 0 y 1
    for probabilidad in probabilidades:
        if not (0 <= probabilidad <= 1):
            return False
    
    # Verificar que la suma total de probabilidades sea igual a 1
    if sum(probabilidad_7) != 1 or sum(probabilidad_8) != 1 or sum(probabilidad_9) != 1:
            return False
    
    #Verificar que los puntos ingresados por el usuario tengan sentido
    if puntos_max_2 > puntos_max_1:
        return False
    if puntos_max_1 <= 0 or puntos_max_2 <= 0:
        return False
    
    #Verificar que la cantidad de rondas no sea negativa
    if cantidad_rondas <= 0:
        return False
    
    return True