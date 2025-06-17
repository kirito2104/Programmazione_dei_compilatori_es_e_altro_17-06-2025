#Esercizio 1: Creare 3 variabillx, y e z assegnando dei valori a scelta. Iniziallzzare una
#nuova variabile risultato che derivi dalla somma delle prime due elevate alla
#seconda, meno z Mandare a schermo il risultato finale.

x=30
y=10
z=50
eta= 25
risultato = (x+y)**2 - z 
# Per far cio che dice l'esercizio bisogna mettere la parentesi per far
#in modo che si possa fare la potenza per entrambi gli elementi
print(risultato - int(eta)*3) # facendo cosi moltiplico per 3 eta trasformandolo in un intero per poi farlo meno il risultato
print(risultato)


#-------------------------------------------------------------------------------------------------------------------------------
#Esercizio 2: Dichiarare ung nuova variabile età con valore stringa "25". A questo punto
#mandare a schermo la differenza tra risultato ed il triplo di età.


età = "25"
new_età = int(età) 

print(int(new_età)*3)
# In questo esercizio, creo come prima cosa una nuova variabile per 
# poi convertire la variaabile eta' in un num. intero 
# dopo di che lo mando a schermo e lo moltiplico per 3

#questo qui sotto e' un altro modo 
#print(risultato - int(eta)*3) # facendo cosi moltiplico per 3 eta trasformandolo in un intero per poi farlo meno il risultato


#---------------------------------------------------------------------------------------------------------------------
#Esercizio 3: Assegnare ad x la somma di sé stessa pilù 2, moltiplicata poi per i resto
#della divisione di y e z.


x=76
y = 30
z = 4
#yz = y/z # divido y e z , mettendo % invece da e caalcola solo il resto dei due
#x += 2   # qui svolgo la somma di se stessa ossia x e poi + 2 
x += 2 *(y % z ) # qui moltiplico il ris di x + 2 e poi moltiplico per il resto di y

print(x)


#---------------------------------------------------------------------------------------------------------------------
# Esercizio 4: Mandare a schermo il valore assoluto della differenza tra y e z elevata alla
#guarta (solo z elevata, non l'intera differenza).
#(differenza ossia - )
x=76
y = 30
z = 4

print (abs(y - z  ** 4 ))   

# come prima cosa faccio la differenza (ossia sottraggo) tra y ez, per poi elevare il risultato alla 4, 
# per renderlo assoluto il valore metto abs

#----------------------------------------------------------------------------------------------------------------------

#Esercizio 5 stampare i resto della divisione tra x elevata alla terza usando pow() e il
#valore intero della metà di età

xm=30
y = 30
z = 50
etaa= "25"
#risultato = pow(x,3) %int(eta) #non va bene siccome 
xm += 2 *(y % z )
risultat = pow(xm, 3) % int(int(etaa)/2) 
# come prima cosa prendo eta e lo converto in un intero per poi  dividerlo per /2
# per poi renderlo a sua volta un intero siccome esce con la visgola 

print(risultat) # il ris e' 0
