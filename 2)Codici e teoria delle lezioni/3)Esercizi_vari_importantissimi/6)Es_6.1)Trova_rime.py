
#Esercizio
#Scrivere una funzione rimario, a cui vengono passati come parametri una lista
# di parole e una parola inserita dall'utente tramite funzione input.

#La funzione rimario dovrà confrontare la parola inserita
# dall'utente con quelle presenti nell'elenco, alla ricerca di rime,
# intese come parole le cui ultime 3 lettere siano uguali alla parola inserita dall'utente.

#Le rime dovranno essere quindi mostrate in output utilizzando il metodo join.

#esempio:

'''
Elenco parole:  ['dare', 'fare', 'andare', 'mangiare', 'dormire', 'piacere', 'salutare']
Parola in input:  volare
Le rime corrispondenti alla parola volare sono le seguenti: dare, fare, andare, mangiare, salutare
'''

''' Comprendere il problema '''
# Devi creare una funzione rimario che:
#
# - Riceve una lista di parole.
# - Riceve una parola inserita dall'utente tramite input().
# - Confronta la parola inserita con quelle presenti nella lista.
# - Trova le parole che fanno rima, ovvero quelle che hanno le ultime 3 lettere uguali alla parola inserita.
# - Stampa tutte le parole che fanno rima, usando il metodo .join() per formattare l'output.

''' Analizzare un esempio '''
# Se hai la lista di parole:
#
# ['dare', 'fare', 'andare', 'mangiare', 'dormire', 'piacere', 'salutare']
#
# E l'utente inserisce la parola:
#
# volare
#
# Le parole che fanno rima con "volare" sono quelle che terminano con "are":
#
# dare, fare, andare, mangiare, salutare
#
# Queste parole devono essere mostrate come output.

''' Scomporre il problema in passi più semplici '''
# 💡 Cosa devi fare passo dopo passo?
#
# 1. Definire una funzione rimario(lista, parola_utente).
# 2. Estrarre le ultime 3 lettere della parola inserita dall'utente.
# 3. Scorrere la lista di parole e controllare se anche loro terminano con le stesse 3 lettere.
# 4. Raccogliere tutte le parole che fanno rima.
# 5. Stampare le parole trovate in una frase ben formattata usando .join().

''' Suggerimenti per scrivere il codice senza aiuti '''
# ✅ Suggerimento per estrarre le ultime 3 lettere di una parola:
#
# Puoi usare slicing su stringhe:
#
# parola = "volare"
# suffisso = parola[-3:]  # Prende le ultime 3 lettere della parola
# print(suffisso)  # Output: "are"

# ✅ Suggerimento per controllare se una parola fa rima:
#
# Puoi usare il metodo .endswith() oppure confrontare il suffisso:
#
# if parola.endswith(suffisso):  # Metodo più leggibile
#     print("Questa parola fa rima!")
#
# # Oppure, confrontando direttamente:
# if parola[-3:] == suffisso:
#     print("Questa parola fa rima!")

''' ✅ Suggerimento per raccogliere e unire parole in una stringa:'''
#
# Puoi usare .join() per unire una lista di parole in un'unica stringa:
#
# parole_rimate = ['dare', 'fare', 'andare']
# print(", ".join(parole_rimate))
# # Output: "dare, fare, andare"

''' Struttura generale dell'algoritmo '''
# 🔹 Definisci la funzione
# 🔹 Ottieni il suffisso della parola inserita
# 🔹 Scorri la lista e confronta le ultime 3 lettere
# 🔹 Salva le parole che fanno rima
# 🔹 Stampa l'elenco delle parole trovate in modo chiaro

# 📌 Ora prova a scrivere il codice da solo!
# 🚀 Segui i passi e prova a ragionare senza guardare codice d'esempio.
# 💡 Se hai bisogno di aiuto, prova a scrivere la tua versione e poi confrontala con l'obiettivo!


#suggerimenti : 
'''
Per svolgere l'esercizio in autonomia, ti consiglio di seguire questi passi senza suggerirti direttamente il codice:  

1. **Definisci la funzione**  
   - Dovrà ricevere una lista di parole e una parola inserita dall'utente.  
   - Assicurati che la parola dell'utente abbia almeno 3 lettere.  

2. **Trova il suffisso**  
   - Estrai le ultime 3 lettere della parola inserita.  
   - Questo sarà il criterio per trovare le rime.  

3. **Scansiona la lista**  
   - Scorri la lista di parole e verifica quali terminano con lo stesso suffisso.  

4. **Raccogli le parole che fanno rima**  
   - Crea una lista che contenga solo le parole che fanno rima.  

5. **Formatta l'output**  
   - Usa un metodo per unire le parole trovate in una stringa leggibile e stampala.  

6. **Testa il codice**  
   - Prova il programma con diverse parole per verificare che funzioni correttamente.  

Se trovi difficoltà in un punto specifico, dimmelo e ti guiderò con un aiuto mirato! 🚀
'''


