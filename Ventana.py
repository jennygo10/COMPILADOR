import ply.lex as lex
from tkinter import *
import AnalizadorLexico as AL
import AnalizadorSintactico as AS

ventana = Tk()
ventana.title("AnalizadorLexico")
ventana.geometry("1300x650")
ventana.config(bg='#282828')
ventana.resizable(False, False)

entrada = StringVar()

f = Frame()
f.pack()
f.config(width="1300", height="650", bg="#282828")
#f.place(x=10, y =10)

##########################  SE DEFINE TODOS LOS CUADROS DE TEXTO Y LABELS
l1 = Label(f, width="20", height="1", bg="#282828", fg='white', font=("Arial Black", 10), text="Código fuente", anchor="w")
l1.grid(sticky="w")
l1.place(x=20, y=10)

c1 = Text(f, width="61", height="26", fg='white', font=("Arial", 14), background='#1F1F1F', insertbackground='white')
c1.place(x=20, y=40)
scrollc1 = Scrollbar(f, command=c1.yview)
scrollc1.grid(sticky="nsew")
scrollc1.place(in_=c1, relx=1, relheight=1, bordermode="outside")
c1.config(yscrollcommand=scrollc1.set)

l2 = Label(f, width="10", height="1", bg="#282828", fg='white', font=("Arial Black", 10), text="Léxico", anchor="w")
l2.place(x=780, y=10)

c2 = Text(f, width="50", height="7", fg='white', font=("Arial", 12), background='#1F1F1F', insertbackground='white')
c2.place(x=780, y=40)
scrollc2 = Scrollbar(f, command=c2.yview)
scrollc2.grid(sticky="nsew")
scrollc2.place(in_=c2, relx=1, relheight=1, bordermode="outside")
c2.config(yscrollcommand=scrollc2.set)
c2.config(state="normal")

l3 = Label(f, width="10", height="1", bg="#282828", fg='white', font=("Arial Black", 10), text="Sintáctico", anchor="w")
l3.grid(sticky="w")
l3.place(x=780, y=180)

c3 = Text(f, wrap="none", width="50", height="7", fg='white', font=("Arial", 12), background='#1F1F1F', insertbackground='white')
c3.place(x=780, y=210)
scrollc3 = Scrollbar(f, command=c3.yview)
scrollc3.grid(sticky="nsew")
scrollc3.place(in_=c3, relx=1, relheight=1, bordermode="outside")
scroll_x = Scrollbar(f, orient=HORIZONTAL, command=c3.xview)
scroll_x.grid(sticky="nsew")
scroll_x.place(in_=c3, rely=1, relwidth=1, bordermode="outside")
c3.config(yscrollcommand=scrollc3.set, xscrollcommand=scroll_x.set)
c3.config(state="normal")

lCodigo = Label(f, width="15", height="1", bg="#282828", fg='white', font=("Arial Black", 10), text="Código intermedio", anchor="w")
lCodigo.place(x=780, y=370)

cCodigo = Text(f, width="50", height="6", fg='white', font=("Arial", 12), background='#1F1F1F', insertbackground='white')
cCodigo.place(x=780, y=400)
scrollCodigo = Scrollbar(f, command=cCodigo.yview)
scrollCodigo.grid(sticky="nsew")
scrollCodigo.place(in_=cCodigo, relx=1, relheight=1, bordermode="outside")
cCodigo.config(yscrollcommand=scrollCodigo.set)
cCodigo.config(state="normal")

l4 = Label(f, width="10", height="1", bg="#282828", fg='white', font=("Arial Black", 10), text="Errores", anchor="w")
l4.grid(sticky="w")
l4.place(x=780, y=515)

c4 = Text(f, width="50", height="2", fg='red', font=("Arial", 12), background='#1F1F1F', insertbackground='white')
c4.place(x=780, y=540)
#c4.config(yscrollcommand=scrollc4.set)
c4.config(state="normal")

l5 = Label(f, width="16", height="1", bg="#282828", fg='green', font=("Arial Black", 20))
l5.grid(sticky="w")
l5.place(x=855, y=580)

