//
// Created by Enzo on 18/01/2025.
//


//4)Puntatori_memoria_statica/dinamica
#include <stdio.h> // Necessaria per l'allocazione dinamica

#include <stdlib.h>
// ci saranno alcuni prototipi delle funzioni , per l'allocazione dinamica
//  queste funz. ritornano un indirizzo del primo  byte allocato
// questo tipo di dato sara' chiamato puntatore



float *crea_arry_d_float(int,float);
float *copia_array_di_float(float *a, int n);
   // la dimensione degli array e fissata al momento della COMPILAZIONE
   // L'allocazione statica : ossia che avviene nel momento in cui viene scritto il codice, viene usato per strutture array piccole
    // per allocare  lo spazio per quelli array si usa uno spazio di memoria limitata.
    // Si puo anche definire una struttura dati di una array di tipo allocazione dinamica, che viene decisa durante la compilazione del programma
    // ossia che una volta compilato decide la dimensione dell'array ossia quanto ne contiene
    // attraverso a delle chiamate possiamo chiedere al sistema operativo di allocare un certo numero di byte
    // il sistema operativo riporta il primo byte allocato, ossia l'indirizzo di memoria,
    //

/*
    * Allocazione della memoria statica e dinamica; i puntatori, definizioni e gli operatori * e &;
    *  le funzioni malloc(), sizeof() e free(); la costante NULL; aritmetica dei puntatori;
    *  definizione di array con allocazione dinamica della memoria; array come input ed output di funzioni
*/

int main0() {
    // *** Allocazione Statica ***
    // L'allocazione statica avviene a tempo di compilazione.
    // La dimensione della memoria viene fissata PRIMA che il programma venga eseguito.
    // Questo tipo di allocazione è utile quando si conosce esattamente
    // quanto spazio sarà necessario.

    // Esempio: creazione di un array di dimensione fissa.
    int arrayStatico[10];

    // Approfondimenti:
    // 1. La memoria per 'arrayStatico' è riservata nello STACK.
    // 2. Questo tipo di allocazione è veloce, poiché la memoria viene riservata automaticamente.
    // 3. Svantaggi: la dimensione non è modificabile durante l'esecuzione,
    //    quindi non è adatta per dati di dimensione variabile.

    // *** Allocazione Dinamica ***
    // L'allocazione dinamica avviene a tempo di esecuzione.
    // La memoria viene richiesta solo quando serve, utilizzando funzioni come malloc, calloc o realloc.
    // Questo tipo di allocazione è utile per gestire dati di dimensione variabile o sconosciuta in anticipo.

    // Esempio: creazione di un array dinamico con malloc.
    int *arrayDinamico = (int *)malloc(10 * sizeof(int)); // Alloca memoria per 10 interi.

    // Approfondimenti:
    // 1. La memoria allocata dinamicamente viene riservata nello HEAP.
    // 2. Vantaggi: flessibilità totale; la dimensione può essere scelta e modificata a runtime.
    // 3. Svantaggi: il programmatore deve gestire manualmente la memoria.
    //    Non liberare la memoria con 'free' può portare a "memory leaks".

    // Verifica dell'allocazione:
    // È importante controllare che 'malloc' non restituisca NULL,
    // poiché ciò indica un errore nell'allocazione della memoria.
    if (arrayDinamico == NULL) {
        printf("Errore: allocazione della memoria fallita.\n");
        return 1; // Uscita immediata in caso di errore.
    }

    // Deallocazione:
    // Una volta che la memoria allocata dinamicamente non è più necessaria,
    // è fondamentale liberarla per evitare memory leaks.
    free(arrayDinamico);

    // *** Differenze principali ***
    // 1. L'allocazione statica è più veloce e semplice da gestire,
    //    ma manca di flessibilità.
    // 2. L'allocazione dinamica è più versatile e permette di gestire dati
    //    la cui dimensione varia a runtime, ma richiede una gestione più attenta.
    // 3. Allocazione statica usa lo STACK, mentre quella dinamica usa lo HEAP.
    //    Lo STACK è limitato in dimensione, ma più veloce rispetto allo HEAP.

    return 0; // Fine del programma.
}

