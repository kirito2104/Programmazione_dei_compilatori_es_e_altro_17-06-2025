//
// Created by Enzo on 29/01/2025.
//
#include <stdio.h>
#include <stdlib.h>

// Struttura per un nodo di una lista doppiamente concatenata
typedef struct nodo {
    float dato;           // Valore memorizzato nel nodo
    struct nodo *succ;    // Puntatore al nodo successivo
    struct nodo *prec;    // Puntatore al nodo precedente
} nodo;

typedef nodo *clista; // Definizione di un alias per la lista concatenata

// Prototipi delle funzioni
clista clista_vuota();                 // Crea una lista vuota
void clista_mostra(clista);             // Mostra gli elementi della lista
nodo *clista_in0(clista, float);        // Inserisce un elemento in testa alla lista
nodo *clista_cerca(clista, float);      // Cerca un elemento nella lista
nodo *clista_out0(clista);              // Rimuove il primo elemento della lista
nodo *clista_out(clista, float, int);   // Rimuove un elemento specificato dalla lista
nodo *clista_in(clista, float, int);    // Inserisce un elemento in una posizione specificata

int main(int n, char *args[]){
    clista L = clista_vuota();  // Creazione di una lista vuota

    // Popolamento della lista con i valori passati come argomenti da linea di comando
    for(int i = 1; i < n; i++){
        float v;
        if (sscanf(args[i], "%f", &v) == 1){
            L = clista_in0(L, v); // Inserisce ogni valore in testa alla lista
        }
    }

    clista_mostra(L); // Mostra lo stato iniziale della lista

    // Test dell'inserimento in posizioni diverse della lista
    L = clista_in(L, 100, 0);   // Inserisce 100 in testa
    L = clista_in(L, 200, 6);   // Inserisce 200 nella posizione 6 (o in fondo se la lista è più corta)
    L = clista_in(L, 300, 1000);// Inserisce 300 alla fine della lista se la posizione è fuori range

    clista_mostra(L); // Mostra la lista dopo gli inserimenti

    return 0;
}

// Funzione per rimuovere un elemento dalla lista e inserirne uno nuovo in una posizione specificata
nodo *clista_out(clista a, float v, int i ){
    nodo *p = a;

    // Se i è 0 o la lista è vuota, inserisce un nuovo nodo in testa e restituisce la lista aggiornata
    if(i == 0 || p == NULL){
        return clista_in0(a, v);
    }

    // Scorre la lista fino alla posizione desiderata o fino alla fine della lista
    while(i != 0 && p != NULL){
        p = p->succ;
        i--;
    }

    /*
     * A questo punto, p punta all'elemento in posizione i-1 oppure all'ultimo elemento.
     * Viene creato un nuovo nodo e inserito subito dopo p.
     */

    nodo *q = clista_in0(p->succ, v); // Inserisce il nuovo nodo
    p->succ = q;  // Collega il nodo precedente al nuovo nodo
    q->prec = p;  // Collega il nuovo nodo al nodo precedente

    return a; // Restituisce la lista aggiornata
}

// Funzione per inserire un elemento in una posizione specificata della lista
clista clista_in(clista a, float v, int i){
    nodo *p = a;

    // Se la posizione è negativa, non fa nulla e restituisce la lista invariata
    if (i < 0)
        return a;

    // Se la posizione è 0 o la lista è vuota, inserisce il nuovo valore in testa
    if (i == 0 || p == NULL)
        return clista_in0(a, v);

    // Scorre la lista fino alla posizione desiderata o fino alla fine
    while (i != 1 && p->succ != NULL){
        p = p->succ;
        i--;
    }

    /*
     * A questo punto, p punta all'elemento in posizione i-1 oppure all'ultimo elemento.
     * Viene creato un nuovo nodo e inserito subito dopo p.
     */

    nodo *q = clista_in0(p->succ, v); // Crea il nuovo nodo
    p->succ = q;  // Collega il nodo precedente al nuovo nodo
    q->prec = p;  // Collega il nuovo nodo al nodo precedente

    return a; // Restituisce la lista aggiornata
}



//----------------------------------------------------------------------------------------------------------------------


clista clista_vuota(){
    return NULL;
}

void clista_mostra(clista a){
    nodo *p;

    p = a;

    printf("Contenuto della lista: ");

    while( p != NULL ){ //non raggiungo il fine lista
        printf("%5.2f, ", (*p).dato  ); // stampo il dato del nodo puntato da p
        p = p->succ; // equivalente a p = (*p).succ;
    }

    printf("\n");
}


nodo *clista_in0(clista a, float v){
    nodo *p = malloc(sizeof(nodo));
    p->dato = v;
    p->succ = a;
    p->prec = NULL;
    if (a != NULL)
        a->prec = p;
    a = p;
    return a; // oppure return p
}

nodo *clista_cerca(clista a, float k){
    nodo *p = a;

    while( p != NULL && p->dato != k ){
        p = p->succ;
    }

    return p;
}


clista clista_out0(clista a){
    clista p = a;
    if( a == NULL)
        return NULL;
    a = a->succ;
    if (a != NULL)
        a->prec = NULL;
    free(p);
    return a;
}

