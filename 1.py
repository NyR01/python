#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("CÁLCULO DE LA MEDIA DE DOS NÚMEROS")
    numero_1 = float(input("Escriba un número: "))
    numero_2 = float(input("Escriba otro número: "))
    media = (numero_1 + numero_2) / 2
    print("La media aritmética de " + str(numero_1) +" y "+str(numero_2) +" es "+ str(media))
    #otra forma
    print("La media aritmética de " ,numero_1," y ",numero_2," es ",media)
    #otra forma
    print("La media aritmética de {} y {} es {}".format(numero_1,numero_2,media))
 
if __name__ == "__main__":
    main()


