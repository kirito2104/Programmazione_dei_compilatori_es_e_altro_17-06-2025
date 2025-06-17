//
// Created by Enzo on 28/01/2025.
//

/*
 * Dizionari in c
 *
 *Si hanno un insieme di elemnti composte da due chiavi , sono delle stringhe, comopste da dei valori:
 *
 *  -Coppie chiave-valore :
 *      (k₀, v₀), (k₁, v₁), ...

 * -Funzione hash che restituisce l'indice di memorizzazione:
 * h(k) -> {0, ..., m-1}  // Importante: h(k) mappa una chiave in un intervallo di indici

  * -Tipi di dati
  *  chiavi: stringhe  // Le chiavi sono stringhe
  *  valori: int       // I valori sono interi

  * -Collisioni
  *h(v'₁) -> p   // Importante: due valori diversi possono avere lo stesso hash
  *h(v''₁) -> p  // Collisione

  * -Effetto delle collisioni
  /*(v'₁, v'₁) e (v''₁, v''₁) nelle stesse liste in pos. p d.d  // Importante: le collisioni vengono gestite tramite liste di elementi

*/


//Indice | Lista Collegata
/*
-------------------------
  0    |  [  ] -> NULL
  i    |  [  ] -> NULL     (h(k) = i)
  p    |  [  ] -> [  ] -> [  ] -> NULL  (h(k) = p, collisione gestita con lista)
  j    |  [  ] -> [  ] -> NULL  (h(k) = j, collisione gestita con lista)
 m-1   |  [  ] -> NULL

- se n e' la  dimensione del dizionario n/m deve essere costante
- gli n elemnti sono distribuiti in mainiera uniforme tra le m liste

 */


# include <stdio.h>
# include <stdlib.h>
# include <string.h>

// Definizione della struttura per un elemento del dizionario (coppia chiave-valore)
typedef struct ditem {
 char *k;  // Puntatore alla chiave (stringa)
 int v;  // Puntatore
} ditem; // Nome del tipo per un elemento del dizionario (coppia chiave-valore)

// Definizione della struttura per un nodo di una lista doppiamente concatenata che contiene un elemento del dizionario
typedef struct nodo {
 ditem dato;        // Elemento del dizionario memorizzato nel nodo
 struct nodo *succ, *prec; // Puntatore al nodo successivo nella lista  // Puntatore al nodo precedente nella lista
} nodo; // Nome del tipo per un nodo della lista

// Definizione di un alias per una lista concatenata basata sulla struttura nodo
typedef nodo *clista; // Tipo "clista" rappresenta un puntatore al primo nodo della lista

typedef struct dict
{
 // avremmo un' array di clista chiamato *a
 clista *a;
 int m; //ossia la dimensione
 /* Dizionario con m liste di trabocco */
}dict;

int hash(char *k,dict d)
{
 return  0;
}
/* dizionario*/
dict dict_init();
int dict_cerca(dict ,char*);

dict dict_add_item(dict, char*, int); // aggiunge elementi al dizionario
void dict_mostra(dict);
int dict_get(dict, char*);
dict dict_del(dict,char*);

/* lista concatenata */
clista clista_vuota();
nodo *clista_cerca(clista ,char*);
nodo *clista_in0(clista , ditem );
void clista_mostra(clista);
//-------------------------------
clista clista_out0(clista );
clista clista_out(clista , char*);


int main()
{
 dict d = dict_init(); // Inizializza il dizionario e lo memorizza in `d`
 d = dict_add_item(d, "chaive0", 0);
 dict_mostra(d);
 d = dict_add_item(d, "chiave0", 0);
 dict_mostra(d);
 d = dict_add_item(d, "chiave1", 1);
 d = dict_add_item(d, "chiave0", 10);
 dict_mostra(d);
 d = dict_add_item(d, "chiave2", 2);
 d = dict_add_item(d, "chiave14", 11);
 dict_mostra(d);

 if (dict_cerca(d,"chiave6")){
 printf("%d\n", dict_get(d, "chiave2"));
}
 d = dict_del(d, "chiave0");
 dict_mostra(d);

}



