





#Scrivere una funzione in python che, date due stringhe in input, restituisce True se le due stringhe sono tra loro anagrammi, False altrimenti.

#Vi ricordo che, date due parole p1 e p2, la parola p1 è un anagramma della parola p2 se spostando i caratteri di p1 è possibile ottenere la parola p2 e viceversa.

#Esempio:

'''
Le parole `riso` e `orsi` sono anagrammi
Le parole `cattive` e `civetta` sono anagrammi
'''





#Passaggi per creare la funzione "anagrams" con Bubble Sort
#Definire una funzione di ordinamento Bubble Sort

#Devi implementare un algoritmo che scambia i caratteri finché la lista non è ordinata.
#Il confronto avviene tra elementi adiacenti.
#Convertire le stringhe in liste

#Poiché Bubble Sort lavora su liste, devi trasformare ogni stringa in una lista di caratteri.
#Ordinare entrambe le liste con Bubble Sort

#Applica la funzione di ordinamento a entrambe le liste di caratteri.
#Confrontare le liste ordinate

#Se le due liste ordinate sono uguali, allora le parole sono anagrammi.

def bubble_sort(a, key =None):
    ''' Algoritmo Bubble Sort con supporto per una funzione chiave 'key'.
        - Trova l'ordine corretto degli elementi nella lista 'a'.
        - Se 'key' non è specificata, confronta direttamente i valori usando la funzione di default 'identity'.
        - La funzione 'key' permette di personalizzare il criterio di confronto.
    '''
    # Funzione 'identity': restituisce l'elemento stesso.
    # Serve come valore di default per 'key' quando questa non è specificata.
    def identity(e):
        return e  # Restituisce l'input originale (funzione identità).
     # METTENDO LA FUNZIONE IDENTITY SL SUO INTERNO DIVENTA UNA FUNZIONE LOCALE 
        # CHE VIENE USATA SOLO DENTRO QUESTA FUNZIONE 
        # QUINID LE FUNZIONI SI POSSO METTERE ANCHE ALLL'INTENO DI ALTRE A SUA VOLTA 
        
    # Lunghezza della lista
    n = len(a)
    # Se 'key' non è specificata, usiamo 'identity' come funzione di confronto.
    if key is None:
        key = identity
    # Ciclo esterno: esegue 'n-1' passate per l'ordinamento
    for c in range(n-1):  
        TERMINATO = True  # Assume che la lista sia già ordinata all'inizio della passata

        # Ciclo interno: scansiona e confronta elementi adiacenti
        for i in range(n-1-c):  # Riduce il numero di confronti ad ogni passata
            if key(a[i]) > key(a[i+1]):  # Confronto basato sulla funzione 'key'
                # Scambio degli elementi se sono fuori ordine
                a[i], a[i+1] = a[i+1], a[i]
                TERMINATO = False  # Imposta False se c'è stato uno scambio

        # Se non ci sono stati scambi, la lista è ordinata
        if TERMINATO:
            break
    

def anagrams(p1,p2):
    
    # convertiamo le parole (stringhe) in liste di caratteri
    # perché la funzione bubble_sort prende in input una stringa
    # complessità temporale: lineare nella lunghezza delle stringhe

    list_p1 = list(p1)
    list_p2 = list(p2)
    
    # ordiniamo le liste corrispndenti alle due parole con bubble_sort
    # complessità temporale: quadratica nella lunghezza delle stringhe (liste)
    bubble_sort(list_p1)
    bubble_sort(list_p2)

    # controlliamo che le due parole siano anagrammi:
    # se le due liste corrispondenti alle parole sono diverse,
    # allora non possono essere anagrammi: restituisci False.
    if list_p1 != list_p2:
        return False 
    # se le due liste sono uguali, allora le parole sono anagrammi:
    # restituisci True.
    return True 




print(anagrams("riso", "orsi"))
print(anagrams("cattive", "civetta"))
print(anagrams("programmazione", "calcolatori"))

list_p1 = str(input("inserisci parola: "))

list_p2 = str(input("inserisci la seconda parola: "))

print(anagrams(list_p1,list_p2))

#def leggi_anagrammi(p1,p2):
    
