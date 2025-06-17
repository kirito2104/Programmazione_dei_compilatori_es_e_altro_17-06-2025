//
// Created by Enzo on 24/01/2025.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Struttura 'elemento' che rappresenta un dato generico nella lista.
// Ogni elemento può essere di tipo:
// - 'i' (intero)
// - 'f' (float, numero in virgola mobile)
// - 's' (stringa).
// Il campo 'dato' è un puntatore generico (void*) che può puntare a un qualsiasi tipo di dato.
typedef struct {
    char tipo; /* 'i' intero; 'f' float; 's' stringa */
    void *dato;
} elemento;

// Struttura 'lista' per una lista dinamica di elementi.
// La lista è implementata come un array dinamico, con i seguenti campi:
// - 'a': puntatore all'array di elementi.
// - 'c': capacità della lista, cioè lo spazio allocato (numero massimo di elementi prima di ridimensionare).
// - 'n': dimensione attuale della lista, cioè il numero effettivo di elementi presenti.
struct lista {
    elemento *a;
    int c;  /* capacità */
    int n;  /* dimensione, numero di elementi */
};
typedef struct lista lista; // Alias per 'struct lista'.

// Funzioni per la gestione della lista.
lista init();                 // Inizializza una lista vuota.
lista append(lista, elemento);// Aggiunge un elemento alla lista.
void mostra(lista);           // Mostra gli elementi della lista.
lista pop(lista);             // Rimuove l'ultimo elemento della lista.
lista insert(lista, elemento, int); // Inserisce un elemento in una posizione specifica della lista.

// Funzioni per creare elementi specifici (intero, float, stringa).
elemento intero(int);         // Crea un elemento di tipo intero.
elemento fpoint(float);       // Crea un elemento di tipo float.
elemento stringa(char*);      // Crea un elemento di tipo stringa.

// Funzione 'cerca_tipo' che determina il tipo del contenuto di una stringa.
char cerca_tipo(char *b) {
    /*
     * Questa funzione restituisce:
     * - 'i' se la stringa contiene solo cifre decimali (numero intero).
     * - 'f' se la stringa contiene cifre decimali e **esattamente un punto** (numero in virgola mobile).
     * - 's' altrimenti (qualsiasi altra stringa).
     */

    int i = 0, numero_punti = 0; // 'i' serve per scorrere la stringa, 'numero_punti' conta i punti trovati.

    while (b[i] != '\0') { // Continua finché non si raggiunge il terminatore di stringa.
        if (b[i] == '.') { // Controlla se il carattere corrente è un punto ('.').
            if (numero_punti > 0) // Se c'è già stato un punto, la stringa non è valida come float.
                return 's';
            else
                numero_punti++; // Incrementa il contatore dei punti.
        } else if (b[i] < '0' || b[i] > '9') { // Se il carattere non è una cifra decimale.
            return 's'; // Restituisce 's' poiché non è un numero valido.
        }
        i++; // Passa al carattere successivo.
    }

    if (numero_punti == 0)
        return 'i'; // Nessun punto: numero intero.
    else
        return 'f'; // Un solo punto: numero in virgola mobile.
}

