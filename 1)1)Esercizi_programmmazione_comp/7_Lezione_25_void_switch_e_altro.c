//
// Created by Enzo on 19/01/2025.
//

/*
 * Array Dinamico
 *
 *
 *
 * */


//   0  1                   i             n-1
// |-+-|---|----------------|--|-------------|
//  __  __
//  d    d
//
// &(a[i]0 e' a + d i atitmedia tra i interi e poi in tempo costante eseguo indicizzazione
//
//                              tra i dati
//                            -------------------
//                                   i
//    ------------------------------------------------------------
//    | | tipo :puntatore|    | tipo : puntatore |                |
//    ------------------------------------------------------------
//             |                           |
//             |                         dato
//             |
//              --------------------------------------> dato
/* UN TIPO DI DATO VOI E' :

* // In C, il tipo di dato `void` rappresenta l'assenza di tipo. È usato in vari contesti per indicare
// che una funzione o un puntatore non ha un tipo di ritorno o di riferimento specifico.

// 1. Funzioni che non restituiscono un valore
// Uno degli usi più comuni di `void` è nelle funzioni che non restituiscono un valore.
// Queste sono comunemente chiamate funzioni "procedure" o "void functions".
// Un esempio è la funzione `printf`, che ritorna un intero per indicare il numero di caratteri stampati,
// ma ci sono molte funzioni, come `exit()`, che non hanno bisogno di restituire un valore e quindi hanno
// un tipo di ritorno `void`.

// Esempio:
// void stampaMessaggio() {
//     printf("Questo è un messaggio.\n");
// }
// In questo esempio, `stampaMessaggio` è una funzione che esegue un'operazione (stampa un messaggio)
// ma non restituisce un valore.

// 2. Puntatori a `void`
// I puntatori di tipo `void` sono puntatori generici che possono puntare a qualsiasi tipo di dato.
// In C, i puntatori a `void` sono utilizzati per scrivere funzioni e librerie che possono operare con
// diversi tipi di dati, senza specificare esplicitamente il tipo di dato nel codice.

// Esempio:
// void* malloc(size_t size);
// La funzione `malloc` restituisce un puntatore di tipo `void*`, il che significa che può
// restituire un puntatore a un blocco di memoria senza specificare di quale tipo sono i dati
// contenuti in quella memoria. Questo permette a `malloc` di essere estremamente versatile,
// poiché il puntatore restituito può essere castato a qualsiasi tipo di puntatore desiderato.

// 3. Parametri di funzioni di tipo `void`
// Alcune funzioni in C possono avere `void` come parametro, il che significa che la funzione non
// accetta alcun parametro. Questo è usato per specificare esplicitamente che una funzione non deve
// essere chiamata con argomenti.

// Esempio:
// void funzioneSenzaParametri(void) {
//     printf("Non ho parametri!\n");
// }
// Questo chiarisce che `funzioneSenzaParametri` non deve accettare alcun argomento quando viene invocata.

// Utilizzo in Interfacce di Programmazione
// `void` è spesso utilizzato nelle interfacce di programmazione, in particolare nelle librerie, per
// fornire funzioni che possono operare con tipi di dati non specificati o per assicurare che certe
// funzioni non ritornino dati o non ricevano parametri. Questo rende il codice più generico e riutilizzabile,
// un principio fondamentale nella progettazione del software.

// Conclusioni
// Il tipo `void` è quindi un elemento molto potente in C, che contribuisce alla flessibilità del linguaggio
// permettendo di scrivere codice generico e funzioni che possono interagire con diversi tipi di dati o che
// eseguono operazioni senza necessità di ritornare un valore.
*/

// Ecco spiegato cosa fa la funzione sotto al testo :

