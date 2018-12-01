#/usr/bin/python3
# -*- coding: utf-8 -*-
from opengl import *
import numpy as np
from itertools import product

class neuron(object):
  def __init__(self, num):
    self.W = np.random.rand(num)
    self.y = 0
    self.sigma = 1
    self.bip = False
    
  def h(self, x):
    return np.dot(self.W.T, x)
    
  def f(self, x):
    if(self.bip):
      return np.tanh(10*self.h(x))
    else:
      return 1/(1 + np.exp(-2*self.h(x)))
    
  def fl(self, x):
    if(self.bip):
      return ( 1 / np.cosh(10*self.h(x)) ) ** 2
    else:
      return x*(1-x)
    
  def definesigma(self, x, i, j, rede):
    if(i == 0):
      self.sigma = self.fl(self.y) * np.sum( x - self.y )
    else:
      self.sigma = self.fl(self.y) * np.sum([ neuronio.W[j]*neuronio.sigma for neuronio in rede[i-1] ] )
    
  def atualizapeso(self, passo, x, i, rede): 
    if(i == 0):
      self.W = self.W + passo * self.sigma * x
    else:
      self.W = self.W + passo * self.sigma * np.array( [neuronio.y for neuronio in rede[i-1]] )
    
  def treina(self, x, bip):
    self.bip = bip
    self.y = self.f(x)
    
class network(object):
  def __init__(self, rede, tela = None):
    self.rede = rede
    self.tela = tela
    self.bip = False
    
  def treina(self, x, y, tolerancia, passo, tela = 0):
    it = 0
    
    if(y.min() == -1):
      print("operaçoes sobre entradas bipolares não suportada, use entradas binarias")
      exit()
      #self.bip = True
    
    while( self.erro(x) > tolerancia ):
      print( self.erro(x) )
      for i, j in zip(x, y):
        self.step1st(i)
        self.step2nd(i, j)
        self.step3rd(i, j, passo)
        it=it+1
        #print(it%100)
        
      if(tela and it%100 == 0):
        for k, l in zip(x,y):
          self.tela.circle(k[1],k[2],1 if (l == 0 or l == -1) else 0)
        
        for i in np.linspace(-2,2,30):
          for j in np.linspace(-2,2,30):
            
            c = self.step1st([1,i,j])
            
            if(c > 0.5):
              self.tela.point(i,j,[1,0,0])
            else:
              self.tela.point(i,j,[1,1,1])
        self.tela.update()
        
  def mostra(self, x):
    for i in x:
      self.step1st(i)
      print(i, [k.y for k in self.rede[-1]])
    
  def erro(self, x):
    local = 0
    for i in x:
      self.step1st(i)
      local += np.sum([abs(j.sigma) for j in self.rede[-1]])
    return local
    
  def step1st(self, x):
    for i, camada in enumerate(self.rede):
      for neuronio in camada:
        if(i == 0):
            neuronio.treina(x, self.bip)
        else:
            neuronio.treina( [j.y for j in self.rede[i-1]], self.bip)
    return self.rede[i-1][0].y
          
  def step2nd(self, x, y):
    rede = list(reversed(self.rede))
    for i, camada in enumerate(rede):
      for j, neuronio in enumerate(camada):
        neuronio.definesigma(y, i, j, rede)
          
  def step3rd(self, x, y, passo):
    for i,camada in enumerate(self.rede):
      for j,neuronio in enumerate(camada):
        neuronio.atualizapeso(passo, x, i, self.rede)
    
      
def main():

  bin = np.array([[1.0 , 0.0, 0.0],
                  [1.0 , 1.0, 1.0],
                  [1.0 , 0.0, 1.0],
                  [1.0 , 1.0, 0.0]])
                  
  _xor = np.array([0,0,1,1])
  _and = np.array([0,1,0,0])
  _or = np.array([0,1,1,1])

  rede = [
    [neuron(3) for i in range(3)],
    [neuron(3) for i in range(2)],
    [neuron(2)]
  ]
  
  backprop = network(rede)
  backprop.treina(bin, _and, 0.001, 0.1)
  backprop.mostra(bin)
  
  
if(__name__ == "__main__"):
  main()