# Esempio passato 
'''
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_cifrato = "nopqrstuvwxyzabcdefghijklm"

def decrypt_rot13(testo_cifrato):
    """
    Questa funzione utilizza l'artimetica modulare:
    https://it.wikipedia.org/wiki/Aritmetica_modulare
    """
    lettura_testo = "" 
    for c in testo_cifrato:
        if c == " ":
            lettura_testo += " "
        else : 
            i = 0 
            while c != alfabeto[i]:
                #La funzione .index() serve per trovare direttamente la posizione di 
                #un elemento in una stringa o lista, senza dover usare un ciclo while. 
                #Ti spiegherò come arrivarci da solo e come semplifica il codice.
                
                i+=1
            index = ( i +13)%26
            lettura_testo += alfabeto_cifrato 
    return lettura_testo
   
s = input('scrive testo da decifrare: ')

print(decrypt_rot13(s))  
'''




    
#############################################################################################################################################################################################################################################



'''
Scrivere una funzione che, data in input una lista che può contenere liste, modifichi la lista in input appiattendola,
cioè la lista deve contenere tutti gli elementi originali ma eliminando le liste annidate.
Guardate l'esempio per capire cosa si intende.

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output : [1,2,3,4,5,6,7,8,9]

Input: ["casa",[4,5,6],3,['a',8,'l'], "programmazione"]
Output : ["casa", 4, 5, 6, 3, 'a', 8, 'l', "programmazione"]
'''

#La funzione riordina_liste_annidate(list_a) prende in ingresso una lista list_a, che può contenere sia elementi singoli sia liste annidate.
# Il suo scopo è appiattire la struttura, ovvero trasformare una lista con elementi e sotto-liste in una lista piatta, dove tutti gli elementi sono sullo stesso livello.





def riordina_liste_annidate(list_a):
    """
    Questa funzione prende in input una lista `list_a`, che può contenere elementi singoli e liste annidate.
    L'obiettivo della funzione è trasformare `list_a` in una lista piatta, cioè senza sottoliste,
    mantenendo l'ordine degli elementi e modificando direttamente `list_a` senza restituire una nuova lista.
    """

    # Creiamo una lista vuota che fungerà da contenitore temporaneo per tutti gli elementi di `list_a`.
    # Se un elemento di `list_a` è una lista, i suoi elementi verranno estratti e aggiunti singolarmente a questa lista.
    list_vuota = []  

    # Iteriamo su ogni elemento della lista `list_a`
    for a in list_a:
        # Dichiarazione non necessaria della variabile `i`, che non viene usata in questo ciclo
        i = 0  

        # Controlliamo se l'elemento `a` è una lista oppure no
        if type(a) != list:
            # Se `a` NON è una lista, lo aggiungiamo direttamente alla lista temporanea `list_vuota`
            list_vuota.append(a)
        else:
            # Se `a` è una lista, iteriamo attraverso i suoi elementi
            for elemnto in a:
                # Aggiungiamo ogni elemento della sotto-lista a `list_vuota`, uno per uno
                list_vuota.append(elemnto)

    # Ora dobbiamo modificare `list_a` in-place per renderla identica a `list_vuota`
    # Questo significa che dobbiamo sostituire i suoi elementi con quelli di `list_vuota`
    
    i = 0  # Reimpostiamo il contatore a 0 per riutilizzarlo nel ciclo seguente

    # Questo ciclo while sostituisce gli elementi di `list_a` con quelli di `list_vuota`
    while i < len(list_vuota):
        if i < len(list_a):
            # Se l'indice `i` è ancora all'interno della lunghezza originale di `list_a`,
            # sovrascriviamo l'elemento corrente di `list_a` con il corrispondente di `list_vuota`
            list_a[i] = list_vuota[i]
        else:
            # Se `list_a` ha meno elementi di `list_vuota`, dobbiamo aggiungere i rimanenti
            # Appendiamo i nuovi elementi alla fine della lista `list_a`
            list_a.append(list_vuota[i])
        i += 1  # Incrementiamo il contatore per passare all'elemento successivo

    # In questa fase, se `list_a` aveva inizialmente più elementi di `list_vuota`,
    # ci saranno degli elementi in eccesso che devono essere eliminati
    while len(list_a) > len(list_vuota):
        # Rimuoviamo l'ultimo elemento di `list_a` fino a quando la sua lunghezza non diventa uguale a quella di `list_vuota`
        del list_a[-1]

'''
Complessità Computazionale
Vediamo ora il costo computazionale dei vari passaggi della funzione:

Primo ciclo for (appiattimento della lista)

Itera su ogni elemento di list_a. Se un elemento è una lista, itera su tutti i suoi elementi.
Se la lista list_a ha n elementi e alcune voci sono liste con una somma totale di m elementi,
il ciclo ha una complessità O(n + m).
Primo ciclo while (ristrutturazione di list_a)

Nel peggiore dei casi, scorre tutti gli n + m elementi di list_vuota e aggiorna list_a di conseguenza.
Complessità: O(n + m).
Secondo ciclo while (rimozione degli elementi extra)

Questo ciclo si attiva solo se list_a era più lunga di list_vuota e rimuove al massimo n - (n + m) = |n - m| elementi.
Complessità nel peggiore dei casi: O(n).
Complessità totale:
I cicli non sono annidati, quindi la complessità totale è O(n + m).

'''



