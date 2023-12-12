import AnalizadorSemantico as ASE
import GenerarCodigo as GC

    #################################
'''
    PRODUCCIONES

    'P\'' : 'P',
    'P' : 'Tipo ID V',
    'P' : 'A',
    'Tipo' : 'int',
    'Tipo' : 'float',
    'Tipo' : 'char',
    'V' : ', ID V',
    'V' : '; P',
    'A' : 'ID = Exp ;',
    'Exp' : '+ Term E',
    'Exp' : '- Term E',
    'Exp' : 'Term E',
    'E' : '+ Term E',
    'E' : '- Term E',
    'E' : '',
    'Term' : 'F T',
    'T' : '* F T',
    'T' : '/ F T',
    'T' : '',
    'F' : 'ID',
    'F' : 'NUMERO',
    'F' : '( Exp )',
'''
###############################################


produccioes = {
    'p0' : 'P',
    'p1' : 'Tipo ID V',
    'p2' : 'A',
    'p3' : 'int',
    'p4' : 'float',
    'p5' : 'char',
    'p6' : ', ID V',
    'p7' : '; P',
    'p8' : 'ID = Exp ;',
    'p9' : '+ Term E',
    'p10' : '- Term E',
    'p11' : 'Term E',
    'p12' : '+ Term E',
    'p13' : '- Term E',
    'p14' : '',
    'p15' : 'F T',
    'p16' : '* F T',
    'p17' : '/ F T',
    'p18' : '',
    'p19' : 'ID',
    'p20' : 'NUMERO',
    'p21' : '( Exp )',
}

no_terminales = {
    'p0' : 'P\'',
    'p1' : 'P',
    'p2' : 'P',
    'p3' : 'Tipo',
    'p4' : 'Tipo',
    'p5' : 'Tipo',
    'p6' : 'V',
    'p7' : 'V',
    'p8' : 'A',
    'p9' : 'Exp',
    'p10' : 'Exp',
    'p11' : 'Exp',
    'p12' : 'E',
    'p13' : 'E',
    'p14' : 'E',
    'p15' : 'Term',
    'p16' : 'T',
    'p17' : 'T',
    'p18' : 'T',
    'p19' : 'F',
    'p20' : 'F',
    'p21' : 'F',
}


