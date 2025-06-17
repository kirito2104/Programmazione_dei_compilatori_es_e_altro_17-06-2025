//
// Created by Enzo on 29/01/2025.
//

/*
 *    progettare struttura dati tipo coda che consenta le seguenti operazioni:
 * - Init coda vuota
 * - Inserimento di  una stringa
 * - Lettura  (stampa ) della stringa piu' "anziana" della struttura
 * - Cancellazione della stringa piu' "anziana" della struttura
 *
 *  */


/*
 *
 * Possibili implementazioni
 *
 * Array dinamico (lista):
 *    - Inserimento in testa (in fondo ) , il costo O(1)
 *    - Lettura della  stringa + anziana (l'elemento in pos 0 della lista ) costo O(1)
 *    - Cancellazione dell'elemento in pos 0 richiede O(n) operazioni
 *
 * Adattamento teniamo traccia della posizione del primo elemento della sequenza
 * che modificheremo al momento della cancellazione.
 *
 *
 *  */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definizione di una struttura generica per contenere diversi tipi di dati
typedef struct {
    char tipo; /* 'i' intero; 'f' float; 's' stringa */
    void *dato; // Puntatore generico per contenere qualsiasi tipo di dato
} elemento;

// Definizione della struttura lista
struct lista {
    elemento *a; // Puntatore all'array di elementi
    int c;  /* Capacità massima della lista */
    int n;  /* Numero di elementi attualmente presenti */
    int p;  /* Posizione del primo elemento, utile per implementazioni circolari */
};
typedef struct lista lista; // Definizione di tipo per una lista

// Prototipi delle funzioni per la gestione della lista
lista init(); // Inizializza una lista vuota
lista append(lista, elemento); // Aggiunge un elemento alla lista
void mostra(lista); // Mostra gli elementi della lista
lista pop(lista); // Rimuove un elemento dalla lista (da implementare)
lista insert(lista, elemento, int); // Inserisce un elemento in una posizione specifica (da implementare)

// Funzioni di creazione degli elementi di diversi tipi
elemento intero(int);
elemento fpoint(float);
elemento stringa(char*);

// Funzione per determinare il tipo di una stringa di input
char cerca_tipo(char *b) {
    /*
     * Ritorna 'i' se e solo se b contiene solo cifre decimali.
     * Ritorna 'f' se e solo se b contiene cifre decimali e un solo punto decimale.
     * Ritorna 's' in tutti gli altri casi.
     */

    int i = 0, numero_punti = 0;

    while (b[i] != '\0') {
        if (b[i] == '.') { // Controlla se è un punto decimale
            if (numero_punti > 0) // Se c'è già un punto, non può essere un numero float
                return 's';
            else
                numero_punti++;
        } else if (b[i] < '0' || b[i] > '9') // Se non è un numero
            return 's';
        i++;
    }

    if (numero_punti == 0) // Se non ci sono punti decimali, è un intero
        return 'i';
    else
        return 'f'; // Altrimenti è un numero float
}

