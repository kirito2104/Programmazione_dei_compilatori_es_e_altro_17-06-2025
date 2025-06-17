 
 
nomi = ['A','B','C','B','D', 'C'] 
pos = [3,1,9,0,10,2,4,2]

#al tempo i pos[i] e' la nuova posizione di nomi[i]

# qual e' l'ultimaa configurazione dei punti? ovvero la posizione dei punti alla fine della serie temporale 

#[d] = p se il punto k si trova in posizione p 
# zip ti stampa la prima posizione delle liste  

n = len(nomi )
d ={}
for i  in range (n): # range
    d[nomi [i]] = pos[i] # tempo medio 
    


d = {}

for nome in zip (nomi , pos):
    d[nome ] = pos 
    
    # complessità temporale: O(n) medio

d = {}

for nome, p in zip(nomi, pos):
    d[nome] = p
#___________________________________________________________________________________________________________________________________________
print(d.keys())
print(d.values())
print(d.items())
#____________________________________________________________________________________________________________________________
nomi = ['A', 'B', 'A', 'C', 'B', 'D', 'A', 'C']
pos = [3, 1, 0, 2, 0, 2, 4, 2]

d = {}

# d[nome] = [lista dei p]

for nome, p in zip(nomi, pos):
    if nome in d :
        d[nome] = nome.append(p)
    else:
        d[ nome] = [p]

print (d)

        