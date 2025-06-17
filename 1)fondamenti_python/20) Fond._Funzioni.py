# 20 funzioni
# Questo è un elenco di argomenti relativi alle funzioni in Python.

# - Cosa sono le funzioni
# Spiegazione del concetto di funzione: blocchi di codice riutilizzabili che eseguono un'azione specifica.

# - Creare una funzione
# Come definire una funzione utilizzando la parola chiave `def`.

# - Chiamare una funzione
# Come invocare una funzione precedentemente definita.

# - Parametri in funzione
# Spiegazione dei parametri: valori che una funzione può accettare per eseguire il suo compito.

# - Differenza tra argomenti e parametri
# Argomenti: valori passati alla funzione.
# Parametri: i "segnaposto" definiti nella funzione per accettare gli argomenti.

# - Arbitrary Arguments, Keyword Arguments, Arbitrary Keyword Arguments (extra)
# Arbitrary Arguments: utilizzo di `*args` per accettare un numero variabile di argomenti.
# Keyword Arguments: argomenti passati esplicitamente con nome, es: `key=value`.
# Arbitrary Keyword Arguments: utilizzo di `**kwargs` per accettare un numero variabile di coppie chiave-valore.

# - Parametri di default
# Parametri con un valore predefinito, usati se l'argomento non è passato.

# - Return dei valori
# Come restituire valori da una funzione con la parola chiave `return`.



#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# le funzioni sono : un blocco di codice riutilizzabile, 
# al cui interno ci sono, delle istruzioni, che verrano eseguiti 
# ogni volta che andro a richiamare un funzione.

''' es: in psudocodice :
 prendi la pasta:
 prendi la pasta
 metti l'acqua
 metti la pasta
 metti il sugo 
 impiatta 
  # tutte queste azioni richiamano una  funzione 
 '''
#CON 'DEF' DEFINISCO UNA FUNZIONE, CON LE SUE VARIE FUNZIONI 

def fai_pasta (): # cosi' e come si comporta una funzione, che puo' contenere al suo interno piu' cose 
    
    print('metti acqua')
    print('fai bollire ')
    print('metti la pasta')
    
fai_pasta( ) # facendo cosi' richiamo la funzione, con varie cose al suo interno 

#---------------------------------------------------------------------------------------------------------------------------------

# - Parametri in funzione
# Spiegazione dei parametri: valori che una funzione può accettare per eseguire il suo compito.

# Definizione della funzione fai_della_pasta

# La funzione accetta un parametro "tipo_pasta" che specifica il tipo di pasta da cucinare.
def fai_della_pasta(tipo_pasta, metti_sugo):  
    # Stampa il primo passo per cucinare la pasta
    print('Metti acqua')  
    
    # Stampa il secondo passo per cucinare la pasta
    print('Fai bollire')  
    
    # Stampa il terzo passo e aggiunge il tipo di pasta specificato come argomento
    print('Metti ' + tipo_pasta)  
    if metti_sugo:
        print('prepara sugo ')

# Chiamata alla funzione fai_della_pasta con "spaghetti" come argomento
fai_della_pasta('spaghetti',True )  #nel caso in cui mettero' false, non stampera' nulla su spaghetti 
#mentre se metto true stampera' metti dugo 


#il parametro e' anche la varibile generica che usiamo nella def della variabile, 
#l'argomento e' cio che noi inseriamo, quaando il prograaaaama funziona 
# si potranno avere naturalmente piu' parametri come 
#----------------------------------------------------------------------------------------------------------------------------------------

# Arbitrary Arguments: utilizzo di `*args` per accettare un numero variabile di argomenti.
print('#-----------------------------------------------------------------')
# Definizione della funzione fai_della_pasta
# Il parametro *opzioni permette di accettare un numero variabile di argomenti.
def fai_della_pasta(*opzioni):  
    # Stampa il primo passo per cucinare la pasta
    print('Metti acqua')  
    
    # Stampa il secondo passo per cucinare la pasta
    print('Fai bollire')  
    
    # Usa il primo argomento di opzioni (opzioni[0]) per indicare il tipo di pasta
    print('Metti ' + opzioni[0])  
    
    # Verifica se c'è un secondo argomento in opzioni e se è True
    # len(opzioni) > 1 verifica se ci sono almeno 2 elementi nella tupla opzioni
    # opzioni[1] verifica il valore del secondo argomento (deve essere True per entrare nel blocco)
    if len(opzioni) > 1 and opzioni[1]:  
        print('Prepara sugo')  # Stampa solo se il secondo argomento esiste ed è True