// Funzione principale del programma
int main( int n, char *args[]) {
    // Inizializza una lista vuota.
    // Si presuppone che la funzione "init()" restituisca una lista vuota su cui poi operare.
    lista L = init();

    // Allocazione dinamica di memoria per due stringhe di massimo 10 caratteri.
    // Questa memoria deve essere liberata successivamente per evitare memory leaks.
    char *s0 = malloc(10);
    char *s1 = malloc(10);

    // Copia le stringhe "dieci" e "undici" nelle aree di memoria appena allocate.
    // La funzione strcpy(dest, src) copia il contenuto di src in dest, includendo il carattere di terminazione '\0'.
    strcpy(s0, "dieci");
    strcpy(s1, "undici");

    // **Inserimento degli argomenti della riga di comando nella lista**
    // Il primo argomento (args[0]) è il nome del programma, quindi il ciclo parte da args[1].
    // Il ciclo itera su tutti gli argomenti passati dalla riga di comando.
    for(int i = 1; i < n; i++){
        // Crea un elemento di tipo 's' con il valore args[i].
        // Si presume che la struttura "elemento" sia definita con un campo 'tipo' (es. 's' per stringa)
        // e un campo 'valore' (puntatore a stringa).
        elemento e = {'s', args[i]};

        // Aggiunge l'elemento alla lista. La funzione "append()" restituisce la lista aggiornata con il nuovo elemento.
        L = append(L, e);
    }

    // Stampa la lista dopo aver aggiunto gli argomenti.
    // La funzione "mostra()" dovrebbe stampare il contenuto della lista.
    mostra(L);

    // **Rimozione di due elementi dalla lista**
    // Si presuppone che la funzione "pop()" rimuova un elemento dalla lista (probabilmente il primo o l'ultimo).
    L = pop(L);
    L = pop(L);

    // **Creazione di nuovi elementi e reinserimento nella lista**
    // Vengono creati tre nuovi elementi:
    // - e0: contiene la stringa "dieci" (puntatore s0)
    // - e1: contiene la stringa "undici" (puntatore s1)
    // - e: contiene il primo argomento args[0] (solitamente il nome del programma)
    elemento e0 = {'s', s0}, e1 =  {'s', s1}, e = {'s', args[0]};

    // Aggiunge il primo argomento della riga di comando alla lista.
    L = append(L, e);

    // Stampa la lista dopo questa modifica per verificare il nuovo stato.
    mostra(L);

    // Aggiunge le stringhe "dieci" e "undici" alla lista.
    L = append(L, e0);
    L = append(L, e1);

    // Stampa la lista finale dopo tutte le modifiche.
    mostra(L);
}



// Funzione per inizializzare una lista vuota
lista init() {
    lista lista_vuota = {NULL, 0, 0, -1}; // Inizializza la lista con valori di default
    return lista_vuota;
}

// Funzione per aggiungere un elemento alla lista
lista append(lista L, elemento e) {
    // Controlla se la lista ha raggiunto la sua capacità massima
    if (L.n == L.c) {
        L.c = 2 * (L.c + 1); // Aumenta la capacità (strategia di ridimensionamento)
        elemento *t = malloc(L.c * sizeof(elemento)); // Alloca un nuovo array di elementi
        for (int i = 0; i < L.n; i++) {
            t[i] = L.a[(L.p + i) % L.n]; // Copia gli elementi esistenti nel nuovo array
        }
        free(L.a); // Libera la memoria del vecchio array
        L.a = t; // Assegna il nuovo array alla lista
        L.p = 0; // Resetta l'indice del primo elemento
    }

    // Aggiunge il nuovo elemento nella posizione corretta
    L.a[(L.p + L.n) % L.c] = e;
    L.n++; // Incrementa il numero di elementi

    return L; // Restituisce la lista aggiornata
}

// Funzione per mostrare gli elementi della lista
void mostra(lista L) {
    int i; // Variabile di iterazione

    printf("==================================\n");

    // Scorre tutti gli elementi presenti nella lista e li stampa in base al loro tipo
    for (i = 0; i < L.n; i++) {
        /*
         * Poiché la lista può essere circolare (con possibile riutilizzo dello spazio),
         * l'indice effettivo dell'elemento viene calcolato con:
         * (L.p + i) % L.c
         * L.p è la posizione del primo elemento nella lista
         * i è l'iterazione corrente
         * L.c è la capacità totale della lista
         * L'uso del modulo assicura che l'indice non superi i limiti dell'array allocato
         */
        switch (L.a[(L.p + i) % L.c].tipo) {
            case 'i': // Se il tipo è intero
                /*
                 * L.a[(L.p + i) % L.c] è un elemento della lista
                 * .dato è il puntatore generico che contiene il valore effettivo
                 * Per ottenere il valore intero, effettuiamo il cast a (int*)
                 * e poi dereferenziamo per ottenere il valore effettivo
                 */
                printf("%d\n", *((int*)L.a[(L.p + i) % L.c].dato));
                break;

            case 'f': // Se il tipo è un float
                /*
                 * Stessa logica del caso precedente, ma con cast a (float*)
                 * per ottenere il valore in virgola mobile
                 */
                printf("%f\n", *((float*)L.a[(L.p + i) % L.c].dato));
                break;

            case 's': // Se il tipo è una stringa
                /*
                 * Poiché le stringhe sono già puntatori a caratteri (char*),
                 * non serve la dereferenziazione. Basta effettuare un cast a (char*)
                 * e stamparla direttamente.
                 */
                printf("%s\n", (char*)L.a[(L.p + i) % L.c].dato);
                break;

            default: // Se il tipo non è riconosciuto
                printf("Tipo non riconosciuto\n");
        }
    }

    // Stampa le informazioni sulla lista dopo aver mostrato gli elementi
    printf("Dimensione: %d, Capacità: %d\n", L.n, L.c);
}

