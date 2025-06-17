//
// Created by Enzo on 27/01/2025.
//


/*
 * NEL CASO IN CUI VOGLIA CANCELLARE UN ELEMNTO :
 * che potrebbe stare ovunque, si in testa che in coda
 *
 *  L -> |--|--| -> |--|--|  -> ......   -> |--|--| -> |--|--| ->...... -> |--|0/ |
 *
 *
 *
 * */







#include <stdio.h>
#include <stdlib.h>

typedef struct nodo {
    float dato;
    struct nodo *succ, *prec; // aggiungo prec che punterà al nodo precedente
} nodo;

typedef nodo *clista; // lista concatenata

clista clista_vuota(); // Funzione per creare una lista vuota
void clista_mostra(clista); // Funzione per stampare il contenuto della lista
nodo *clista_in0(clista, float); // Funzione per inserire un elemento in testa
nodo *clista_cerca(clista, float); // Funzione per cercare un elemento nella lista

nodo *clista_out0(clista);// questa funzione elimina un elemento dalla lista
nodo *clista_out(clista, float );// questa funzione permette di scegliere che elemnto elimnare dalla lista, prima elimanava gli elemnti consecutivamente


int main() {
    clista L = clista_vuota(); // Inizializzazione della lista come vuota

    // Inserisco 10 elementi nella lista, i valori saranno [9, 8, ..., 0]
    for (int i = 0; i < 10; i++) {
        L = clista_in0(L, i);
    }

    clista_mostra(L); // Stampo il contenuto della lista

/*    // Cerco il nodo contenente il valore 9
    nodo *point = clista_cerca(L, 9);

    // Se il nodo è trovato e ha un nodo precedente, stampo il valore del precedente
    if (point != NULL && point->prec != NULL) {
        printf("%f\n", point->prec->dato);
    } else {
        printf("Non trovato\n"); // Altrimenti stampo che non è stato trovato
    }*/
    //==================================================================================================================
    /*
      * **Cosa fa il `while` aggiunto:**
      * - Itera sulla lista concatenata e rimuove un elemento alla volta dalla testa.
      * - Dopo ogni rimozione, stampa lo stato aggiornato della lista.
      *
      * **Passaggi dettagliati:**
      * 1. Controlla se la lista non è vuota (`L != NULL`).
      * 2. Chiama la funzione `clista_out0(L)` per rimuovere il primo nodo:
      *    - La funzione avanza la testa della lista al nodo successivo.
      *    - Libera la memoria del nodo rimosso.
      * 3. Stampa il contenuto aggiornato della lista con `clista_mostra(L)`.
      * 4. Continua fino a quando la lista è vuota (`L == NULL`).
      */

     while (L != NULL) {
         L = clista_out0(L); // Rimuove il primo nodo e aggiorna la testa della lista.
         clista_mostra(L);  // Mostra lo stato attuale della lista.
     }

    /*
     * **Risultato:**
     * - La lista concatenata viene svuotata completamente.
     * - Dopo ogni rimozione, lo stato della lista viene stampato.
     *
     * **Esempio di output:**
     * - Prima rimozione: [9, 8, ..., 0]
     * - Dopo la rimozione del primo elemento: [8, 7, ..., 0]
     * - Ripetuto fino a quando la lista è vuota: []
     *
     * **Nota:** Alla fine del ciclo, tutta la memoria allocata dinamicamente per i nodi è stata liberata,
     * prevenendo memory leak.
     */
    // Inserisco 10 elementi nella lista, i valori saranno [9, 8, ..., 0]
    for(int i = 0; i < 10; i++){
        L = clista_in0(L, i);
    }

    clista_mostra(L); // stampo il contenuto della lista

    L = clista_out(L, 5);

    clista_mostra(L);

    //------------------------------------------------------------------------------
    clista_mostra(L); // stampo il contenuto della lista

    L = clista_out(L, 0);

    clista_mostra(L);
    //------------------------------------------------------------------------------
    clista_mostra(L); // stampo il contenuto della lista

    L = clista_out(L, 9);

    clista_mostra(L);
    //------------------------------------------------------------------------------
    //------------------------------------------------------------------------------

    clista L1 = clista_vuota();
    L1 =clista_in0(L1, 0);

    clista_mostra(L1);

    L1 = clista_out(L1, 0);

    clista_mostra(L1);
    //------------------------------------------------------------------------------
    //------------------------------------------------------------------------------


}

// Funzione per inizializzare una lista vuota
clista clista_vuota() {
    return NULL; // Una lista vuota è rappresentata come un puntatore a NULL
}