/* USando `typedef` per definire un nuovo tipo denominato `elemento`.
Ecco un riassunto di cosa hai fatto e perché:
### Struttura e Typedef
- **`typedef struct elemento {...} elemento;`**:
Questa sintassi permette di definire un tipo di dati strutturato e di assegnargli un nome attraverso `typedef`.
La parola chiave `typedef` è usata per creare un alias di tipo, che ti permette di usare semplicemente `elemento`
invece di `struct elemento` quando dichiari variabili di quel tipo. Questo rende il codice più pulito e facile
da gestire, specialmente quando lavori con strutture complesse o con puntatori a strutture.

### Campi della Struttura
- **`char tipo;`**: Questo campo è utilizzato per identificare il tipo di dato contenuto nel puntatore
`dato`. I valori come `'i'`, `'f'`, `'s'` servono per distinguere tra interi,
numeri in virgola mobile (float) e stringhe, rispettivamente.
- **`void *dato;`**: Questo è un puntatore di tipo `void` che può puntare a qualsiasi tipo di dato.
L'uso di `void *` è particolarmente utile in contesti come strutture dati generiche dove il tipo di
elemento contenuto può variare. Il puntatore può essere successivamente castato al tipo appropriato
a seconda del valore di `tipo`.

### Uso del `void *`
- Il `void *` ti permette di scrivere funzioni e tipi di dati più generici e riutilizzabili.
Ad esempio, potresti avere una funzione che accetta un `void *` e basandosi sul campo `tipo`,
esegue operazioni diverse.
- Inoltre, l'utilizzo di `void *` elimina la necessità di definire multiple strutture o
funzioni per gestire tipi di dati diversi. Questo approccio è comune nelle librerie che
devono gestire dati di tipi diversi in modo uniforme.

### Commenti sui Puntatori e Conversione dei Tipi
- **Conversione e manipolazione di puntatori**: I commenti chiariscono come la manipolazione di
puntatori (ad esempio, l'aritmetica dei puntatori quando sono castati a `char *`) permetta di
gestire i dati in maniera flessibile, permettendo ad esempio di accedere a dati di varia dimensione e tipo.

### Definizione del Tipo di Ritorno `void` nelle Funzioni
- Hai anche menzionato l'uso del tipo `void` in funzioni che non hanno un valore di ritorno.
Questo è utile per funzioni che eseguono operazioni ma non necessitano di restituire un valore,
come le funzioni che inizializzano o modificano strutture dati o che eseguono operazioni di logging o di output.

In conclusione, hai creato un tipo di dato `elemento` che può essere utilizzato per costruire liste
o altre strutture dati che possono contenere elementi di tipi diversi, rendendo il tuo codice più generico
e flessibile. Questo approccio è estremamente utile in programmazione di sistemi, librerie, e applicazioni
dove la generalizzazione e la riutilizzabilità del codice sono prioritarie.

*/
#include <stdio.h>
#include <stdlib.h>

typedef struct elemento{ // uso la type def insieme alla struct, per poter  togliere il nome nella struct perche' andro a definire il nome del tipo
  char tipo ; /* se il char e' i , intero  ; 'f' float ; 's' stringa*/
   void *dato; // e' un tipo di dato a puntatore
   // si usa il  tipo di dato void che e'  usato per indicare diverse cose :
   // che puo' essere convertito nel tipo di dato che serve
   // un puntatore e' un indirizzo, ache cosa serve il tipo del puntatore, un puntatore a char sommato aggiunge un valore a quel puntatore
   // quindi il puntatore puo' essere un indirizzo che punta qualunque cosa
   // quindi questo puntatore qui sopra punta qualcosa che sara' definito in seguito
   // il tipo di dato void si usa anche  nelle funzioni  come tipoo di otput, per indicare che una funz non ha un return , sensa il tipo , viene considerato come output il tipo di default ossia int
   // se mettiamo a  void significa che npn vuole restitutiop nulla


}elemento; // sto definendo un nuovo tipo che sara' elemento, che definisce la struct list



struct lista {
    elemento *a;    // a e' l'array vero e' proprio
    int c; // capacita'
    int n ;// dimensione di elementi

}; // e' un tipo di dato composto
/* ci consente di rendere un tipo piu' definito, ci consente di dare un nuovo nome ad un tipo gia esistente  */


