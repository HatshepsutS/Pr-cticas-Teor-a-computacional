# -*- coding: utf-8 -*-


import shutil

class Automata:

    def __init__(self,texto):
        self.texto=texto
    def AnalizadorLexico(self):   
        nums0 = ['1', '2', '3','4','5','6','7','8','9'] 
        octalist = ['0','1','2', '3','4','5','6','7'] 
        hexa = ['A','B','C', 'D','E','F']   

        self.estado='inicio' 
        for i in range(0,len(self.texto)):
            self.transicion=self.texto[i]
            ##print(self.estado,self.transicion)
            
            ##Estado inicial
            if self.estado == "inicio":
                if self.transicion in nums0:
                    self.estado="auxDec"
                elif self.transicion=='+' or self.transicion=='-':
                    self.estado="signo" 
                elif self.transicion=='0':
                    self.estado="Cero"  
                elif self.transicion=='/':
                    self.estado="com"      
                elif self.transicion.isalpha()  or self.transicion=='_' or self.transicion=='$':
                    self.estado="Alpha"                      
                else:
                    return False

            ##Estado 'auxDec'    
            elif self.estado =="auxDec": 
                if self.transicion == '.':
                  self.estado='puntoE'    
                elif str.isdigit(self.transicion):
                  self.estado='Decimal' 
                else: 
                    return False
                
            ##Estado 'puntoD'    
            elif self.estado =="puntoD": 
                if str.isdigit(self.transicion):
                  self.estado='DecimalsE' 
                else: 
                    return False
        
        
        
            ##Estado 'Decimal'    
            elif self.estado =="Decimal": 
                if self.transicion == '.':
                  self.estado='puntoD'  
                elif str.isdigit(self.transicion):
                  self.estado='Decimal' 
                else: 
                    return False
                
            ##Estado 'puntoE'    
            elif self.estado =='puntoE':
                if str.isdigit(self.transicion):
                  self.estado='DecimalsE2'      
                else: 
                    return False

            
            ##Estado 'DecimalsE'    
            elif self.estado =='DecimalsE':
                if str.isdigit(self.transicion):
                  self.estado='DecimalsE' 
                else: 
                    return False   
                
            ##Estado 'DecimalsE2'    
            elif self.estado =='DecimalsE2':
                if str.isdigit(self.transicion):
                  self.estado='DecimalsE2' 
                elif self.transicion=='E':
                  self.estado='E'                   
                else: 
                    return False                   
                
            ##Estado 'signo'    
            elif self.estado =='signo':
                if self.transicion in nums0:
                  self.estado='auxDec'
                elif self.transicion == '0':
                  self.estado='Cero'   
                else: 
                    return False    
                
            ##Estado 'aux'    
            elif self.estado =='aux':
                if str.isdigit(self.transicion):
                  self.estado='DecimalsE0'  
                else: 
                    return False   
                
            ##Estado 'DecimalsE0'    
            elif self.estado =='DecimalsE0':
                if str.isdigit(self.transicion):
                  self.estado='DecimalsE0' 
                elif self.transicion=='E':
                  self.estado='E'                    
                else: 
                    return False   

                
                
            ##Estado 'cero'    
            elif self.estado =='Cero':
                if self.transicion =='.':
                  self.estado='aux' 
                elif self.transicion in octalist:
                  self.estado='Octal'  
                elif self.transicion=='X'or self.transicion=='x':
                  self.estado='0X'                    
                else: 
                    return False 
                
             ##Estado 'E'
            elif self.estado =='E':
                if self.transicion=='+' or self.transicion=='-':   
                    self.estado='Signo2'
                elif str.isdigit(self.transicion):
                    self.estado='digitE'
                else: 
                    return False  
                
            ##Estado 'Octal'  
            elif  self.estado=='Octal':
                if self.transicion in octalist:
                    self.estado='Octal'
                else :
                    return False
                
             ##Estado 'digitE'
            elif self.estado =='digitE':
                if str.isdigit(self.transicion):
                    self.estado='DecimalExp'
                else: 
                    return False
                
              ##Estado 'Signo2'
            elif self.estado =='Signo2':              
                if str.isdigit(self.transicion):
                    self.estado='digitE'
                else: 
                    return False

            ##Estado 'cero-x'    
            elif self.estado =='0X':
                if str.isdigit(self.transicion) or self.transicion in hexa:
                  self.estado='Hexadecimal'                     
                else:
                  return False

            ##Estado 'Hexadecimal'          
            elif self.estado =='Hexadecimal':
                if str.isdigit(self.transicion) or self.transicion in hexa:
                  self.estado='Hexadecimal' 
                else:
                 return False

            ##Estado 'com'          
            elif self.estado =='com':
                if self.transicion=='*':
                    self.estado='*'
                elif self.transicion=='/':
                   self.estado='Comentario'
                else: 
                    return False
                
            ##Estado '*'          
            elif self.estado =='*':
                if self.transicion=='*':
                    self.estado='com2'
                else: 
                    self.estado='*'
                
            ##Estado 'com2'          
            elif self.estado =='com2':
                if self.transicion=='/':
                    self.estado='ComentarioAs'
                else: 
                    return False

            elif self.estado =='Comentario':  
                return True

            
            ##Estado 'Alpha'          
            elif self.estado =='Alpha':
                if self.transicion.isalnum() or self.transicion=='_' or self.transicion=='$':
                    self.estado='Alpha'
         
                else: 
                   return False

           
            else:
              return False          
        
        if self.estado=="DecimalsE":
            return True
        elif self.estado=="DecimalsE2":
            return True    
        elif self.estado=="DecimalsE0":
            return True        
        elif self.estado=="Decimal":
            return True
        elif self.estado=="Octal":
            return True
        elif self.estado=="DecimalExp":
            return True               
    
        elif self.estado=="Hexadecimal":
            return True 
        elif self.estado=="Comentario":
            return True
        elif self.estado=="ComentarioAs":
            return True 
        elif self.estado=="auxDec":
            return True 
        elif self.estado=="Alpha":
            return True         
        elif self.estado=="*":
            return False                    
        


    

def main():

    count = 0 
    b=0
    archivos()
    with open('copy.txt','r') as file:
     for line in file:
        count=count+1
  
        
        for word in line.split():
            if checkpalabrasReservadas(word)==False :

               AFD=Automata(word) 
         
               if AFD.AnalizadorLexico() == False:
                b=1   
                print("Error en la linea " +str(count))     
            
    if b!=1:
     print("No se han encontrado errores gramaticales en el archivo")   

  
   
    
def archivos():
    original = r'EjemploPrac3caAnalizador.java'
    target = r'copy.txt'

    shutil.copyfile(original, target)   
    
    with open('copy.txt', 'r') as file :
     filedata = file.read()
     
    filedata = filedata.replace(';',' ') 
    filedata = filedata.replace(',',' ')  
    filedata = filedata.replace('=',' ')  
    filedata = filedata.replace('(',' ')  
    filedata = filedata.replace(')',' ')
    filedata = filedata.replace('{',' ')
    filedata = filedata.replace('>',' ') 
    filedata = filedata.replace('<',' ')   
    filedata = filedata.replace('}',' ') 
    filedata = filedata.replace('[',' ') 
    filedata = filedata.replace(']',' ')  
    filedata = filedata.replace('"',' ')          
    
    with open('copy.txt', 'w') as file:
     file.write(filedata)    

def checkpalabrasReservadas(word):
  with open('Palabras reservadas de java.txt') as file:
    contents = file.read()
  if word in contents:
    return True
  else:
    return False


if __name__ == "__main__":
    main()