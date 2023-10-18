# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:57:39 2020

@author: finfa
"""

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

    def hayespacio(self):
        return len(self.bolas)<self.largo
    
    def texto(self):
        return ''.join(self.bolas)
        

        
tubos=[]

# tubos.append(tubo(['5','B','8','3','2']))
# tubos.append(tubo(['B','5','3','6','4']))
# tubos.append(tubo(['C','8','3','6','9']))
# tubos.append(tubo(['4','9','B','4','3']))
# tubos.append(tubo(['3','C','7','7','5']))
# tubos.append(tubo(['4','6','1','5','C']))
# tubos.append(tubo(['7','6','B','B','1']))
# tubos.append(tubo(['2','2','7','8','8']))
# tubos.append(tubo(['8','A','9','2','A']))
# tubos.append(tubo(['1','A','9','A','5']))
# tubos.append(tubo(['C','6','1','7','C']))
# tubos.append(tubo(['2','9','4','A','1']))
# tubos.append(tubo([]))
# tubos.append(tubo([]))

# tubos.append(tubo(['7', '2', 'A', '4', '7']))
# tubos.append(tubo(['3', '3', '3', '8', '9']))
# tubos.append(tubo(['6', 'A', '8', '2', '5']))
# tubos.append(tubo(['8', '7', 'C', 'A', '6']))
# tubos.append(tubo(['A', '6', '1', '3', 'B']))
# tubos.append(tubo(['B', '6', '1', '2', 'B']))
# tubos.append(tubo(['9', '4', '9', '4', '2']))
# tubos.append(tubo(['1', '4', 'B', 'C', '9']))
# tubos.append(tubo(['4', '3', '5', '1', '6']))
# tubos.append(tubo(['5', 'A', '5', '1', 'C']))
# tubos.append(tubo(['2', '8', '5', 'C', 'B']))
# tubos.append(tubo(['8', '7', '7', 'C', '9']))



# tubos.append(tubo(['8', '7', '4', '1', '7']))
# tubos.append(tubo(['4', 'B', '3', '7', '4']))
# tubos.append(tubo(['A', '4', '8', '8', '8']))
# tubos.append(tubo(['A', '5', '1', '9', 'B']))
# tubos.append(tubo(['3', '5', '1', '6', '5']))
# tubos.append(tubo(['2', '3', '8', '4', 'C']))
# tubos.append(tubo(['1', 'A', '6', '2', '6']))
# tubos.append(tubo(['2', 'B', '6', '5', 'B']))
# tubos.append(tubo(['3', 'A', 'C', 'C', 'A']))
# tubos.append(tubo(['1', '9', '6', '2', 'C']))
# tubos.append(tubo(['C', '3', '9', '7', '9']))
# tubos.append(tubo(['5', 'B', '9', '2', '7']))

# tubos.append(tubo(['4', '7', '3', '9', '9']))
# tubos.append(tubo(['B', '4', 'A', '5', '6']))
# tubos.append(tubo(['B', '2', '3', '1', '7']))
# tubos.append(tubo(['7', '7', 'A', '8', 'C']))
# tubos.append(tubo(['B', '5', '1', '8', '2']))
# tubos.append(tubo(['C', '6', '8', '3', '4']))
# tubos.append(tubo(['A', '8', 'A', 'B', '9']))
# tubos.append(tubo(['3', '6', 'B', '8', '5']))
# tubos.append(tubo(['5', '1', '1', 'C', 'C']))
# tubos.append(tubo(['6', '3', 'A', '2', '4']))
# tubos.append(tubo(['9', '1', '2', '7', '2']))
# tubos.append(tubo(['6', 'C', '9', '4', '5']))





# tubos.append(tubo(['2', 'C', '5', 'C', 'C']))
# tubos.append(tubo(['6', '2', '2', 'A', '6']))
# tubos.append(tubo(['8', '8', '9', '4', '8']))
# tubos.append(tubo(['1', '4', 'A', '7', '7']))
# tubos.append(tubo(['4', '7', '8', 'A', '6']))
# tubos.append(tubo(['9', '4', '6', '5', 'B']))
# tubos.append(tubo(['7', 'B', '9', '9', '1']))
# tubos.append(tubo(['3', '4', '3', '3', '9']))
# tubos.append(tubo(['B', 'B', '2', '3', '5']))
# tubos.append(tubo(['A', 'C', '8', 'B', 'A']))
# tubos.append(tubo(['C', '2', '1', '1', '5']))
# tubos.append(tubo(['7', '5', '1', '6', '3']))


# tubos.append(tubo([]))
# tubos.append(tubo([]))


# tubos.append(tubo(['5', '7', '5', '5']))
# tubos.append(tubo(['C', 'C', 'C', 'C']))
# tubos.append(tubo(['3', '6', 'A', 'A', 'A']))
# tubos.append(tubo(['4', '7', '1', '4', '3']))
# tubos.append(tubo(['5', '9', '2', '2']))
# tubos.append(tubo(['A', '8', '3', '9', '7']))
# tubos.append(tubo(['9', 'C', '8', '2', '6']))
# tubos.append(tubo(['B', '6', 'B', 'A', '7']))
# tubos.append(tubo(['2', '4', 'B', 'B', 'B']))
# tubos.append(tubo(['5', '4', '8', '8', '8']))
# tubos.append(tubo(['7', '3', '6', '9', '']))
# tubos.append(tubo(['9', '3', '4', '2', '6']))
# tubos.append(tubo(['1', '1', '1', '1']))
# tubos.append(tubo([]))

# tubos.append(tubo(['5', '7', '5', '8', '1']))
# tubos.append(tubo(['C', 'C', 'A', 'A', '8']))
# tubos.append(tubo(['3', '6', 'A', '2', '1']))
# tubos.append(tubo(['4', '7', '1', '4', '3']))
# tubos.append(tubo(['5', '9', '2', 'B', '5']))
# tubos.append(tubo(['A', '8', '3', '9', '7']))
# tubos.append(tubo(['9', 'C', '8', '2', '6']))
# tubos.append(tubo(['B', '6', 'B', 'A', '7']))
# tubos.append(tubo(['2', '4', 'B', 'B', '1']))
# tubos.append(tubo(['5', '4', '8', 'C', '1']))
# tubos.append(tubo(['7', '3', '6', '9', 'C']))
# tubos.append(tubo(['9', '3', '4', '2', '6']))
# tubos.append(tubo([]))
# tubos.append(tubo([]))


# tubos.append(tubo(['7', '9', '5', '4', '8']))
# tubos.append(tubo(['A', '8', '1', '8', '9']))
# tubos.append(tubo(['B', 'C', '5', '4', '3']))
# tubos.append(tubo(['7', '5', '6', 'B', '6']))
# tubos.append(tubo(['1', '2', '7', '4', 'C']))
# tubos.append(tubo(['2', 'C', '3', 'B', 'A']))
# tubos.append(tubo(['8', '7', '6', 'B', 'B']))
# tubos.append(tubo(['A', '5', 'A', '2', '3']))
# tubos.append(tubo(['4', 'A', '1', '9', '9']))
# tubos.append(tubo(['2', '7', '6', '4', '3']))
# tubos.append(tubo(['6', '9', '1', '3', '1']))
# tubos.append(tubo(['C', 'C', '2', '8', '5']))
# tubos.append(tubo([]))
# tubos.append(tubo([]))



# tubos.append(tubo(['1','1','1','1']))
# tubos.append(tubo(['2','2','2','2','2']))
# tubos.append(tubo(['3','3','3','3','3']))
# tubos.append(tubo(['4','4','4','4','4']))
# tubos.append(tubo(['5','5','5','5','5']))
# tubos.append(tubo(['6','6','6','6','6']))
# tubos.append(tubo(['7','7','7','7','7']))
# tubos.append(tubo(['8','8','8','8','8']))
# tubos.append(tubo(['9','9','9','9','9']))
# tubos.append(tubo(['0','0','0','0','0']))
# tubos.append(tubo(['A','A','A','A','A']))
# tubos.append(tubo(['S','S','S','S','S']))
# tubos.append(tubo(['1']))
# tubos.append(tubo([]))

# tubos.append(tubo(['7', 'B', 'C', '8', '5']))
# tubos.append(tubo(['5', '6', 'C', 'C', '6']))
# tubos.append(tubo(['C', '5', '2', 'C', '1']))
# tubos.append(tubo(['9', '7', '2', 'A', '3']))
# tubos.append(tubo(['9', '7', '5', '1', 'B']))
# tubos.append(tubo(['8', '5', '7', 'A', '3']))
# tubos.append(tubo(['9', '4', '8', '1', 'B']))
# tubos.append(tubo(['8', 'B', '3', '6', '1']))
# tubos.append(tubo(['9', '7', 'A', 'A', '4']))
# tubos.append(tubo(['2', '6', '8', '1', '2']))
# tubos.append(tubo(['6', 'A', 'B', '4', '3']))
# tubos.append(tubo(['3', '4', '9', '2', '4']))
# tubos.append(tubo([]))
# tubos.append(tubo([]))


# tubos.append(tubo(['6', '4', 'C', '1', 'C']))
# tubos.append(tubo(['8', '2', '6', '5', '7']))
# tubos.append(tubo(['2', 'C', '9', '4', '9']))
# tubos.append(tubo(['B', 'C', '3', '8', '6']))
# tubos.append(tubo(['A', '4', '8', '8', '9']))
# tubos.append(tubo(['3', 'B', '5', '3', '9']))
# tubos.append(tubo(['B', '2', '4', 'A', '2']))
# tubos.append(tubo(['A', 'B', '6', '1', 'B']))
# tubos.append(tubo(['1', '5', '5', '4', '5']))
# tubos.append(tubo(['1', '6', '7', 'A', 'C']))
# tubos.append(tubo(['8', '7', '7', 'A', '3']))
# tubos.append(tubo(['3', '9', '1', '7', '2']))
# tubos.append(tubo([]))
# tubos.append(tubo([]))

# tubos.append(tubo(['3', '3', 'B', '5', '1']))
# tubos.append(tubo(['4', 'C', 'B', '5', '5']))
# tubos.append(tubo(['6', '7', '2', '5', '4']))
# tubos.append(tubo(['9', '7', 'A', '1', '2']))
# tubos.append(tubo(['3', '4', '5', '6', '8']))
# tubos.append(tubo(['7', '9', 'A', 'C', '2']))
# tubos.append(tubo(['3', '9', 'C', 'A', '2']))
# tubos.append(tubo(['8', '2', 'B', '8', '6']))
# tubos.append(tubo(['9', '4', 'B', '6', 'C']))
# tubos.append(tubo(['1', 'A', 'A', '4', 'C']))
# tubos.append(tubo(['9', '6', 'B', '1', '7']))
# tubos.append(tubo(['7', '1', '8', '8', '3']))
# tubos.append(tubo([]))
# tubos.append(tubo([]))


# tubos.append(tubo(['7', '1', '6', '3'],largo=4))
# tubos.append(tubo(['2', '1', '6', '5'],largo=4))
# tubos.append(tubo(['3', '5', '5', 'A'],largo=4))
# tubos.append(tubo(['8', '1', '9', '3'],largo=4))
# tubos.append(tubo(['4', '4', '6', '9'],largo=4))
# tubos.append(tubo(['3', '7', '4', '1'],largo=4))
# tubos.append(tubo(['9', '7', '7', '8'],largo=4))
# tubos.append(tubo(['A', '8', '2', '9'],largo=4))
# tubos.append(tubo(['A', '4', '2', '8'],largo=4))
# tubos.append(tubo(['A', '5', '6', '2'],largo=4))
# tubos.append(tubo([],largo=4))
# tubos.append(tubo([],largo=4))

# tubos.append(tubo([*'AB44'],largo=4))
# tubos.append(tubo([*'C298'],largo=4))
# tubos.append(tubo([*'3674'],largo=4))
# tubos.append(tubo([*'656C'],largo=4))
# tubos.append(tubo([*'7ACC'],largo=4))
# tubos.append(tubo([*'B641'],largo=4))
# tubos.append(tubo([*'9728'],largo=4))
# tubos.append(tubo([*'9A83'],largo=4))
# tubos.append(tubo([*'AB71'],largo=4))
# tubos.append(tubo([*'9585'],largo=4))
# tubos.append(tubo([*'3321'],largo=4))
# tubos.append(tubo([*'152B'],largo=4))
# tubos.append(tubo([],largo=4))
# tubos.append(tubo([],largo=4))


# tubos.append(tubo([*'4632'],largo=4))
# tubos.append(tubo([*'71B3'],largo=4))
# tubos.append(tubo([*'198C'],largo=4))
# tubos.append(tubo([*'2169'],largo=4))
# tubos.append(tubo([*'587B'],largo=4))
# tubos.append(tubo([*'A18B'],largo=4))
# tubos.append(tubo([*'4568'],largo=4))
# tubos.append(tubo([*'265A'],largo=4))
# tubos.append(tubo([*'743C'],largo=4))
# tubos.append(tubo([*'4973'],largo=4))
# tubos.append(tubo([*'A25B'],largo=4))
# tubos.append(tubo([*'9CCA'],largo=4))
# tubos.append(tubo([],largo=4))
# tubos.append(tubo([],largo=4))

tini=[]

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

tubos=tini


incompletos=[]
for k in range(len(tubos)):
    incompletos.append(k)

disponible=[]

def actualizadisponible(k=99):
    global disponible
    global tubos
    
    
    if k==99:
        disponible=[]
        i=0
        for tubo in tubos:
            if tubo.hayespacio():
                disponible.append(i)
            i+=1
    else:
        if tubos[k].hayespacio():
            if k not in disponible:
                disponible.append(k)
        else:
            if k in disponible:
                disponible.remove(k)
                
        
    
def esposible(s,t):

    if s==t:
        return False
    
    if tubos[s].completo or tubos[t].completo:
        return False
    
    bola_s, num_s=tubos[s].primerab()
    bola_t, num_t=tubos[t].primerab()
        
    if num_s==0 or num_s==tubos[s].largo:
        return False
    
    if num_s==len(tubos[s].bolas) and num_t==0:
        return False
    
    if num_t==0:
        return True
    
    if len(tubos[t].bolas)+num_s>tubos[t].largo:
        return False
    
    if bola_s!=bola_t:
        return False
    
    return True


def moverb(s,t):
    global tubos
    tubos[t].colocarb(tubos[s].sacarb())
    # print("s", s, tubos[s].bloques)
    # print("t", t, tubos[t].bloques)
    
    


def mover(s,t):
    global tubos
    if (t in disponible) and (len(tubos[s].bolas)>0) and (s!=t):
        if len(tubos[t].bolas)==0:
            orig=tubos[s].primera()
            i=0
            while orig==tubos[s].primera():
                tubos[t].colocar(tubos[s].sacar())
                i+=1
            return i
        elif tubos[s].primera()==tubos[t].primera():
            orig=tubos[s].primera()
            bb=tubos[s].bolas[:]
            bb.reverse()
            i=0
            while i<=len(bb) and orig==bb[i]:
                i+=1
            
            if i+len(tubos[t].bolas)<=tubos[t].largo:
                while orig==tubos[s].primera():
                    tubos[t].colocar(tubos[s].sacar())
                
    else:
        return False

def moverf(s,t):
    global tubos
    tubos[t].colocar(tubos[s].sacar())
    

def fin():
    global disponible
    global tubos
    return len(disponible)==2 and (tubos[0].completo or tubos[1].completo or tubos[2].completo)

def escompleto():
    global tubos
    for i in incompletos:
        if tubos[i].completo==False and tubos[i].vacio==False:
            return False
    return True


def lista_tubos():
  global tubos
  t=[]
  for tubo in tubos:
    t.append("".join(tubo.bolas))
  t.sort()
  return ",".join(t)




def estado():
    global tubos
    global movimientos
    lista=[]
    lista2=[]
    for tubo in tubos:
        lista.append(tubo.texto())
        lista2.append(tubo.bolas)
    lista.sort()
    listatxt=",".join(lista)
    return listatxt, lista2, movimientos[:]

lista_tableros=[]
lista_tablerostxt=[]
lista_movimientos=[]

# lista_tableros=lista_tableros
# lista_tablerostxt=lista_tablerostxt
# lista_movimientos=lista_movimientos

def registra_estado():
    global lista_tableros
    global lista_tablerostxt
    global lista_movimientos
    
    listatxt, lista2, movs=estado()
    
    if listatxt not in lista_tablerostxt:
        lista_tableros.append(lista2)
        lista_tablerostxt.append(listatxt)
        lista_movimientos.append(movs[:])

movimientos=[]

# best_len=52
# best=[(0, 12), (1, 13), (3, 0), (13, 3), (4, 13), (9, 13), (8, 9), (8, 12), (2, 8), (1, 2), (0, 1), (7, 0), (7, 4), (7, 12), (1, 7), (13, 1), (4, 13), (5, 4), (5, 1), (6, 5), (10, 4), (10, 13), (5, 10), (2, 5), (2, 7), (0, 2), (0, 6), (1, 0), (6, 1), (5, 6), (3, 5), (3, 1), (3, 8), (3, 5), (6, 3), (6, 13), (8, 6), (9, 8), (9, 6), (8, 9), (2, 8), (2, 4), (9, 2), (10, 9), (10, 3), (4, 10), (11, 9), (7, 4), (11, 2), (11, 5), (11, 6), (11, 12)]
# count=0

tableros=[]
best_len=999
best=[]
count=0
# registro=[]

def brutforce(deep=0):
    global tubos
    global movimientos
    global incompletos
    global best_len
    global best
    global disponible
    global count
    global tableros
    # global registro
    
    cincompletos=incompletos[:]
    
    for s in cincompletos:
        ddisp=disponible[:]
        for t in ddisp:
            if esposible(s,t):
                bola,num=tubos[s].primerab()
                movimientos.append((bola,s,t))
                # if len(movimientos)<=20:
                #     print(movimientos)
                moverb(s,t)
                
                deep+=1
                count+=1
                lt=lista_tubos()
                if lt not in tableros or escompleto():
                  tableros.append(lt)
                  # registro.append([len(tableros),count])
                  if count%20000==0:
                      #print(best_len, count)
                      pass
                      if count%1000000==0:
                          print(best_len, movimientos)
                          pass
                  actualizadisponible(s)
                  actualizadisponible(t)
                  if escompleto():
                      if len(movimientos)<best_len:
                          best=movimientos[:]
                          best_len=len(movimientos)
                          print(count, best_len, movimientos)
                          print("")
                          # kkk=input()
                  elif len(movimientos)<best_len:
                      brutforce(deep)
                
                for n in range(num):
                    moverf(t,s)
                movimientos=movimientos[:-1]
                deep-=1
                actualizadisponible(s)
                actualizadisponible(t)
                
                    
                
def avanza_arbol():
    global lista_tableros
    global lista_tablerostxt
    global lista_movimientos
    global tubos
    global best_len
    global best
    
    tablero = lista_tableros[0]
    movs = lista_movimientos[0]
    i=0
    
    for tubo in tubos:
        tubo.bolas=tablero[i]
        actualizadisponible(i)
        i+=1
    
    for s in range(14):
        for t in range(14):
            if esposible(s,t):
                bola,num=tubos[s].primerab()
                movs.append((s,t))
                moverb(s,t)
                actualizadisponible(s)
                actualizadisponible(t)
                if escompleto():
                    if len(movs)<best_len:
                        best=movs[:]
                        best_len=len(movs)
                        print(count, best_len, movs)
                        print("")
                        # kkk=input()
                
                registra_estado()
                moverf(t,s)
                movs=movs[:-1]
                actualizadisponible(s)
                actualizadisponible(t)
    lista_tableros=lista_tableros[1:]
    lista_tablerostxt=lista_tablerostxt[1:]
                
                
    
        
# registra_estado()   
# avanza_arbol()   
    
    
    
t=time.time()    
actualizadisponible()    
brutforce()   
print("Tiempo ",(time.time()-t))

# moverb(11,12)
# moverb(8,11)
# moverb(0,8)
# moverb(3,0)
# moverb(1,3)
# moverb()
# moverb()
# moverb()
# moverb()
# moverb()
# moverb()


    

# print(disponible)
    


    


    
    
        