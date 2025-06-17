//
// Created by Enzo on 26/01/2025.
//
#include <stdio.h>
#include <stdlib.h>



// lista concatenata definz. prof.
/*
 *le liste concatenate gli elementi possono essere distribuiti come risulta piu'comodo al sistema operativo,
 * essendo distribuiti in memoria gli elemeenti, si ha un altro vantaggio ossia quello di dover richiedere una serie celle consecutive in memoria
 *
 *nella lista concatenata nella memoria localizzo un elemento

* Tutti gli elementi sono in posti diversi della memoria pero'
*
* per fa agregare tali oggetti qui sotto, creo un puntatore "L"
* E A TALE ASSEGNO L'INDIRIZZO DEL PRIMO ELEMNTO
*
*            nodo : contera'una serie di informazioni, ossia { - in c sara una struct che contera', un dato ( float )
*                                                              - avra'un' altra info che ci dira'di che tipo sara' un puntatore a (*nodo)
*
* L ---> |   3.14  |   // tale ha delle info aggiuntive, tra queste c'é l'informazione dell'elemnto successivo
*             |
*             |
*         |  0.0  | // ( da una altra parte avro ad es: |0.0| ) e tale avra'la posiz di quello dopo
*             |------------>  |   2.71   |  // e questo a sua volta su quello sucessivo
*                                   |
*                               | 1.4 0/ | // e tale sara' lúltimo e'puntera'ad un'elemento vuoto
*
*       |         |
*       |         |
*       |         |

 **/



// LISTA CONCATENATA
/*
 * Le liste concatenate sono strutture dati formate da nodi, ciascuno dei quali contiene due informazioni:
 * 1. Il **dato** (ad esempio un numero, una stringa, un riferimento a un oggetto, ecc.).
 * 2. Un **puntatore** al nodo successivo nella lista (o NULL se è l'ultimo elemento).
 *
 * Caratteristiche principali:
 * ---------------------------------
 * 1. **Distribuzione degli elementi in memoria:**
 *    - Gli elementi di una lista concatenata non devono essere memorizzati in celle consecutive di memoria.
 *      Questo è un vantaggio significativo rispetto agli array, che invece richiedono blocchi contigui.
 *    - Ogni nodo può essere allocato in una qualsiasi posizione della memoria disponibile.
 *      Questo rende le liste concatenate particolarmente utili in sistemi con memoria frammentata.
 *
 * 2. **Inserimento ed eliminazione:**
 *    - Gli elementi possono essere inseriti o eliminati facilmente, senza dover spostare altri elementi.
 *    - L'inserimento in testa o in coda richiede solo la modifica dei puntatori, con complessità **O(1)**.
 *    - L'inserimento in una posizione arbitraria o la cancellazione richiedono di iterare fino alla posizione desiderata
 *      (complessità **O(n)** nel caso peggiore).
 *
 * 3. **Accesso sequenziale:**
 *    - Per accedere a un elemento in una lista concatenata, è necessario iterare attraverso i nodi partendo dalla testa.
 *    - Questo rende l'accesso agli elementi meno efficiente rispetto agli array (complessità **O(n)** contro **O(1)** degli array).
 *
 * Vantaggi delle liste concatenate rispetto agli array:
 * ------------------------------------------------------
 * - Non è necessario richiedere blocchi di memoria contigui, rendendo la struttura più flessibile.
 * - La dimensione della lista può crescere dinamicamente senza dover riallocare memoria (come accade con gli array).
 *
 * Svantaggi:
 * ------------------------------------------------------
 * - Maggiore utilizzo di memoria: ogni nodo necessita di spazio aggiuntivo per memorizzare il puntatore.
 * - Accesso meno efficiente: per trovare un elemento specifico, è necessario iterare dalla testa fino al nodo desiderato.
 *
 * Esempio pratico:
 * ------------------------------------------------------
 * Supponiamo di voler memorizzare i valori [10, 20, 30] in una lista concatenata.
 *
 * Struttura in memoria:
 *
 * [10 | puntatore] -> [20 | puntatore] -> [30 | NULL]
 *
 * - Ogni elemento è un nodo.
 * - Il "puntatore" indica l'indirizzo del nodo successivo.
 * - L'ultimo nodo punta a NULL.
 *
 * Esempi di operazioni:
 * 1. **Inserimento in testa:**
 *    Per inserire un nuovo nodo con valore `5`:
 *    - Creiamo un nuovo nodo e lo facciamo puntare al nodo corrente in testa.
 *    - Aggiorniamo il puntatore della testa per puntare al nuovo nodo.
 *
 *    Risultato:
 *    [5 | puntatore] -> [10 | puntatore] -> [20 | puntatore] -> [30 | NULL]
 *
 * 2. **Eliminazione di un nodo (es. 20):**
 *    - Cerchiamo il nodo che punta a 20 (in questo caso il nodo contenente 10).
 *    - Modifichiamo il puntatore di 10 per puntare al nodo successivo (30).
 *    - Liberiamo la memoria del nodo contenente 20.
 *
 *    Risultato:
 *    [10 | puntatore] -> [30 | NULL]
 *
 * Complessità:
 * ------------------------------------------------------
 * - **Inserimento in testa:** O(1)
 * - **Inserimento in una posizione generica:** O(n) (dobbiamo trovare il nodo precedente).
 * - **Cancellazione in testa:** O(1)
 * - **Cancellazione in una posizione generica:** O(n) (dobbiamo trovare il nodo da eliminare).
 * - **Accesso a un elemento specifico:** O(n)
 *
 * Codice di esempio per una lista concatenata:
 * ------------------------------------------------------
 */