# Define las entradas de la tabla
tabla_sintactica = {
    ("q0", "ID"): "q7",("q0", "INT"): "q4",("q0", "FLOAT"): "q5",("q0", "CHAR"): "q6",("q0", "P"): "q1",("q0", "Tipo"): "q2",("q0", "A"): "q3",
    
    ("q1", "$"): "p0",
    
    ("q2", "ID"): "q8",
    
    ("q3", "$"): "p2",
    
    ("q4", "ID"): "p3",
    
    ("q5", "ID"): "p4",
    
    ("q6", "ID"): "p5",
    
    ("q7", "ASIGNACION"): "q9",

    ("q8", "COMA"): "q11",("q8", "PUNTOCOMA"): "q12",("q8", "V"): "q10",

    ("q9", "ID"): "q18",("q9", "NUMERO"): "q19",("q9", "MAS"): "q14",("q9", "MENOS"): "q15",("q9", "LPAREN"): "q20",("q9", "Exp"): "q13",("q9", "Term"): "q16",("q9", "F"): "q17",
    
    ("q10", "$"): "p1",
    
    ("q11", "ID"): "q21",
    
    ("q12", "ID"): "q7",("q12", "INT"): "q4",("q12", "FLOAT"): "q5",("q12", "CHAR"): "q6",("q12", "P"): "q22",("q12", "Tipo"): "q2",("q12", "A"): "q3",
    
    ("q13", "PUNTOCOMA"): "q23",
    
    ("q14", "ID"): "q18",("q14", "NUMERO"): "q19",("q14", "LPAREN"): "q20",("q14", "Term"): "q24",("q14", "F"): "q17",
    
    ("q15", "ID"): "q18",("q15", "NUMERO"): "q19",("q15", "LPAREN"): "q20",("q15", "Term"): "q25",("q15", "F"): "q17",

    ("q16", "PUNTOCOMA"): "p14",("q16", "MAS"): "q27",("q16", "MENOS"): "q28",("q16", "RPAREN"): "p14",("q16", "E"): "q26", #sdfdfsd

    ("q17", "PUNTOCOMA"): "p18",("q17", "MAS"): "p18",("q17", "MENOS"): "p18",("q17", "MULTIPLI"): "q30",("q17", "DIVISION"): "q31",("q17", "RPAREN"): "p18",("q17", "T"): "q29",
    
    ("q18", "PUNTOCOMA"): "p19",("q18", "MAS"): "p19",("q18", "MENOS"): "p19",("q18", "MULTIPLI"): "p19",("q18", "DIVISION"): "p19",("q18", "RPAREN"): "p19",

    ("q19", "PUNTOCOMA"): "p20",("q19", "MAS"): "p20",("q19", "MENOS"): "p20",("q19", "MULTIPLI"): "p20",("q19", "DIVISION"): "p20",("q19", "RPAREN"): "p20",

    ("q20", "ID"): "q18",("q20", "NUMERO"): "q19",("q20", "MAS"): "q14",("q20", "MENOS"): "q15",("q20", "LPAREN"): "q20",("q20", "Exp"): "q32",("q20", "Term"): "q16",("q20", "F"): "q17",

    ("q21", "COMA"): "q11",("q21", "PUNTOCOMA"): "q12",("q21", "V"): "q33",

    ("q22", "$"): "p7",

    ("q23", "$"): "p8",

    ("q24", "PUNTOCOMA"): "p14",("q24", "MAS"): "q27",("q24", "MENOS"): "q28",("q24", "RPAREN"): "p14",("q24", "E"): "q34",

    ("q25", "PUNTOCOMA"): "p14",("q25", "MAS"): "q27",("q25", "MENOS"): "q28",("q25", "RPAREN"): "p14",("q25", "E"): "q35",

    ("q26", "PUNTOCOMA"): "p11",("q26", "RPAREN"): "p11",

    ("q27", "ID"): "q18",("q27", "NUMERO"): "q19",("q27", "LPAREN"): "q20",("q27", "Term"): "q36",("q27", "F"): "q17",

    ("q28", "ID"): "q18",("q28", "NUMERO"): "q19",("q28", "LPAREN"): "q20",("q28", "Term"): "q37",("q28", "F"): "q17",

    ("q29", "PUNTOCOMA"): "p15",("q29", "MAS"): "p15",("q29", "MENOS"): "p15",("q29", "RPAREN"): "p15",

    ("q30", "ID"): "q18",("q30", "NUMERO"): "q19",("q30", "LPAREN"): "q20",("q30", "F"): "q38",

    ("q31", "ID"): "q18",("q31", "NUMERO"): "q19",("q31", "LPAREN"): "q20",("q31", "F"): "q39",

    ("q32", "RPAREN"): "q40",

    ("q33", "$"): "p6",

    ("q34", "PUNTOCOMA"): "p9",("q34", "RPAREN"): "p9",

    ("q35", "PUNTOCOMA"): "p10",("q35", "RPAREN"): "p10",

    ("q36", "PUNTOCOMA"): "p14",("q36", "MAS"): "q27",("q36", "MENOS"): "q28",("q36", "RPAREN"): "p14",("q36", "E"): "q41",

    ("q37", "PUNTOCOMA"): "p14",("q37", "MAS"): "q27",("q37", "MENOS"): "q28",("q37", "RPAREN"): "p14",("q37", "E"): "q42",

    ("q38", "PUNTOCOMA"): "p18",("q38", "MAS"): "p18",("q38", "MENOS"): "p18",("q38", "MULTIPLI"): "q30",("q38", "DIVISION"): "q31",("q38", "RPAREN"): "p18",("q38", "T"): "q43",

    ("q39", "PUNTOCOMA"): "p18",("q39", "MAS"): "p18",("q39", "MENOS"): "p18",("q39", "MULTIPLI"): "q30",("q39", "DIVISION"): "q31",("q39", "RPAREN"): "p18",("q39", "T"): "q44",

    ("q40", "PUNTOCOMA"): "p21",("q40", "MAS"): "p21",("q40", "MENOS"): "p21",("q40", "MULTIPLI"): "p21",("q40", "DIVISION"): "p21",("q40", "RPAREN"): "p21",

    ("q41", "PUNTOCOMA"): "p12",("q41", "RPAREN"): "p12",

    ("q42", "PUNTOCOMA"): "p13",("q42", "RPAREN"): "p13",

    ("q43", "PUNTOCOMA"): "p16",("q43", "MAS"): "p16",("q43", "MENOS"): "p16",("q43", "RPAREN"): "p16",

    ("q44", "PUNTOCOMA"): "p17",("q44", "MAS"): "p17",("q44", "MENOS"): "p17",("q44", "RPAREN"): "p17",
}

operadores = ["MAS","MENOS","MULTIPLI","DIVISION","LPAREN","RPAREN", "PUNTOCOMA"]

