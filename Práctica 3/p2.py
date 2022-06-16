# -*- coding: utf-8 -*-
"""

"""
class AutomatadePila:
   
    def __init__(self,cadena):
        self.cadena=cadena
        self.stack = []
        
    def GIC(self): 
        
        signosEsp = ['+','-', '*','/','%'] 
        masomenos = ['+','-'] 
        self.estado='inicio' 
        
        for i in range(0,len(self.cadena)):
            self.transicion=self.cadena[i]
            """
            print(self.estado)
            print(self.transicion) 
            print(self.stack)
            """
           
            if self.estado=='inicio': 
               if self.transicion.isalpha() or self.transicion=='_':
                   self.estado='q1';
               else:
                   break;
                   
                   
            elif self.estado=='q1': 
                if self.transicion.isalnum() or self.transicion=='_':
                    self.estado='q1';
                elif self.transicion=='=':
                    self.estado='q2';
                else:
                    break;
                          
                    
            elif self.estado=='q2':
               if self.transicion=='(':
                    self.stack.append('(')  
                    self.estado='q2'
               elif self.transicion.isalpha() or self.transicion=='_': 
                    self.estado='q3'
               elif self.transicion.isdigit(): 
                    self.estado='q4' 
               elif self.transicion in masomenos:   
                   self.estado='q3'
               else:
                    break; 
                    
                    
            elif self.estado=='q3':
               if self.transicion.isalnum() or self.transicion=='_':      
                   self.estado='q3'
               elif self.transicion=='(':
                    self.stack.append('(')
                    self.estado='q3' 
               elif self.transicion==';': 
                   self.estado='q6' 
               elif self.transicion==')':  
                    self.stack.pop() 
                    self.estado='q5'                   
               elif self.transicion in signosEsp:
                    self.estado='q2';   
               else:
                    break; 
                  
                    
                  
            elif self.estado=='q4': 
               if self.transicion.isdigit():
                  self.estado='q4'
               elif self.transicion in signosEsp: 
                  self.estado='q2'
               elif self.transicion==')': 
                  self.stack.pop() 
                  self.estado='q5' 
               elif self.transicion==';': 
                  self.estado='q6' 
               else:
                    break;
                    
            elif self.estado=='q5':                   
                if self.transicion in signosEsp:
                   self.estado='q2'
                elif self.transicion==')':
                   self.stack.pop()
                   self.estado='q5'
                elif self.transicion==';':
                   self.estado='q6'
                else:
                    break;
           

        if not self.stack and self.estado=='q6':
            return True
        

def main():
 print("PRACTICA 3. Gramaticas independientes del contexto (GIC).")
 word = input("Introduzca la palabra ")
 checkPalabra=AutomatadePila(word)   
 if checkPalabra.GIC()==True:
      print('Palabra Aceptada!')
 else:
     print('Palabra no Aceptada! ')
     
if __name__ == "__main__":
    main()
