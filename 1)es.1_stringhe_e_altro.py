def string_filter(string, filter_string):
    # Inizializza una stringa vuota per raccogliere i caratteri comuni
    common_characters = ""
    # Imposta il primo indice per il ciclo esterno
    i = 0
    # Il ciclo esterno itera attraverso ogni carattere nella stringa 'string'
    while i < len(string):
        # Imposta il secondo indice per il ciclo interno
        j = 0
        # Il ciclo interno itera attraverso ogni carattere nella stringa 'filter_string'
        while j < len(filter_string):
            # Verifica se il carattere corrente in 'string' corrisponde a quello in 'filter_string'
            # e che non sia già presente in 'common_characters' per evitare duplicati
            if string[i] == filter_string[j] and string[i] not in common_characters:
                # Aggiunge il carattere comune a 'common_characters'
                common_characters += string[i]
            # Incrementa l'indice del ciclo interno
            j += 1
        # Incrementa l'indice del ciclo esterno
        i += 1

    # Ritorna la stringa contenente tutti i caratteri comuni trovati
    return common_characters


def string_filter_compact(string, filter_string):
    # Inizializza una stringa vuota per raccogliere i caratteri comuni
    common_characters = ""
    # Itera su ogni carattere nella stringa 'string'
    for c in string:
        # Verifica se il carattere è presente in 'filter_string'
        if c in filter_string:
            # Aggiunge il carattere a 'common_characters' (questo metodo non verifica i duplicati)
            common_characters += c

    # Ritorna la stringa contenente tutti i caratteri comuni trovati
    return common_characters


# Main function to handle user input and display the output
def main():
    # Chiede all'utente di inserire la prima stringa
    x = input("type first string: ")
    # Chiede all'utente di inserire la seconda stringa
    y = input("type second string: ")
    # Chiama la funzione 'string_filter' per trovare i caratteri comuni
    result = string_filter(x, y)
    # Stampa i caratteri comuni trovati
    print("Common characters:", result)

# Verifica se lo script è eseguito come programma principale
if __name__ == "__main__":
    main()


#=================================================================================================================================================================================================================================================================================

#Scrivere un programma che date due stringe in input, in output stampa solo
# i caratteri che la prima stringa ha in comune con la seconda stringa. Utilizzare le funzioni.

#< (min)
# > (magg)

def trova_stringa(stringa1, stringa2): # qui dichiaro le due variabili che voglio conforntare, dentro la funzione, come variabili locali 
    
    conta_caratteri = '' # inizializza una stringa vuota per raccogliere i caratteri comuni della stringa 
    
    i = 0  # imposto un indice per controllare la pozizione della prima stringa, che parte da 0 
     
     # Il ciclo esterno itera attraverso ogni carattere nella stringa 'string
    while i < len(stringa1): # qui confronta i che sarebbe l'indice, itera con la prima stringa legendo il suoi caratteri 
        j=0 # inizializzo il primo carattere  
        
        while j < len(stringa2): 
            if stringa1[i] == stringa2[j] and stringa1 not in conta_caratteri: # complessita' temporale O(n**2)
                conta_caratteri += stringa1[i]
            j+= 1
        i+= 1
    
    return conta_caratteri


y= input('inserisci testo1 : ')
x = input('inserisci testo2 : ')


print('ecco i caratteri uguali : ',trova_stringa(x,y))





