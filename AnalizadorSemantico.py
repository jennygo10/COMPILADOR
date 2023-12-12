import GenerarCodigo as GC

precedencia = {
    ';' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '(' : 3
}

reglas_semanti = {
    (0, 0): 0,(0, 1): 1,
    
    (1, 1): 1,(1, 0): 1,

    (2, 2): 2
}

reglasAsig = {
    (0, 0): True,
    
    (1, 1): True,(1, 0): True,

    (2, 2): True
}

tablaSemantica = []

def llenarTabla(tipo, ide, tablaSemantica):
    #print("IDE QUE BUSCO: ", ide)
    existe = False
    if tablaSemantica != []:
        for ideExiste in tablaSemantica:
            #print("IDE EXISTENTE: ", ideExiste[1])
            if ide == ideExiste[0]:
                existe = True
                break
        if existe == False:
            tablaSemantica.append((ide, tipo))
            print("---------------------------------------TABLA SEMÁNTICA")
            print(tablaSemantica)
        existe = False
    else:
        tablaSemantica.append((ide, tipo))
        print("---------------------------------------TABLA SEMÁNTICA")
        print(tablaSemantica)
    return tablaSemantica

def llenarPilaSemantica(ide, pilaSemantica, errorSemantico, tablaSemantica):
    tipo = ""
    for tupla in tablaSemantica:
        ideExistente = tupla[0]
        if ide == ideExistente:
            tipo = tupla[1]
            #print("Este es el tipo: ", tipo)
            break
    if ide == "NUMERO":
        pilaSemantica.append(0)
        tipo = "INT"
    if tipo == "":
        errorSemantico = True

    if tipo == "INT":
        pilaSemantica.append(0)
    elif tipo == "FLOAT":
        pilaSemantica.append(1)
    elif tipo == "CHAR":
        pilaSemantica.append(2)

    #pilaSemantica.append(token)
    print("---------------------------------------PILA SEMÁNTICA")
    print(pilaSemantica)
    return pilaSemantica, errorSemantico

def llenarPilaOperadores(ide, pilaOperadores, pilaSemantica, tipoResultante, intermedio, VarsIntermedio, posfija, contaCodigo):
    if pilaOperadores != []:
        cima_Operadores = pilaOperadores[-1]
        ultimo_valor = precedencia[cima_Operadores]
        valor_ide = precedencia[ide]
        print("Este es el operador que llegó: " + ide)
        #print("Y este es su valor: ", valor_ide)
        print("Este es el operador de la cima: " + cima_Operadores)
        #print("Y este es su valor: ", ultimo_valor)
        if ide != ";":
            if ultimo_valor >= valor_ide:
                operador = pilaOperadores.pop()
                ###################################### EN ESTA PARTE MANDAMOS A LLAMAR AL GENERDOR DE CODIGO INTERMEDIO            
                intermedio, posfija, contaCodigo = GC.operar(operador, intermedio, VarsIntermedio, posfija, contaCodigo)

                posfija.append(operador)
                print("---------------------------------------POSFIJA")
                print(posfija)  
                ######################################## AQUI ES DONDE SE SACA EL OPERADOR Y SE OPERA SEMATICAMENTE 
                ######################################## Y CÓDIGO INTERMEDIO

                v2 = pilaSemantica.pop()
                v1 = pilaSemantica.pop()
                pilaSemantica, tipoResultante = verificarTipos(v1, v2, pilaSemantica, tipoResultante)
                print("---------------------------------------PILA OPERADORES")
                print(pilaOperadores)          
            pilaOperadores.append(ide)
        else:
            while pilaOperadores != []:                
                operador = pilaOperadores.pop()
                intermedio, posfija, contaCodigo = GC.operar(operador, intermedio, VarsIntermedio, posfija, contaCodigo)
                
                #posfija.append(operador)
                print("---------------------------------------POSFIJA")
                print(posfija)  
                v2 = pilaSemantica.pop()
                v1 = pilaSemantica.pop()
                pilaSemantica, tipoResultante = verificarTipos(v1, v2, pilaSemantica, tipoResultante)   
                print("---------------------------------------PILA OPERADORES")
                print(pilaOperadores) 
    else:
        if ide != ";":
            pilaOperadores.append(ide)

    print("---------------------------------------PILA OPERADORES")
    print(pilaOperadores)

    print("---------------------------------------PILA SEMÁNTICA")
    print(pilaSemantica)
    return pilaOperadores, tipoResultante, intermedio, VarsIntermedio, posfija, contaCodigo

def verificarTipos(v1, v2, pilaSemantica, tipoResultante):
    tipoResultante = reglas_semanti.get((v1, v2), "ErrorTipo")
    if tipoResultante != "ErrorTipo":
        pilaSemantica.append(tipoResultante)
    print("---------------------------------------TIPO RESULTANTE")
    print(tipoResultante)
    #if len(pilaSemantica) == 2:
    #    asignarTipo(pilaSemantica)
    return pilaSemantica, tipoResultante
'''
def asignarTipo(pilaSemantica):
    v1 = pilaSemantica.pop()
    valorRecibe = pilaSemantica.pop()
    valorRecibe = reglasAsig.get((valorRecibe, v1), "ErrorAsignacion")
    print("---------------------------------------VALOR RECIBE")
    print(valorRecibe)
    pilaSemantica.append(valorRecibe)
    return valorRecibe
'''

'''
def operaciones(operador, v1, v2):
    if operador == "+":
        v1 = v1 + v2
    elif operador == "-":
        v1 = v1 - v2
    elif operador == "*":
        v1 = v1 * v2
    elif operador == "/":
        v1 = v1 / v2
    
    print("############################ v1 = ", v1)
'''