'''
 15 /3 
 15 - 3= 12
 12-3 = 9
 9- 3 = 6 
 6 - 3 = 3
 3 - 3   = 0
 while divendendo<divisore
    dividendo = dividendo - divisore
 
 15/3 = 5  resto : 0
 
 11 / 3 
 11-3= 8
 8-3=5
 5-3=2
 
 11 /3 = 3 resto:2
 '''

divisore = 14
dividendo = 2

risultato = 1

while dividendo < divisore:
    divisore = divisore - dividendo  # Qui sottraiamo il valore del divisore dal dividendo in ogni ciclo, il che porta subito il dividendo a un valore negativo.
    risultato = risultato + 1  # Incrementiamo il contatore `risultato` ogni volta che viene eseguito il ciclo.
   
       
print(risultato)
#-------------------------------------------------------------------------------------------------------------------------
#in quest esempio nel caso in cui e minore dira che nella prima condizione  e vera e quindi stampera' true
# mentre se e' maggiore stampera' false, nel caso in cui e' uguale a 10 stampera il secondo elif
y=13
if y < 10:
    print("True")
elif y > 10:
    print("False")
elif y==10:
    print("E' uguale a 10")

 # s = 3 assegnazione
 # y == verifica se la codizione' euguale a tre
 
 #-------------------------------------------------------------------------------------------------------------------

# in questo programma richiede le taglie per una maglietta 


maglietta = (input('scegli colore: ' )) 
taglia = (input("Che taglia e?" ))

if maglietta == 'nero' and (taglia == 'M' or taglia == 'L'): # qui controlla che le taglie siano M  o L , 
    #altrimenti non e' verificata 
    print ('il colore e nero')
else : 
    print(" e'di un'altro colore ")
if taglia == 'M' or taglia == 'L':
    print("la taglia e",taglia)
else :
    ('le altre taglie non sono accettate')
  
  
  
  
#-------------------------------------------------------------------------------------------------------------------------

#qui cerca i multipli di 3 
flag =True
while flag:
    flag = False
    numero = int (input('inserire unmultiplo di 3 :'))
    if numero % 3 == 0: # a differenza di prima l differenza e' che cambia il multiplo ossia 3
        break # permette di interrompere il programma, quando il multiplo e'stato trovato
    else :
        print('numero non multiplo di 3, rifare') 
        flag = True