A = [0]
N = [0]

F = [0,0,0,1,1]

Fban= [10,10,10,10,10]
Fvdu= [3,2,5,5,4]
Flat= [1,1,1,1,1]

N=   [0,1,2] #Demanda de VDUs 
NB=  [30,30,30]#Demanda de base
NVDu=[4,9,8]

Lmax = 2 #limite banda total

aloc = [0,0,0] # cria uma matriz vazia

for a in A: #todas as BS
  for n in N: #todas as nuvens
    for f in F: #todas as funcoes possiveis da BS
      if (F[f] == 0):
          if((Fvdu[f] <= NVDu[n]) and (Fban[f] <= NB[n]) and (Flat[f]<=Lmax)):
              F[f]=2           
              NB[n]-=Fban[f]
              NVDu[n]-=Fvdu[f]
        
              aloc[n]="*"
              print("F",F) 
              print("Nbanda",NB)  
              print("Nvdu",NVDu)      
              print("Aloc Nivel",aloc)   
              print("===================")  
              

   

