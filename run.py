#/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
from adaline import *
from perceptron import *
from backpropagation import *

def main():
  bip = np.array([[1.0 , -1.0, -1.0],
                  [1.0 ,  1.0,  1.0],
                  [1.0 , -1.0,  1.0],
                  [1.0 ,  1.0, -1.0]])

  bin = np.array([[1.0 , 0.0, 0.0],
                  [1.0 , 1.0, 1.0],
                  [1.0 , 0.0, 1.0],
                  [1.0 , 1.0, 0.0]])
                  
  _or1  = np.array([-1, 1, 1, 1])
  _and1 = np.array([-1, 1,-1,-1])
  _xor1 = np.array([-1,-1, 1, 1])
  
  _or2  = np.array([0, 1, 1, 1])
  _and2 = np.array([0, 1, 0, 0])
  _xor2 = np.array([0, 0, 1, 1])
  
  rede = [
    [neuron(3) for i in range(3)],
    [neuron(3) for i in range(2)],
    [neuron(2)]
  ]
  
  op = int(input("digite o codigo do algoritimo:\n0 - adaline\n1 - perceptron\n2 - backpropagation\ncod: "))
  intervalo = int(input("digite o codigo do intervalo:\n0 - bipolar\n1 - binario\nn: "))
  porta = int(input("digite o codigo da porta:\n0 - or\n1 - and\n2 - xor\nn: "))
  
  tolerancia = float(input("digite a tolerancia a erro: "))
  passo = float(input("digite o passo da convergencia: "))
  video = int(input("mostrar tela(0 - 1): "))
  
  if(intervalo):
    x = bin
    if(porta == 0):
      y = _or2
    if(porta == 1):
      y = _and2
    if(porta == 2):
      y = _xor2
  else:
    x = bip
    if(porta == 0):
      y = _or1
    if(porta == 1):
      y = _and1
    if(porta == 2):
      y = _xor1
  
  if(video):
    tela = screen()
  else:
    tela = None
  
  if(op == 0):
    ada = adaline(tela)
    ada.treina(x, y, tolerancia, passo, video)
    ada.mostra(x)
  
  if(op == 1):
    perc = perceptron(tela)
    perc.treina(x, y, tolerancia, passo, video)
    perc.mostra(x)
  
  if(op == 2):
    backprop = network(rede, tela)
    backprop.treina(x, y, tolerancia, passo, video)
    backprop.mostra(x)
    
if(__name__ == "__main__"):
  main()