typedef struct lista lista ; // ci consente di richiamare i parametri precedenti facendo in modo di creare una nuova lista

lista init();/*Crea un lista vuota */
lista append(lista, elemento);/* appende un elemento puntato */
void mostra(lista);
lista pop(lista);

elemento intero(int);
elemento fpoint(float);
elemento stringa(char*);
lista pop(lista);

int main (){

    lista L = init();
    L = append(L, intero(10) ); // intero crea una funz. di tipo intero e li passa
    L = append(L, fpoint(3.14) );
    L = append(L, stringa("programma") );
    L = append(L, fpoint(2.71) );
    L = append(L, stringa("lista") );

    L = append(L, intero(7) );
    L = append(L, intero(10) );
    L = append(L, fpoint(3.14) );
    L = append(L, stringa("programma") );
    L = append(L, fpoint(2.71) );
    L = append(L, stringa("lista") );
    L = append(L, intero(7) );
    L = append(L, intero(10) );
    L = append(L, fpoint(3.14) );
    L = append(L, stringa("programma") );

    /*L = append(L, fpoint(2.71) );
    L = append(L, stringa("lista") );
    L = append(L, intero(7) );
    L = append(L, intero(10) );
    L = append(L, fpoint(3.14) );
    L = append(L, stringa("programma") );
    L = append(L, fpoint(2.71) );
    L = append(L, stringa("lista") );
    L = append(L, intero(7) );*/

    /**
 * Questo ciclo while rimuove elementi dalla lista L fino a quando non è vuota,
 * mostrando lo stato della lista ad ogni iterazione.
 */
    while (L.n > 0) { // Esegue fino a che la lista non è vuota
        /**
         * Rimuove l'ultimo elemento dalla lista L.
         * - `pop(L)` decrementa il contatore degli elementi e libera la memoria dell'elemento rimosso,
         *   evitando perdite di memoria e riducendo la dimensione della lista di uno.
         */
        L = pop(L);

        /**
         * Mostra lo stato attuale della lista dopo la rimozione di un elemento.
         * - `mostra(L)` visualizza i dati rimanenti nella lista, permettendo di verificare
         *   l'efficacia delle operazioni di rimozione.
         */
        mostra(L);
    }
    /**
     * Alla fine, la lista L è completamente svuotata. Questo ciclo è utile per pulire la lista
     * prima di liberare le risorse, assicurando la gestione corretta della memoria.
     */

    mostra (L);


}


/*
 * Funzione pop per rimuovere l'ultimo elemento dalla lista e ottimizzare l'uso della memoria.
 * Riduce il numero di elementi e potenzialmente ridimensiona il buffer di memorizzazione se molto spazio è inutilizzato.
 *
 * @param L La lista da cui rimuovere l'elemento.
 * @return lista La lista aggiornata dopo la rimozione dell'elemento.
 */
lista pop(lista L)
{
    // Verifica che ci siano elementi nella lista da rimuovere.
    if (L.n > 0) {
        // Decrementa il contatore degli elementi, "rimuovendo" l'ultimo elemento.
        L.n--;

        // Controlla se la memoria allocata è ora eccessivamente grande rispetto al numero di elementi.

        // Riduce la capacità della lista se meno di un quarto della capacità allocata è in uso.
        if (L.n < L.c / 4) {
            // Riduce la capacità della lista a metà della capacità corrente.
            L.c = L.c / 2;
            // Realloca l'array per adattarlo alla nuova dimensione ridotta.
            // Questo può aiutare a risparmiare memoria se la lista si è ridotta significativamente.
            L.a = realloc(L.a, L.c * sizeof(elemento)); /* richiede sempre tempo costante */
            // È importante controllare se realloc ha successo qui. Se realloc fallisce, potrebbe
            // restituire NULL e causare la perdita della lista originale. Questo controllo è omesso qui
            // per brevità ma è essenziale in un'applicazione reale.
        }

        // Libera la memoria allocata per il dato dell'ultimo elemento solo se il tipo non è 's' (stringa).
        // Questo presuppone che i dati di tipo 's' possano essere gestiti diversamente o non necessitino di liberazione.
        // È importante liberare solo i tipi di dati che sono stati allocati dinamicamente.
        if (L.a[L.n].tipo != 's') {
            free(L.a[L.n].dato);
        }
        // Riduce il conteggio degli elementi, effettuando la rimozione logica.
    }
    return L;  // Restituisce la lista aggiornata con meno elementi e potenzialmente meno capacità.
}






