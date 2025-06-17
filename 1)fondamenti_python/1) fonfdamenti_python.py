'''
1) #servira per poter stampare a schermo solo il messaggio "ciao"
print("ciao")       #stampaa schermo 

2)questo pezzettino di codice permette come prima cosa di chiedere di scrivere  il messaggio, e poi di poterlo inseriere 

messagggio= input ("inserisci qualcosa:")
print(messaggio)
 '''

'''
 variabili ossia un contenitore di un valore o collezioni di valori, 
ossia un posto dove possiamo assegnare uun volare che possiamo riprendere piu volte
ad  esempio
se scrivo 
x=5 
va bene 

mentre se scrivo 
y 
sensa un valore il programma va in errore
*le variabili devono avere un nome specifico 

- Si puo anche scrivere l a variabili in una singola riga assegnandogli un sigolo valore per elemento
x,y,z=32,100,987
per stampare i valori qui sopra a schermo faccio
print (x)
print(y)
print(z)  

mentre se si vuole mettere un unico valore per tutte e tre le variabili faccio:
x=y=z=32
'''                                                                                                                    
''' In caso si voglia fare in modo che criamo una lista di citta dove ci sono tre valori contenuti nella 
variabile citta e li assegno a sua volta negli altri tre 
 
 citta=  ["roma","milano", "napoli"] -> la differenza sostanziale e che i valori sono assegnsati ad es su x tutti e tre e non solo uno come in { x,y,z="milano","Roma","napoli"} ed x in questo modo puo averne piu di uno 
 x,y,z=citta
  print(x)
  print(y)
  print(z)
  '''            
'''
per fare un calcolo e restituire un valore faccio 
x=32
y=8
z=x+y+x+X
print(z)  
  qui somma i vari valori x e y, stampandoli nel risultato z, mettendo print(z)

  '''  
  # TIPI DI DATI
  #str: x= "ciao"
  # int: x=20
  #float:x= 20.5  
  #bool: x= True 
  
  #list: x= ["roma","milano","napoli"]
  #tuple: x=("roma","milano","napoli")
  #range: x= range (6)
  #dict x= {"roma","milano","napoli": 25}  ossia i dizzionari, usano una chiave valore 
  #set: x= {"roma","milano","napoli"}  
''' 
 * in pyhthon non e' nescessario assegnarte la variabili        
x = 5                                                                                        
print(type(x)) # fa in modo che il tipo di dato venga dato a schermo, mentre type fa si in modo che venga mandato in 
console\schermo il tipo di x
______________________________________________________________________
facendo invece 
x= 5.5
print (type(x)) #verra' riconosciuta come float 
x= "ciao" # che poteva essere anche x="sono del testo"
print(type(x))
verra' riconosciuta come una stringa
'''
'''
1) bolean -> sta per valore boleano ossia:
x= False
x= True 


2) i range sono che e un generatore di valori, nel es qui sotto avra un range da 1 a 5
range: x= range(6) 
'''


#CASTING -> cambio di un valore 
'''ossia che cambia/converte il tipo di dato/varibile di un valore.
castare significa prendere un valore di una variabile che puo' essere ad es: un numero, convertire un "int" in un "float" e vice versa.
lo si fa quando:
x= "5"
y=5 
print(x+y)
facendo cosi' dara' errore mentre invertendo x ed y,
*IN PYTHON NON SI POSSONO FARE OP DEL GENERE, SICCOME ABBIAMO VALORI DI TIPO DIVERSO  
  
PER FAR SI CHE I VALORI SI POSSANO CONCATENARE A VICENDA CON DIVERSE STRINGHE 

x= "ciao sono"
y="Luca"
print(x+y)
COSI E' CORRETTO SICCOME PYTHON NON PUO  CONCATENARE VALORI DIVERSI 
'''


#Per far si che python possa concatenare due variabili diverse bisogna fare il CASTING
'''
x= "ciao sono"
y= str(5)
print(x+y)

** E cosi' si potra concatenare  la stringa e l'intero insieme 
'''

#Mentre per fare lo stesso con una variabile intera 
'''
x= 5
y= int("5")
print(x+y)
facendo cosi' si potra concatenare la variabbile intera con la stringa "5" e facendo cosi sommera' 
i due valori in un variabile 10, mentre se era una carettere dava errore, non ce lo portra tradurre in un numero
  
'''
