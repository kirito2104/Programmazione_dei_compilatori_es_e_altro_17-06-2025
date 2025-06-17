#include <stdio.h>
#include <stdlib.h>

''' Puntatore singolo (*) → Memorizza l'indirizzo di una variabile '''
#int x = 10;
#int *p = &x; # p è un puntatore che contiene l'indirizzo di x

''' Puntatore doppio (**) → Memorizza l'indirizzo di un puntatore '''
#int **pp = &p; # pp è un puntatore a un puntatore,
              # quindi memorizza l'indirizzo di p

''' Allocazione dinamica con malloc '''

#int *arr = (int *)malloc(5 * sizeof(int)); 
# malloc alloca memoria per 5 interi e restituisce un puntatore al primo elemento

''' Reallocazione dinamica con realloc '''
'''arr = (int *)realloc(arr, 10 * sizeof(int)); '''
# realloc ridimensiona la memoria già allocata per contenere 10 interi

''' Doppio asterisco nel contesto del dizionario (hash table) '''
'''
typedef struct nodo {
    int valore;       # Dato contenuto nel nodo
    struct nodo *succ; # Puntatore al prossimo nodo nella lista
} nodo;

typedef struct dict {
    nodo **a; # Doppio asterisco: array di puntatori a liste (gestione collisioni)
    int m;    # Numero di liste (dimensione di 'a')
    int n;    # Numero di elementi nel dizionario
} dict;
'''
# "nodo **a" significa che abbiamo un array di puntatori a nodo
# Permette di avere più liste concatenate nella tabella hash

''' Spiegazione Breve '''
# * → Puntatore singolo, memorizza l'indirizzo di una variabile.
# ** → Puntatore doppio, memorizza l'indirizzo di un puntatore (usato per array di puntatori o gestione dinamica).
# malloc(size) → Alloca dinamicamente `size` byte di memoria e restituisce un puntatore.
# realloc(ptr, new_size) → Ridimensiona un'area di memoria allocata con `malloc`.

''' Complessità Computazionale '''

''' 1️⃣ Puntatori e Accesso alla Memoria '''
# L'accesso a un puntatore ha complessità O(1)


'''int y = *p;  # O(1) → Dereferenziazione per ottenere il valore'''

''' 2 Allocazione Dinamica (malloc, realloc) '''
# malloc e realloc hanno complessità diverse:
# - malloc → O(1) se memoria contigua disponibile, O(n) se deve cercare spazio
# - realloc → O(1) se espansione contigua, O(n) se copia necessaria

''' 3 Doppio Asterisco e Liste Concatenate (nodo **a) '''
# Inserimento in lista concatenata → O(1)
# Ricerca in lista concatenata → O(n/m) ≈ O(1) se m ≈ n
# Cancellazione segue la stessa logica della ricerca

''' 4 Confronto con una Tabella Hash con Ridimensionamento '''
# Se il dizionario cresce, ridimensionamento comporta reallocazione e inserimenti → O(n)
# Se il ridimensionamento raddoppia la capacità, costo ammortizzato inserimento rimane O(1)

''' 📌 Riepilogo delle Complessità '''
# | Operazione                 | Complessità |
# |-----------------------------|------------|
# | Accesso a un puntatore (`*p`) | **O(1)** |
# | Allocazione (`malloc`)      | **O(1) ~ O(n)** |
# | Riallocazione (`realloc`)   | **O(n)** |
# | Inserimento in lista (`dict->a[hash]`) | **O(1)** |
# | Ricerca in lista concatenata | **O(n/m) ≈ O(1) se m ≈ n** |
# | Cancellazione               | **O(n/m) ≈ O(1) se m ≈ n** |
# | Ridimensionamento dell'array | **O(n)** |

''' Se vuoi un'implementazione dettagliata, fammelo sapere! 🚀 '''