// Funzione che crea una lista vuota:

lista init(){ // Non prende parametri in input
    lista lista_vuota = {NULL, 0, 0};
    /*
    Inizializza una lista vuota con i seguenti valori:
    - `NULL`: Nessun puntatore allocato per l'array
    - `0`: Numero di elementi nella lista è inizialmente zero
    - `0`: Capacità della lista è zero (nessuna memoria allocata)
    */
    return lista_vuota; // Restituisce la lista vuota
}


lista append(lista L, elemento e){
    // Aggiunge `e` a `L`, raddoppiando la capacità se `L.n == L.c`.

    if (L.n == L.c) {
        // Espansione necessaria: raddoppia la capacità e rialloca
        L.c = 2 * (L.c + 1);
        L.a = realloc(L.a, L.c * sizeof(elemento));
    }

    // Inserisce l'elemento e aggiorna il conteggio
    L.a[L.n] = e;
    L.n++;

    // Restituisce la lista aggiornata. L'operazione di append ha costo O(1) ammortizzato
    // perché raddoppiare la capacità riduce la frequenza delle riallocazioni.
    return L;
}


/*Spiegazione dei Commenti del cod sopra:
Aggiunta e Riallocazione: Il commento iniziale spiega brevemente l'operazione principale della funzione
e il suo comportamento in caso di necessità di espansione della capacità della lista. Questo è essenziale
per comprendere la logica di base senza entrare nei dettagli di ogni passaggio.

Dettagli Tecnici Compressi: I dettagli su come e perché la capacità viene raddoppiata
e la memoria riallocata sono riassunti in una sola riga per mantenere il codice leggibile
e non sovraccaricarlo di informazioni.
Costo dell'Operazione: Un breve commento finale chiarisce il costo ammortizzato
dell'operazione di append, che è un concetto importante per comprendere l'efficienza
della funzione nel tempo.
*/


void mostra(lista L){
  int i ;
    printf("==================================\n");

  for(i=0 ; i<L.n ; i++){// dal primo elemnto fino all'elemento n
    /*Stampa L.n[i] */

    /*if (L.a[i].tipo == 'i'){
      printf("%d\n", *((int*)L.a[i].dato));// * per puntare al tipo di dato ossia int, devo convertire il tipo di dato in int
      // aggiungendo (int)* esegueo un operazione di casting perche' perima il dato era vuto ed ora sara' int
      */


      switch (L.a[i].tipo){// usoro' switch che prende un espressione la valuta e poi va a vedere e confrontare quale
                           // e il valore eseguendo varie opzioni che andro' ad indicare poi entro nel blocco li dove c'e' l'opzione giusta  a verificare  dei valori
      /* le varie opzioni le andro' a confrontare con case:*/
      case 'i': /* quando sara' questo caso andrea' a fare :*/
           printf("%d\n", *((int*)L.a[i].dato) );// * per puntare al tipo di dato ossia int, devo convertire il tipo di dato in int
          // aggiungendo (int)* esegueo un operazione di casting perche' perima il dato era vuto ed ora sara' int
      break; /* facendo cio' usira' in caso si verifichi questo caso, uscendo dal ciclo */
      case 'f':
          printf("%s\n", (char*)L.a[i].dato);
          break;
      case 's':
          printf("%s\n", (char*)L.a[i].dato);// non bisognera' mettere il puntatore all'inizio perche' la stringa e' gia' un array e quindi eseque solo il casting
          break;
      default: // andra' messo default nel caso in cui non siano veri  tutti i casi precedenti  allora deve eseguire il codice
      /* se non vero i precedenti */
          printf("Tipo non riconosciuto.\n");
          break;
      }

  }
    printf("dimensione %d, capacita' %d\n",L.n,L.c);
}







