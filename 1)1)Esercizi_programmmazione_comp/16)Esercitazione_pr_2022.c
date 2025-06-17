//
// Created by enzob on 16/02/2025.
//




/*
Ecco la trascrizione del testo presente nell'immagine:

---

Programmazione dei calcolatori con laboratorio
26 settembre 2022

### Consegna

Fare **reply** all’email ricevuta allegando i codici C e Python
(una unica email con i due sorgenti). I formati ammessi sono:

- per Python: `.py`, `.ipynb`, export `html`
- per C: `.c`

**NB. Verranno sottratti punti in proporzione ai minuti di ritardo dalla scadenza.**


### **1) C**

Si considerino le strutture dati definite dal seguente frammento di codice:
*/

/*
e restituisca un puntatore ad un nuovo `segment` tale che i due `point`
che lo compongono abbiano coordinate `ax` e `ay` per il primo e `bx` e `by`
per il secondo.
*/

/*
#### **Per il codice in C (`new_segment`)**
1. **Allocazione dinamica della memoria**
   - Usare `malloc` per creare dinamicamente due strutture `point` e una `segment`.
   - Controllare che la memoria sia stata allocata correttamente (evitare memory leaks).

2. **Inizializzazione dei valori**
   - Assegnare i valori `ax`, `ay`, `bx`, `by` ai campi `x` e `y` dei due `point`.

3. **Restituire il segmento**
   - Restituire il puntatore al segmento dopo aver assegnato i puntatori ai `point`.

4. **Deallocazione della memoria**
   - È importante creare anche una funzione di deallocazione (`free_segment`) per evitare memory leaks.
*/

/*
 * consigli per il codice :
 *  - usare malloc per allocare la memoria nella funzione new_segment
 *  poi controllare se l'allocazione e' andata a buon fine
 *  dopo di che si assegnano i valori ai puntatori, e poi si ritorna il puntatore
 *
 *  dopo creare una funzione free_segment che prende in input un puntatore a segment
 *  e che ogni volta che si chiama deve liberare la memoria allocata per il segmento
 *  poi si dealloca la memoria allocata per s->a e s->b e poi si dealloca la memoria allocata per s
 *  ed infine si dealloca la memoria allocata per s
 *
 *
 */


#include <stdio.h>   // Libreria necessaria per l'input/output standard (printf, scanf, ecc.)
#include <stdlib.h>  // Libreria necessaria per l'allocazione dinamica della memoria (malloc, free)

// ****************************
// ** DEFINIZIONE DELLE STRUTTURE DATI **
// ****************************

// La struttura `point` rappresenta un punto nel piano cartesiano bidimensionale.
// Ogni punto è caratterizzato da due coordinate di tipo float: `x` e `y`.
struct point {
    float x, y;  // Coordinate cartesiane del punto
};

// Utilizziamo `typedef` per creare un alias della struttura, così possiamo usare `point` invece di `struct point`
// Questo semplifica la scrittura e migliora la leggibilità del codice.
typedef struct point point;
/*
// La struttura `segment` rappresenta un segmento nel piano bidimensionale.
// Un segmento è definito da due punti: `a` (inizio) e `b` (fine).
// Tuttavia, invece di contenere direttamente due strutture `point`, memorizza due **puntatori** a `point`.
// Questo è utile quando si lavora con allocazione dinamica della memoria.
*/

struct segment {
    point *a; // Puntatore al primo punto (inizio del segmento)
    point *b; // Puntatore al secondo punto (fine del segmento)
};

// Creiamo un alias `segment` per `struct segment`, per rendere il codice più leggibile.
typedef struct segment segment;

// ****************************
// ** PROTOTIPI DELLE FUNZIONI **
// ****************************

// Funzione che alloca dinamicamente un segmento e inizializza i suoi punti con le coordinate fornite.
segment *new_segment(float ax, float ay, float bx, float by);

// Funzione che dealloca la memoria di un segmento precedentemente creato con `new_segment`.
void free_segment(segment *s);

/* ***********************************
// ** FUNZIONE PRINCIPALE (MAIN) **
***********************************/

int main() {
    // Creazione di un nuovo segmento con coordinate (1.0, 2.0) per il punto A e (3.0, 4.0) per il punto B.
    segment *s = new_segment(1.0, 2.0, 3.0, 4.0);

    // Verifichiamo se l'allocazione è avvenuta correttamente.
    if (s != NULL) {
        // Se l'allocazione è avvenuta con successo, stampiamo le coordinate dei due punti del segmento.
        printf("Segmento: A(%.2f, %.2f), B(%.2f, %.2f)\n", s->a->x, s->a->y, s->b->x, s->b->y);

        // Dopo aver usato il segmento, è essenziale deallocare la memoria per evitare memory leaks.
        free_segment(s);
    } else {
        // Se `s == NULL`, significa che l'allocazione della memoria è fallita.
        printf("Errore nell'allocazione del segmento\n");
    }

    return 0; // Termine del programma, indica che l'esecuzione è avvenuta correttamente.
}

// ****************************
// ** FUNZIONE DI ALLOCAZIONE DI UN SEGMENTO **
// ****************************
/*
// Questa funzione alloca dinamicamente memoria per un segmento e per i due punti che lo compongono.
// Inizializza le coordinate dei punti e restituisce un puntatore alla struttura `segment`.
// Se l'allocazione della memoria fallisce in qualsiasi fase, restituisce `NULL`.
*/

