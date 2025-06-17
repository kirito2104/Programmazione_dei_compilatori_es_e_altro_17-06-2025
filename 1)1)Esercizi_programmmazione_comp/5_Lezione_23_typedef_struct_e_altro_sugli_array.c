//
// Created by Enzo on 18/01/2025.
//

#include <stdio.h>
#include <stdlib.h>


/*
### Proprietà di `sizeof` e `malloc`

#### **`sizeof`**
`sizeof` è un operatore in C utilizzato per ottenere la dimensione in byte di una variabile, di un tipo di dato o di un'espressione.

##### **Caratteristiche principali di `sizeof`:**
1. **Determinazione della dimensione in byte:**
   - Restituisce il numero di byte occupati da un tipo o un'espressione.
   - È un operatore valutato a compile-time (salvo nei casi di array dinamici).

2. **Utilizzo con array:**
   - Quando applicato a un array dichiarato staticamente, restituisce la dimensione totale in byte dell'intero array.
   - Quando applicato a un puntatore, restituisce la dimensione del puntatore
   (es. 4 o 8 byte, a seconda dell'architettura), non dell'array a cui punta.

3. **Sintassi:**
   sizeof(expression or type)
   - `sizeof(int)` -> Restituisce la dimensione di un tipo `int`.
   - `sizeof(variable)` -> Restituisce la dimensione della variabile.
   - `sizeof(array)` -> Restituisce la dimensione totale di un array statico (in byte).

4. **Esempi:**
   int a = 10;
   float b[5];
   printf("%zu\n", sizeof(a));      // Dimensione di un int (es. 4 byte)
   printf("%zu\n", sizeof(b));      // Dimensione totale di un array float[5] (es. 20 byte se float è 4 byte)
   printf("%zu\n", sizeof(b)/sizeof(float)); // Numero di elementi nell'array b

---

#### **`malloc`**
`malloc` (memory allocation) è una funzione della libreria standard di C (`stdlib.h`)
utilizzata per allocare memoria dinamica durante l'esecuzione.

##### **Caratteristiche principali di `malloc`:**
1. **Allocazione dinamica di memoria:**
   - Alloca un blocco di memoria contiguo di una dimensione specificata in byte.
   - Restituisce un puntatore al primo byte del blocco allocato.
   - Se l'allocazione fallisce (es., memoria insufficiente), restituisce `NULL`.

2. **Sintassi:**
   void *malloc(size_t size);
   - `size`: La dimensione in byte della memoria da allocare.
   - Restituisce un puntatore di tipo `void*` che deve essere castato al tipo desiderato.

3. **Esempio:**
   int *array;
   int n = 5;

   // Alloca memoria per 5 interi
   array = (int *)malloc(n * sizeof(int));

   if (array == NULL) { // Controllo dell'allocazione
       printf("Memoria insufficiente\n");
       return -1;
   }

   // Utilizzo della memoria
   for (int i = 0; i < n; i++) {
       array[i] = i;
   }

   // Deallocazione della memoria
   free(array);

##### **Note importanti su `malloc`:**
1. La memoria allocata con `malloc` **non viene inizializzata**. Contiene valori indefiniti.
2. La memoria deve essere deallocata esplicitamente usando `free()` per evitare **memory leaks**.
3. Per inizializzare la memoria a zero, si usa la funzione `calloc`, o si impiega `memset()` dopo `malloc`.

---

#### **Combinazione di `sizeof` e `malloc`:**
Spesso `sizeof` è usato con `malloc` per calcolare la dimensione necessaria alla memoria dinamica:

   int n = 10;
   int *array = (int *)malloc(n * sizeof(int)); // Alloca memoria per 10 interi

Questo approccio garantisce che la dimensione allocata sia adattata automaticamente al tipo di dato, rendendo il codice portabile e robusto.
*/


//====================================================================================================================================================