//Ecco degli esempi :
/*
#include <stdio.h>
#include <stdlib.h>

// Nodo della lista concatenata
typedef struct Nodo {
    int dato;              // Valore del nodo
    struct Nodo *next;     // Puntatore al nodo successivo
} Nodo;

// Funzione per creare un nuovo nodo
Nodo* crea_nodo(int valore) {
    Nodo* nuovo = (Nodo*)malloc(sizeof(Nodo));
    nuovo->dato = valore;
    nuovo->next = NULL;
    return nuovo;
}

// Funzione per inserire un nodo in testa
Nodo* inserisci_in_testa(Nodo* testa, int valore) {
    Nodo* nuovo = crea_nodo(valore);
    nuovo->next = testa;
    return nuovo;
}

// Funzione per stampare una lista concatenata
void stampa_lista(Nodo* testa) {
    Nodo* corrente = testa;
    while (corrente != NULL) {
        printf("%d -> ", corrente->dato);
        corrente = corrente->next;
    }
    printf("NULL\n");
}

// Funzione per eliminare un nodo dalla testa
Nodo* elimina_testa(Nodo* testa) {
    if (testa == NULL) return NULL;
    Nodo* nuovo_testa = testa->next;
    free(testa);
    return nuovo_testa;
}

// Esempio di utilizzo
int main() {
    Nodo* lista = NULL;

    // Inserimento in testa
    lista = inserisci_in_testa(lista, 30);
    lista = inserisci_in_testa(lista, 20);
    lista = inserisci_in_testa(lista, 10);

    // Stampa della lista
    printf("Lista iniziale: ");
    stampa_lista(lista);

    // Eliminazione del primo nodo
    lista = elimina_testa(lista);
    printf("Lista dopo eliminazione della testa: ");
    stampa_lista(lista);

    return 0;
}
*/

/*
 * Output atteso:
 * Lista iniziale: 10 -> 20 -> 30 -> NULL
 * Lista dopo eliminazione della testa: 20 -> 30 -> NULL
*/