// Definisce una funzione che crea un elemento con dati di tipo intero.
elemento intero(int d) {
    // Inizializza una struttura 'elemento' con il tipo 'i' (intero) e un puntatore dati inizialmente nullo.
    elemento e = {'i', NULL};

    // Alloca memoria sufficiente per contenere un intero.
    // `sizeof(int)` calcola la dimensione di un intero in byte.
    e.dato = malloc(sizeof(int));

    // Cast del puntatore void* restituito da malloc a int* e assegna il valore di d a questa locazione di memoria.
    *((int*)e.dato) = d;  // Deriferenzia e assegna il valore intero

    // Restituisce la struttura 'elemento' popolata.
    return e;
}



// Definisce una funzione che crea un elemento con dati di tipo float.

elemento fpoint(float d) {
    // Inizializza una struttura 'elemento' con il tipo 's' (string, usato impropriamente qui per float).
    elemento e = {'s', NULL};

    // Alloca memoria sufficiente per contenere un float.
    e.dato = malloc(sizeof(float));

    // Cast del puntatore void* restituito da malloc a float* e assegna il valore di d a questa locazione di memoria.
    *((float*)e.dato) = d;  // Deriferenzia e assegna il valore float

    // Restituisce la struttura 'elemento' popolata.
    return e;
}



/* Definisce una funzione che crea un elemento con dati di tipo stringa (puntatore a char).*/

elemento stringa(char *d) {
    // Inizializza una struttura 'elemento' con il tipo 'f' (float, usato impropriamente qui per stringa).
    elemento e = {'f', NULL};

    // Codice commentato che mostra come si potrebbe allocare memoria per un puntatore a char.
    /*e.dato = malloc(sizeof(char*));  // Alloca memoria per un puntatore a char
    *((char**)e.dato) = d;  // Assegna il puntatore alla stringa fornita */

    // Restituisce la struttura 'elemento' popolata.
    return e;
}


/**
 * `malloc` e `sizeof` sono due funzioni fondamentali nella gestione della memoria in C.
 *
 * `sizeof`:
 * - `sizeof` è un operatore che restituisce la dimensione in byte di un tipo di dato o di una variabile.
 * - Viene usato per determinare quanta memoria deve essere allocata per un certo tipo di dati.
 * - Ad esempio, `sizeof(int)` restituisce la dimensione di un intero, che può variare a seconda dell'architettura
 *   del sistema (tipicamente 4 byte su sistemi moderni).
 *
 * `malloc`:
 * - `malloc(size_t size)` è una funzione della libreria standard C che alloca `size` byte di memoria
 *   non inizializzata e restituisce un puntatore a void a questa memoria.
 * - Questo spazio di memoria può poi essere utilizzato per memorizzare dati di qualsiasi tipo.
 * - È importante controllare se `malloc` restituisce NULL, che indica un fallimento nell'allocazione della memoria,
 *   tipicamente a causa di memoria insufficiente.
 * - La memoria allocata rimane occupata fino a quando non viene liberata esplicitamente usando `free()`,
 *   altrimenti può causare una perdita di memoria.
 *
 * Nell'uso di queste funzioni, è critico gestire correttamente gli errori e assicurarsi di liberare
 * la memoria allocata quando non è più necessaria.
 */





//---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