//**********************************************************************************************************************
dict dict_del(dict d, char *k)
{
 // come prima cosa eseguo la solita ricrca
 int i = hash(k, d);
 clista_out(d.a[i],k);
 return d;

}



/*--------------------------------------------------------------------------------------------------------------------*/
// Funzione per ottenere il valore associato a una chiave `k` nel dizionario `d`.
// Parametri:
// - dict d: il dizionario da cui recuperare il valore.
// - char *k: la chiave (stringa) il cui valore deve essere restituito.
// Restituisce:
// - Il valore associato alla chiave `k`, se la chiave è presente.
// - Se la chiave non esiste, il comportamento non è definito (potenziale errore critico!).
int dict_get(dict d, char *k){
    /*
     * ⚠️ PROBLEMA CRITICO: Non viene controllato se la chiave esiste prima di accedere al valore.
     * Se la chiave `k` non è presente nel dizionario, `clista_cerca` restituirà NULL,
     * e tentare di accedere a `p->dato.v` causerà un *segmentation fault*.
     *
     * 🔹 SOLUZIONE: Prima di procedere con l'accesso al valore, si dovrebbe verificare
     * se la chiave esiste con `dict_cerca(d, k)`.
     * Se la chiave non esiste, si può restituire un valore di default o segnalare un errore.
     *
     * Esempio di controllo:
     * if (dict_cerca(d, k) == 0) {
     *     return -1;  // Restituisce un valore speciale se la chiave non è trovata
     * }
     */

    // Calcola l'indice hash per la chiave `k`.
    // La funzione `hash(k, d)` restituisce un valore intero tra 0 e `d.m-1`
    // che rappresenta il bucket nella tabella hash dove cercare la chiave.
    int i = hash(k, d);

    // Cerca la chiave `k` nella lista concatenata situata nel bucket `d.a[i]`.
    // La funzione `clista_cerca` restituisce:
    // - Un puntatore al nodo se la chiave è presente.
    // - NULL se la chiave non è presente.
    nodo *p = clista_cerca(d.a[i], k);

    /*
     * ⚠️ ERRORE POTENZIALE: Se `clista_cerca` restituisce NULL (cioè la chiave non è trovata),
     * il tentativo di accedere a `p->dato.v` causerà un comportamento indefinito.
     *
     * 🔹 SOLUZIONE: Aggiungere un controllo per verificare se `p == NULL` prima di accedere al valore.
     */
    /*if (p == NULL) {
        fprintf(stderr, "Errore: chiave '%s' non trovata nel dizionario.\n", k);
        exit(EXIT_FAILURE); // Termina il programma in caso di errore (può essere evitato con un valore di default).
    }*/

    // Restituisce il valore associato alla chiave `k`, ora che siamo sicuri che `p != NULL`.
    return p->dato.v;
}



//--------------------------------------------------------------------------------------------------------------------
/* Funzione per cercare una chiave in un dizionario.
// Parametri:
// - dict d: il dizionario in cui cercare la chiave.
// - char *k: la chiave (stringa) da cercare nel dizionario.
// Restituisce:
// - 1 se la chiave `k` è presente nel dizionario.
// - 0 se la chiave `k` non è presente.*/

int dict_cerca(dict d, char *k)
{
 // Calcola l'indice hash per la chiave `k` nel dizionario `d`.
 // La funzione `hash` genera un valore intero corrispondente a un indice
 // valido all'interno dell'array `d.a` (che rappresenta i bucket del dizionario).
 int i = hash(k, d);

 // Cerca nella lista collegata situata nel bucket `d.a[i]`.
 // La funzione `clista_cerca` dovrebbe:
 // - Restituire un puntatore al nodo della lista che contiene la chiave `k`, se presente.
 // - Restituire `NULL` se la chiave `k` non è presente nella lista.
 nodo *p = clista_cerca(d.a[i], k);

 // Verifica se la chiave è stata trovata.
 if (p == NULL) // Caso: la chiave `k` non è presente.
 {
  return 0; // Restituisce 0 per indicare che la chiave non è stata trovata.
 }
 else // Caso: la chiave `k` è stata trovata nella lista.
 {
  return 1; // Restituisce 1 per indicare che la chiave è presente nel dizionario.
 }
}