// Funzione per stampare il contenuto della lista
void clista_mostra(clista a) {
    nodo *p; // Puntatore per attraversare la lista
    p = a;

    printf("Contenuto della lista: ");

    // Itero sulla lista finché non raggiungo la fine
    while (p != NULL) {
        printf("%.2f, ", (*p).dato); // Stampo il valore del nodo puntato
        // "%.2f, " facendo cosi' aggiungera' solo due 0 nel float

        p = p->succ; // Passo al nodo successivo
    }

    printf("\n");
}

/*
nodo *clista_in0(clista a, float v){
    nodo *p = malloc(sizeof(nodo));
    p->dato = v;
    p->succ = a;
    a = p;
    return a; // oppure return p
}*/
// la funzione qui sopra sara modificata siccome, devo eseguire una cancellazione, e quindi varia la funz

nodo *clista_in0(clista a, float v) {
    // Alloco dinamicamente memoria per un nuovo nodo della lista concatenata.
    // La dimensione allocata è quella della struttura `nodo`.
    nodo *p = malloc(sizeof(nodo));

    // Assegno il valore `v` al campo `dato` del nuovo nodo.
    p->dato = v;

    // Faccio puntare il nuovo nodo `p` al nodo attualmente in testa alla lista.
    // Il nodo successivo a `p` è quindi l'attuale lista.
    p->succ = a;

    // Poiché `p` è ora il primo elemento, il suo campo `prec` deve essere NULL.
    // Questo indica che non c'è un nodo precedente a `p`.
    p->prec = NULL;

    // Controllo se la lista iniziale non era vuota (ovvero `a` non è NULL).
    if (a != NULL) {
        // Se la lista non è vuota, aggiorno il campo `prec` del vecchio nodo di testa (`a`).
        // Ora il vecchio nodo punta al nuovo nodo come suo nodo precedente.
        a->prec = p;
    }

    // Aggiorno la testa della lista per puntare al nuovo nodo `p`.
    // Indipendentemente dal fatto che la lista fosse vuota o meno,
    // il nuovo nodo `p` diventa il primo elemento della lista.
    a = p;

    // Restituisco il nuovo nodo `p` come la nuova testa della lista concatenata.
    return a;
}






// Funzione per cercare un nodo contenente un valore specifico
nodo *clista_cerca(clista a, float k) {
    nodo *p = a; // Parto dalla testa della lista

    // Itero finché non trovo il nodo con il valore cercato o raggiungo la fine della lista
    while (p != NULL && p->dato != k) {
        p = p->succ; // Passo al nodo successivo
    }

    return p; // Restituisco il nodo trovato o NULL se non trovato
}

nodo *clista_out0(clista a) {
    clista p = a; // Salvo il riferimento all'attuale testa della lista per liberare la memoria più tardi.

    // Controllo se la lista è vuota (testa == NULL).
    // Se la lista è vuota, non c'è nulla da rimuovere e ritorno NULL.
    if (a == NULL) {
        return NULL;
    }

    // Avanzo la testa della lista al nodo successivo.
    a = a->succ;

    // Se la nuova testa della lista non è NULL (cioè la lista non è vuota dopo lo spostamento):
    if (a != NULL) {
        a->prec = NULL; // Il nuovo nodo di testa non ha un nodo precedente, quindi `prec` viene impostato a NULL.
    }

    // Libero la memoria allocata per il vecchio nodo di testa (`p`).
    free(p);

    // Ritorno il nuovo nodo di testa della lista concatenata.
    return a;
}

/*
 * **Dettagli su cosa fa il codice:**
 * 1. Controlla se la lista è vuota (`a == NULL`):
 *    - Se è vuota, restituisce subito NULL, indicando che la lista rimane vuota.
 *
 * 2. Avanza la testa della lista al nodo successivo (`a = a->succ`):
 *    - Rimuove logicamente il primo nodo, rendendo il nodo successivo la nuova testa.
 *
 * 3. Aggiorna il puntatore `prec` del nuovo nodo di testa:
 *    - Imposta `prec = NULL` per il nodo che diventa la nuova testa, indicando che non ha più un precedente.
 *
 * 4. Libera la memoria del vecchio nodo di testa (`free(p)`):
 *    - Dealloca la memoria del nodo rimosso per prevenire memory leak.
 *
 * **Nota:**
 * - Questa funzione rimuove in modo sicuro il primo nodo della lista concatenata doppiamente collegata.
 * - Se la lista contiene un solo nodo, dopo la rimozione la lista diventa vuota (testa = NULL).
 */



// versione precedente del clista_out che permetteva diu eliminare un num
/*nodo *clista_out(clista a , float k  )    // questa funzione permette di scegliere che elemnto elimnare dalla lista, prima elimanava gli elemnti consecutivamente
{
    nodo  *p = clista_cerca(a,k);
    if (p == NULL) // nel caso in cui il valore sia nullo
    {
        return a; // ritorna alla lista a nel caso in cui non ci sia nulla da cancellare
    }
    nodo *q = p->succ;

    q ->succ = clista_out0(q -> succ);
    q ->succ->prec = q;
    return a;
}*/


