def simBP(n:int, m:int) -> int:
    ''' Requiere: n>0, m>0
        Devuelve: la similitud binaria de prefijo entre n y m, definida como
        la longitud del prefijo común más largo entre las representaciones
        binarias de n y m. '''
    # Inicialización
    i:int=0 #  para iterar el ciclo while
    res:int=0 #  variable retorno
    # Transformacion de los parametros a binario
    num_binario_n:int=bin(n).replace('0b','') 
    num_binario_m:int=bin(m).replace('0b','')
    #Longitudes de los numeros binarios
    longitud_binario_n:int=len(num_binario_n)
    longitud_binario_m:int=len(num_binario_m)
    #ciclo para obtener la simbp
    while(i<longitud_binario_n and i<longitud_binario_m): 
        # si ambos tienen los mismos valores en su posicion i, res aumenta en 1
        if(num_binario_n[i]==num_binario_m[i]):
            res=res+1
        # en caso contrario, que es cuando se acaba la simbp, detemos el ciclo while
        else:
            i=longitud_binario_n # para que no se cumpla la condicion del while y acabe el ciclo
        i=i+1 
    return res


def cantidad_con_simBP_en_intervalo(n:int, a:int, b:int, k:int) -> int:
    ''' Requiere: n>0, a>0, b>0, k>0, a<=b
        Devuelve: la cantidad de números entre a y b (inclusive)
        cuya simBP con n es k.'''
    # Inicialización
    i:int=0 # para iterar el ciclo while
    res:int=0 # variable retorno
    diferencia_ab:int=b-a
    while(i<=diferencia_ab):
        #usamos la funcion auxiliar simBP() y pasamos los parametros
        if(simBP((b-i), n) == k): # en b-i, se recorre de b a a
            res =  res + 1 #aumenta res en 1
        i=i+1
    return res 


def existe_con_simBP_en_intervalo(n:int, a:int, b:int, k:int) -> bool:
    ''' Requiere: n>0, a>0, b>0, k>0, a<=b
        Devuelve: True si existe algún número entre a y b (inclusive)
        cuya simBP con n es k; False en caso contrario.'''
    # uso la funcion auxiliar cantidad_con_simBP_en_intervalo()
    # cuando lo que devuelve es diferente a cero nos quiere decir que hay al menos 1 numero que cumple la condicion, por lo tanto si existe y si es igual a cero, no existe
    return cantidad_con_simBP_en_intervalo(n, a, b, k) !=0


def numero_con_mayor_simBP_en_intervalo(n:int, a:int, b:int) -> int:
    ''' Requiere: n>0, a>0, b>0, a<=b
        Devuelve: el número entre a y b (inclusive) con mayor simBP con n. En caso de haber más de uno, devuelve el menor de ellos.'''
    #Inicialización
    i:int=0 #  para iterarel ciclo while
    mayor_simbp:int=0 # donde se va a guardar el mayor simbp entre a y b con n
    res:int=0 # variable retorno
    simBP_valor:int=0 # guardara la simbp entre un numero con n
    numero_en_intervalo:int=0 # guardara un numero entre a y b
    diferencia_ab:int=b-a # si a y b son iguales, la variable valdria 0, por lo tanto solo se evalúa un número
    while(i<=diferencia_ab):
        numero_en_intervalo=b-i #  recorre desde el mayor(b) hasta  el menor(a)
        simBP_valor=simBP(numero_en_intervalo, n) # se calcula la simbp 
        if(simBP_valor >= mayor_simbp): 
            mayor_simbp=simBP_valor
            res=numero_en_intervalo # guarda el  menor numero con mayor simbp
        i=i+1 
    return res

