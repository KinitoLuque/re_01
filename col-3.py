#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Crea una lista de números enteros con datos introducidos por teclado. Tu programa
#debe sumarlos

def sumali(lista):
	suma = 0
	for numero in lista:
		if numero <=0:
			suma = suma + numero
		else:
			suma = suma + numero
	return suma