clista clista_out(clista a, float k) {
    // Trovo il nodo con il valore `k` usando la funzione `clista_cerca`.
    // Se il nodo non viene trovato (`p == NULL`), ritorno la lista invariata.
    nodo *p = clista_cerca(a, k);
    if (p == NULL)
        return a;

    // Salvo un riferimento al nodo precedente a `p`.
    nodo *q = p->prec;

    // Caso 1: Il nodo `p` è il primo nodo della lista (testa).
    // Questo accade se `q == NULL`, poiché `p->prec` è NULL per il primo nodo.

    if (q == NULL) {    /* p e' il primo nodo della lista ovvero p == a*/
        // Uso la funzione `clista_out0` per rimuovere il primo nodo della lista.
        // Questa funzione aggiorna la testa della lista e libera la memoria del nodo.
        return clista_out0(p);
    }

    // Caso 2: Il nodo `p` non è il primo nodo della lista.
    // Aggiorno il puntatore `succ` del nodo precedente (`q`) per saltare il nodo `p`.
    q->succ = clista_out0(q->succ);

    // Dopo l'aggiornamento, controllo se il nodo successivo esiste.
    // Se esiste, aggiorno il suo puntatore `prec` per puntare al nodo precedente `q`.
    if (q->succ != NULL)
    {
        q->succ->prec = q;
    }
    // Ritorno la lista invariata, poiché la testa (`a`) non cambia.
    return a;
}


/*
Commenti approfonditi sul comportamento del codice
Ricerca del nodo (clista_cerca):

La funzione utilizza clista_cerca per trovare il nodo p contenente il valore k.
Se il nodo non viene trovato (p == NULL), significa che il valore k non è presente nella lista, quindi la funzione ritorna la lista invariata.
*/

// Caso 1: Nodo p è la testa della lista (q == NULL):
/*
Se p è il primo nodo della lista, il campo prec di p sarà NULL, quindi q == NULL.
In questo caso, la funzione delega la rimozione del nodo a clista_out0, che è progettata per rimuovere il primo nodo di una lista concatenata.
La funzione clista_out0:
- Aggiorna la testa della lista.
- Libera la memoria del nodo rimosso.
*/

// Caso 2: Nodo p non è la testa della lista:
/*
Se p ha un nodo precedente (q != NULL), la rimozione avviene aggiornando i puntatori:
- q->succ viene aggiornato per saltare il nodo p e puntare direttamente al successivo nodo dopo p.
- La funzione clista_out0(q->succ) viene chiamata per liberare il nodo p.
*/

// Aggiornamento del puntatore prec del nodo successivo:
/*
Se il nodo successivo a p (q->succ) esiste, il suo puntatore prec viene aggiornato per puntare al nodo precedente q.
Questo passaggio è fondamentale per mantenere la coerenza della lista doppiamente concatenata.
*/

// Ritorno della lista:
/*
La funzione restituisce la lista invariata, poiché la testa della lista (a) non cambia, a meno che il nodo rimosso non fosse la testa stessa.
*/

// Punti chiave
// Questo codice gestisce correttamente sia la rimozione del primo nodo della lista che la rimozione di nodi intermedi o finali.
// Utilizza la funzione clista_out0 in modo efficace per rimuovere nodi specifici.
// Mantiene la coerenza dei puntatori succ e prec per garantire che la lista doppiamente concatenata rimanga valida.
// La lista viene restituita invariata, a meno che la testa della lista non venga modificata dalla rimozione.


//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




/*
 * Rappresentazione grafica della lista doppiamente concatenata dopo l'inserimento di un elemento in testa.
 *
 * La funzione `clista_in0` crea un nuovo nodo `p` con il valore `v` e lo inserisce in testa
 * alla lista concatenata. Poiché si tratta di una lista **doppiamente concatenata**, ogni nodo
 * contiene due puntatori:
 * - `succ`: che punta al nodo successivo.
 * - `prec`: che punta al nodo precedente.
 *
 * Rappresentazione in memoria:
 * ----------------------------------------------
 * L -> [ v | prec=NULL | succ ] -> [ ... ] -> NULL
 *
 * Dettagli:
 * - `L`: è il puntatore alla testa della lista concatenata.
 * - `[ v | prec=NULL | succ ]`: è il nuovo nodo creato con il valore `v`.
 *   - `prec=NULL`: Indica che non ha un nodo precedente, poiché è il primo elemento della lista.
 *   - `succ`: Punta al nodo che era precedentemente in testa alla lista (`a`).
 * - `[ ... ]`: Rappresenta gli altri nodi della lista concatenata (se esistono).
 * - `NULL`: L'ultimo nodo nella lista ha il puntatore `succ` che punta a NULL.
 *
 * Inserimento in testa:
 * ---------------------
 * Dopo l'esecuzione della funzione, il nuovo nodo `p` diventa la testa della lista (`a = p`).
 *
 * Esempio di sequenza grafica:
 *
 * Prima dell'inserimento:
 * L -> [ dato1 | prec=NULL | succ ] -> [ dato2 | prec | succ ] -> NULL
 *
 * Dopo l'inserimento di `v`:
 * L -> [ v | prec=NULL | succ ] -> [ dato1 | prec | succ ] -> [ dato2 | prec | succ ] -> NULL
 *
 * Dettagli del codice:
 * ---------------------
 * 1. Allocazione dinamica di memoria per il nuovo nodo:
 *    nodo *p = malloc(sizeof(nodo));
 * 2. Inizializzazione del valore `dato` del nuovo nodo:
 *    p->dato = v;
 * 3. Collegamento del nodo al resto della lista:
 *    p->succ = a;  // Il nodo successivo al nuovo nodo è la vecchia testa.
 *    p->prec = NULL;  // Il nodo precedente è NULL, poiché è il primo nodo della lista.
 * 4. Aggiornamento della testa della lista:
 *    a = p;  // La testa della lista ora punta al nuovo nodo.
 */