int main1() {

    /*Tipo puntatore:
     *Un puntatore è una variabile che memorizza l'indirizzo di memoria di un'altra variabile.
     *In pratica, invece di contenere un valore diretto, il puntatore contiene un riferimento
     *a una posizione in memoria dove è memorizzato un dato.
     *
     */

    float *p; // quindi p e' un puntatore che puntera' ad elementi float

    // l'indirizzo contenuto in p contiene un variabili di tipo float

    // i puntatori possono essere usati in diversi modi come:

    float f = 3.14;

    p = &f;   // Puntatore che contiene l'indirizzo di 'f'
    // gli sto assegnando quindi il tipo di f con il suo valore a p

    /*
    - &f restituisce l'indirizzo di f.
    - *p accede al valore memorizzato all'indirizzo puntato da p
     */

    //Creato un puntatore p che contiene l'indirizzo di memoria della variabile f./*

    /*
     *Quindi, p "punta" alla posizione in cui è memorizzato f.
      Una cella contiene il valore 3.14 (valore di f),
      e un'altra contiene l'indirizzo fittizio 123 (l'indirizzo a cui p punta).
    */
    printf("%f,%f\n",f,*p );// QUI ACCEDDO ALL'INDIRIZZO DI MEMORIA USANDO P, PUNTA AL FLOAT
    // *p e' un puntatore che tira fuori il valore dell'oggetto puntato da p

    //attraverso ad f abbiamo potuto inizializzare p
    // In alternativo uso p direttamente, dove richiedo al sistema oporativo memoria per p,
    // uso lo stesso puntatore ed a p assegno malloc


    p = malloc(sizeof(float))  ;
    // malloc verifica chiedendo al sistema operativo  se puo' allocare i byte, nel caso positivo ritorna il num di byte

    printf("sizeof(float) = %d\n", sizeof(float)); //e dara' come valore 4 ossi la dimensione dei byte
    printf(" valore di p  = %p\n", p); // e' un indirizzo , si puo' stampare sia  come un indirizzo che valore , ossia che

    /*  %p: È il formato specifico per stampare un indirizzo di memoria.
    Stampa il valore del puntatore (un indirizzo in esadecimale, ad esempio 0x7ffeeabc1234).
    Cosa stai facendo:
    Stai mostrando l'indirizzo di memoria a cui il puntatore p punta.
    Questo ti permette di vedere in quale posizione di memoria è stato allocato il blocco da malloc.
    */



    // cosa fa malloc :
    // prende in input un itero e restituisce un puntatore, l'intero che prende in input e'
    // il numero di byte che servono che voglio allocare e cio' che ritorna nel caso
    // di successo ritorna l'indirizzo il primo di questi byte allocati
    //Concludendo:
    //malloc è una funzione che alloca dinamicamente un blocco di memoria della dimensione specificata(in byte)
    //e restituisce un puntatore al primo byte di quel blocco
    // un float occupa 4 byte, ma non e' certo
    // Usando sizeof :
    // ritorna dato un tipo, ritorna il numero di byte necessari per quel tipo

}

int main() {

    float *p;

    float f = 3.14;

    p = &f;   // Puntatore che contiene l'indirizzo di 'f'

    printf("%f,%f\n",f,*p );// QUI ACCEDDO ALL'INDIRIZZO DI MEMORIA USANDO P, PUNTA AL FLOAT

    p = 0 ;

    p = malloc(sizeof(float))  ;
    // malloc verifica chiedendo al sistema operativo  se puo' allocare i byte, nel caso positivo ritorna il num di byte

    printf("sizeof(float) = %d\n", sizeof(float)); //e dara' come valore 4 ossi la dimensione dei byte
    printf(" valore di p  = %p\n", p); // e' un indirizzo , si puo' stampare sia  come un indirizzo che valore , ossia che



    *p = 2.71 ;

    printf("%f,%f\n",f,*p);

    free (p); // usando p, si potra riutilizzare lo    spazzio di memoria ssegnato a p che e' uguale a 2.71

    // nel caso di python si occupa l'interprete dell'allocazione della momoria


    /*
     *
    *La funzione `free(p);` serve a **liberare la memoria dinamica** che hai allocato con `malloc`.
    Nel tuo caso, anche se il valore `2.71` rimane fuori (non è più accessibile perché `p` punta altrove),
    devi comunque usare `free(p);` per:
    - **Evitare un memory leak**: libera la memoria allocata inutilmente.
    - **Permettere al sistema operativo di riutilizzare quella memoria**.

    In breve, `free(p);` è necessario per una corretta gestione della memoria.
     */





    // Dopo che assegni `*p = 0;`, stai dicendo che:

    // - Stai modificando il valore nella memoria a cui il puntatore `p` punta.
    // - Non stai cambiando l'indirizzo memorizzato in `p`, ma stai impostando a `0` il valore contenuto
    //   in quella posizione di memoria.

    // In pratica:
    // - Se `p` punta a un blocco di memoria (ad esempio allocato con `malloc`),
    //   assegnare `*p = 0;` significa che in quel blocco verrà memorizzato il valore `0`.

    // Esempio visivo:
    // 1. Prima:
    //    - `p` punta a un indirizzo di memoria, ad esempio `0x1234`.
    //    - In quell'indirizzo c'è il valore `2.71`.

    // 2. Dopo `*p = 0;`:
    //    - L'indirizzo `0x1234` rimane lo stesso, ma il valore contenuto diventa `0`.

    // Nota:
    // - Se `p` non punta a una posizione valida (es. se è `NULL`), fare `*p = 0;` causerebbe
    //   un errore di segmentazione (segmentation fault).

    p = malloc (2*sizeof(float)); //quindi facendo cosi' i
    /*stai allocando dinamicamente memoria per 2 valori di tipo float (8 byte totali).
     *Ora puoi usare p come un array per memorizzare due numeri in sequenza, ad esempio p[0] e p[1].*/

    *p = 0.1 ; // scrivera' sul primo di questi float
    // Scrive il valore 0.1 nel primo elemento della memoria a cui p punta.

    *(p+1)=  0.2; // sara' l'indirizzo del float successivo a quello puntato da p, quindi il suo valore dipende da sizeof(float)

    //Scrive il valore 0.2 nel secondo elemento (alla posizione successiva nella memoria,
    //perché p+1 si sposta di 1 float avanti).

    float f0 = *p, f1 = *(p+1); // qui andro' ad assegnare i valori

    /*stai copiando i valori dalla memoria puntata da p in due variabili float:
        f0 riceve il valore del primo elemento puntato da p.
        f1 riceve il valore del secondo elemento (alla posizione successiva, p+1).
    In pratica, stai leggendo i valori memorizzati in memoria e salvandoli in variabili locali.
    */
    printf("%f,%f\n",f0,f1);
    printf("%f,%f\n",*(p+2));// possibile segmentation fault, memorrrria non allocata

    printf("%f,%f\n",p[0],p[1]); // equivalente a *(p+1)

    if (p == NULL) {
        // allocazione di memoria effetuata
         return -1;

    }
    /*
     *Stampando `*(p+2)` senza averlo inizializzato, otterrai un valore casuale
     *(memoria non inizializzata) o rischi un **segmentation fault** se accedi fuori dai limiti della memoria allocata.
     */

    free(p); // voglio cambiare valore e quindi, faccio puntare p da una nuova variabile liberando spazio

    p = crea_arry_d_float(10,2.71);

    for (int i = 0 ; i<10;i++) {    // non e' definito perche stiamo assegnando ad una variabile definita prima in un altra funz


        printf("%f\n",p[i]);
    }

    //definisco un nuovo array di float
    float b[10] = {0}; // questo e' un array statico, e voglio fare una copia di b


    p = copia_array_di_float(b, 10);// prede in input l'arry insieme alla sua dimensione

    for(int i = 0; i < 10; i++)
        printf("%f\n", p[i]);
}


