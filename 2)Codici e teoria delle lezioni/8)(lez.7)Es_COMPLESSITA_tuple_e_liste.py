#Le **tuple** sono più veloci e occupano meno memoria rispetto alle **liste**, grazie alla loro immutabilità,
# che le rende ideali per rappresentare dati fissi o strutturati, come coordinate o configurazioni.
# 
# Le **liste**, invece, sono mutabili e perfette per gestire dati dinamici che possono cambiare nel tempo.
# A differenza delle liste, le tuple sono hashabili (se contengono solo elementi immutabili) e possono essere usate come chiavi nei dizionari. 
# 
# 
# In sintesi, usa le liste per dati che richiedono modifiche frequenti e le tuple per dati fissi o prestazioni ottimali.

'''============================================================================================================================================================================================================================='''


# la differenza sostanziale  tra tupla e lista e che :

# la lista ha un suo peso maggiore rispetto alla tupla e quindi anche la gestione complessiva risulta essere piu' inefficente 

#la tupla invece e' molto piu' snella, ma ci si puo' fare poco 
#ci sono dei casi in cui una sequenza e' fissa o sia non va modificata , ne fatto nulla trnne che portarla a presso, allora conviene usare la tupla ,  
# che poi occupa pure meno spazio.

# es n.1


a = [ ('a',6),('b',9,0),('c',0,1),('d',-2 , -2 )]

r = 2.9

#creare una lista che contiene nomi  dei punti in "a" a distanza al piu' "r" da 


b = [] 

#calcolo il punto di distanza tra essi 
a = [ ('A', 2, 7), ('B', 3, -1), ('C', 0, 1), ('D', -2, -2) ]  # Lista di punti, ciascuno rappresentato come una tupla (nome, x, y)
r = 2.9  # Raggio massimo consentito per la distanza dal punto di origine (0, 0)

# Creare una lista che contiene i nomi dei punti in `a` che sono a distanza al più `r` dall'origine (0,0,0)
''' n = lunghezza lista (a)'''
b = []  # vado ad analizzare punto per punto i punti che sono in a 
# Lista vuota per memorizzare i nomi dei punti che soddisfano il criterio

# Iterazione su ogni punto nella lista `a`
# facendo cosi' spachetto la tupla in piu' variabili
for nome, x, y in a:  # Destruttura ogni tupla in `n` (nome), `x` (coordinata x), `y` (coordinata y)
    # Calcola la distanza al quadrato del punto (x, y) dall'origine (0, 0) utilizzando la formula della distanza euclidea:
    # distanza² = x² + y²
    # Confrontiamo con r² (anziché calcolare la radice quadrata per la distanza effettiva), per evitare calcoli inutili.
    
    if x**2 + y**2 <= r**2:  # Verifica se la distanza² è minore o uguale a r²
        #calcola il punto di distanza dall'origine e ci sda la distanza al quadrato 
        
        b.append(nome)  # Aggiungi il nome del punto alla lista `b`                 
        ''' APPEND HA UN TEMPO  COSTANTE " IN MEDIA  O(1)  " '''
        
        # A questo punto, `b` contiene i nomi dei punti che soddisfano il criterio
print(b)
    # w' piu' efficente usare la tupla per una questione di leggibilita' per far si che non venga modificata 
    
    
    
