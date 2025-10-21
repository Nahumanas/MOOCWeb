#Escribir un programa que pregunte al usuario una cantidad a invertir, 
#el interés anual y el número de años, y muestre por pantalla 
#el capital obtenido en la inversión cada año que dura la inversión.

inversion = float(input("Ingrese su inversion : "))

interes = float(input("Ingrese los interes : "))

años = int(input("Ingrese la cantidad de años : "))

count = 0

for año in range(1 , años + 1 ): 
    capital= inversion * ((1 + interes)**año)
    
    print(f"El capital obtenido en este {año} es :  {capital}" , "\n")