/*====================================================================================================================*/

// Funzione che rimuove l'elemento in testa alla lista L
lista pop(lista L) {
    // Verifica se la lista contiene almeno un elemento
    if (L.n > 0) {
        /*
         * Se il tipo dell'elemento che stiamo rimuovendo non è una stringa ('s'),
         * signifca che abbiamo allocato dinamicamente la memoria per quell'elemento
         * (ad esempio, per un intero o un float). In questo caso, è necessario
         * liberare la memoria puntata da L.a[L.p].dato con free().
         */
        if (L.a[L.p].tipo != 's')
            free(L.a[L.p].dato);

        /*
         * Aggiorna la posizione del primo elemento della lista:
         * - L.p è l'indice del primo elemento
         * - (L.p+1) % L.c sposta l'indice del primo elemento "in avanti" di 1 posizione,
         *   garantendo di rimanere all'interno dell'array grazie all'operazione di modulo.
         */
        L.p = (L.p + 1) % L.c;

        // Decrementa il numero di elementi nella lista
        L.n--;

        /*
         * Controlla se dopo la rimozione la dimensione è diventata troppo piccola
         * rispetto alla capacità (condizione L.n < L.c/4).
         * Se la lista è molto "sottoutilizzata", si decide di ridurre la capacità
         * a metà (L.c = L.c/2) per recuperare memoria inutilizzata.
         */
        if (L.n < L.c / 4) {
            // Riduce la capacità a metà
            L.c = L.c / 2;

            // Alloca un nuovo array di 'elemento' con la capacità aggiornata
            elemento *t = malloc(L.c * sizeof(elemento));

            /*
             * Copia gli elementi rimanenti dal vecchio array al nuovo.
             * Si itera fino a i < L.n, per trasferire solo gli elementi effettivamente presenti.
             * Per ciascun elemento, si calcola l'indice relativo con (L.p + i) % L.n.
             * NOTA: qui si assume che la logica circolare sia ancora gestita correttamente
             * utilizzando % L.n. In alcune implementazioni, si potrebbe anche usare la
             * vecchia capacità, ma in questo caso la strategia è quella di copiare
             * gli elementi "veri" (L.n) come se il nuovo array ripartisse da zero.
             */
            for(int i = 0; i < L.n; i++) {
                t[i] = L.a[(L.p + i) % L.n];
            }

            // Libera il vecchio array
            free(L.a);

            // Assegna il nuovo array all'interno di L
            L.a = t;

            /*
             * Reimposta L.p a 0, dal momento che ora i primi L.n elementi
             * si trovano ordinati a partire dall'indice 0 nel nuovo array
             */
            L.p = 0;
        }
    }
    // Ritorna la lista aggiornata (eventualmente con un elemento in meno)
    return L;
}







/**********************************************************************************************************************/
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





//cd C:\Users\enzob\CLionProjects\2_Programmazione_2025\