'''
LA COMPLESSITA' TEMPORALE DI QUESTO ALGORITMO :

*PER OGNI PUNTO CHE HO NELLA LISTA ESEGUO :  x**2 + y**2 <= r**2 , QUINDI IN TOTALE ESEGUO 4 OPERAZIONI IN UN TEMPO COSTANTE QUINDI VALE 1,
OGNI VOLTA CHE E' VERO AGGIUNGO UN ELEMENTO ALLA LISTA, QUINDI ESEGUO UNA MODIFICA DI B AGGIUNGENDO IL NUOVO VALORE AGGIUNGTO, ESGUEO QUESTA MODIFICA 
IN BASE HAI PUNTI CHE RICADONO NELLA LISTA DI INPUT 

NEL CASO PEGGIORE GLI INPUT SONO TUTTI ALL'INTERNO DEL RAGGIO DEL CERCHIO R 

# USO L'OPERAZIONE APPEND AL MASSIMO N VOLTE , perche' aggiungere un elemnto infodo alla lista ha lo stesso costo, quindi tempo costante 
# quindi a prescindere dalla lista il tempo sara' costante 


** tempo costante ** 
E' UNA COSA CHE RICORRE SPESSO E' L'ORDINE DI GRANDEZZA E' O(1)
ps: (IL TEMPO COSTANTE SI SCRIVE O(1) )
* QUINDI 'APPEND' RICHIEDERA' TEMPO LINEARE, (PERCHE' PER N VOLTE ESEGUO UN OPERAZIONE DI COSTO COSTANTE)

# SE LO SPAZIO E' PIENO : CI SARANNO PERAZIONI CHE SARANNO COSTOSE E ALTRE NON 

* LE PROPRIETA' COSTOSE SONO POCHE, SE SONO TALI DEVO ESEGUIRE PRIMA QUELLA : 

DEVO ESEGUEIRE ALMENO N  OPERAZIONI NON SCOSTOSE,NECCESSARIAMENTE 


QUINDI CI SARANNO DUE SOLUZIONI :


QUANDO  IL COSTO E' COSTANTE PER OGNI AGGIUNTA NELLA LISTA E O(1)
E QUANDO NON C'E' SPAZIO PER UN AGGIUNTA , DOPO ED E' O(N)

N +1+1+1+1+1++1/N 
( SI LIMITA A SCRIVERE A DESTRA DELL'ELEMENTO, QUINDI SIGNIFICA CHE SE GUARDO IL COSTO COMPLESSIVO DI QUESTE OPERZIONI E' N + N )


N+N/N+1 = 1 QUINDI IN MEDIA UNA SINGOLA OPERAZIONE COSTA 2 IN MEDIA

'''

# QUINDI LE OPERAZIONI COSTOSE :
'''le operazioni costose e non costose in una struttura di dati, come un array dinamico. 
Le operazioni costose, come la riallocazione della memoria quando l'array è pieno, richiedono tempo elevato (O(n)) 
perché comportano la copia di tutti gli elementi in un nuovo array più grande. 
Tuttavia, queste operazioni sono rare.

Dopo una riallocazione, le operazioni successive, come l'aggiunta di nuovi elementi,
diventano non costose (O(1)), poiché sfruttano lo spazio libero nel nuovo array. 
Per ottimizzare le prestazioni, è consigliabile gestire le operazioni
costose in anticipo quando prevedibili, così da minimizzare i ritardi e garantire 
un'esecuzione più fluida delle operazioni meno onerose.'''







    
#==========================================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================================

''' **Spiegazione Approfondita**

#### **Perché si usa il quadrato della distanza e non la radice quadrata?**
La **formula della distanza euclidea** per un punto `(x, y)` rispetto all'origine `(0, 0)` è:

\[\text{distanza} = \sqrt{x^2 + y^2}\]

- Tuttavia, calcolare la **radice quadrata** è un'operazione relativamente costosa in termini di prestazioni.
- Per confrontare se un punto è entro una certa distanza `r`, possiamo semplicemente confrontare il **quadrato della distanza** con il **quadrato del raggio**:
  \[x^2 + y^2 \leq r^2\]
  
- Questo confronto evita di calcolare la radice quadrata, rendendo il codice più efficiente.

#### **Esempio Numerico**
- Se `r = 2.9`, allora:
  \[ r^2 = 2.9^2 = 8.41\]
  
- Per un punto `(3, -1)`, la distanza² è:
  \[x^2 + y^2 = 3^2 + (-1)^2 = 9 + 1 = 10\]
  
  Poiché `10 > 8.41`, il punto `(3, -1)` è escluso.

#### **Cosa fa questo codice?**
1. **Iterazione sulla lista `a`:**
   Ogni elemento di `a` è una tupla `(nome, x, y)` che rappresenta un punto.
2. **Calcolo della distanza al quadrato:**
   Utilizzando la formula `x**2 + y**2`.
3. **Confronto con il raggio al quadrato:**
   Se la distanza al quadrato è minore o uguale a `r**2`, significa che il punto è entro il raggio.
4. **Aggiunta alla lista `b`:**
   Se il punto soddisfa il criterio, il suo nome viene aggiunto alla lista `b`.

'''
#==================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================================

