#/usr/bin/python3
# -*- coding: utf-8 -*-
from opengl import *
import numpy as np

class perceptron(object):
    def __init__(self, screen):
        self.W = np.random.rand(3)
        self.tela = screen
        self.bin = True

    def h(self, x):
        return np.dot(self.W.T, x)

    def f(self, x):
        if(self.bin):
          return 1/(1 + np.exp(-4*self.h(x)))
        else:
          return np.tanh(10*self.h(x))
        
    def atualizapeso(self, x, y, alpha):
        self.W = self.W + alpha * ( y - self.f(x) ) * x

    def erro(self, x, y):
        erro = 0
        for i, j in zip(x,y):
            erro += (j - self.f(i))**2
        return erro

    def treina(self, x, y, tolerancia, passo, tela = 0):
      
        while (self.erro(x,y) > tolerancia):
            if(y.min() == -1):
              self.bin = False
            print(self.erro(x,y))
            for i, j in zip(x,y):
                if(tela):
                  
                  for k, l in zip(x,y):
                    self.tela.circle(k[1],k[2],0 if (l == 0 or l == -1) else 1)
          
                  self.atualizapeso(i, j, passo)
                  self.tela.dreta(self.W);
                  self.tela.update()
                  
                else:
                
                  self.atualizapeso(i, j, passo)
                

    def mostra(self, x):
      for i in x:
        print(i, self.f(i))

def main():

    bip = np.array([[1.0 , -1.0, -1.0],
                    [1.0 ,  1.0,  1.0],
                    [1.0 , -1.0,  1.0],
                    [1.0 ,  1.0, -1.0]])

    bin = np.array([[1.0 , 0.0, 0.0],
                    [1.0 , 1.0, 1.0],
                    [1.0 , 0.0, 1.0],
                    [1.0 , 1.0, 0.0]])

    _or  = np.array([0, 1, 1, 1])
    _orbip = np.array([-1,1,1,1])
    _and = np.array([0, 1, 0, 0])
    _xor = np.array([0, 0, 1, 1])
    
    b = screen()
    a = perceptron(b)
    a.treina(bin,_or, 0.0001, 0.01)
    a.mostra(bin)
        

if(__name__ == "__main__"):
  main()