typedef struct nodo { //  creo una struttura dati per definire il tipo ossi: nodo, i campi saranno
    float dato; // un dato di tipo float
    struct nodo *succ; // e tale sarà il tipo di dato puntato al nodo successivo
} nodo;

typedef nodo *clista; // lista concatenata, va il puntatore a clista

// Funzione per inizializzare una lista concatenata vuota.
// Una lista vuota è rappresentata da un puntatore a NULL.
clista clista_vuota();

// Funzione per mostrare gli elementi nella lista concatenata.
// Itera su ogni nodo della lista e stampa il valore contenuto nel campo "dato".
void clista_mostra(clista);

// Funzione per aggiungere un elemento in testa alla lista concatenata.
// La funzione crea un nuovo nodo con il valore specificato e lo inserisce in testa.
nodo *clista_in0(clista, float);

// Funzione per cercare un elemento nella lista concatenata.
// Restituisce un puntatore al nodo contenente il valore cercato, oppure NULL se non trovato.
nodo *clista_cerca(clista, float);

int main() {
    clista L0 = clista_vuota(); // facendo così abbiamo inizializzato una lista concatenata vuota.

    clista_mostra(L0); // Mostra la lista vuota (non stampa nulla).

    nodo q = {3.14, NULL}; // Creazione di un nodo con il valore 3.14 e nessun successivo (NULL).
    nodo p = {0.0, NULL}; // Creazione di un altro nodo con il valore 0.0.

    L0 = &q; // q diventa la testa della lista.

    // Aggiungo il nodo p in coda alla lista:
    p.succ = &q; /* modo alt. p.succ = L0 */
    L0 = &p; // Ora p è in testa, e q segue p nella lista.

    clista_mostra(L0); // Mostra la lista: 0.0, 3.14.

    clista L1 = clista_vuota(); // Creo una nuova lista vuota.

    // Aggiungo 10 elementi (0.0, 1.0, ..., 9.0) in testa alla lista L1.
    for (int i = 0; i < 10; i++) {
        L1 = clista_in0(L1, i); // Inserimento dinamico in testa.
    }
    clista_mostra(L1); // Mostra la lista: 9.0, 8.0, ..., 0.0.

    nodo *point = clista_cerca(L1, 6); // Cerco il valore 6 nella lista L1.
    if (point != NULL) {
        printf("Ecco il dato: %f\n", point->dato); // Se trovato, stampo il valore.
    } else {
        printf("Error, non trovato\n"); // Se non trovato, stampo un messaggio di errore.
    }
}

// Funzione per inizializzare una lista concatenata vuota.
// Restituisce NULL per indicare che la lista non contiene elementi.
clista clista_vuota() {
    return NULL;
}


void clista_mostra (clista a )
{
    nodo *p; // a p gli assegnamo il nodo
    p = a;
    printf("Contenuto nella lista: ");
    while (p != NULL) // quindi facendo cosi'finche'la lista risultera' con un elemnto continua finche'non e'vuota
        // fin tanto che non raggiungo la fine della lista, se p punta la fine della lista, stampiamo il dato dentro il nodo
    {
        printf("%f , ", (*p).dato); // facendo cois'stampera'l'elemento (*p).dato , *p ->dato, e' equivalente

        p = p->succ; // si puo'usare anche questa sintassi che equivale a quella qui sotto
        // sono equivalenti:
        /*p = (*p).succ; // facendo cosi'puntera' al dato sucessivo*/
    }
    printf("\n");// non averemmo nulla se la lista e'vuota
}

