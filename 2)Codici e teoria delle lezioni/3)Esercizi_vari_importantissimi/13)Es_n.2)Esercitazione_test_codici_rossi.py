
'''
2) Python
Scrivere una funzione chiamata unique che prenda come argomento 
una lista di interi a e restituisca una nuova lista contenente 
soltanto gli elementi di a che compaiono una sola volta.
Non è consentito l'utilizzo di funzioni di librerie esterne.

'''

'''
definire la funzione unique 
- deve restituire solo gli elementi di a che compaiono una volta 
- ssolo gli elementi che ci sono una volta sola 

'''
# Per l’esercizio in Python (unique)

# 📌 Analizza il problema
# - Devi restituire solo i numeri che compaiono una sola volta nella lista.
# - Non puoi usare funzioni di librerie esterne, quindi niente collections.Counter.
# - La funzione deve essere efficiente e gestire correttamente tutti i casi limite.

# 🛠 Scomponi il problema in passi più piccoli
# 1. Creare un dizionario per contare quante volte appare ogni numero nella lista.
# 2. Scorrere nuovamente il dizionario e selezionare solo gli elementi con conteggio pari a 1.
# 3. Restituire il risultato come una nuova lista.

# 🔄 Possibili approcci
# - Usare un dizionario `{}` per tenere traccia delle occorrenze senza dover iterare più volte sulla lista.
# - Utilizzare `.get(key, default)` per evitare errori di chiave non esistente.
# - Separare la fase di conteggio dalla fase di filtraggio per evitare errori.

# 🚀 Pensare alla complessità
# - Quante volte visiti ogni elemento?
#   - Con un dizionario, puoi contare gli elementi in **O(n)** e filtrare in **O(n)**, quindi la complessità totale è **O(n)**.
# - Stai usando spazio extra?
#   - Il dizionario usa spazio extra **O(n)**, ma è necessario per tenere traccia delle occorrenze.
# - Pensa a possibili approcci più efficienti:
#   - Se l'input è ordinato, si potrebbe usare un altro metodo senza dizionario.

# ✅ Testare il codice con casi differenti
# - Lista vuota → `[]` (deve restituire `[]`)
# - Lista con un solo elemento → `[7]` (deve restituire `[7]`)
# - Lista con tutti elementi ripetuti → `[2, 2, 2, 2]` (deve restituire `[]`)
# - Lista con numeri in ordine casuale → `[4, 3, 2, 3, 1, 4, 5]` (deve restituire `[2, 1, 5]`)
# - Lista con numeri negativi → `[-1, -2, -1, 3]` (deve restituire `[-2, 3]`)

# 🔥 Debugging: Se il codice non funziona come previsto
# - Stampare il dizionario dopo il conteggio per verificare se registra i valori correttamente.
# - Controllare se la fase di filtraggio sta davvero selezionando solo gli elementi con `value == 1`.
# - Assicurarsi che il `return` sia nella posizione giusta per restituire i risultati corretti.






lista_a = [1,2,1,2,3,4,5,6,6,7,8,9]

'''

def unique(lista_a):
     
   
    # Creiamo un dizionario vuoto per contare le occorrenze di ogni numero
    dict_vuota = {}

    # Creiamo una lista vuota per contenere i numeri che appaiono solo una volta
    list_b = []

    # FASE 1: Conta le occorrenze di ogni numero nella lista
    for a in list_a:
        # Se il numero esiste già nel dizionario, incrementa il conteggio
        # Se non esiste, inizializzalo a 1
        dict_vuota[a] = dict_vuota.get(a, 0) + 1  

    # FASE 2: Filtra gli elementi unici (quelli che compaiono solo una volta)
    for key, value in dict_vuota.items():
        if value == 1:  # Se il numero appare una sola volta
            list_b.append(key)  # Aggiungilo alla lista di output
        # return dict_vuota non va messo 
        
    return list_b 
    
'''    





def unique(list_a):
     
    dict_vuota = {}
    list_b = []
    
    # FASE 1: Conta le occorrenze di ogni numero
    for a in list_a:
        dict_vuota[a] = dict_vuota.get(a, 0) + 1 # Aggiorna il conteggio
    '''
    Errire commesso prima 
    Nel tuo codice, hai questo blocco dentro il primo ciclo (for a in list_a):

    for key , value in dict_vuota.items():
        if value == 1 :
            list_b.append(key)  # Aggiungi solo i numeri con valore 1
    🔍 Perché è sbagliato?

    Il dizionario non è ancora completo quando inizi a filtrare i valori.
    Ogni volta che aggiungi un nuovo elemento, il ciclo interno itera su
    tutti gli elementi aggiunti fino a quel punto, inserendo duplicati in list_b.
    Questo porta al risultato sbagliato con troppi valori ripetuti.

    ✅ Soluzione corretta: Separare la fase di conteggio dalla fase 
        di filtraggio
    Sposta la parte in cui controlli if value == 1 in un ciclo
    separato dopo aver completato il conteggio:
    '''
        
        # FASE 2: Filtra gli elementi unici
    for key , value in dict_vuota.items():
        if value == 1 :
            list_b.append(key)  # Aggiungi solo i numeri con valore 1
         
    return list_b 

lista_test = [4, 3, 2, 3, 1, 4, 5]

print(unique(lista_test))


###########################################################################################################################################################################################################
###################################################################################################################################################################################################################
'''
Codice corretto e commentato 

'''


def unique(list_a):
    # Creiamo un dizionario vuoto per contare le occorrenze di ogni numero
    dict_vuota = {}

    # Creiamo una lista vuota per contenere i numeri che appaiono solo una volta
    list_b = []

    # FASE 1: Conta le occorrenze di ogni numero nella lista
    for a in list_a:
        # Se il numero esiste già nel dizionario, incrementa il conteggio
        # Se non esiste, inizializzalo a 1
        dict_vuota[a] = dict_vuota.get(a, 0) + 1  

    # FASE 2: Filtra gli elementi unici (quelli che compaiono solo una volta)
    for key, value in dict_vuota.items():
        if value == 1:  # Se il numero appare una sola volta
            list_b.append(key)  # Aggiungilo alla lista di output
        # return dict_vuota non va messo 
        
    return list_b 


lista_test = [4, 3, 2, 3, 1, 4, 5]

print(unique(lista_test))