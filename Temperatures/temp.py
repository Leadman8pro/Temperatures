#Joel H. Maisonet Ayala
#Comp315
#Prof. Hector Encarnación 

"""
Este trabajo consta de poder colocar 
la temperatura que desees y se convierta a celsius o 
fahrenheit

"""


#Creo una clase de temperatura para poder trabajar más comodamente
class Temperatura():
    
    #Función inicial de python (__init__) para guardarlos en listas cada uno
    def __init__(self):
        self.fahrenheit = []
        self.celsius = []
        
        
    #Función de solicitud para preguntar las temperaturas y cual quiere usar
    def solicitud(self):
        
        
        #Uso un búcle try para capturar errores en el código
        try:
         
          pregunta = int(input("Cuantas temperaturas quieres convertir? "))
     
        #Búcle for dependiendo de la variable pregunta
          for temp in range(pregunta):
            numero = float(input(f"Introduce las temperatura {temp}: "))
            print(f"Temperatura {temp}: {numero}")
            
            
            while True: 
             tipo = input("Esta temperatura esta en (f) o (c)? ").lower()
            
            #Escoge entre fahrenheit para pasarlo a celsius
             if tipo == "f":
                self.fahrenheit.append(numero)
                self.celsius.append((numero - 32) * 5/9) 
                
                #Detiene el while si escoge "f"
                break
                
            #Escoge entre celsius para pasarlo a fahrenheit
             elif tipo == "c":
                self.celsius.append(numero)
                self.fahrenheit.append((numero * 9/5) + 32) 
                
                #Se detiene el while si escoge "c"
                break
                
            #De marcar un dato erroneo sale esto:
             else:
                print("Ingresaste un dato erróneo, debe ser (f) o (c).")
          
          #Manejo errores 
        except Exception as error:
            print(f"Lo siento, tienes un error llamado: {error}")
            
        except TypeError as error:
            print(f"Lo siento, introdujo un {error}")
            
    #Función para mostrar los resultados
    def mostrar_resultados(self):
        print(f"\n{'-'*5} Original {'-'*5} {'-'*5} Convertida {'-'*5}")
        for i in range(len(self.fahrenheit)):
            print(f"Temperatura {i+1}: {self.fahrenheit[i]:.2f}°F => {self.celsius[i]:.2f}°C")


#Llamo a la clase para poder ver en la terminal 
tempe = Temperatura()

#Para ver lo que proceso
tempe.solicitud()
tempe.mostrar_resultados()

#Fin del código