#psudocodice :
'''
eleco =  ['dare', 'fare', 'andare', 'mangiare', 'dormire', 'piacere', 'salutare']

def rimario (elenco, parole_rima)

    rime= []
    
    for elmento in elenco :
        if len(elemento[i]) > 3 
            print("Riprova di nuovo: ")
       
        se elemento [-3:] == elenco [-3:]
            appendo le parole con le stesse rime 
            
    Se invece non sono rime    
        stampa ("la parola inserita' non fa rima")
    invece se : 
        output  = " , ".join(rime) # prendera' ogni stringa che ha le rime e la inserira in in ot
        stampa("ecco le rime corrispondenti "+ parole + "ecco l'elenco delle parole con la stessa rima " + output)
    
    
    


'''
#=========================================================================================================================

''' Ti spiego passo passo cosa fa questa parte di codice e perché ha quella struttura. '''

# 📌 Codice da analizzare:
# output = ", ".join(rime)
# print(
#     "Le rime corrispondenti alla parola "
#     + parola
#     + " sono le seguenti: "
#     + output
# )

# --- 

# 🔹 Cosa fa `output = ", ".join(rime)`?
# 1. `rime` è una lista che contiene tutte le parole che fanno rima con quella inserita dall'utente.
# 2. `", ".join(rime)` prende tutti gli elementi della lista `rime` e li **unisce in un'unica stringa**, separandoli con `", "`.
# 3. Il risultato viene assegnato alla variabile `output`.

''' Esempio pratico '''
# rime = ["dare", "fare", "andare", "mangiare", "salutare"]
# output = ", ".join(rime)
# print(output)

# **Output atteso:**
# dare, fare, andare, mangiare, salutare

# **Senza `join()`, la lista verrebbe stampata con le parentesi quadre**:
# print(rime)  # Output: ['dare', 'fare', 'andare', 'mangiare', 'salutare']

# Con `join()`, invece, la lista diventa una **stringa leggibile**.

# --- 

''' 🔹 Cosa fa la `print()` e perché ha quella struttura?
'''
# print(
#     "Le rime corrispondenti alla parola "
#     + parola
#     + " sono le seguenti: "
#     + output
# )

# 1. La funzione `print()` stampa il messaggio finale con le parole che fanno rima.
# 2. Le **stringhe vengono concatenate (`+`)** per formare una frase leggibile.
# 3. La scrittura su **più righe** serve solo per migliorare la leggibilità del codice, ma è equivalente a:
#    print("Le rime corrispondenti alla parola " + parola + " sono le seguenti: " + output)

# --- 

'''🔍 Esempio con dati reali:'''

# Se l'utente inserisce `"volare"`, e le parole trovate sono:
# rime = ["dare", "fare", "andare", "mangiare", "salutare"]
# allora:
# output = ", ".join(rime)

# diventa:
# output = "dare, fare, andare, mangiare, salutare"

# e il messaggio finale stampato sarà:
# Le rime corrispondenti alla parola volare sono le seguenti: dare, fare, andare, mangiare, salutare

# --- 

# 🔥 **Riassunto finale**
# ✅ `join()` **unisce gli elementi della lista** in una stringa separata da `", "`.  
# ✅ `output` **contiene la lista delle rime in formato stringa leggibile**.  
# ✅ La `print()` **compone e stampa la frase con i risultati**.  
# ✅ La scrittura su più righe **è solo per rendere il codice più leggibile**.  

'''
===========================================================================================================================================
==================================================================================================================================================
'''
# Ecco l'esercizio svolto : 

#Scrivere una funzione rimario, a cui vengono passati come parametri una lista
# di parole e una parola inserita dall'utente tramite funzione input.

#La funzione rimario dovrà confrontare la parola inserita
# dall'utente con quelle presenti nell'elenco, alla ricerca di rime,
# intese come parole le cui ultime 3 lettere siano uguali alla parola inserita dall'utente.

#Le rime dovranno essere quindi mostrate in output utilizzando il metodo join.

#esempio:


#Elenco parole:  ['dare', 'fare', 'andare', 'mangiare', 'dormire', 'piacere', 'salutare']
#Parola in input:  volare
#Le rime corrispondenti alla parola volare sono le seguenti: dare, fare, andare, mangiare, salutare



Elenco =  ['dare', 'fare', 'andare', 'mangiare', 'dormire', 'piacere', 'salutare']

# codice con alcuni errori comessi : 
'''
✅ Errore 1: Controllavi la lunghezza delle parole nella lista, invece della parola dell'utente.
✅ Errore 2: Stavi confrontando Elenco[-3], che restituisce un elemento della lista, 
    invece di controllare le ultime 3 lettere di ogni parola.
✅ Errore 3: Variabile elemnto era scritta male (corretto in elemento).
✅ Errore 4: join() era usato in modo errato su una stringa invece che su una lista.
✅ Errore 5: print() cercava di concatenare una stringa con una lista (rime), causando un errore.
✅ Errore 6: Non serve str(input()), perché input() restituisce già una stringa.
'''
#===========================================================================================================================================12