//---------------------------------------------------------------------------------------------------------------------
/* Funzione per mostrare il contenuto di un dizionario.
// Il dizionario è implementato come una tabella hash con array di liste concatenate.
// Parametro:
// - dict d: il dizionario da stampare, contenente un array `a` di liste concatenate e un intero `m`
//   che rappresenta il numero di bucket (dimensione dell'array).*/
void dict_mostra(dict d) {

 // Dichiarazione di una variabile intera `i` utilizzata come contatore nel ciclo.
 int i;

 // Itera su ciascun bucket del dizionario (da 0 a `m-1`), dove `m` è la dimensione della tabella hash.
 for (i = 0; i < d.m; i++) {

  // Stampa l'indice del bucket corrente.
  // Questo serve a identificare chiaramente il bucket nel quale i dati sono memorizzati.
  printf("d[%d] = ", i);

  // Chiama la funzione `clista_mostra` per stampare il contenuto della lista concatenata
  // situata nel bucket `d.a[i]`. Se la lista è vuota, non stamperà alcun elemento.
  clista_mostra(d.a[i]);
 }
}









//----------------------------------------------------------------------------------------------------------------------
/*
// Funzione per aggiungere un elemento a un dizionario implementato come hash table con liste collegate
// Parametri:
// - dict d: il dizionario in cui aggiungere l'elemento
// - char *k: la chiave dell'elemento (stringa)
// - int v: il valore associato alla chiave
// Restituisce:
// - Il dizionario aggiornato
*/

// Funzione per aggiungere un elemento al dizionario
dict dict_add_item(dict d, char *k, int v) {
 // Calcola l'indice della chiave 'k' utilizzando una funzione hash
 int i = hash(k, d);

 // Cerca se la chiave 'k' esiste già nel dizionario alla posizione calcolata
 nodo *p = clista_cerca(d.a[i], k);

 if (p != NULL) {
  // Se la chiave esiste già, aggiorna il valore associato
  p->dato.v = v;
 } else {
  // Se la chiave non esiste, crea un nuovo elemento del dizionario
  ditem itm = {NULL, v}; // Inizializza l'elemento con la chiave NULL e il valore v

  // Alloca memoria per copiare la chiave 'k' e la assegna all'elemento
  itm.k = malloc(sizeof(char) * (strlen(k) + 1));
  strcpy(itm.k, k); // Copia il contenuto della chiave

  // Inserisce il nuovo elemento nella lista associata alla posizione calcolata
  d.a[i] = clista_in0(d.a[i], itm);
 }

 // Restituisce il dizionario aggiornato
 return d;
}


//---------------------------------------------------------------------------------------------------------------------


/**/

dict dict_init()
{
 dict d = { NULL, 7 };  // Inizializza il dizionario con m = 7
 d.a = malloc(d.m * sizeof(clista)); // Alloca memoria per l'array di liste

 // Inizializza ogni bucket della tabella hash come una lista vuota
 for (int i = 0; i < d.m; i++)
 {
  d.a[i] = NULL; // Imposta ogni posizione della tabella come lista vuota
 }

 return d; // Restituisce il dizionario inizializzato
}
/*
 * Inizializza una nuova istanza del dizionario.
 *
 * Alloca memoria per un dizionario e inizializza:
 * - La dimensione della tabella hash (`m = 7`).
 * - Un array di liste concatenate, con ogni bucket inizializzato come vuoto.
 *
 * @return Un dizionario inizializzato.
 */
//---------------------------------------------------------------------------------------------------------------------


/* Funzione per inizializzare una lista vuota*/
clista clista_vuota() {
 return NULL; // Una lista vuota è rappresentata come un puntatore a NULL
}

//----------------------------------------------------------------------------------------------------------------------

