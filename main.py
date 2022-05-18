import numpy as np

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

print("F",F) 
print("FNvdu",Fvdu)  
print("Nbanda",NB)  
print("Nvdu",NVDu)      
print("Aloc Nivel",aloc)   
print("===================")  

#gerar numeros aleatorios

Fban = np.random.randint(100, size=(10, 10))
Fvdu = np.random.randint(1,12,100)
Flat = np.random.randint(1, size=100)

N =  np.random.randint(1, size=10)
NB =  np.random.randint(10, size=(10, 10))
NVDu =  np.random.randint(1,12,10)

#print(randnums)

for a in range(1): #todas as BS
  for n in range(3): #todas as nuvens
    for f in range(5): #todas as funcoes possiveis da BS
       if (F[f] == 0):
          if((Fvdu[f] <= NVDu[n]) and (Fban[f] <= NB[n]) and (Flat[f]<=Lmax)):
              NB[n]-=Fban[f]
              NVDu[n]-=Fvdu[f]   
              F[f] = 1
              aloc[n]="*"
              print("F", F)
              print("FNvdu",Fvdu[f])  		
              print("Nbanda",NB)  
              print("Nvdu",NVDu)         
              print("Aloc Nivel",aloc)   
              print("===================") 