/*
 * VERSIONE ERRATA,

float *crea_array_di_float(int n, float v){
    float a[n]; // il valore di 'a' e' un indirizzo del primo byte della sequenza, 'a' e' definito come array statico

    for(int i=0; i < n; i++){
        a[i] = v;
    }

    return a; // a contiene l'indirizzo del primo byte della sequenza
}
*
* viene restituito l'indirizzo di una variabile locale
*
*
* da errore perche' ci dice che il programma sta restituendo qualcosa all'interno della variabile locale
*   'a' una variabile locale, quindi solo dentro il programma ha visibilita'
*
* // l'errore e' che abbiamo restituito qualcosa che non ci appartiene piu'
*
*/




float *crea_arry_d_float(int n,float v ) {

    // quando si definisce un array in modo statico e' un indirizzo

        // Alloca dinamicamente un array di 'n' elementi di tipo float
        float *a = malloc(n * sizeof(float));// ciservono n float
    // BISOGNA DIRE CHE 'a' e' del tipo giusto

        // alla funz deve tornare un puntatore a float, in caso di errore ritorna NULL

        // Verifica se l'allocazione di memoria è fallita
        if (a == NULL) { // ritorna
            return NULL; // Se malloc fallisce, restituisce NULL
        } // ritorna NULL o il puntatore se qualcosa va storto

        // Inizializza ogni elemento dell'array con il valore 'v'
        for (int i = 0; i < n; i++) {
            a[i] = v; // Assegna il valore 'v' all'elemento 'i'-esimo
        }

        // Restituisce il puntatore al primo elemento dell'array
        return a; // L'array è pronto per essere usato
    // contiene l'indirizzo del primo byte della sequenza

    }

//La funzione `crea_array_di_float` crea dinamicamente un array di `n` elementi di tipo `float`,
//inizializzati tutti con il valore `v`, e restituisce un puntatore al primo elemento.
//Se l'allocazione fallisce, restituisce `NULL`.


    //float *puntatore;
    //float a =2.34;
    //puntatore = &a;
    //istruzione

float *copia_array_di_float(float *a, int n) {
    // Alloca dinamicamente memoria per un nuovo array di 'n' elementi di tipo float
    // malloc(n * sizeof(float)) calcola il numero di byte necessari per 'n' float e li riserva
    float *b = malloc(n * sizeof(float));

    // Controlla se l'allocazione è andata a buon fine
    if (b == NULL) {
        // Se malloc fallisce, restituisce NULL per indicare che la memoria non è stata allocata
        return NULL;
    }

    // Ciclo per copiare i valori dall'array originale 'a' al nuovo array 'b'
    for (int i = 0; i < n; i++) {
        // Assegna il valore dell'elemento 'i'-esimo di 'a' all'elemento corrispondente di 'b'
        b[i] = a[i];
    }

    // Restituisce il puntatore al primo elemento del nuovo array copiato
    // Questo puntatore può essere usato per accedere ai dati copiati
    return b;
}