lista_test = [1, [2, 3], 4, [5, 6, 7], 8,['casa','gino'],'gino']
riordina_liste_annidate(lista_test)
print(lista_test)  # Output atteso: [1, 2, 3, 4, 5, 6, 7, 8]






#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Calcolare la complessità di una funzione può sembrare complicato all'inizio, 
ma con un metodo strutturato diventa più semplice. 
Ti do delle dritte passo-passo per calcolare la complessità in autonomia.
'''

# 1. Identifica i cicli e le operazioni principali
# Ogni volta che vediamo un ciclo `for` o `while`, dobbiamo capire quante volte viene eseguito e cosa fa.
# - Se il ciclo scorre una lista di lunghezza `n`, il costo è O(n).
# - Se il ciclo scorre una lista annidata, allora potrebbe iterare su più elementi, diventando O(n + m).

# Esempio nel codice:
# - Il primo `for` scorre tutti gli elementi di `list_a` e, se trova una lista, 
# scorre anche gli elementi interni. → O(n + m)

# - Il primo `while` copia i valori da `list_vuota` a `list_a` → O(n + m)
# - Il secondo `while` rimuove elementi in eccesso da `list_a` → O(n) nel caso peggiore.

'''

2. Analizza se i cicli sono annidati o separati
'''
# - Se un ciclo è dentro un altro ciclo, la complessità si moltiplica: O(n) * O(n) = O(n²).
# - Se i cicli sono separati (uno dopo l'altro), la complessità si somma: O(n) + O(m) = O(n + m).

# Esempio nel codice:
# - I cicli non sono annidati, ma eseguiti in sequenza.
# - Quindi sommiamo le complessità di ogni ciclo.
# Risultato: O(n + m) + O(n + m) + O(n) = O(n + m) (semplificato eliminando costanti inutili).


#- O(n/2 *n ) = O(n/2)
'''
3. Ignora costanti e coefficienti non necessari
'''
# Se un ciclo viene eseguito, per esempio, 2n volte, si dice che ha una complessità O(2n),
# ma semplifichiamo a O(n) perché la costante 2 non è rilevante per n molto grande.

# Esempi:
# - O(3n + 5) → O(n) (il `+5` è trascurabile per `n` grande)
# - O(n + n) → O(n) (perché `2n` è ancora O(n))

# Nel nostro caso, O(n + m) è già la forma semplificata.

'''
4. Fai una verifica con un esempio pratico
'''
# Per assicurarti di aver calcolato bene la complessità, prova con un input molto grande.

# Esempio pratico:
lista_test = [1, [2, 3, 4, 5, 6, 7, 8, 9, 10], 11, [12, 13, 14], 15]
# riordina_liste_annidate(lista_test)
# print(lista_test)

# - La lista originale ha 5 elementi principali, ma alcuni di essi sono liste.
# - Dopo la trasformazione, diventa una lista piatta con 15 elementi totali.
# - La funzione lavora su un totale di n + m = 15 elementi.
# - Quindi il tempo di esecuzione cresce linearmente con la somma degli elementi.

'''
5. Cosa succede se ci sono più livelli di annidamento?
'''
# Nel codice, il ciclo non gestisce liste dentro liste dentro liste (esempio: [1, [2, [3, 4]], 5]).
# Se servisse una funzione ricorsiva per gestire annidamenti multipli, la complessità potrebbe diventare più grande (O(n²) o peggio).
# Se vuoi una funzione che gestisca qualsiasi profondità di annidamento, dovresti usare una funzione ricorsiva.

'''
Conclusione
'''
# Ora hai un metodo per calcolare la complessità da solo:
# ✅ Identifica i cicli e vedi quante iterazioni fanno.
# ✅ Guarda se sono annidati o separati (moltiplica se annidati, somma se separati).
# ✅ Ignora costanti e coefficienti inutili.
# ✅ Prova con un esempio pratico per vedere se la complessità è coerente.
# ✅ Pensa a casi speciali, come liste molto annidate.

# 💡 Vuoi provare tu stesso? Prendi un altro pezzo di codice e prova a calcolare la sua complessità, poi fammelo controllare! 🚀