# Chiamata alla funzione fai_della_pasta con due argomenti
fai_della_pasta('spaghetti', True)

#nel caso sia false, non prepara il sugo 
#--------------------------------------------------------------------------------------------------------------------------------

# Keyword Arguments: argomenti passati esplicitamente con nome, es: `key=value`.

print('#-----------------------------------------------------------------')


### **Cos’è un Keyword Argument (Argomento con nome)?**
'''
- Un **Keyword Argument** è un argomento passato a una funzione **specificando 
il nome del parametro**, seguito da un valore.  
- Questo approccio permette di passare gli argomenti senza preoccuparsi
dell'ordine in cui i parametri sono definiti nella funzione.
'''

'''**Vantaggi dei Keyword Arguments:**'''
#1. **Chiarezza:** Specificare il nome del parametro rende il codice più leggibile e facile da capire.
#2. **Flessibilità:** Non è necessario rispettare l'ordine dei parametri posizionali.
#3. **Default Parameters:** È possibile combinare keyword arguments con valori predefiniti dei parametri.

### **Esempio di utilizzo dei Keyword Arguments:**
#-------------------------------------------------------------------------------------------------------------------
# Definizione della funzione con due parametri
def fai_pasta(tipo_pasta, sugo):
    # Stampa il tipo di pasta specificato
    print("Tipo di pasta:", tipo_pasta)
    # Verifica se il sugo deve essere preparato
    if sugo:
        print("Prepara il sugo")
    else:
        print("Niente sugo")

# Chiamata alla funzione usando Keyword Arguments
fai_pasta(tipo_pasta="spaghetti", sugo=True)  # Specifico il nome dei parametri

#----------------------------------------------------------------------------------------------------------------------------------

#### **Output:**

'''Tipo di pasta: spaghetti
Prepara il sugo'''


''' **Come funzionano i Keyword Arguments?** '''
#1. Durante la chiamata della funzione, usi la sintassi `nome_parametro=valore`.
#2. Python associa automaticamente il valore al parametro corrispondente.

#### Esempio con l'ordine invertito:

# Chiamata con ordine diverso, usando Keyword Arguments
fai_pasta(sugo=False, tipo_pasta="penne")
'''
**Output:**

Tipo di pasta: penne
Niente sugo


'''

### **Combinazione di Argomenti Posizionali e Keyword Arguments:**

'''È possibile combinare argomenti **posizionali** e **keyword** nella stessa chiamata, 
ma gli argomenti posizionali devono essere dichiarati **prima** dei keyword arguments.'''


# Chiamata combinata
fai_pasta("fusilli", sugo=True)


### **Errore comune da evitare:**
'''Gli argomenti posizionali devono **sempre** precedere i keyword arguments. Ad esempio, questo genererà un errore:'''

#fai_pasta(tipo_pasta="farfalle", True)  # Errore!


### **Keyword Arguments con Valori Predefiniti (Default Arguments):**
'''Puoi definire parametri con valori predefiniti nella funzione, in modo che siano opzionali.'''

# Funzione con un valore di default per sugo
def fai_pasta(tipo_pasta, sugo=False):  # Il parametro sugo è opzionale
    print("Tipo di pasta:", tipo_pasta)
    if sugo:
        print("Prepara il sugo")
    else:
        print("Niente sugo")

# Chiamata senza specificare "sugo"
fai_pasta("rigatoni")

# Chiamata specificando "sugo"
fai_pasta("penne", sugo=True)


#### **Output:**
'''
Tipo di pasta: rigatoni
Niente sugo

Tipo di pasta: penne
Prepara il sugo
```
'''

