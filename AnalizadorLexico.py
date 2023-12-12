import ply.lex as lex
import re
import codecs
import os
import sys
from tkinter import *

tokens = [
    "RESERVADA",
    "ID",
    "TIPO",
    "INT",
    "FLOAT",
    "CHAR",
    "NUMERO",
    "MAS",
    "MENOS",
    "MULTIPLI",
    "DIVISION",
    "ASIGNACION",

    "IGUAL",
    #"DIFERENTE",
    #"MAYORQUE",
    #"MENORQUE",
    #"MAYORIGUAL",
    #"MENORIGUAL",

    #"PUNTO",
    "COMA",
    #"DOSPUNTOS",
    "PUNTOCOMA",
    "COMILLASSIMPLE",
    #"COMILLADOBLE",
    "LPAREN",
    "RPAREN",
    #"LLLAVE",
    #"RLLAVE",
    #"LCORCHETE",
    #"RCORCHETE"
]

reservadas = {
    'P':'INICIAL'

}

tipo = {
    'int':'INT',
    'float':'FLOAT',
    'char':'CHAR'
}

tokens = tokens + list(reservadas.values()) + list(tipo.values())

t_ignore = ' \t\r'

#OPERADORES MATEMATICOS
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULTIPLI = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r'='

#OPERADORES RACIONALES
t_IGUAL = r'=='
#t_DIFERENTE = r'!='
#t_MAYORQUE = r'>'
#t_MENORQUE = r'<'
#t_MAYORIGUAL = r'>='
#t_MENORIGUAL = r'<='

#VARIABLES
#t_IDENTIFICADOR = r
#t_PUNTO = r'\.'
t_COMA = r'\,'
#t_DOSPUNTOS = r'\:'
t_PUNTOCOMA = r'\;'
t_COMILLASSIMPLE = r'\''
#t_COMILLADOBLE = r'"'

t_LPAREN = r'\('
t_RPAREN = r'\)'
#t_LLLAVE = r'\{'
#t_RLLAVE = r'\}'
#t_LCORCHETE = r'\['
#t_RCORCHETE = r'\]'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reservadas:
        t.type = reservadas[t.value]  # Establece el tipo del token como 'RESERVADA'
        #t.type = t.value
    elif t.value in tipo:
        t.type = tipo[t.value]  # Establece el tipo del token como 'TIPO'
        #t.type = t.value
    return t

def t_CHAR(t):
    r"'.*'"
    t.value = t.value[1]  # Obtiene el carácter del interior de las comillas simples
    return t

def t_SALTOLINEA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMENTARIO(t):
    r'\#.*'
    pass

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    #print("caracter ilegal ", str(t.value[0]))
    t.lexer.skip(1)
    return "Caracter ilegal"

a=[]

def analisis(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    a.clear()
    #salida = ''
    while True:
        tok = analizador.token()
        if not tok : break
        #print (tok)
        a.append(str(tok))
    return a