a = [ ('a',6),('b',9,0),('c',0,1),('d',-2 , -2 )]

r = 2.9

#creare una lista che contiene nomi  dei punti in "a" a distanza al piu' "r" da 


b = [] 

#calcolo il punto di distanza tra essi 
a = [ ('A', 2, 7), ('B', 3, -1), ('C', 0, 1), ('D', -2, -2) ]  # Lista di punti, ciascuno rappresentato come una tupla (nome, x, y)
r = 2.9  # Raggio massimo consentito per la distanza dal punto di origine (0, 0)

# Creare una lista che contiene i nomi dei punti in `a` che sono a distanza al più `r` dall'origine (0,0,0)
''' n = lunghezza lista (a)'''
b = []  # vado ad analizzare punto per punto i punti che sono in a 
# Lista vuota per memorizzare i nomi dei punti che soddisfano il criterio

# Iterazione su ogni punto nella lista `a`
# facendo cosi' spachetto la tupla in piu' variabili
for nome, x, y in a:  # Destruttura ogni tupla in `n` (nome), `x` (coordinata x), `y` (coordinata y)
    # Calcola la distanza al quadrato del punto (x, y) dall'origine (0, 0) utilizzando la formula della distanza euclidea:
    # distanza² = x² + y²
    # Confrontiamo con r² (anziché calcolare la radice quadrata per la distanza effettiva), per evitare calcoli inutili.
    
    if x**2 + y**2 <= r**2:  # Verifica se la distanza² è minore o uguale a r²
        #calcola il punto di distanza dall'origine e ci sda la distanza al quadrato 
        
        b.append(nome)  # Aggiungi il nome del punto alla lista `b`                  ''' HA UN TEMPO  COSTANTE " IN MEDIA " 
        # A questo punto, `b` contiene i nomi dei punti che soddisfano il criterio
print(b)


'''    
# DIVENTA' piu' efficente usare la tupla per una questione di leggibilita' per far si che non venga modificata 

'''    

# -----------------------------------------------------
# Complessità Temporale dell'Algoritmo
# -----------------------------------------------------

# Per ogni punto nella lista `a`:
# - Viene calcolata l'espressione `x**2 + y**2 <= r**2`, che richiede 4 operazioni costanti:
#   - Il calcolo di `x**2` (elevamento al quadrato di `x`),
#   - Il calcolo di `y**2`,
#   - La somma `x**2 + y**2`,
#   - E infine il confronto con `r**2`.
# - Poiché queste operazioni richiedono un tempo costante, possiamo considerarle O(1).

# Se la condizione `x**2 + y**2 <= r**2` è verificata:
# - Viene eseguita un'operazione di `append` per aggiungere il nome del punto alla lista `b`.
# - La complessità di `append` è anch'essa O(1) per ogni operazione.

# Nel caso peggiore:
# - Tutti i punti nella lista di input `a` ricadono all'interno del raggio `r`.
# - In questo scenario, l'operazione di `append` verrà eseguita per tutti gli elementi della lista di input.

# -----------------------------------------------------
# Analisi Complessiva
# -----------------------------------------------------
# - Se la lista `a` contiene `n` punti:
#   - Il calcolo della distanza e il confronto vengono eseguiti `n` volte, con complessità totale O(n).
#   - L'operazione di `append` viene eseguita al massimo `n` volte, anch'essa con complessità totale O(n).
# - Quindi, la complessità temporale complessiva dell'algoritmo è O(n).

# -----------------------------------------------------
# Conclusione
# -----------------------------------------------------
# L'algoritmo è lineare rispetto alla dimensione della lista di input `a`.
# Nel caso peggiore, in cui tutti i punti ricadono all'interno del raggio `r`,
# il tempo di esecuzione è proporzionale al numero di punti nella lista.
   
    
    
    
    
    
     









































