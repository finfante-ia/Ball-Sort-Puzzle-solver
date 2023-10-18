# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 02:24:19 2023

@author: finfa
"""

import copy
import time

class tubo:
    def __init__(self, bolas, largo=5):
        self.bolas=bolas
        self.largo=largo
        self.completo=False
        self.bloques=[]
        self.detbloques()
        self.revisarcompleto()
        
    def detbloques(self):
        self.bloques=[]
        last="zzzz"
        for i in range(len(self.bolas)):
            if self.bolas[i]==last:
                self.bloques[len(self.bloques)-1].append(last)
            else:
                self.bloques.append([self.bolas[i]])
            last=self.bolas[i]
                
    def primera(self):
        return self.bolas[len(self.bolas)-1]    
    
    def primerab(self):
        if len(self.bloques)>0:
            return self.bloques[len(self.bloques)-1][0], len(self.bloques[len(self.bloques)-1])
        else:
            return "",0
        
    def colocar(self, bola):
        if len(self.bolas)<self.largo:
            self.bolas.append(bola)
            self.revisarcompleto()
            self.detbloques()
            # actualizadisponible()
            return True
        else:
            return False

    def colocarb(self, bloquec):
        self.bloques.append(bloquec[:])
        self.bolas=sum(self.bloques,[])
        self.detbloques()
        self.revisarcompleto()
        # actualizadisponible()
            
    def sacarb(self):
        bloque=self.bloques[-1]
        self.bloques=self.bloques[:-1]
        self.bolas=sum(self.bloques,[])
        self.revisarcompleto()
        return bloque
            
    def revisarcompleto(self):
        if len(self.bolas)==self.largo and len(set(self.bolas))==1:
            self.completo = True
        else:
            self.completo=False
            
        if len(self.bolas)==0:
            self.vacio=True
        else:
            self.vacio=False
    
    def sacar(self):
        bola = self.primera()
        self.bolas=self.bolas[:-1]
        self.detbloques()
        self.completo=False
        self.revisarcompleto()
        return bola
        
    def escompleto(self):
        return self.completo
    
    def esvacio(self):
        return self.vacio

    def hayespacio(self):
        return len(self.bolas)<self.largo
    
    def texto(self):
        return ''.join(self.bolas)
        

tini=[]

# tini.append(tubo([*'4632'],largo=4))
# tini.append(tubo([*'71B3'],largo=4))
# tini.append(tubo([*'198C'],largo=4))
# tini.append(tubo([*'2169'],largo=4))
# tini.append(tubo([*'587B'],largo=4))
# tini.append(tubo([*'A18B'],largo=4))
# tini.append(tubo([*'4568'],largo=4))
# tini.append(tubo([*'265A'],largo=4))
# tini.append(tubo([*'743C'],largo=4))
# tini.append(tubo([*'4973'],largo=4))
# tini.append(tubo([*'A25B'],largo=4))
# tini.append(tubo([*'9CCA'],largo=4))
# tini.append(tubo([],largo=4))
# tini.append(tubo([],largo=4))


# tini.append(tubo(['3', '3', 'B', '5', '1'],largo=5))
# tini.append(tubo(['4', 'C', 'B', '5', '5'],largo=5))
# tini.append(tubo(['6', '7', '2', '5', '4'],largo=5))
# tini.append(tubo(['9', '7', 'A', '1', '2'],largo=5))
# tini.append(tubo(['3', '4', '5', '6', '8'],largo=5))
# tini.append(tubo(['7', '9', 'A', 'C', '2'],largo=5))
# tini.append(tubo(['3', '9', 'C', 'A', '2'],largo=5))
# tini.append(tubo(['8', '2', 'B', '8', '6'],largo=5))
# tini.append(tubo(['9', '4', 'B', '6', 'C'],largo=5))
# tini.append(tubo(['1', 'A', 'A', '4', 'C'],largo=5))
# tini.append(tubo(['9', '6', 'B', '1', '7'],largo=5))
# tini.append(tubo(['7', '1', '8', '8', '3'],largo=5))
# tini.append(tubo([],largo=5))
# tini.append(tubo([],largo=5))


# tini.append(tubo([*'123'],largo=3))
# tini.append(tubo([*'321'],largo=3))
# tini.append(tubo([*'231'],largo=3))
# tini.append(tubo([],largo=3))
# tini.append(tubo([],largo=3))

# tini.append(tubo([*'12'],largo=2))
# tini.append(tubo([*'21'],largo=2))
# tini.append(tubo([],largo=2))


tini.append(tubo([*'5B832'],largo=5))
tini.append(tubo([*'B5364'],largo=5))
tini.append(tubo([*'C8369'],largo=5))
tini.append(tubo([*'49B43'],largo=5))
tini.append(tubo([*'3C775'],largo=5))
tini.append(tubo([*'4615C'],largo=5))
tini.append(tubo([*'76BB1'],largo=5))
tini.append(tubo([*'22788'],largo=5))
tini.append(tubo([*'8A92A'],largo=5))
tini.append(tubo([*'1A9A5'],largo=5))
tini.append(tubo([*'C617C'],largo=5))
tini.append(tubo([*'294A1'],largo=5))
tini.append(tubo([],largo=5))
tini.append(tubo([],largo=5))


def lista_tubos(tubos):
  t=[]
  
  for tubo in tubos:
    t.append("".join(tubo.bolas))
  
  l=t[:]
  t.sort()
  return ",".join(t), ",".join(l)

# tab_ordenado, tablero=lista_tubos(tini)

def lee_tablero(tabtxt):
    ts=[]
    for t in tabtxt.split(","):
        ts.append(tubo([*t],largo=4))
    return ts


def esposible(s,d,tubos):

    if s==d:
        return False
    
    if tubos[s].completo or tubos[d].completo:
        return False
    
    bola_s, num_s=tubos[s].primerab()
    bola_d, num_d=tubos[d].primerab()
        
    if num_s==0 or num_s==tubos[s].largo:
        return False
    
    if num_s==len(tubos[s].bolas) and num_d==0:
        return False
    
    if num_d==0:
        return True
    
    if len(tubos[d].bolas)+num_s>tubos[d].largo:
        return False
    
    if bola_s!=bola_d:
        return False
    
    return True


def moverb(s,d,tubos):
    tubos[d].colocarb(tubos[s].sacarb())

def moverf(s,t,tubos):
    tubos[t].colocar(tubos[s].sacar())

def escompleto(tubos):
    for t in tubos:
        if t.completo==False and t.vacio==False:
            return False
    return True



def profundidad_2(tini):
    tab_ordenado, tab=lista_tubos(tini)
    movimiento=[]
    
    movimiento.append([0,'0',0,0])
    
    tableros=[]
    tableros.append(tini)
    
    tab_ordenados=[]
    tab_ordenados.append(tab_ordenado)
    
    # tabs=[]
    # tabs.append(tab)
    
    n=len(tini)
    
    i=0
    
    for tablero in tableros:
        # t=copy.deepcopy(tablero)
        tab_ordenado, tab=lista_tubos(tablero)
        for s in range(n):
            if (not tablero[s].escompleto()) or (not tablero[s].esvacio()):
                for d in range(n):
                    if tablero[d].hayespacio():
                        if esposible(s,d,tablero):
                            # tn=tablero
                            bola,num=tablero[s].primerab()
                            moverb(s,d,tablero)
                            tab_ordenado, tab=lista_tubos(tablero)
                            if tab_ordenado not in tab_ordenados:
                                tab_ordenados.append(tab_ordenado)
                                # tabs.append(tab)
                                tableros.append(copy.deepcopy(tablero))
                                movimiento.append([i,bola,s,d])
                                if escompleto(tablero):
                                    return movimiento, len(tableros)
                            for j in range(num):
                                moverf(d,s,tablero)
                            tab_ordenado, tab=lista_tubos(tablero)
        i+=1
                        
                        
def profundidad(tini):
    tab_ordenado, tab_ini=lista_tubos(tini)
    movimiento=[]
    
    movimiento.append([0,'0',0,0])
    
    tableros=[]
    tableros.append(tini)
    
    tab_ordenados=[]
    tab_ordenados.append(tab_ordenado)
    
    tabs=[]
    tabs.append(tab_ini)
    
    n=len(tini)
    
    i=0
    
    for tablero in tableros:
        # t=copy.deepcopy(tablero)
        for s in range(n):
            for d in range(n):
                if esposible(s,d,tablero):
                    tn=copy.deepcopy(tablero)
                    bola,num=tn[s].primerab()
                    moverb(s,d,tn)
                    tab_ordenado, tab=lista_tubos(tn)
                    if tab_ordenado not in tab_ordenados:
                        tab_ordenados.append(tab_ordenado)
                        tabs.append(tab)
                        tableros.append(copy.deepcopy(tn))
                        movimiento.append([i,bola,s,d])
                        if escompleto(tn):
                            return movimiento, tabs
        i+=1                        
                    
                    
                    
t=time.time()  
            
movs, revisados =profundidad_2(tini)    
# movs, ordenados =profundidad(tini)  

movimiento=movs[-1][0]
pasos=[]
pasos.append(movs[-1][1:])
while movimiento!=0:
    pasos.append(movs[movimiento][1:])
    movimiento=movs[movimiento][0]

pasos.reverse()
print(pasos)
print("Pasos ", len(pasos))
print("Revisados ", revisados)

print("Tiempo ",(time.time()-t))   