/*
 * Caso: Cancellazione di un nodo dalla lista doppiamente concatenata.
 *
 * Rappresentazione iniziale della lista:
 *
 * L -> [ dato1 | prec=NULL | succ ] <-> [ dato2 | prec | succ ] <-> [ dato3 | prec | succ ] -> NULL
 *
 * Operazione:
 * - Supponiamo di voler cancellare il nodo contenente `dato2`.
 * - Dopo la cancellazione, il nodo precedente (`dato1`) punterà al nodo successivo (`dato3`) e viceversa.
 *
 * Rappresentazione grafica dopo la cancellazione di `dato2`:
 *
 * L -> [ dato1 | prec=NULL | succ ] <-> [ dato3 | prec | succ ] -> NULL
 *
 * Passaggi della cancellazione:
 * ------------------------------
 * 1. Individuazione del nodo da eliminare:
 *    - Utilizziamo un puntatore per iterare sulla lista e trovare il nodo con `dato2`.
 *
 * 2. Aggiornamento dei puntatori:
 *    - Il puntatore `succ` del nodo precedente (`dato1`) viene aggiornato per saltare il nodo da eliminare
 *      e puntare direttamente al nodo successivo (`dato3`).
 *    - Il puntatore `prec` del nodo successivo (`dato3`) viene aggiornato per saltare il nodo da eliminare
 *      e puntare direttamente al nodo precedente (`dato1`).
 *
 * 3. Deallocazione del nodo:
 *    - Dopo aver aggiornato i puntatori, il nodo contenente `dato2` viene deallocato con `free()`.
 *
 * Codice esemplificativo:
 */
/*
void clista_cancella(clista *a, nodo *da_eliminare) {
    if (da_eliminare == NULL) return; // Se il nodo da eliminare è NULL, non faccio nulla.

    if (da_eliminare->prec != NULL) {
        // Aggiorno il puntatore `succ` del nodo precedente per saltare `da_eliminare`.
        da_eliminare->prec->succ = da_eliminare->succ;
    } else {
        // Se il nodo da eliminare è il primo, aggiorno la testa della lista.
        *a = da_eliminare->succ;
    }

    if (da_eliminare->succ != NULL) {
        // Aggiorno il puntatore `prec` del nodo successivo per saltare `da_eliminare`.
        da_eliminare->succ->prec = da_eliminare->prec;
    }

    free(da_eliminare); // Libero la memoria associata al nodo eliminato.
}
*/
/*
 * Esempio:
 * Supponiamo di avere una lista doppiamente concatenata con 3 nodi:
 *
 * L -> [ dato1 | prec=NULL | succ ] <-> [ dato2 | prec | succ ] <-> [ dato3 | prec | succ ] -> NULL
 *
 * Eseguendo `clista_cancella(&L, nodo_con_dato2)`, otteniamo:
 *
 * L -> [ dato1 | prec=NULL | succ ] <-> [ dato3 | prec | succ ] -> NULL
 *
 * Dettagli grafici:
 * -----------------
 * - Prima della cancellazione:
 *   - `dato1.succ` punta a `dato2`, e `dato2.prec` punta a `dato1`.
 *   - `dato2.succ` punta a `dato3`, e `dato3.prec` punta a `dato2`.
 *
 * - Dopo la cancellazione di `dato2`:
 *   - `dato1.succ` viene aggiornato per puntare direttamente a `dato3`.
 *   - `dato3.prec` viene aggiornato per puntare direttamente a `dato1`.
 *
 * Nota:
 * - Il nodo `dato2` viene scollegato completamente dalla lista e la memoria associata viene liberata.
 */