/*
### Perché usare `malloc` e `sizeof`?

#### **Uso di `malloc`**
1. **Allocazione dinamica della memoria:**
   - La funzione `malloc` permette di allocare memoria durante l'esecuzione del programma (runtime).
   - È utile quando non si conosce in anticipo la quantità di memoria necessaria,
   ad esempio per array o strutture dati il cui numero di elementi dipende da input esterni.

2. **Gestione manuale della memoria:**
   - Con `malloc`, puoi controllare esplicitamente quando allocare e deallocare memoria.
   - Questo è particolarmente utile per programmi complessi, dove l'uso efficiente della memoria è critico.

3. **Flessibilità:**
   - A differenza degli array statici, che hanno una dimensione fissata
   al momento della compilazione, la memoria allocata con `malloc`
   può essere dimensionata dinamicamente in base alle esigenze del programma.

---

#### **Uso di `sizeof`**
1. **Portabilità:**
   - Usare `sizeof` garantisce che il programma funzioni correttamente su architetture diverse.
   Ad esempio, un tipo `int` può occupare 2, 4 o 8 byte a seconda della piattaforma.
   - Evita di fare supposizioni sulla dimensione dei tipi di dato.

2. **Calcolo automatico della memoria:**
   - Quando si usa `malloc`, `sizeof` permette di calcolare automaticamente
   la quantità di memoria necessaria per un determinato tipo o struttura, riducendo il rischio di errori.

---

### Perché scrivere `malloc` con `sizeof` in un determinato modo?

1. **Sintassi standard:**
   tipo *variabile = (tipo *)malloc(n * sizeof(tipo));
   - **`n * sizeof(tipo)`**: Calcola il numero totale di byte da allocare,
   moltiplicando il numero di elementi `n` per la dimensione di un singolo elemento (`sizeof(tipo)`).
   - **Casting a `tipo*`**: `malloc` restituisce un puntatore generico (`void*`).
   Il cast esplicito a `tipo*` rende chiaro il tipo di dati che verranno archiviati nella memoria allocata.

   Esempio:
   int *array = (int *)malloc(10 * sizeof(int)); // Alloca memoria per 10 interi.

2. **Vantaggi della sintassi:**
   - **Rende il codice portabile**: `sizeof(tipo)` garantisce che il programma funzioni correttamente
   su diverse piattaforme e con diversi compilatori.

   - **Facile manutenzione**: Cambiare il tipo di dato richiede solo la modifica di `tipo` nel codice. Ad esempio:
     float *array = (float *)malloc(10 * sizeof(float)); // Cambia solo il tipo di dato.
   - **Evita errori di calcolo**: Usare `sizeof` assicura che la dimensione sia calcolata correttamente,
   indipendentemente dalle dimensioni effettive dei tipi di dato.

---

### Perché non scrivere la dimensione direttamente?

Esempio **NON consigliato**:
int *array = (int *)malloc(40); // Presuppone che `int` sia 4 byte.

**Problemi:**
1. **Non portabile**:
   - Se la dimensione di `int` varia (es. su alcune piattaforme `int` potrebbe essere 2 o 8 byte), il codice non funziona correttamente.

2. **Difficile da leggere e mantenere**:
   - Non è immediatamente chiaro che `40` rappresenta la memoria per 10 interi.
   In caso di modifica del tipo o del numero di elementi, è più facile introdurre errori.

---

### In sintesi:
- Usare `malloc` con `sizeof` nella forma standard garantisce portabilità, leggibilità e manutenzione del codice.
- La sintassi è progettata per calcolare automaticamente la quantità di memoria richiesta e adattarsi a cambiamenti futuri senza errori.
*/




//lista_f init(); // Deve restituire un tipo `lista_f`
float *copia_array_di_float(float *a, int n);


/*
 *    CHE COS'E' LA STRUCT?:
 * E un tipo di struttura  che contiente dei dati in nuovo tipo di dato che andremo a definire
 *
 *
 */

// lo descriviamo con tre grandezze , la prima il puntatore all'array vero e proprio, gli alri due sono interi, 1 la capacita'
// e l'altro e' la dimensione

struct lista_f {
   float *a;
   int c; // capacita'
   int n ;// dimensione di elementi

}; // e' un tipo di dato composto
/* ci consente di rendere un tipo piu' definito, ci consente di dare un nuovo nome ad un tipo gia esistente  */


typedef struct lista_f lista_f; // ci consente di richiamare i parametri precedenti facendo in modo di creare una nuova lista
lista_f init();
lista_f append( lista_f L,float e  );// dovrea' restituire l'attuale lista modificata

