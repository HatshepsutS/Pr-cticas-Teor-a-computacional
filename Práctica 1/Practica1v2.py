# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:01:08 2021

@author: Enriquez Ballesteros Daniela Montserrat, Lopez de la Concha Cesar Alfonso Práctica 1
"""
import pandas as pd
import random 
import re
def rango():
    r1=1
    r2=0
    while r1>r2 or validalenghtAl(list(map(chr,range(r1,r2+1))))==False:
     r1=ord(input("Escriba un rango de caracteres para formar el alfabeto\nPrimer digito: "))
     r2=ord(input("Ultimo digito: ")) 
     if  r1>r2:
         print("Introduzca un rango valido ! ") 
    return list(map(chr,range(r1,r2+1)))
def caracterxcaracter():
    alfabeto2=[]
    c=1
    while c<3:
     c=int(input("Ingrese el numero de caracteres "))
     if  c<3:  
       print("El alfabeto debe tener minimo 3 caracteres!\n\n")  
    for x in range(c):
     alfabeto2.append(input())   
    return alfabeto2
def validalenghtAl(al3):
    if len(al3)<3:
        print("El alfabeto debe tener minimo 3 caracteres!\n\n")
        return False
    else: 
        return True
def menuAlfabeto(): 
    print("Elija la creacion de su alfabeto\n1. Por rango\n2.Caracter x caracter")
    opc=int(input())
    if(opc==1):
        alpha=rango()
    else:
         alpha=caracterxcaracter()
    return alpha

def validarCad(w1,alph1):
    for index in range(len(w1)):
        if w1[index] in alph1:
            continue
        else :
            print("Algún digito de la cadena no esta en el alfabeto, ingrese una correcta")
            return(False)
    return(True)

def buscarsubsequence(w1,w2):
   s = []
   for i in range(len(w2)):
     s.append(w2[i])
   for i in range(len(w1) - 1, -1, -1):
      if (len(s) == 0):
            return True 
      if (w1[i] == s[-1]):
          s.pop()
   if (len(s) == 0):
       return True
   else:
       return False    

def cadenas(alph1):
 opc=False

 while opc==False:
    w1=str(input(" Digite la cadena w1 "))
    opc=validarCad(w1,alph1)
     
 opc=False

 while opc==False:
    w2=str(input(" Digite la cadena w2 "))
    opc=validarCad(w2,alph1)
 
 if(w2.startswith(w1)):
    if w1==w2:  
        print (w1 +" es un prefijo propio de ",w2)
    else: 
        print (w1 +" es un prefijo impropio de ",w2)
 if(w2.endswith(w1)):
    if w1==w2:  
        print (w1 +" es un sufijo propio de ",w2)
    else: 
        print (w1 +" es un sufijo  impropio de ",w2)
 if w2.find(w1)!=-1:
    print(w1+" Es subcadena de ",w2+" y se encuentra en la posicion ",w2.find(w1))
 if buscarsubsequence(w2,w1):
    print(w1+" Es subsecuencia de ",w2)

 return 


def generarL(alph1,nstrings,lstrings):
  lenguaje = []
  for x in range(nstrings): 
   lenguaje.append(''.join(random.choice(alph1 + alph1) for _ in range(lstrings))) 
  return lenguaje


def concatenar(L1,L2):
 conc = []  
 for i in range(len(L1)):
    for j in range(len(L2)):
        conc.append(L1[i]+L2[j])
   
 return conc


def  menugenerarL(alph1):
 
 nstrings=int(input("Introduzca cuantas palabras tendra L1 ? "))
 lstrings=int(input("Introduzca la longitud de las palabras de L1 ? "))
 L1=generarL(alph1,nstrings,lstrings)
 nstrings=int(input("Introduzca cuantas palabras tendra L2 ? "))
 lstrings=int(input("Introduzca la longitud de las palabras de L2 ? "))
 L2=generarL(alph1,nstrings,lstrings)
 
 print("L1: ", L1)
 print("L2: ", L2)
 print ("LU: ",L1+L2 )
 print ("LC: ",concatenar(L1,L2))
 return 


def lenguajevscad(alph1): 
    print("Elija que hacer con su alfabeto\n1.Jugar con cadenas \n2.Crear lenguaje")
    opc=int(input())
    if(opc==1):
       cadenas(alph1)
    else:
         menugenerarL(alph1)
    return  

def eval_string(x:str):
    return re.match('^\d+$', x) is not None   

def expresionesReg():
   print("Inciso 7 opción B\n-------\nTodas las cadenas de dígitos que tengan por lo menos un dígito repetido. Los dígitos no tienen que estar en orden") 
   palabra=str(input("Escriba una palabra a analizar "))
   if eval_string(palabra):
      result = re.findall(r'(.)(?=.+\1)', palabra)
      if len(result)>0:  
          print("Palabra correcta")
      else:
          print("Palabra incorrecta")
   else:
      print("Palabra incorrecta")

def prac1():
   print("Seleccione una opcion \n1.Lenguajes y cadenas \n2.Expresiones Regulares")
   opc=int(input())
   if(opc==1):
      alph1=menuAlfabeto()
      print("Su alfabeto es: ", alph1)
      lenguajevscad(alph1) 
   else:
     expresionesReg()
   return 


prac1()
