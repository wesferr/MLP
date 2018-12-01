#/usr/bin/python3
# -*- coding: utf-8 -*-
from opengl import *
import numpy as np

class adaline(object):
    def __init__(self, screen):
        self.W = np.random.rand(3)
        self.tela = screen
        self.bip = False

    def h(self, x):
        return np.dot(self.W.T, x)
        
    def f(self, x):
        if(self.bip):
          return np.tanh(10*self.h(x))
        else:
          return 1/(1 + np.exp(-4*self.h(x)))
        
    def atualizapeso(self, x, y, alpha):
        self.W = self.W + alpha * ( y - self.h(x) ) * x

    def erro(self, x, y):
        return np.sum([(j-self.f(i))**2 for i,j in zip(x,y)])

    def treina(self, x, y, tolerancia, passo, tela = 0):
        if(y.min() == -1):
          self.bip = True
        else:
          print("formato do input não suportado pelo adaline, por favor use o formato bipolar")
          exit()
        while (self.erro(x,y) > tolerancia):
            print(self.erro(x,y))
            for i, j in zip(x,y):
                if(tela):
                
                  for k, l in zip(x,y):
                    self.tela.circle(k[1],k[2],0 if (l == 0 or l == -1) else 1)
                  self.atualizapeso(i, j, passo)
                  self.tela.dreta(self.W)
                  self.tela.update()
                  
                else:
                  self.atualizapeso(i, j, passo)
        while True:      
          for i in range(1000):
            a = random.uniform(-2,2)
            b = random.uniform(-2,2)
            
            c = self.h([1,a,b])
            
            if(c > 0):
              self.tela.point(a,b,[1,0,0])
            else:
              self.tela.point(a,b,[0,1,0])
            self.tela.dreta(self.W)
          self.tela.update()
            
          
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

    _or  = np.array([-1, 1, 1, 1])
    _orbin  = np.array([0, 1, 1, 1])
    _and = np.array([-1, 1,-1,-1])
    _xor = np.array([-1,-1, 1, 1])

    b = screen()
    a = adaline(b)
    a.treina(bin, np.array([0, 1, 0, 0]), 0.0001, 0.01)
    a.mostra(bin)
        
if(__name__ == "__main__"):
  main()
  