int main () {
   struct lista_f L; // usando l posso accedere hai sigoli elemnti

   lista_f L1; // e' una nuova lista a tutti gli effetti

   L.c =10 ; // voglio creare un array con capacita' di 10 elementi
   L.n = 0 ;
   L.a = malloc( L.c*sizeof(float));// fara' lc, ossia la capacita' per la dimensione del float e' sara' il doppio

   // abbbiamo creato l che e' di tre campi
   L.a [0] = 3.14;
   L.a[1] = 2.71;

// e' posso aggire andando a definire
   L.n+=2; //incremento n che era 0

   for (int i = 0; i < L.n; i++) {
      // Stampa tutti gli elementi della lista dinamica.
      // L.a[i]: Accede al valore nell'array in posizione `i`.
      // L.n: Indica il numero di elementi effettivi nella lista.

      printf("%f\n", L.a[i]); // Stampa il valore dell'elemento `i` come float.
   }

   L1 = init(); // Inizializza una lista vuota utilizzando la funzione `init`

   for (int i = 0; i < 20; i++) {

      // Aggiunge 20 elementi alla lista `L1` con valori multipli di 10
      // Ogni elemento viene calcolato come `i * 10` e aggiunto con `append`
      L1 = append(L1, i * 10);
      printf("%d,%d\n", L1.n,L.c);


   }
   for (int i = 0; i < 20; i++) {
      // Aggiunge 20 elementi alla lista `L1` con valori multipli di 10
      // Ogni elemento viene calcolato come `i * 10` e aggiunto con `append`
      printf("%f\n",L1.a[i]);
   }

}

// Funzione che crea una lista vuota:

lista_f init(){ // Non prende parametri in input
   lista_f lista_vuota = {NULL, 0, 0};
   /*
   Inizializza una lista vuota con i seguenti valori:
   - `NULL`: Nessun puntatore allocato per l'array
   - `0`: Numero di elementi nella lista è inizialmente zero
   - `0`: Capacità della lista è zero (nessuna memoria allocata)
   */
   return lista_vuota; // Restituisce la lista vuota
}



lista_f append(lista_f L, float e){
   /*
   Aggiunge un nuovo elemento `e` alla lista dinamica `L`.
   La funzione gestisce automaticamente la crescita della memoria,
   raddoppiandola se necessario.
*/
   if (L.n == L.c) {

/* // Caso in cui c'è spazio sufficiente nella lista:
      L.a[L.n] = e; // Aggiunge il nuovo elemento nella posizione `n` disponibile.
      L.n++;        // Incrementa il numero di elementi effettivi nella lista.
      */
      L.c = 2*(L.c+1); // Raddoppia la capacità dell'array , in  questo modo, quando c e' 0 ela dimensione e' 2 .
      L.a = realloc( L.a, L.c*sizeof(float) );// Rialloca la memoria con la nuova capacità.
   }
     /*
      Caso in cui la capacità della lista non è sufficiente:
      - La capacità totale `L.c` viene raddoppiata.
      - Rialloca memoria per l'array con la nuova capacità.
      */
    // Aggiunge il nuovo elemento alla lista dopo aver riallocato la memoria.
   L.a[L.n] = e; // Inserisce il nuovo elemento nella posizione disponibile.
   L.n++; // Incrementa il numero di elementi effettivi.

   return L;
}/* Questa operazione fa in modo che il costo delle operaziioni nel caso peggiore costi n odine di n, nel caso peggiore.
Questa operazione costa **O(n)** nel caso peggiore a causa del comportamento della funzione
`realloc` quando la capacità dell'array deve essere raddoppiata.

Ecco il motivo in dettaglio:

1. **Riallocazione della memoria con `realloc`:**
   - Quando `L.n == L.c`, significa che l'array ha raggiunto la sua capacità massima (`L.c`)
   e non può più contenere nuovi elementi senza espandere la memoria.
   - La funzione `realloc` viene chiamata per allocare un nuovo blocco
   di memoria di dimensione maggiore (raddoppiata in questo caso: `2 * (L.c + 1)`).

   - Se non c'è spazio sufficiente contiguo nella memoria per espandere l'array nello stesso luogo,
   `realloc` alloca un nuovo blocco di memoria e copia tutti gli elementi esistenti dal vecchio blocco al nuovo blocco.

2. **Costo della copia degli elementi:**
   - Copiare tutti gli elementi esistenti richiede **n operazioni**, dove `n` è il numero di elementi già presenti nell'array.
   - Questo è dovuto al fatto che ogni elemento deve essere spostato dalla vecchia posizione di memoria alla nuova posizione.

3. **Numero di operazioni:**
   - Durante la copia, ogni elemento richiede una scrittura nella nuova memoria, e questo processo
   è proporzionale al numero di elementi, ovvero **O(n)** per quella chiamata a `realloc`.

4. **Caso peggiore:**
   - Il caso peggiore si verifica quando `realloc` deve essere eseguito.
   Poiché il numero di elementi cresce nel tempo, il costo della copia aumenta progressivamente.

### Sintesi del costo:

- **Caso in cui c'è spazio sufficiente (`L.n < L.c`):**
  L'operazione è **O(1)**, poiché il nuovo elemento viene semplicemente aggiunto alla fine dell'array.

- **Caso in cui la capacità deve essere raddoppiata (`L.n == L.c`):**
  L'operazione è **O(n)**, poiché `realloc` deve copiare tutti gli elementi esistenti nel nuovo blocco di memoria.

### Costo ammortizzato:
Nel caso di molte operazioni di `append`, il costo medio per ogni operazione diventa **O(1)**.
Questo accade perché raddoppiando la capacità, il numero di volte in cui `realloc` viene eseguito diminuisce in proporzione al numero di elementi totali.
*/





