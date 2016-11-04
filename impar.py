#!/usr/bin/env python
#-*- coding: utf-8 -*-
def impar(lista):
	otralista = []
	impar = False
	for ele in lista:
		if impar:
			otralista.append(ele)
		impar = not impar
	return otralista
