#!/usr/bin/env python
#_*_	coding:utf-8 _*_
def main(): 
	print("CONVERTIR GRADOS CELSIUS A GRADOS FAHRENHEIT")
	numero_1 = float(input("Escriba un número:"))
	media = numero_1 * 9/5+32
	print("El paso de grados celsius a grados fahrenheit es" + str(numero_1) + "es" + str(media))
	#otra forma
	print("El paso de grados celsius a grados fahrenheit es" ,numero_1," es ",media)
	#otra forma
	print("El paso de grados celsius a grados fahrenheit {} es {}". format(numero_1,media))

if __name__ == "__main__":
	main()
	
