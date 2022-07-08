import random
import time
import numpy as np
tempo_inicial=time.time() # em segundos

#teste


A = [0]
#N = [0]

F = [0,0,0,0,0,0,0,0,0,0]



Fvdu= [1,2,3,4,5,6,7,8,9,1]#[3,2,5,6,4]
Fban= [4,2,6,2,8,6,9,3,4,9]
Flat= [1,1,1,1,1,1,1,1,1,1]

N=   [0,1,2]
NB=  [20,20,10]#Demanda de base
NVDu=[10,90,230] #Demanda de VDUs 



Lmax = 2 #limite banda total
aloc = [0,0,0] # cria uma matriz vazia

latencia = [12,8,3] #latencia nuvem em relacao basestation
#NB.sort() #ordenar de acordo com latencia

#gerar numeros aleatorios
#tam=1 #tam nuvem
val= 10 #tam vetor
#F= [random.randint(0, 0) for _ in range(val)]
#Fban= [random.randint(0, 10) for _ in range(val)]
Fvdu= [random.randint(1, 5) for _ in range(val)]
#Flat= [random.randint(1, 1) for _ in range(val)]

#N = list(range(tam))
#NB= [random.randint(10, 10) for _ in range(val)]
#NVDu = [random.randint(10, 10) for _ in range(val)]
#aloc = list(range(tam))

#print("Fvdu", Fvdu)
#print("fban", Fban)
print("Nvdu",NVDu)
print("Nbanda",NB)
print("Aloc",aloc)

print("---")
for a in range(1):
    for n in range(1):
        for f in range(10):
            if (F[f] == 0):
                if((Fvdu[f] <= NVDu[n]) and (Fban[f] <= NB[n]) and (Flat[f]<=Lmax)):
                    NB[n]-=Fban[f]
                    NVDu[n]-=Fvdu[f]
                    F[f] = 1
                    aloc[n]="*"
                    
                  #  print("Fvdu", Fvdu)
                   # print("Nbanda",NB)
                   # print("Nvdu",NVDu)
                  #  print("Aloc Nivel",aloc)
                  #  print("===================") 

print("Fvdu", Fvdu)
print("fban", Fban)
print("Nvdu",NVDu)
print("Nbanda",NB)
print("F",F)


#vet=[]
#cont=0
#for x in range(10):
#	if (aloc[x] == '*' ):
#		vet.append(Fvdu[x])
#		cont+=1
#print("vet",vet)
#print( np.mean(vet) )

tempo_final=time.time() # em segundos

print("tempo", tempo_final - tempo_inicial)