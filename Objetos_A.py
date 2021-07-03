#PRIMER VIDEO DE PROGRAMACION EN PYTHON PARA PRINCIPIANTES.
#TEMA:  PROGRAMACION ORIENTADA A OBJETOS
#BY DAVID RUIZ


#Definimos y/o creamos nuestro objeto

class Persona:
    def __init__(self,nombre,colorojos,edad): 
        self.nombre = nombre
        self.colorojos = colorojos
        self.edad = edad


#Definimos el nombre de la clase
class Nombre: 
    def __init__(self,primernombre,apellido):
        self.primernombre = primernombre
        self.apellido = apellido



#Creamos una persona con color de ojos 'Verdes' con edad de 200 años y un nombre ''David'' con apellido ''Ruiz'' 

#Puedes editar tu nombre,apellido,color de ojos y edad en las letras naranjas.

myPersona = Persona(Nombre('David','Ruiz'), 'Verdes',100) 
print(myPersona.nombre.primernombre)
print(myPersona.nombre.apellido)
print(myPersona.colorojos)
print(myPersona.edad) 