segment *new_segment(float ax, float ay, float bx, float by) {
    /* 1. Allocazione della memoria per la struttura `segment`*/
    segment *s = (segment *) malloc(sizeof(segment));

    /* 2. Controllo se l'allocazione del segmento è riuscita*/
    if (s == NULL) {
        return NULL; // Se l'allocazione fallisce, restituiamo NULL per segnalare l'errore.
    }

    /* 3. Allocazione della memoria per il primo punto `a` */
    s->a = (point *) malloc(sizeof(point));
    if (s->a == NULL) { // Controlliamo se l'allocazione è riuscita
        free(s); // Se fallisce, deallochiamo la memoria del segmento `s`
        return NULL; // Restituiamo NULL per segnalare l'errore
    }

    /* 4. Allocazione della memoria per il secondo punto `b`*/

    s->b = (point *) malloc(sizeof(point));
    if (s->b == NULL) { // Controlliamo se l'allocazione è riuscita
        free(s->a); // Deallochiamo la memoria allocata per `s->a`
        free(s); // Deallochiamo la memoria allocata per `s`
        return NULL; // Restituiamo NULL per segnalare l'errore
    }

    /* 5. Assegnazione delle coordinate ai punti*/
    s->a->x = ax; // Impostiamo la coordinata x del primo punto
    s->a->y = ay; // Impostiamo la coordinata y del primo punto
    s->b->x = bx; // Impostiamo la coordinata x del secondo punto
    s->b->y = by; // Impostiamo la coordinata y del secondo punto

    return s; // Restituiamo il puntatore alla struttura `segment` appena creata.
}

/* ****************************
// ** FUNZIONE DI DEALLOCAZIONE DEL SEGMENTO **
// *****************************/

/*
// Questa funzione libera la memoria occupata da un segmento creato con `new_segment`.
// È essenziale chiamarla dopo aver terminato l'uso del segmento per evitare memory leaks.
*/
void free_segment(segment *s) {
    if (s != NULL) { // Controlliamo che il segmento non sia NULL prima di procedere
        free(s->a); // Deallochiamo la memoria del primo punto `a`
        free(s->b); // Deallochiamo la memoria del secondo punto `b`
        free(s); // Deallochiamo la memoria della struttura `segment` stessa
    }
}

/*Questa funzione evita memory leaks, eliminando correttamente tutti
 *i blocchi di memoria allocati dinamicamente per il segmento.
 *
 */



//istruzioni codice
/*
 * UNa volta creata una struttura point
 * creo un typedef per poterla usare come tipo di dato e quindi faccio typedef struct point point;
 *
 * poi faccio una sctruct segment segment che rapresenta un segmnto che ha due punti a e b
 *
 *poi dopo aver creato il prototipo della funzione new_segment
 * creo la funzione new_segment che prende in input 4 float
 * e restituisce un puntatore a segment
 * creo un puntatore a segment e lo alloco con malloc
 * controllo se l'allocazione e' andata a buon fine
 * se non e' andata a buon fine ritorno NULL
 * se e' andata a buon fine ritorno il puntatore
 *
 *poi alloco i due punti a e b
 * con s->a = (point *) malloc(sizeof(point)); che alloca la memoria per un punto
 * poi faccio un if per controllare se l'allocazione e' andata a buon fine
 * se non e' andata a buon fine ritorno NULL
 * prima però devo liberare la memoria che ho allocato per s
 *
 * POI alloco la memoria per il secondo punto
 *   s -> b = ( point *) malloc (sizeof(point)); // qui alloco la memoria per il secondo punto
 *  S-> b significa che sto accedendo al campo b della struttura s
 *   poi lo pongo uguale a point * e per allocare la memoria per un punto
 *   poi con malloc alloco la memoria per un punto lo pongo a sizeof(point) per allocare la memoria per un punto
 *   poi controllo se l'allocazione e' andata a buon fine con un if dove controllo se s->b e' uguale a NULL
 *   e poi se e' uguale a NULL allora devo liberare la memoria allocata per s->a
 *   e con il secondo free devo liberare la memoria allocata per s, mentre nel primo free(s-b) devo liberare la memoria allocata per s->b
 *   ed infine ritorna Null se l'allocazione non e' andata a buon fine
 *
 *   infine del cod restituisce il puntatore ossia s
 * dopo creo una funzione free_segment che prende in input un puntatore a segment
 *  che ogni volta che si chiama deve liberare la memoria allocata per il segmento
 *  infatti creao tale per una deallocazione della memoria
 *
 * Poi creo una funziione free_segment che prende in input un puntatore a segment
 * e che ogni volta che si chiama deve liberare la memoria allocata per il segmento
 * poi si dealloca la memoria allocata per s->a e s->b e poi si dealloca la memoria allocata per s
 * ed infine si dealloca la memoria allocata per s
 *
 *  poi creo la funz main che crea un segmento e poi lo dealloca
 *
 */
//---------------------------------------------------------------------------------------------
/*
Errori Comuni da Evitare
Dimenticare la deallocazione della memoria (free)
→ Risultato: Memory leaks.

Non controllare se malloc() ha restituito NULL
→ Risultato: Possibile crash del programma se si tenta di accedere a un puntatore NULL.

Dimenticare di restituire il puntatore segment * correttamente
→ Assicurarsi che la funzione new_segment restituisca effettivamente un puntatore valido.

Usare un puntatore non inizializzato
→ Prima di assegnare valori a s->a o s->b, bisogna allocare la memoria.

*/

