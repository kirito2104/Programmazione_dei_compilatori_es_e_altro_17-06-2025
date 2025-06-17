#Esercizio n.1, 
# creare una variabile chiamata "numero" ed assegnare il valore 5 ad esso 
'''
numero = 5
print(numero)
'''

#ESERCIZIO N.2 
#Creare una variabile chiamata nome ed assegnare la stringa "Mario" ad esso 
'''
nome="Mario"
print (nome)
'''
#ESERCIZIO N.3
#Creare una variabile chiamata pi ed assegnare il val. 3.14
'''
pi= 3.14
print(pi)
'''
#ESERCIZIO N.4
#Creare una variabile chiamata vero_falso ed assegnare il val. True
'''
vero_falso = True
print(vero_falso)
'''

#ESERCIZIO N.5
#Converire la variabile in numero in (punto1) in una stringa e 
# asssegnarlo ad una nuova variabile chiamta numero_stringa
'''
Numero = 7

num_stringa= str(Numero)       # equivale ha dire che num_striga diventi = "7"

print(type(num_stringa))
'''
#QUI IL VALORE NUMERO verra' converirto in una varibile int in una stinga scrivendo str

#ESERCIZIO N.6
#Converire la variabile della valore (punto3) in un intero e 
# asssegnarlo ad una nuova variabile chiamta pi_cm_intero

#Type serve per identifica che tipo di valore e la variabile che potrebbe essere una variabile: float,int,str
'''
Numero = 7.5

pi_cm_intero= int(Numero)       # equivale ha dire che num_striga diventi = "7"

print(type(pi_cm_intero))   
'''

#ESERCIZIO N.7
#Converire la variabile vero_falso in una stringa e 
# assegnarlo ad una nuova variabile chiamta v_f_ stringa
'''
vero_falso = True
v_f_stringa = str (vero_falso)  # che sarebbe scritto "True" e quindi viene letto come una stringa 

print(vero_falso)

'''

#ESERCIZIO N.8
# Dichiarare la variabile x con valore 10 ed una variabile y con valore 20 e stampare la somma tra essi

'''
x = 10
y = 20
print(x+y)

'''
#ESERCIZIO N.9
# Dichiarare la variabile z con valore "30"(stinga) ed convvertire 
# il valore della variabile in un intero e aggiungerlo alla somma del es.8 e stampare il risultato


'''
x = 10
y = 20
z= "30"
new_z = int(z)

print(x + y +int(z))''' # Cio' permettera di far si la stringa del val. z venga convertita ad intero ed quindi poddibile sommarli

# invece di scrivere new_z = int(z)  si fa |||print(x + y +int(z))|||


#ESERCIZIO N.10

#Dichiarare la variabile stringa_1 con "hello"(stinga) e la variabile stringa_2
#con valore  "word". Concatenare  le due stringhe ed assegnnate il risultato ad unas nuova variabile stringa_concatenata.
#stampare poi la nuova stringa concatenata
'''
stringa_1 = "hello"

stringa_2 = "word"

stringa_concatenata =stringa_1 +""+ stringa_2  
#qui sopra fa in modo che concateni le due stringhe in una, per far si che ci sia uno spazio vuoto si mettono le virgolette 

print(stringa_concatenata)
'''

#ESERCIZIO N.11

#Dichiarare la variabil variab_bool con valore  True. Controlli se il tipo  di dato variab.bool e' un booleano,
# stampando poi il risultato 
'''
variab_bool = True

print(type(variab_bool) == bool ) 
'''
# USANDO TYPE INFATTI CONTROLLA ATTENATAMENTE CHE IL VALORE SIA BOOLEANO DICENDO DICENDO DI CHE TIPO E' poi bisogna
# mettere fuori dalla parentesi == bool per verificare 
# se lo e' in caso non lo sia mettendo print(type(variab_bool) == int ) dira che False, ossia non e booleano 
# lo stesso sara' anche se il valore nella variabile riportata non lo dicendo che e' False 


#ESERCIZIO N.12

#Dichiarare la variabilI LISTE con valore [1,2,3]. 
# Controllare se il tipo di lista e' una lista e stampare il risultaro

'''
LISTE = [1,2,3]
print (type(LISTE)== list)'''
# controlla sempre di che tipo e' la variabile lista e se una stringa o meno
#per verificare ulteriormente che il valore sia una lista scriviamo ||print (type(LISTE)== list)|| 
#in caso non lo sia dira che la variabile e false un valore booleano per dirci che e  vera o falsa 