nodo *clista_in0(clista a, float v)
{


    nodo *p = malloc(sizeof(nodo)); // Alloca dinamicamente memoria per il nodo
    p->dato = v; // Assegna il valore `v` al campo `dato`
    p->succ = a; // Fai puntare il nuovo nodo `p` alla lista corrente (testa precedente)

    // Nota: Le linee commentate sono un'alternativa, ma non funzionano correttamente per liste concatenate:
    /* nodo p = {v, NULL}; */ // Questa crea un nodo nello stack (non persistente)
    /* p.succ = a; */         // Questo collega il nodo temporaneo al resto della lista
    /* a = &p; */             // Questo assegna `a` al puntatore di un nodo nello stack (non valido fuori dalla funzione)

    a = p; // Assegna la nuova testa della lista (il nuovo nodo `p`)

    return a; // Restituisce il puntatore al nuovo nodo
}
/*
     * Differenza tra l'implementazione attuale e quella illustrata nei commenti:
     *
     * 1. **Implementazione attuale (attiva nel codice):**
     *    - Alloca dinamicamente memoria per un nuovo nodo con `malloc(sizeof(nodo))`.
     *    - Il nuovo nodo `p` viene popolato con il valore `v` (nel campo `dato`) e il puntatore al nodo precedente (nel campo `succ`).
     *    - La memoria per il nodo rimane valida finché non viene esplicitamente liberata con `free()`.
     *    - La funzione restituisce il puntatore al nodo appena creato.
     *    - Vantaggi: Questa implementazione è **dinamica**, quindi può essere utilizzata senza problemi con liste concatenate di dimensione variabile.
     *
     * 2. **Versione commentata:**
     *    - Invece di allocare memoria dinamica, crea un nodo temporaneo `p` come variabile locale nello stack.
     *      ```c
     *      nodo p = {v, NULL};
     *      ```
     *    - La variabile `p` esiste solo all'interno della funzione. Quando la funzione termina, la memoria per `p` viene automaticamente liberata.
     *    - Quando si tenta di restituire `a = &p;` (un puntatore a un nodo nello stack), il comportamento è **non definito**, poiché il puntatore fa riferimento a memoria non valida.
     *    - Limiti: Questa versione **non è valida** per liste concatenate, poiché il nodo non è persistente.
     *
     * Conclusione:
     * - La versione attuale è corretta ed efficiente per la gestione dinamica della memoria.
     * - La versione commentata **non funziona**, poiché il nodo creato nello stack viene distrutto quando la funzione termina.
     */
// facendo cosi'a differenza di prima andro ad allocare la memoria'della lista in modo dinamico a differenza di prima
    // siccome perche'c'era la variabile p che veniva presa da un altra parte quindi non e'dinamica


nodo *clista_cerca (clista a, float k)
{
    nodo *p = a; // Inizializzo il puntatore `p` alla testa della lista (primo nodo).

    // verifichiamo che se il dato nel nodo, sia uguale !k
    while (p != NULL && p->dato != k) /* bisogna   prima nel caso in cui sia null , noi andiamo a leggere un puntatore, quindi se e'ugule null esce subito dal while */
    {
        p = p->succ; // Passo al nodo successivo nella lista concatenata.
    }

    /*
     * Quando il ciclo termina:
     * - Se `p` è diverso da NULL, significa che abbiamo trovato il nodo il cui valore `dato` è uguale a `k`.
     * - Se `p` è NULL, significa che abbiamo raggiunto la fine della lista e il valore `k` non è presente.
     */

    return p; // Restituisco il nodo trovato o NULL se non trovato.
}





/*
 * L = 0/, alla lista vuota
 * L = assegnero'líndirizzo di q
 *
 *  |3.14|Null| // che punta a alla lista vuot
 *     ^
 *     |
 *   |0.0|   // puntera'allémento 3.14 , p.succ = &p; /* modo alt. p.succ = l
 *     ^
 *     |
 *     L
 * --------------------------------------------------------------------------------------
 *          p
 *          |
 *  ----> |--|--| --->  |--|--| ---> null
 *        *p
 *        (*p).dato /.succ
 *
 *
 */
/*
L= &q;// gli dovro asseganre quindi dopo líndirizzo di p
// e quindi poi l andra'a puntare a p , mentre prima puntava a q
*/

//================================================================================================================================================================================================================================================================================