int main() {
    lista L = init(); // Inizializza una lista vuota.
    char buffer[1024]; // Buffer per memorizzare l'input dell'utente.
    int n = 0;

    while (n < 5 ) { // Ciclo infinito per chiedere all'utente input ripetuto.
        printf("Inserisci un intero, un float o una stringa e premi invio: ");

        // Legge una stringa dall'utente.
        // Usa `%s` per leggere fino a uno spazio o a un invio.
        scanf("%s", buffer);
        /*
        if (buffer[0] == '\0') // Se il buffer è vuoto (l'utente non ha inserito nulla), esce dal ciclo.
            break;*/

        // Determina il tipo della stringa inserita (intero, float, stringa).
        switch (cerca_tipo(buffer)) {
            case 'i': {
                // Se la stringa rappresenta un numero intero:
                int a; // Variabile per memorizzare l'intero.
                sscanf(buffer, "%d", &a); // Converte la stringa in un intero.
                L = append(L, intero(a)); // Aggiunge l'intero alla lista.
                break;
            }
            case 'f': {
                // Se la stringa rappresenta un numero in virgola mobile:
                float f; // Variabile per memorizzare il float.
                sscanf(buffer, "%f", &f); // Converte la stringa in un float.
                L = append(L, fpoint(f)); // Aggiunge il float alla lista.
                break;
            }
            default:
                char *s = malloc(sizeof(char) * (strlen(buffer) + 1)); // Allocazione dinamica per la stringa.
            /*
             * Alloca memoria sufficiente per memorizzare la stringa `buffer`.
             * La lunghezza di `buffer` è calcolata con `strlen(buffer)` e aggiungiamo 1 per il terminatore '\0'.
             * Questo crea una nuova stringa indipendente da `buffer`.
             */

            strcpy(s, buffer); // Copia il contenuto di `buffer` nella nuova stringa `s`.
            /*
             * `strcpy` copia carattere per carattere il contenuto di `buffer` nella memoria puntata da `s`.
             * Ora `s` contiene una copia della stringa originale.
             */

            L = append(L, stringa(s)); // Aggiunge la nuova stringa alla lista.
            /*
             * Passa la stringa duplicata `s` alla funzione `stringa()`, che la incapsula in un elemento
             * da aggiungere alla lista. A differenza di `buffer`, `s` è una copia indipendente e non sarà
             * sovrascritta durante ulteriori iterazioni.
             */

        }
        n++;
    }
    mostra(L);
}
/*QUESTO SARA' QUELLO CHE USCIRA'
* Inserisci un intero, un float o una stringa e premi invio:12.3

Inserisci un intero, un float o una stringa e premi invio:stringa1

Inserisci un intero, un float o una stringa e premi invio:2

Inserisci un intero, un float o una stringa e premi invio:una

Inserisci un intero, un float o una stringa e premi invio:una

==================================
12.300000
una
2
una
una
dimensione 5, capacita' 6

VENGO INSERITE TRE VOLTE UNA, PERCHE' E' IL VALORE DI BUFFER

L= 0  BUFFER -> |U|N|O|\0|--|--|--|
                ^______     E' VERRA' SOSTITUTITA LA STRINGA SOPRA
                      |------------------
STRINGA (BUFFER ) -> |S|----|           |
                                        |
STRINGA(BUFFER) -> |S|------| -----------

// QUINDI PRATICAMENTE L'ULTIMO ELEMENTO VERRA' AGGIUNGTO A TUTTE E TRE LE STRINGHE
 */






lista init(){
    lista lista_vuota = {NULL, 0, 0};
    return lista_vuota;
}

lista append(lista L, elemento e){
    if (L.n == L.c) {
        L.c = 2*(L.c+1);
        L.a = realloc( L.a, L.c*sizeof(elemento) );
    }

    L.a[L.n] = e;
    L.n++;

    return L;
}

lista insert(lista L, elemento e, int p){
    int i;

    if(p < 0){
        p = 0;
    }

    L = append(L, e);

    for( i = L.n-1; i > p; i--){
        L.a[i] = L.a[i-1];
        L.a[i-1] = e;
    }


    return L;

    /*
     * Complessita' temporale O(L.n - p) e quindi O(n) nel caso peggiore
     *
     * */

}


void mostra(lista L){
    int i;

    printf("==================================\n");

    for(i = 0; i < L.n; i++){
        /* stampa L.a[i] */
        /*
         * if( L.a[i].tipo == 'i' )
            printf("%d\n", *((int*)L.a[i].dato) );
        */
        switch  (L.a[i].tipo) {
            case 'i':
                printf("%d\n", *((int*)L.a[i].dato) );
                break;
            case 'f':
                printf("%f\n", *((float*)L.a[i].dato) );
                break;
            case 's':
                printf("%s\n", (char*)L.a[i].dato );
                break;
            //default:
                /* se non vero i precedenti*/
        }
    }

    printf("dimensione %d, capacita' %d\n", L.n, L.c);
}

lista pop(lista L){
    if(L.n > 0 ){
        L.n--;
        if (L.n < L.c/4){
            L.c = L.c/2;
            L.a = realloc(L.a, (L.c)*sizeof(elemento));
        }
        if (L.a[L.n].tipo != 's')
            free(L.a[L.n].dato);
    }
    return L;
}

elemento intero(int d){
    elemento e = {'i', NULL};

    e.dato = malloc(sizeof(int));
    *((int*)e.dato) = d;

    return e;
}

elemento fpoint(float d){
    elemento e = {'f', NULL};

    e.dato = malloc(sizeof(float));
    *((float*)e.dato) = d;

    return e;
}

elemento stringa(char *d){
    elemento e = {'s', NULL};

    e.dato = d;

    return e;
}
