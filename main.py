import random

import time

tempo_inicial=time.time() # em segundos

#parte do código que vamos verificar o tempo de execução


A = [0]
#N = [0]

F = [0,0,0,0,0]

Fban= [10,10,10,10,10]
Fvdu= [3,2,5,6,4]
Flat= [1,1,1,1,1]

N=   [0,1,2]
NB=  [30,20,10]#Demanda de base
NVDu=[12,9,23] #Demanda de VDUs 

Lmax = 2 #limite banda total
aloc = [0,0,0] # cria uma matriz vazia

latencia = [12,8,3] #latencia nuvem em relacao basestation
#NB.sort() #ordenar de acordo com latencia

#gerar numeros aleatorios

F = []

Fban= []
Fvdu= []
Flat= []

N=   []
NB=  []#Demanda de base
NVDu=[] #Demanda de VDUs 

aloc = [] 

#setar numeros fakes

A = 10
nuv = 50
nfv = 500

for _ in range(nfv):#nfv

    F.append(0)

    Fban.append(10)
    Fvdu.append(random.choice(range(10)))
    Flat.append(1)

for _ in range(nuv):#nuvem

    N.append(random.choice(range(10)))
    NB.append(random.choice(range(30)))
    NVDu.append(random.choice(range(10)))

    aloc.append(0)

#print("F",F) 
#print("Fban", Fban)  
#print("Fvdu", Fvdu)  
#print("Flat", Flat)      
#print("N", N)  
#print("NB", NB)   
#print("NVDu", NVDu)    
#print("===================")  


for a in range(1):
    for n in range(nuv):
        for f in range(nfv):
            if (F[f] == 0):
                if((Fvdu[f] <= NVDu[n]) and (Fban[f] <= NB[n]) and (Flat[f]<=Lmax)):
                    NB[n]-=Fban[f]
                    NVDu[n]-=Fvdu[f]
                    F[f] = 1
                    #aloc[n]="*"
                    #print("F", F)
                    #print("FNvdu",Fvdu[f])
                    #print("Nbanda",NB)
                    #print("Nvdu",NVDu)
                    #print("Aloc Nivel",aloc)
                    #print("===================") 


tempo_final=time.time() # em segundos

print("tempo", tempo_final - tempo_inicial)
