#!/usr/bin/bash   python 5.py
#__*__   coding:utf-8   __*__
def main():
    print("ORDENAR 3 NÚMEROS")
    lista = []

    lista.append( int(input("Introduzca el primer número: ")) )
    lista.append( int(input("Introduzca el segundo número: ")) )
    lista.append( int(input("Introduzca el tercer número: ")) )

    lista.sort()

    print(lista)

if __name__ == "__main__":
    main()
    

    
