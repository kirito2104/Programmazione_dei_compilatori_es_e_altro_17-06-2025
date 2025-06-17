
#14 Introduzione teorica a collezioni di dati
#⁃ list,tuple,set,dictionary
#⁃ spiegazione di collezione



#⁃ spegazione termini:
    #-ordinato: la collezione ha ordine ben definito l'aggiunta di elementi non incide
    #-indicizzato: possiamo accedere agli elementi tramite indice (index)
    #modificabile: possiamo aggiungere, cambiare e rimuovere elementi una volta creata la collezione
    # -immutabile: non possiamo aggiungere, cambiare e rimuovere elementi
    #-permette duplicati: possono esserci più elementi con lo stesso valore


#Le liste sono collezioni ordinate e modificabili. Permettono duplicati
#Le tuple sono collezioni ordinate ma immutabili. Permettono duplicati
#I set sono collezioni non ordinate e perciò non indicizzate. Non permettono duplicati
#I dictionary sono collezioni ordinate* e modificabili (dalla versione 3.7). Non permettono duplicati


#------------------------------------------------------------------------------------------------------------------------------------------------------


'''Una collezzione di dati e' cio' che ditingue  list,tuple,set,dictionary tra loro  dalle variabili normali, 
che potranno avere solo un singolo varolore, qui sotto ecco delle variabili come esempio: '''

x = 1 # ci si puo metteree un solo valore, mentrte con una collezione piu' valori 

x= '1'
x = True
'''TUTTE QUSTE PERO' POSSONO AVERE UN SINGOLO VALORE, PER FAR SI CHE POSSANO ESSERE DI PIU SI POSSO USARE LE PARENTESI'''
'''OGNI PARENTESI HA UNA SUA FUNZIONE DIVERSA'''
#-ordinato: la collezione ha ordine ben definito l'aggiunta di elementi non incide
# qualsiasi cosa ordinata e' indicizata
    #-indicizzato: possiamo accedere agli elementi tramite indice (index)

'''Questa e' una lista '''
citta = ['napoli',"livorno",'Palermo']
citta = [0]
#facendo cosi il primo valore sara' 0 e da li in poi 1 e 2, aggiungendo piu valori vanno ad accodarsi in ordine 
# di conseguenza 0 e' l'indice 

#----------------------------------------------------------------------------------------------------------------------------------
'''ENTRAMBI SONO L'OPPOSTO DELL'ALTRO '''
# - modificabile: possiamo aggiungere, cambiare e rimuovere elementi una volta creata la collezione
# - immutabile: non possiamo aggiungere, cambiare e rimuovere elementi
#-permette duplicati: possono esserci più elementi con lo stesso valore

#--------------------------------------------------------------------------------------------------------------------------
#Le liste sono collezioni ordinate( ANCHE IDICIZZATE) e modificabili. Permettono duplicati
''' -ordinato: la collezione ha ordine ben definito l'aggiunta di elementi non incide
    -qualsiasi cosa ordinata e' indicizata
    -indicizzato: possiamo accedere agli elementi tramite indice (index)'''
#-------------------------------------------------------------------------------------------------------------------------------
#Le tuple sono collezioni ordinate ma immutabili. Permettono duplicati
'''UNA VOLTA CHE DECIDIAMO CHE UNA TUPLA A TOT ELEMENTI, QUI ELEMENTI SONO, NON POSSONO PIU' CAMBIARE, 
 NON SI POSSONO MODIFICARE, SI POSSONO PERO' DUPLICARE '''

# Creazione di una tupla
tupla = (1, 2, 3, 2, 4)
print("Tupla originale:", tupla)

# Tentativo di modifica (genera errore)
# tupla[1] = 10  # Questo genera un errore perché le tuple sono immutabili

# Accesso agli elementi (è consentito)
print("Elemento alla posizione 1:", tupla[1])

# Possono contenere duplicati
print("La tupla contiene duplicati? Sì, 2 appare più volte.")

#---------------------------------------------------------------------------------------------------------------------------
#I set sono collezioni non ordinate e perciò non indicizzate. Non permettono duplicati

'''SONO COLLEZIONI NON ORDINATE E PER QUESTO NON SONO INDICIZZATE E NON SI POSSONO DIPLICARE'''

# Creazione di un set
insieme = {1, 2, 3, 4, 4, 5}  # Il numero 4 è duplicato ma sarà presente solo una volta
print("Set originale:", insieme)

# Accesso diretto tramite indice non è possibile (genera errore)
# print(insieme[1])  # Questo genera un errore

# Aggiungere un elemento al set
insieme.add(6)
print("Set dopo aggiunta di 6:", insieme)

# Rimuovere un elemento
insieme.remove(3)
print("Set dopo rimozione di 3:", insieme)


#----------------------------------------------------------------------------------------------------------------------------
#I dictionary sono collezioni ordinate* e modificabili (dalla versione 3.7). Non permettono duplicati

'''sONO COLLEZIONI ORDINATE E MODIFICABILI, MA NON SI POSSONO DUPLICARE'''

# Creazione di un dizionario
dizionario = {
    "nome": "Mario",
    "cognome": "Rossi",
    "eta": 25
}
print("Dizionario originale:", dizionario)

# Aggiunta di un nuovo elemento
dizionario["citta"] = "Roma"
print("Dizionario dopo aggiunta:", dizionario)

# Modifica di un valore esistente
dizionario["eta"] = 26
print("Dizionario dopo modifica:", dizionario)

# Duplicati nelle chiavi non sono consentiti
dizionario["nome"] = "Luigi"  # Sovrascrive il valore precedente per la chiave "nome"
print("Dizionario dopo sovrascrittura:", dizionario)

# Accesso a un valore tramite chiave
print("Valore associato alla chiave 'cognome':", dizionario["cognome"])










