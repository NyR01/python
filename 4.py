#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("CONVERTIR UNA CANTIDAD DE TIEMPO EN SEGUNDOS A EL FORMATO HORAS-MINUTOS-SEGUNDOS")
    segundos = int(input("Escriba una cantidad en segundos: "))
    
    horas = segundos / 3600
    resto 1 = segundos % 3600
    minutos = resto 1//60
    resto = resto 1 % 60
    
    print("{0} segundos son {2} horas, {1} minutos y {3} segundos".format(segundos,minutos,horas,resto))
 
if __name__ == "__main__":
    main()