###################################################################### PROGRAMACIÓN
#################################################  FUNCION ANALIZAR
def analizar():
    entrada = c1.get("1.0","end-1c")
    print(entrada)
    c2.delete("1.0","end")
    c3.delete("1.0","end")
    c4.delete("1.0","end")
    cCodigo.delete("1.0","end")
    l5.config(text="")

    a=AL.analisis(entrada)
    tokens, errorLexico = hacerTokens(a)
    print("--------------------------------------------ANALIZADOR LÉXICO--------------------------------------------")    
    print(tokens)

    #print("--------------------------------------------ANALIZADOR SINTÁCTICO--------------------------------------------")
    asig = ""
    posfija = []
    VarsIntermedio = []
    contaCodigo = 0
    intermedio = ""
    tipoResultante = ""
    errorSemantico = False
    declarando = False
    tipoActual = ""
    tablaSemantica = []
    pilaOperadores = []
    pilaSemantica = []
    estado = "q0"
    i = 0
    pila = ["$", "q0"]
    if entrada != "" and errorLexico == False:
        c3.insert(INSERT, str(pila)+"\n")
        while i < len(tokens):
            tupla = tokens[i]
            token = tupla[0]
            #EL NÚMERO DE LÍNEA SE CAMBIA AQUÍ PARA CONTROLAR CUANDO FALTA EL ÚLTIMO TOKEN DE LA LÍNEA
            if token != "$":
                numLinea = tupla[1]
                ide = tupla[2]
            #ide = tupla[2]
            #AQUÍ SE MADA LLAMAR AL ANALIZADOR SINTÁCTICO
            estado, ban, pila, tipoActual, declarando, errorSemantico, tipoResultante, intermedio, contaCodigo, VarsIntermedio, posfija, asig = AS.analisisSinta(estado, token, pila, ide, tipoActual, tablaSemantica, pilaOperadores, pilaSemantica, declarando, errorSemantico, tipoResultante, intermedio, contaCodigo, VarsIntermedio, posfija, asig)
            c3.insert(INSERT, str(pila)+"\n")
            if estado == "Error":
                c4.insert(INSERT, f"ERROR SINTÁCTICO en línea {numLinea}\n")
                break
            ################## EN ESTA PARTE SE VERIFICAN LOS ERRORES SEMANTICOS
            elif errorSemantico == True:
                c4.insert(INSERT, f"ERROR SEMÁNTICO en línea {numLinea}. Variable \"{ide}\" no declarada\n")
                break
            elif tipoResultante == "ErrorTipo":
                c4.insert(INSERT, f"ERROR SEMÁNTICO en línea {numLinea}. Tipos de datos incompatibles\n")
                break
            elif estado == "ACEPTA":
                l5.config(text="CADENA ACEPTADA")
                cCodigo.insert(INSERT, intermedio)
                break

            #EN ESTA PARTE ES DONDE VERIFICAMOS SI SE AVANZARÁ O NO DE TOKEN
            if ban == True:
                pass
            else:
                i = i + 1
    #return a

def hacerTokens(a):
    errorLexico = False
    tokens = []
    for x in a:
        c2.insert(INSERT, x + "\n")
        if x != "Caracter ilegal":
            token = x.split(',')[0]
            token = token.split('(')[1]
            numLinea = x.split(',')[2]
            if token != "NUMERO":
                ide = x.split("'")[1]
            else:
                ide = x.split(",")[1]
            #print(ide)
            #ESTO RESUELVE CUANDO EL NUMERO DE LINEA ES '
            if token == "COMA":
                numLinea = x.split(',')[3]
                #ide = ","
            tokens.append((token, numLinea, ide))
        else:
            c4.insert(INSERT, f"ERROR LÉXICO: {x} en la línea {numLinea}\n")
            errorLexico = True
    tokens.append("$")
    return tokens, errorLexico

####################################################################  BOTON ANALIZAR
bAn = Button(f, text="Analizar", font=("Arial Black", 12), bg="#FFB800", fg="black", command=analizar)
bAn.place(x=615, y=10, width=100, height=25)

ventana.mainloop()