nodo *clista_in0(clista a, ditem v) {

 // Alloca memoria per un nuovo nodo della lista.
 nodo *p = malloc(sizeof(nodo));

 // Assegna il valore `v` al campo `dato` del nuovo nodo.
 p->dato = v;

 // Imposta il campo `succ` del nuovo nodo per puntare alla vecchia testa della lista (ovvero `a`).
 p->succ = a;

 // Imposta il campo `prec` del nuovo nodo a NULL, poiché sarà la nuova testa della lista
 // e non avrà un nodo precedente.
 p->prec = NULL;

 // Se la lista non è vuota (cioè, `a` non è NULL),
 // aggiorna il campo `prec` della vecchia testa per puntare al nuovo nodo `p`.
 if (a != NULL) {
  a->prec = p;
 }

 // Aggiorna il puntatore `a` per farlo puntare al nuovo nodo `p`,
 // che diventa la nuova testa della lista.
 a = p;

 // Restituisce il nuovo nodo `p` come nuova testa della lista concatenata.
 return a;
}




/*
 * Funzione per cercare un nodo contenente un valore specifico in una lista concatenata.
 *
 * La funzione scorre la lista concatenata per trovare un nodo che abbia la chiave `k` nella sua coppia chiave-valore.
 *
 * @param a - La testa della lista concatenata in cui effettuare la ricerca.
 * @param k - La chiave da cercare all'interno della lista.
 * @return Un puntatore al nodo che contiene la chiave `k`, oppure NULL se la chiave non è presente nella lista.
 */
nodo *clista_cerca(clista a, char *k) {
 nodo *p = a; // Parto dalla testa della lista

 /**
  * Itero finché non trovo il nodo con la chiave cercata oppure raggiungo la fine della lista.
  *
  * - `strcmp(p->dato.k, k)`: confronta la chiave `k` con la chiave del nodo corrente.
  * - `strcmp` restituisce:
  *    - 0 se le due stringhe sono identiche.
  *    - Un valore negativo se `p->dato.k` è minore di `k` (in ordine lessicografico).
  *    - Un valore positivo se `p->dato.k` è maggiore di `k`.
  * - Il ciclo continua finché non troviamo un nodo con chiave uguale a `k` oppure la lista termina (`p == NULL`).
  */
 while (p != NULL && strcmp(p->dato.k, k) != 0) {
  p = p->succ; // Passo al nodo successivo
 }

 return p; // Restituisco il nodo trovato oppure NULL se la chiave non esiste nella lista
}


/*
 * La funzione strcmp() (string compare) è usata per confrontare due stringhe.
 *
 *  Perché non si usa p->dato.k == k?
 *
 * In C, le stringhe sono gestite come array di caratteri terminati da \0 e sono rappresentate da puntatori.
 * L'operatore == in C confronta gli indirizzi di memoria, non il contenuto delle stringhe.
 * strcmp() invece confronta i caratteri delle due stringhe una lettera alla volta.
 *
 * 🔹 Come funziona strcmp()
 *
 * ```c
 * int strcmp(const char *s1, const char *s2);
 * ```
 * Restituisce 0 se s1 e s2 sono uguali.
 * Restituisce un valore negativo se s1 viene prima di s2 (es. "apple" < "banana").
 * Restituisce un valore positivo se s1 viene dopo s2 (es. "banana" > "apple").
 *
 * 🔹 Esempi di strcmp()
 *
 * ```c
 * strcmp("abc", "abc")  // Restituisce 0  (stringhe uguali)
 * strcmp("abc", "abd")  // Restituisce < 0 (abc è lessicograficamente prima di abd)
 * strcmp("abd", "abc")  // Restituisce > 0 (abd è lessicograficamente dopo abc)
 * ```
 *
 * Esempio pratico di utilizzo della funzione clista_cerca()
 *
 * ```c
 * nodo *risultato = clista_cerca(lista, "chiave_da_cercare");
 * if (risultato != NULL) {
 *     printf("Chiave trovata! Valore associato: %s\n", risultato->dato.v);
 * } else {
 *     printf("Chiave non trovata nella lista.\n");
 * }
 * ```
 */


// Funzione per stampare il contenuto di una lista doppiamente concatenata.
// Parametro:
// - clista a: la lista da stampare (può essere NULL se la lista è vuota).