def analisisSinta(estado, token, pila, ide, tipoActual, tablaSemantica, pilaOperadores, pilaSemantica, declarando, errorSemantico, tipoResultante, intermedio, contaCodigo, VarsIntermedio, posfija, asig):
    
    accion = tabla_sintactica.get((estado, token), "Error")
    carac1 = accion[0]
    ban = False
    if carac1 == "q":
        tipoActual, declarando, errorSemantico, tipoResultante, intermedio, contaCodigo, VarsIntermedio, posfija, asig = desplazar(token, accion, pila, ide, tipoActual, tablaSemantica, pilaOperadores, pilaSemantica, declarando, errorSemantico, tipoResultante, intermedio, contaCodigo, VarsIntermedio, posfija, asig)
    elif carac1 == "p":
        accion = reducir(accion, pila)
        ban = True    
    #print(pila)
    return accion, ban, pila, tipoActual, declarando, errorSemantico, tipoResultante, intermedio, contaCodigo, VarsIntermedio, posfija, asig

def estado_reduccion(estado, token):
    estado_redu = tabla_sintactica.get((estado, token), "Error")
    return estado_redu

def desplazar(token, accion, pila, ide, tipoActual, tablaSemantica, pilaOperadores, pilaSemantica, declarando, errorSemantico, tipoResultante, intermedio, contaCodigo, VarsIntermedio, posfija, asig):
    pila.append(token)
    pila.append(accion)
    ############################################## AQUÍ ES DONDE SE COMIENZA A TRABAJAR CON EL SEMÁNTICO        
    ############### SE LLENA LA TABLA DE SIMBOLOS, LA PILA DE OPERADORES Y LA PILA SEMÁNTICA
    if token == "INT" or token == "FLOAT" or token == "CHAR":
        tipoActual = token
        declarando = True
    if token == "PUNTOCOMA":
        declarando = False    
    if declarando == True:
        if token == "ID":
            tablaSemantica = ASE.llenarTabla(tipoActual, ide, tablaSemantica)
            ###################################### EN ESTA PARTE MANDAMOS A LLAMAR AL GENERDOR DE CODIGO INTERMEDIO
            intermedio = GC.codigoDeclar(ide, intermedio, tipoActual)
    else:
        if token == "ID":
            pilaSemantica, errorSemantico = ASE.llenarPilaSemantica(ide, pilaSemantica, errorSemantico, tablaSemantica)
            ###################################### EN ESTA PARTE MANDAMOS A LLAMAR AL GENERDOR DE CODIGO INTERMEDIO           
            intermedio, contaCodigo, VarsIntermedio, asig = GC.codigoAsig(ide, intermedio, contaCodigo, VarsIntermedio, asig)

    if token == "NUMERO":
        pilaSemantica, errorSemantico = ASE.llenarPilaSemantica(token, pilaSemantica, errorSemantico, tablaSemantica)

        intermedio, contaCodigo, VarsIntermedio, asig = GC.codigoAsig(ide, intermedio, contaCodigo, VarsIntermedio, asig)
        posfija.append(ide)
        print("---------------------------------------POSFIJA")
        print(posfija)  

    if token in operadores:
        pilaOperadores, tipoResultante, intermedio, VarsIntermedio, posfija, contaCodigo = ASE.llenarPilaOperadores(ide, pilaOperadores, pilaSemantica, tipoResultante, intermedio, VarsIntermedio, posfija, contaCodigo)
    
    if declarando == False:
        if token == "PUNTOCOMA":
            intermedio = intermedio + asig
    
    #intermedio = GC.generarCodigo(ide, intermedio, declarando, tipoActual)
    #print("---------------------------------------------CÓDIGO INTERMEDIO")
    #print(intermedio)
    
    return tipoActual, declarando, errorSemantico, tipoResultante, intermedio, contaCodigo, VarsIntermedio, posfija, asig

def reducir(accion, pila):
    reduccion = produccioes[accion]
    lista_reduccion = reduccion.split()

    for x in lista_reduccion:
        pila.pop()
        pila.pop()
    no_terminal = no_terminales[accion]

    if no_terminal != "P'":
        pila.append(no_terminal)
        penultimo = pila[-2]
        accion2 = estado_reduccion(penultimo, no_terminal)
        pila.append(accion2)
        accion = accion2
        carac1 = accion[0]
    else:
        #msj = "FELICIDADES!!! CADENA VÁLIDA"
        #print(msj)
        accion = "ACEPTA"
    return accion
