
# CICLO While 

'''In Python, un ciclo `while` è una struttura di controllo che ripete un blocco
di codice finché una condizione specificata rimane vera. La sintassi base è la seguente:
'''
#Il ciclo continua ad essere eseguito finché la condizione valutata è vera. 
#Una volta che la condizione diventa falsa, il ciclo termina e il programma 
#prosegue con il codice successivo al blocco `while`.


#ad esempio :


x = 0
while x < 5:
    print(x)
    x += 1  # Incrementa x di 1 a ogni iterazione

'''
In questo esempio, il ciclo stampa i numeri da 0 a 4.
Il ciclo `while` si arresta quando `x` raggiunge il valore 5, 
poiché la condizione `x < 5` non è più vera.f

'''

#----------------------------------------------------------------------------------------------------------------------------


#- cosa sono i loop/ cicli 
# - sintassi del while 
# - break, continua, else 

x = ['milano', 'roma','napoli']



# SONO UN CICLI DI OPERAZIONI,FINCHE UNA CONSDIZIONENON E' VERIFICATA 
# IL WHILE HA BISOGNO DI UN ITERATORE/ CONTATORE, CHE TIENE TRACCIA A CHE PUNTO STIAMO 
#AD ES: 

i= 0 # conta a che punto siamo arrivati, 

while i< 6 : # va in loop fino ache non arriva a 6, per poi uscire 
    print(i) # e finche la variabile di e minore a 6 ci manda a schermo i , ossia incrementa fino a 5, 
    i+= 1 # serve per incrementare i finche' non arriva a 5 
    #sensa l'incremento andrebbe all'infinito 
    # prende i, stampa 0, per poi incrementarlo , si incrementa finche i e' minore di 6,
    # per poi aarrivare a 6 ed uscire dal programma   
print('ciao')
#------------------------------------------------------------------------------------------------------------------------


i= 0 # conta a che punto siamo arrivati, 

while i< 6 : # va in loop fino ache non arriva a 6, per poi uscire 
    print(i) # e finche la variabile di e minore a 6 ci manda a schermo i , ossia incrementa fino a 5, 
   
    if i == 5: #aggiungiendo l'if va avanti ad incrementare fino a che non e uguale a 5 
        break # per poi usando break per stoppare quando arriva a 5 ( interrompere)
    i+= 1

print('ciao')

# break serve ad interrompere il ciclo ad un determinaato punto, quindi interrompe tutto 

#---------------------------------------------------------------------------------------------------------------------------

#while ---->>> funzione continue ( che passaa alla prossima iterazione )

i= 0 # conta a che punto siamo arrivati, 
c=0

while i< 6:
    i += 1
    if i == 5 or i == 3:
        continue  #Salta tutto cio che c'e' sotto in questo caso saltera' 3 e 5 andando avanti 
    print(i,end=" ") # end serve per non adare a capo 
    print("ciao",i)
    c+=1  # conta i giri che faa in totale 
    
print ('ciao')
print(c)
#-------------------------------------------------------------------------------------------------------------------------
# aggiungendo else si leva il print ciao 

i= 0 # conta a che punto siamo arrivati, 
c=0

while i< 6:
    i += 1
else:
    print('ho finito')
#stampa che a finito quando esce dal while     
    
    