void clista_mostra(clista a) {

 // Dichiarazione di un puntatore per attraversare i nodi della lista.
 nodo *p;

 // Inizializzo il puntatore `p` alla testa della lista, ovvero `a`.
 p = a;

 // Itero sulla lista finché il puntatore `p` non diventa NULL
 // (NULL indica che abbiamo raggiunto la fine della lista).
 while (p != NULL) {

  // Stampo il contenuto del nodo corrente:
  // - `p->dato.k` è la chiave associata al nodo (stringa).
  // - `p->dato.v` è il valore associato alla chiave (intero).*/
  printf("(%s, %d)", p->dato.k, p->dato.v);

  /*NOTA: la frase "aggiungerà solo due 0 nel float" è errata,
  // in quanto non vi è alcun riferimento a numeri in virgola mobile.
  // Qui si stanno stampando solo stringhe e interi.

  // Passo al nodo successivo, utilizzando il campo `succ` del nodo corrente,
  // che punta al prossimo nodo nella lista.*/
  p = p->succ;
 }

 // Dopo aver stampato tutti gli elementi, aggiungo un carattere di nuova linea
 // per terminare l'output in modo ordinato.
 printf("\n");
}




/*--------------------------------------------------------------------------------------------------------------------*/

// Funzione per rimuovere il primo nodo di una lista doppiamente concatenata.
// Parametro:
// - clista a: la lista dalla quale rimuovere il primo nodo.
// Restituisce:
// - La nuova testa della lista (il secondo nodo, se esiste, oppure NULL se la lista era vuota).
clista clista_out0(clista a){

    // Salvo un puntatore al nodo attuale (testa della lista) per poterlo liberare successivamente.
    clista p = a;

    // Se la lista è vuota (`a == NULL`), restituisco subito NULL.
    if (a == NULL)
        return NULL;

    // Sposto la testa della lista al nodo successivo.
    a = a->succ;

    // Se esiste un nuovo primo nodo (`a != NULL`), imposto il suo puntatore `prec` a NULL
    // perché ora sarà la testa della lista.
    if (a != NULL)
        a->prec = NULL;

    // Libero la memoria allocata per la chiave `k` del nodo che sto rimuovendo.
    free(p->dato.k);

    // Libero la memoria allocata per il nodo stesso.
    free(p);

    // Restituisco la nuova testa della lista.
    return a;
}

// -----------------------------------------------------------------------------------------------------------------------

// Funzione per rimuovere un nodo con chiave `k` da una lista doppiamente concatenata.
// Parametri:
// - clista a: la lista dalla quale rimuovere il nodo.
// - char *k: la chiave del nodo da rimuovere.
// Restituisce:
// - La nuova testa della lista, aggiornata dopo la rimozione del nodo specificato.
clista clista_out(clista a, char *k){

    // Cerco nella lista il nodo con chiave `k` usando la funzione `clista_cerca`.
    // La funzione `clista_cerca` restituisce:
    // - Un puntatore al nodo se la chiave `k` è trovata.
    // - NULL se la chiave `k` non è presente nella lista.
    nodo *p = clista_cerca(a, k);

    // Se la chiave `k` non è presente nella lista, restituisco la lista invariata.
    if (p == NULL)
        return a;

    // Salvo il nodo precedente `q`, che punta al nodo che precede `p` nella lista.
    nodo *q = p->prec;

    // Caso speciale: il nodo `p` è la testa della lista (quindi `q == NULL`).
    // In questo caso, utilizzo `clista_out0` per rimuovere il primo nodo.
    if (q == NULL) // Significa che p == a
    {
        return clista_out0(p);
    }

    // Rimuovo `p` dalla lista collegata:
    // - `q->succ` diventa `p->succ`, escludendo `p` dalla sequenza della lista.
    q->succ = clista_out0(q->succ);

    // Se il nuovo nodo successivo (`q->succ`) non è NULL,
    // aggiorno il suo puntatore `prec` per farlo puntare a `q`,
    // mantenendo la connessione corretta nella lista doppiamente concatenata.
    if (q->succ != NULL)
        q->succ->prec = q;

    // Restituisco la testa della lista originale (`a`), che potrebbe essere invariata.
    return a;
}





