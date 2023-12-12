def codigoDeclar(ide, intermedio, tipoActual):        
    intermedio = intermedio + tipoActual.lower() + " " + ide + ";" + "\n"
    print("-------------------------------------CÓDIGO INTERMEDIO")
    print(intermedio)
    return intermedio

def codigoAsig(ide, intermedio, contaCodigo, VarsIntermedio, asig):
    
    if contaCodigo == 0:
        asig = ide + " = V1 \n"
        #intermedio = intermedio + asig
        contaCodigo += 1
    else:
        VarsIntermedio.append(contaCodigo)
        pegar  = "V" + str(contaCodigo) + " = " + ide
        intermedio = intermedio + pegar + "\n"
        contaCodigo += 1

    #intermedio = intermedio + asig + "\n"

    print("-------------------------------------CÓDIGO INTERMEDIO")
    print(intermedio)
    return intermedio, contaCodigo, VarsIntermedio, asig


def operar(operador, intermedio, VarsIntermedio, posfija, contaCodigo):
    v2 = VarsIntermedio.pop()
    v1 = VarsIntermedio.pop()
    operacion = "V" + str(v1) + " = " + "V" + str(v1) + " " + operador + " V" + str(v2)
    intermedio = intermedio + operacion + "\n"
    VarsIntermedio.append(v1)
    contaCodigo -= 1
    return intermedio, posfija, contaCodigo