# CODICE ERRATO: 
'''
def Trova_rima(Elenco,parole_con_rima):

    rime = []
    for elemnto in Elenco :
        if len(elemnto) < 3 :
            print("riprova deve essere di piu' di tre parole: ")
        if elemnto[-3:] == parole_con_rima[-3]:
            rime.append(elemnto)
    if not rime :
            print("non e' una  parola con una rima, riprova ")
    else : 
        output = " , ".join(elemnto)
        print("le parole corrispondenti: ", parole_con_rima + " ecoo le corispondenti : " + rime)


Elenco =  ['dare', 'fare', 'andare', 'mangiare', 'dormire', 'piacere', 'salutare']

parole_con_rima = str(input("inserisci parola da verificare la rima : ") )

s = Trova_rima(Elenco,parole_con_rima)

print(s)
'''
#=========================================================================================================================================
#psudocodice :
'''
eleco =  ['dare', 'fare', 'andare', 'mangiare', 'dormire', 'piacere', 'salutare']

def rimario (elenco, parole_rima)

    rime= []
    
    for elmento in elenco :
        if len(elemento[i]) > 3 
            print("Riprova di nuovo: ")
       
        se elemento [-3:] == elenco [-3:]
            appendo le parole con le stesse rime 
            
    Se invece non sono rime    
        stampa ("la parola inserita' non fa rima")
    invece se : 
        output  = " , ".join(rime) # prendera' ogni stringa che ha le rime e la inserira in in ot
        stampa("ecco le rime corrispondenti "+ parole + "ecco l'elenco delle parole con la stessa rima " + output)
    
'''

#ECCO IL CODICE CORRETTO : 

'''
    Errore 1: Controllavi la lunghezza delle parole nella lista, invece della parola dell'utente.
    Errore 2: Stavi confrontando Elenco[-3], che restituisce un elemento della lista, 
    invece di controllare le ultime 3 lettere di ogni parola.
    Errore 3: Variabile elemnto era scritta male (corretto in elemento).
    Errore 4: join() era usato in modo errato su una stringa invece che su una lista.
    Errore 5: print() cercava di concatenare una stringa con una lista (rime), causando un errore.
    Errore 6: Non serve str(input()), perché input() restituisce già una stringa.
    Errore 7 : parole_con_rima è una stringa e non una lista
        input() restituisce una stringa, quindi devi usare parole_con_rima[-3:] 
        invece di parole_con_rima[-3] per confrontare le ultime tre lettere.
        
'''

# Funzione per trovare parole che fanno rima con una parola data
def Trova_rima(Elenco, parola_con_rima):
    # Creiamo una lista vuota dove salveremo le parole che fanno rima
    rime = []

    # Iteriamo su ogni parola nella lista Elenco
    for elemento in Elenco:
        # Controlliamo se la parola inserita è lunga almeno 3 caratteri
        if len(parola_con_rima) < 3:
            print("Riprova: la parola deve avere almeno tre lettere.")  # Messaggio di errore se è troppo corta
            return  # Terminiamo la funzione senza fare ulteriori controlli

        # Confrontiamo le ultime tre lettere della parola inserita con quelle della parola in Elenco
        if elemento[-3:] == parola_con_rima[-3:]:
            # Se corrispondono, aggiungiamo la parola alla lista delle rime
            rime.append(elemento)

    # Dopo il ciclo, verifichiamo se la lista rime è vuota
    if not rime:
        print("Non è stata trovata alcuna parola con una rima. Riprova.")  # Messaggio se nessuna parola fa rima
    else:
        # Usiamo ".join()" per trasformare la lista delle parole trovate in una stringa
        # Il metodo join() prende una lista di stringhe e le unisce in un'unica stringa, separate dal separatore scelto.
        # In questo caso, ", " è il separatore, quindi le parole saranno separate da una virgola e uno spazio.
        output = " , ".join(rime)

        # Stampiamo il risultato con un messaggio descrittivo
        print("Le parole corrispondenti: ", parola_con_rima + " ecco le corrispondenti: " + output)

        # Restituiamo la lista delle parole che fanno rima
        return rime

# Lista di parole con cui confrontare la rima
Elenco = ['dare', 'fare', 'andare', 'mangiare', 'dormire', 'piacere', 'salutare']

# Chiediamo all'utente di inserire una parola da controllare
parola_con_rima = input("Inserisci una parola per verificare la rima: ")

# Chiamiamo la funzione e salviamo il risultato in 's'
s = Trova_rima(Elenco, parola_con_rima)

# Stampiamo il risultato della funzione
print(s)