/*
 * Rappresentazione grafica della cancellazione di un elemento in una lista doppiamente concatenata.
 *
 * Contesto:
 * - Una lista doppiamente concatenata permette di navigare sia avanti che indietro tra i nodi grazie ai puntatori `succ` (successivo) e `prec` (precedente).
 * - La cancellazione di un nodo consiste nel scollegarlo dalla lista aggiornando i puntatori del nodo precedente e del nodo successivo.
 * - Successivamente, il nodo viene deallocato con `free()` per evitare memory leak.
 *
 * Rappresentazione della lista prima della cancellazione:
 *
 * [ ... ] <-> [ dato_prec | prec | succ ] <-> [ dato_p | prec | succ ] <-> [ dato_succ | prec | succ ] <-> [ ... ]
 *
 * Descrizione:
 * - `dato_p` rappresenta il nodo che vogliamo eliminare.
 * - `dato_prec` è il nodo precedente.
 * - `dato_succ` è il nodo successivo.
 *
 * Passaggi della cancellazione:
 * --------------------------------
 * 1. Il nodo precedente (`dato_prec`) aggiorna il suo puntatore `succ` per saltare il nodo da eliminare e puntare direttamente al nodo successivo (`dato_succ`).
 *    Codice: `dato_prec->succ = dato_p->succ;`
 *
 * 2. Il nodo successivo (`dato_succ`) aggiorna il suo puntatore `prec` per puntare direttamente al nodo precedente (`dato_prec`).
 *    Codice: `dato_succ->prec = dato_p->prec;`
 *
 * 3. Il nodo `dato_p` viene scollegato e deallocato con `free()`.
 *    Codice: `free(dato_p);`
 *
 * Rappresentazione grafica dopo la cancellazione:
 *
 * [ ... ] <-> [ dato_prec | prec | succ ] <-> [ dato_succ | prec | succ ] <-> [ ... ]
 *
 * Implementazione visiva (linee guida per il codice e l'immagine sopra):
 * -----------------------------------------------------------------------
 * Nodo `p`:
 * - Nodo da eliminare: [ dato_p | prec | succ ].
 * - Collegamenti:
 *   - Precendente: [ dato_prec | prec | succ ].
 *   - Successivo: [ dato_succ | prec | succ ].
 *
 * Dopo la cancellazione:
 * - Collegamenti aggiornati:
 *   - `dato_prec->succ` punta a `dato_succ`.
 *   - `dato_succ->prec` punta a `dato_prec`.
 *
 * Nodo `p` viene rimosso:
 * - `free(p)` dealloca la memoria associata a `dato_p`.
 *
 * Codice esempio:
 * --------------------------------
 */
/*
void clista_cancella(nodo **a, nodo *p) {
    if (p == NULL) return; // Se il nodo da eliminare è NULL, non faccio nulla.

    // Aggiorno il nodo precedente, se esiste.
    if (p->prec != NULL) {
        p->prec->succ = p->succ;
    } else {
        // Se il nodo è il primo, aggiorno la testa della lista.
        *a = p->succ;
    }

    // Aggiorno il nodo successivo, se esiste.
    if (p->succ != NULL) {
        p->succ->prec = p->prec;
    }

    // Dealloco il nodo rimosso.
    free(p);
}
*/
/*
 * Descrizione dell'immagine rappresentata sopra:
 *
 * 1. Prima della cancellazione:
 *    - Nodo `p` è al centro, con collegamenti a `prec` (nodo precedente) e `succ` (nodo successivo).
 *    - Nodo `p` è scollegato aggiornando i puntatori:
 *        - `prec->succ = succ`
 *        - `succ->prec = prec`
 *
 * 2. Dopo la cancellazione:
 *    - Il nodo `p` è completamente scollegato e deallocato.
 *    - La lista rimane coerente, con i nodi `prec` e `succ` direttamente collegati.
 */
