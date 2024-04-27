import random

def tirar_bolos(prob_1, prob_7, prob_8, prob_9):
    # Calcular los límites de los intervalos acumulados para el primer tiro
    probabilidades_acumuladas_primer_tiro = [sum(prob_1[:i+1]) for i in range(len(prob_1))]
        
    # Generar un número aleatorio para el primer tiro
    numero_aleatorio_primer_tiro = random.random()
        
    # Determinar la cantidad de bolos derribados en el primer tiro según el número aleatorio generado
    bolos_primer_tiro = None
    for i, prob in enumerate(probabilidades_acumuladas_primer_tiro):
        if numero_aleatorio_primer_tiro <= prob:
            bolos_primer_tiro = i + 7
            break
    
    # Si se derribaron todos los bolos en el primer tiro, devolver el resultado y None para el segundo tiro
    if bolos_primer_tiro == 10:
        return bolos_primer_tiro, None
    
    # Probabilidades para cada cantidad de bolos derribados en el segundo tiro
    probabilidades_segundo_tiro = None
    
    # Si el primer tiro fue 7, usar las probabilidades para el segundo tiro correspondientes a 7
    if bolos_primer_tiro == 7:
        probabilidades_segundo_tiro = prob_7
    # Si el primer tiro fue 8, usar las probabilidades para el segundo tiro correspondientes a 8
    elif bolos_primer_tiro == 8:
        probabilidades_segundo_tiro = prob_8
    # En cualquier otro caso, usar las probabilidades para el segundo tiro correspondientes a 9
    else:
        probabilidades_segundo_tiro = prob_9
    
    # Calcular los límites de los intervalos acumulados para el segundo tiro
    probabilidades_acumuladas_segundo_tiro = [sum(probabilidades_segundo_tiro[:i+1]) for i in range(len(probabilidades_segundo_tiro))]
            
    # Generar un número aleatorio para el segundo tiro
    numero_aleatorio_segundo_tiro = random.random()
    
    # Determinar la cantidad de bolos derribados en el segundo tiro
    bolos_segundo_tiro = None
    for i, prob in enumerate(probabilidades_acumuladas_segundo_tiro):
        if numero_aleatorio_segundo_tiro <= prob:
            bolos_segundo_tiro = i
            break
    
    # Devolver el resultado del primer y segundo tiro
    return bolos_primer_tiro, bolos_segundo_tiro
        


#Funcion que revisa cada dato que cargo el usuario devuelve True si esta todo ok o False si algo no esta bien
def validar_datos(probabilidades_1, probabilidad_7, probabilidad_8, probabilidad_9, puntos_max_1, puntos_max_2, cantidad_rondas):
    probabilidades = probabilidades_1 + probabilidad_7 + probabilidad_8 + probabilidad_9
    
    # Verificar que todas las probabilidades estén entre 0 y 1
    for probabilidad in probabilidades:
        if not (0 <= probabilidad <= 1):
            return False
    
    # Verificar que la suma total de probabilidades sea igual a 1
    if sum(probabilidades_1) != 1 or sum(probabilidad_7) != 1 or sum(probabilidad_8) != 1 or sum(probabilidad_9) != 1:
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