### **Quando usare i Keyword Arguments?**
#1. **Per chiarezza:** Quando i parametri sono tanti e vuoi specificare esattamente cosa rappresenta ogni valore.
#2. **Quando l'ordine non è rilevante:** Se hai una funzione con molti parametri, 
# i keyword arguments evitano errori dovuti all'ordine sbagliato.
#3. **In combinazione con parametri opzionali:** Puoi usare keyword arguments per
# impostare solo i parametri che ti interessano, lasciando i valori di default per gli altri.


#---------------------------------------------------------------------------------------------------------------------------------
# **Arbitrary Keyword Arguments** (USIAMO `**kwargs`)




### **Esempio 1: Creare un profilo utente con parametri arbitrari**


# Definizione di una funzione per creare un profilo utente
# La funzione accetta un numero variabile di keyword arguments tramite **kwargs
def crea_profilo(nome, cognome, **kwargs):
    # Stampa i dati obbligatori: nome e cognome
    print("Nome:", nome)
    print("Cognome:", cognome)
    
    # Itera su tutti gli altri argomenti arbitrari (kwargs)
    for chiave, valore in kwargs.items():
        # Stampa ogni coppia chiave-valore
        print(f"{chiave.capitalize()}: {valore}") 
        '''osa fa in breve:
kwargs.items():

Restituisce tutte le coppie chiave-valore del dizionario kwargs (argomenti arbitrari passati alla funzione).
chiave.capitalize():

Trasforma la prima lettera della chiave in maiuscolo (esempio: "nome" → "Nome").
f"{chiave.capitalize()}: {valore}":

Formatta la stringa mostrando la chiave capitalizzata seguita da : e dal valore.
print():

Stampa ogni coppia chiave-valore formattata.'''

# Chiamata alla funzione con argomenti obbligatori e arbitrari
crea_profilo(
    nome="Luca", 
    cognome="Rossi", 
    età=30, 
    professione="Programmatore", 
    città="Milano"
)


#### **Output spiegato:**

'''Nome: Luca  ''' # Dati obbligatori
'''Cognome: Rossi ''' # Dati obbligatori
'''Età: 30   '''   # Dato aggiuntivo passato tramite kwargs
'''Professione: Programmatore ''' # Dato aggiuntivo passato tramite kwargs
'''Città: Milano'''        # Dato aggiuntivo passato tramite kwargs



### **Spiegazione Passo per Passo (Commenti):**
'''1. **Definizione della funzione:**
   - `nome` e `cognome` sono parametri obbligatori.
   - `**kwargs` permette di accettare un numero arbitrario di argomenti con nome (keyword arguments).

2. **Uso di `**kwargs`:**
   - Gli argomenti arbitrari vengono raccolti in un dizionario.
   - Puoi accedere a ogni coppia chiave-valore con `kwargs.items()`.

3. **Chiamata alla funzione:**
   - Oltre ai parametri obbligatori (`nome` e `cognome`), puoi aggiungere quanti keyword 
   arguments vuoi (es. `età`, `professione`, `città`).

'''
#---------------------------------------------------------------------------------------------------------------------------------------
### **Esempio 2: Calcolare il costo totale di un ordine con parametri arbitrari**


# Definizione di una funzione per calcolare il costo totale
# La funzione accetta un numero variabile di keyword arguments tramite **kwargs
def calcola_ordine(cliente, **kwargs):
    # Stampa il nome del cliente
    print(f"Ordine per: {cliente}")
    
    # Inizializza il totale a 0
    totale = 0
    
    # Itera su tutti gli articoli e i relativi costi passati tramite kwargs
    for articolo, prezzo in kwargs.items():
        # Aggiunge il prezzo dell'articolo al totale
        print(f"{articolo.capitalize()}: €{prezzo}")
        totale += prezzo
    
    # Stampa il costo totale
    print(f"Totale ordine: €{totale}")

# Chiamata alla funzione con il nome del cliente e un numero arbitrario di articoli
calcola_ordine(
    cliente="Mario", 
    pizza=8.5, 
    bibita=2.5, 
    dolce=5.0
)


#### **Output spiegato:**

'''Ordine per: Mario '''          # Cliente specificato
'''Pizza: €8.5 '''                # Prezzo della pizza
'''Bibita: €2.5 '''               # Prezzo della bibita
'''Dolce: €5.0'''                 # Prezzo del dolce
'''Totale ordine: €16.0 '''       # Somma dei prezzi