int main1() {
    int n = 10;
    float *a = malloc(n *sizeof(float)); // ci dice che, questa operazione ha costo costante tempo O(1)

   for (int i=0;i<n;i++) {

      a[i] = 10+i;
   }

   n++; // incrementiamo n sopra

   /*Le modifiche al codice apportano i seguenti miglioramenti:

1. **Incremento di `n` prima di `realloc`**:
   - Rende esplicito che si sta aggiungendo un nuovo elemento all'array.
   - Migliora la leggibilità e la chiarezza della logica.
*/


   //possiamo sperare che ha sinistra ci sia dello spazio,

   /* Costo della struttura nel caso peggiore O(n) in cui richiede copia, altrimenti O(1)  */
   a = realloc (a, n * sizeof(float)); // il suo obbiettivo e' tentare di estendere la memoria o modificare ,
   //l'allocazione che e' stata precedentemente allocata essa prende in indirizzo
   //la funzione che dobbiamo ridimensionare e la nuova dimensione, in caso di successo ritorna l'indirizzo alla nuova memoria riallocata
   // la rialloca verifica se la memoria,
   // ci possono essere due casi , la memoria la sposto a destra perche' c'e' spazio per4 byte in piu' e quindi ritorna la stassa funz che passiamo
   // In tal caso se non ci sia, va a cercare spazio da qualche altra parte per verificare che non ci sia un'altra struttura dati
   //Ci puo' essere anche un terzo dove non c'e' spazio in memoria per la nuova struttura dati, in quel caso ritorniamo None.

   /* Il caso peggiore e' quando non possiamo allargare a destra, ma c'e' spazio da un'altra parte e quindi andiamo a copiare la struttura
    * il costo sara' della struttra O(n)
    * In tutti gli altri casi il costo e' costante O(1)
    */

   a [n- 1 ] = 0 ;
   /*2. **Uso di `a[n - 1]`**:
   - Garantisce coerenza nell'accesso all'ultimo elemento del nuovo array riallocato.
   - Evita errori legati all'indicizzazione errata.
3. **Inizializzazione del nuovo elemento (`a[n - 1] = 0`)**:
   - Assicura che il nuovo spazio aggiunto sia gestito correttamente e inizializzato.
   */

   //possiamo chidere al dispositivo se c'e' spazio e' quindi di chiedere di riallocare spazio per l'array
   for (int i=0;i<n;i++) {

     printf("%f\n", a[i]);
   }

   free(a); // Libera eventuale memoria allocata precedentemente dal puntatore 'a'

   int m = 100; // Numero di iterazioni del ciclo principale, rappresenta il numero massimo di espansioni
   n = 1; // Dimensione iniziale dell'array

   // Alloca memoria per un array di un elemento di tipo float
   a = malloc(1 * sizeof(float));
   // malloc restituisce un puntatore a un blocco di memoria di dimensione 1 * sizeof(float).
   // Se l'allocazione fallisce, malloc restituisce NULL.

   a[0] = 10; // Inizializza il primo elemento dell'array con il valore 10

   // Ciclo per espandere dinamicamente l'array
   //NEL CASO PEGGIORE IL TEMPO O(n^2), osservazione il costo n append in python e', nel caso peggiore o(n)

 /*
   for (int i = 0; i < m; i++) { //nel caso peggiore ha costo quadratico
      n++; // Incrementa la dimensione dell'array di 1

      // Rialloca memoria per l'array, aumentando la dimensione a 'n' elementi
      a = realloc(a, n * sizeof(float));
      // realloc tenta di estendere o modificare la memoria precedentemente allocata.
      // - Se c'è spazio disponibile subito dopo l'allocazione esistente, rialloca nello stesso posto (O(1)).
      // - Se non c'è spazio, copia l'intero contenuto in un nuovo blocco di memoria (O(n)).
      // Se realloc fallisce, restituisce NULL e l'array precedente rimane intatto.

      a[n - 1] = n; // Inizializza il nuovo elemento aggiunto con il valore 'n'
}

Il ciclo ha costo quadratico nel caso peggiore a causa della riallocazione ripetuta della memoria con realloc,
   che potenzialmente richiede la copia degli elementi già allocati ad ogni iterazione.

   ### Analisi dettagliata del costo:

   1. **Costo di una singola chiamata a realloc:**
      - Quando realloc non può estendere la memoria contigua (perché non c'è abbastanza spazio immediatamente a destra del blocco attuale), è necessario:
        - Allocare un nuovo blocco di memoria abbastanza grande per contenere tutti gli elementi.
        - Copiare gli elementi esistenti dal vecchio blocco al nuovo blocco.
      - Questo processo di copia ha costo O(n), dove n è il numero di elementi già presenti nell'array.

   2. **Numero totale di chiamate a realloc:**
      - Il ciclo esegue m iterazioni e in ciascuna viene incrementato n di 1 e viene chiamato realloc.
      - Di conseguenza, il numero di chiamate a realloc è pari a m.

   3. **Costo complessivo del ciclo:**
      - In ogni iterazione i, se viene eseguita la copia, il costo è proporzionale al numero di elementi già presenti nell'array, cioè i.
      - La somma dei costi su tutte le iterazioni è:
        C = 1 + 2 + 3 + ⋯ + m = m(m + 1) / 2
      - Questo è un costo O(m²), poiché la somma dei primi m numeri naturali è quadratica rispetto a m.

   ### Riassunto del comportamento:
   - **Caso ottimale:** Se c'è spazio contiguo sufficiente in memoria ad ogni chiamata a realloc,
     l'operazione è O(1) per ogni iterazione, e il ciclo ha un costo totale di O(m).
   - **Caso peggiore:** Se la memoria contigua non è disponibile, ogni chiamata a realloc copia tutti gli elementi già allocati,
     portando il costo complessivo a O(m²).

*/
   // ECCO UNA VERSIONE DOVE IL COSTO NEL CASO PEGGIORE NON E' M^2
   //Dobbiamo escludere che la realloc possa richieda tempo lineare, facendo chje in modo che la realocc si comporti male in alcune situazioni
    //bisogna introdurre una nuova grandezza,l'arry e' caratterizzato da tre info, il tipo e la dimensione dell'array
   //La nuova  grandezza sara' la capacita' di contenimento di un array
    //     ___________
   // a-> |___________|che ha un certo num di posizioni
   // l'array contiene un certo num

   // e' un aray con un certo numero di posizioni :

   //     0    1             N-1
   //e -> |----|----|----|----|----|----|----|----|
   //     |-------------------|
   //      gli elementi effettivi
   //      sono nell'array sono:
   //                N
   //     |---------------------------------------|
   //                      C

   /*
    * n < c
    * N = sara' la dimensione, ovvero num. di elementi
    * c = dimensione del contenitore, ovvero la capacita' dell'array, quanri elemnti ci posso inserire
    *
    * quando n e' piu' piccolo di c significa sfruttare nella posizione succesivva che n e' cresciuta
    * questo richiede costo costante
    * Quando invece la dimensione n e' uguale a c non si puo ma bisogna riallocare la memoria
    *
    * - append ---> n< c usiamo la posizione n di a visto che c'e' spazio
    * e' quindi e' costante O(1)
    * n++
    ** - se n e' = c
    *  realloc  O(n) nel caso peggiore viene tempo lineare, non andiamo memoria giusta per il nuovo elemento
    *  realloc (2*c) raddopio per le prossimi n append, raddopiandola memoria diventa lineare perche'?
    *
    *
    *1) n = c             |----------|                QUESTA OP. E' COSTATA
    *1)RADDOPPIO L'ELEMENTO |----------|-----------| O(n) append |
    *                                                            |    TUTTO CIO' ANDRA'
    *2)                     |---------------------| costo O(1)   |      A COSTARE
    *3)                     |---------------------| costo O(1)   |       n append
    *
    *       Co n + (n-1) c1 = O(n)  costo nel caso peggiore e' lineare
    *
    *       il costo medio di un append e' O(1)
    *
    */



   for (int i = 0; i < m; i++) { //nel caso peggiore ha costo quadratico


      n++; // Incrementa la dimensione dell'array di 1

      // Rialloca memoria per l'array, aumentando la dimensione a 'n' elementi
      a = realloc(a, n * sizeof(float));


      a[n - 1] = n; // Inizializza il nuovo elemento aggiunto con il valore 'n'
   }

   // Ciclo per stampare tutti gli elementi dell'array
   for (int i = 0; i < n; i++) {
      printf("%f\n", a[i]); // Stampa ogni elemento dell'array
   }

   printf("\n"); // Stampa una riga vuota per separare visivamente l'output




}