/*
 * malloc:
 * `malloc` è una funzione di libreria standard del linguaggio C che alloca un blocco di memoria
 * sul heap e restituisce un puntatore a void a questa memoria. La memoria allocata rimane occupata
 * finché non viene liberata esplicitamente tramite una chiamata a `free`. Questo è essenziale per
 * gestire la memoria in programmi C, specialmente quando la dimensione del dato non è conosciuta
 * al momento della compilazione o è dinamicamente variabile durante l'esecuzione del programma.
 *
 * sizeof:
 * `sizeof` è un operatore in C che restituisce la dimensione in byte di un tipo di dato o di una
 * variabile. Viene utilizzato frequentemente con `malloc` per assicurarsi che la quantità di memoria
 * allocata sia adeguata per il tipo di dati che si vuole memorizzare. Questo previene errori come
 * buffer overflow o accesso a memoria non allocata, garantendo che il puntatore restituito da `malloc`
 * abbia spazio sufficiente per i dati di quel tipo.
 *
 * Utilizzando `sizeof` si garantisce che il codice sia portabile tra piattaforme con diverse
 * dimensioni di tipi di dati standard (come interi o float). Ad esempio, la dimensione di un intero
 * può variare tra sistemi a 32 e 64 bit, e `sizeof(int)` gestisce automaticamente queste differenze.
 */
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


// L e' la nostra struct
//                                                                         0                    1 //Secondo append ,      2
// L      |     | --------------> creo un array di dimensione  | 'i' |copiera l'elemnto 10 ||puntatore '*'| 3.14     || '*' | stringa
//     n  |  2  |                                                           ^
//     c  |  6  |                                                           |
//                                                                          |
//                                                                          |
// lista e                                                                  |
//  |  i  |                                                                 |
//  |     | -----------------> |10|-----------------------------------------|


/* Dopo aver fatto cio' andra' a copiare l'elemnto 10 in i e la lista e andra' a sparire perche' era una lista di appoggio */
// lo stesso fara' con i float e char



//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


/*
 * Funzione pop per rimuovere l'ultimo elemento dalla lista e liberare la memoria associata.
 * Questa funzione non solo riduce il conteggio degli elementi nella lista ma si occupa anche
 * di liberare la memoria allocata per i dati dell'elemento rimosso.
 *
 * @param L La lista da cui rimuovere l'elemento.
 * @return lista La lista aggiornata dopo la rimozione dell'elemento.
 *
 * Dettagli:
 * - La funzione verifica prima se la lista contiene elementi (L.n > 0).
 *   Se la lista non è vuota, procede con le operazioni di rimozione.
 * - Utilizza `free()` per liberare la memoria allocata al dato dell'ultimo elemento,
 *   prevenendo così perdite di memoria. Questo passaggio è cruciale in gestione dinamica della memoria.
 * - Successivamente, decrementa il contatore degli elementi (L.n), riducendo la dimensione logica della lista.
 *   Questo decremento simula l'effettiva rimozione dell'elemento.
 *
 * Considerazioni sulla sicurezza e stabilità:
 * - La chiamata a `free()` assicura che non ci siano perdite di memoria. Tuttavia, è essenziale
 *   che ogni dato dentro la lista sia stato allocato dinamicamente prima di questa operazione.
 * - Dopo la chiamata a `free()`, il puntatore al dato viene liberato ma non automaticamente impostato a NULL.
 *   Ciò può portare a potenziali errori di "dangling pointer" se il dato è accesso successivamente.
 * - Questo metodo di 'pop' è sicuro solo se la lista gestisce correttamente la proprietà dei dati
 *   (cioè, ogni elemento deve essere responsabile per la liberazione dei propri dati).
 *
 * Utilizzo:
 * - Questa funzione è utile in contesti dove è richiesta una corretta gestione della memoria,
 *   come in applicazioni che allocano e deallocano frequentemente grandi quantità di dati.
 * - È particolarmente importante in contesti di programmazione di sistemi o applicazioni
 *   dove le risorse sono limitate e la gestione efficiente della memoria è critica.
 */






