### **Spiegazione Passo per Passo (Commenti):**
'''1. **Definizione della funzione:**
   - Il parametro `cliente` è obbligatorio.
   - `**kwargs` accetta articoli e prezzi come coppie chiave-valore.

2. **Uso di `**kwargs`:**
   - Gli articoli e i relativi prezzi vengono raccolti in un dizionario.
   - Puoi iterare sul dizionario per calcolare il totale e stampare ogni articolo con il relativo prezzo.

3. **Calcolo del totale:**
   - Ogni prezzo viene aggiunto a una variabile `totale`.
   - Alla fine, il costo totale viene stampato.

4. **Chiamata alla funzione:**
   - Puoi aggiungere quanti articoli desideri (es. `pizza=8.5, bibita=2.5`).
   '''


#Quando usare `**kwargs`?

'''1. **Per flessibilità:** Quando non sai in anticipo quali argomenti extra potrebbero essere necessari.
2. **Per funzioni generiche:** Ad esempio, costruire profili, ordini o configurazioni dinamiche.
3. **Per leggibilità:** Usare keyword arguments con nome è spesso più chiaro rispetto all'uso di un dizionario.
'''
#---------------------------------------------------------------------------------------------------------------------------------------

# - Parametri di default
# Parametri con un valore predefinito, usati se l'argomento non è passato


def fai_pasta(tipo_pasta = 'fusilli', sugo =  True ): # gli assegnamo un valore di defaault quando non metto nullaa, quando 
    # nel richiamo della funzione non e' specificato il valore e' quindi restiusce fusilli
    # quando non c'e nulla.
    
    # Stampa il tipo di pasta specificato
    print("Tipo di pasta:", tipo_pasta)
    # Verifica se il sugo deve essere preparato
    if sugo : 
        print ('sugo ')

fai_pasta() # non e' assegnato nulla quindi restituira' ddei valori di default, sopra riportati 

# fai_pasta ('fusilli',false ) # mettendo false non restituira' il valore di sugo 



#---------------------------------------------------------------------------------------------------------------------------------------------
# - Return dei valori
# Come restituire valori da una funzione con la parola chiave `return`.

# Definizione della funzione fai_pasta
# La funzione accetta due parametri: num1 e num2
def fai_somma(num1, num2): 
    # Calcola la somma di num1 e num2 e la memorizza nella variabile locale 'sooma'
    soomma = num1 + num2
    return soomma # La somma viene restituita al chiamante

# Chiamata alla funzione fai_somma (che non esiste nel codice, sembra un errore)
x = fai_somma(2, 2) # La funzione restituisce il valore 4, che viene memorizzato in x


# Stampa del risultato memorizzato in 'x'
print('il valore e',x) # Stampa: 4


#Cosa cambia con return?
#Il risultato diventa utilizzabile:

'''Con return, puoi utilizzare il risultato della funzione al di fuori di essa. Ad esempio:
python

y = fai_pasta(3, 4) + 10  # Utilizzi il valore restituito e lo sommi a 10
print(y)  # Stampa: 17
Eviti il valore None:
'''


#Senza return, la funzione non restituisce un valore utile, quindi non puoi
#fare nulla con il risultato (a parte vederlo come None).
#Più flessibilità:

#Il valore restituito può essere passato ad altre funzioni, memorizzato in una variabile, o direttamente stampato:


print(fai_pasta(5, 5))  # Stampa: 10
#Quando usare return?

'''
Usa return quando vuoi che la funzione restituisca un valore per essere utilizzato altrove nel programma.
Evita return se la funzione esegue un'azione senza bisogno di restituire 
un valore (esempio: una funzione che stampa qualcosa ma non deve calcolare un risultato).

'''



'''
______________________________________________________________________________ 
Senza return	Con return                                                    |
Restituisce sempre None. |          Restituisce il valore specificato.        |
Non puoi utilizzare      |                                                    |
il risultato.	         |          Puoi utilizzare il valore restituito.     |
Utile solo per eseguire  |                                                    |
azioni.	                 |        Utile per calcoli e funzioni riutilizzabili.|
_______________________________________________________________________________


'''
































