int main0() {
/*
    Il codice copia un array statico di numeri `float` in un array dinamico.
    Calcola il numero di elementi dell'array (`n`) dividendo la dimensione
    totale in byte (`sizeof(v)`) per quella di un singolo elemento (`sizeof(float)`)
    e utilizza questa informazione per chiamare la funzione `copia_array_di_float`, che crea la copia dinamica.
*/
    // Definizione dell'array statico con valori iniziali
    float v[20] = {0,1,2}; // Array di 20 float, i primi 3 inizializzati a 0, 1, 2, gli altri a 0.

/*
    float *w = copia_array_di_float (v,sizeof(v)/sizeof(float));// usaimo la funzione size_of di (v)
                                                     // ritorna la dimensione in byte della struttura v
                                                     // perche' v e' stato dichiarato il suo array statico
                                                     // ritorna la dimensione in byte di v, a noi seve sapere il num di float dentro v
    // usiamo tutto cio' qui sopra definedo il numero di variabili n
    */




        // Calcolo del numero di elementi nell'array v
        int i, n = sizeof(v) / sizeof(float);
        // sizeof(v) restituisce la dimensione in byte dell'intero array.
        // sizeof(float) restituisce la dimensione di un singolo float.
        // Dividendo i due, otteniamo il numero di elementi nell'array.

        // Creazione di un array dinamico copiando i dati dall'array statico v

        float *w = copia_array_di_float(v, n);
        // copia_array_di_float prende l'array v e il numero di elementi n,
        // e restituisce un puntatore a un nuovo array dinamico che contiene gli stessi valori di v.

        // Stampa degli elementi dell'array dinamico w
        for (i = 0; i < n; i++) {
            printf("%f\n", w[i]); // Stampa ciascun elemento di w.
        }

        free(w); // Dealloca la memoria allocata dinamicamente per evitare perdite di memoria.
        return 0; // Termina il programma con successo.
    }

    // Funzione per copiare un array statico in un array dinamico
    float *copia_array_di_float(float *a, int n) {
        // Alloca memoria per un array di n float
        float *b = malloc(n * sizeof(float));

        // Debug: stampa la dimensione del puntatore 'a' (non utile in questo contesto)
        printf("%d\n", sizeof(a) / sizeof(float)); // stampa due perche e' una variabile di tipo puntatore,non e' un array statico
                                                        // facendo cosi' lo dividera'

        // sizeof(a) restituisce la dimensione del puntatore (non la dimensione dell'array originale),
        // quindi questa stampa non è significativa qui.

        // Controlla se l'allocazione della memoria è fallita

        if (b == NULL)
            return NULL; // Ritorna NULL se la memoria non può essere allocata.

        // Copia i valori dall'array 'a' al nuovo array 'b'
        for (int i = 0; i < n; i++) {
            b[i] = a[i];
        }

        // Restituisce il puntatore al nuovo array
        return b;
    }
























