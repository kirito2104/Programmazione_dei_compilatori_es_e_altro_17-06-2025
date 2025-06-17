

#include <stdio.h>
#include <stdlib.h>


/*Tutti nel caso peggiore*/

//                         Ricerca per posiziz.                Pop e Append                 inserimento e Cancellazione                                  Ricerca(di una chiave)
//                                                                                                                                                     dato un elemento,dire o meno
//                                   W.c                          W.c                                                                                     se appartiene alla lista
// Liste(array dinamici)|           O(1)        |                O(n)                   |                       O(n)                            |               O(n) operazioni                   |
//                      |                       |        se eseguo n operazioni         |               nel caso peggiore                       | quindi la chiave non  appartiene alla lista     |
//                      |                       |(ce ne puo'esere uno che costa n append|              (per entrambi i casi )                   | Confrontare quindi ogni elemento con la lista   |
//                      |                       |       [ nel caso del realloc ]        |    (tutti gli elemnti alla destra saranno traslati    |                                                 |
//                      |                       |     ( In media costa temp costanete ) |             nel caso della cancellazione)             |                                                 |
//                      |                       |                                       |                                                       |                                                 |
//                      |                       |                                       |-------------------------------------------------------|-------------------------------------------------|
//                      |                       |                                       |  IL costo della lista nel caso medio:                 |                                                 |
//                      |                       |                                       |   saranno tutti gli 'n' che variano da p              |                                                 |
//                      |                       |                                       |   sommando tutti i costi dellóperazione               |                                                 |
//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
//                      |                       |                                       |                                                       |                                                 |
//                      |                       |                                       |                                                       |                                                 |
// Dizionari            |          /            |                 /                     |                    O(n) Nel caso medio                |             O(n) Nel caso medio                 |
//                      |                       |                                       |                                                       |                                                 |
//                      |                       |                                       |                                                       |                                                 |
//                      |                       |                                       |                                                       |                                                 |
//                      |                       |                                       |                                                       |                                                 |
//                      |                       |                                       |                                                       |                                                 |


// Calcoli e altro lez. :
// Nel caso di una lista dinamica nel caso medio :
// -----------------------------------------------------------------------------
// INSERT (L, e, p)
// -----------------------------------------------------------------------------
// - **Descrizione:** La complessità di inserire un elemento `e` nella lista `L`
//   alla posizione `p` dipende dal numero di elementi che devono essere spostati
//   per fare spazio al nuovo elemento.
// - **Formula:**
//   La complessità per un'operazione di inserimento è data da:
//       c * (n - p)
//   dove:
//       c: è il costo costante per spostare un singolo elemento.
//       n - p: è il numero di elementi da spostare (dalla posizione `p` fino
//              alla fine della lista di lunghezza `n`).
//
// -----------------------------------------------------------------------------
// - Somma totale dei costi (più operazioni):
//   Quando vengono eseguite molteplici operazioni di inserimento, possiamo
//   calcolare il costo totale sommando i costi per ogni inserimento:
//       Σ(costi) = c * Σ(p=0 to n) (n - p)
//   dove la somma Σ(n - p) rappresenta il numero totale di spostamenti
//   necessari per inserire in ogni posizione `p`.
//
// -----------------------------------------------------------------------------
// - Espansione della somma:
//   Espandiamo il termine (n - p):
//       Σ(costi) = c * Σ(p=0 to n) (n - p)
//   Cambiamo l'indice di somma per semplificare il calcolo:
//       Σ(costi) = c * Σ(i=0 to n) i
//   (dove i = n - p).
//
// -----------------------------------------------------------------------------
// - Calcolo della somma:
//   La somma dei numeri da 1 a n è una somma aritmetica:
//       Σ(i=0 to n) i = (n * (n + 1)) / 2
//
// -----------------------------------------------------------------------------
// - Costo totale:
//   Sostituendo nella formula:
//       Σ(costi) = c * (n * (n + 1)) / 2
//
// -----------------------------------------------------------------------------
// - Costo medio:
//   Per calcolare il costo medio per un'operazione, dividiamo il costo totale
//   per il numero di operazioni `n`:
//       costo medio = Σ(costi) / n
//                   = (c * (n * (n + 1)) / 2) / n
//   Semplificando:
//       costo medio = c * (n + 1) / 2
//
// -----------------------------------------------------------------------------
// - Conclusione:
//   - Per grandi `n`, il costo medio si approssima a:
//         costo medio ≈ c * (n / 2)
//   - **Caso medio:** La complessità media di un'operazione `insert` è
//     proporzionale alla lunghezza della lista (O(n)).
//   - **Caso peggiore:** Inserire all'inizio della lista richiede di spostare
//     tutti gli elementi (n).
//
// -----------------------------------------------------------------------------
// CANCELLAZIONE
// -----------------------------------------------------------------------------
// - **Descrizione:** La complessità di rimuovere un elemento dalla lista
//   dipende dal numero di elementi da spostare per riempire lo spazio lasciato
//   vuoto.
// - **Formula:**
//   La complessità per un'operazione di cancellazione è data da:
//       c * (n - p)
//   dove:
//       c: è il costo costante per spostare un singolo elemento.
//       n - p: è il numero di elementi da spostare (dalla posizione `p` fino
//              alla fine della lista di lunghezza `n`).
//
// -----------------------------------------------------------------------------
// - Somma totale dei costi (più operazioni):
//   Quando vengono eseguite molteplici operazioni di cancellazione, il costo
//   totale è simile a quello dell'inserimento:
//       Σ(costi) = c * Σ(p=0 to n) (n - p)
//
// -----------------------------------------------------------------------------
// - Costo medio:
//   Analogamente al caso dell'inserimento:
//       costo medio = c * (n + 1) / 2
//
// -----------------------------------------------------------------------------
// - Conclusione per cancellazione:
//   - **Caso medio:** La complessità media di una cancellazione è O(n).
//   - **Caso peggiore:** Rimuovere il primo elemento richiede di spostare
//     tutti gli elementi successivi (n).
// -----------------------------------------------------------------------------





/**
 * Ecco una spiegazione approfondita sulla complessità delle operazioni elencate per
 * **liste implementate come array dinamici**:
 *
 * 1. Ricerca per posizione: O(1)
 * ---------------------------------
 * - **Descrizione:**
 *   - Quando si accede a un elemento in una lista (array dinamico) tramite il suo indice,
 *     come in `lista[i]`, l'accesso è diretto.
 *   - Questo avviene perché la memoria degli array è contigua, quindi l'indirizzo di un elemento
 *     può essere calcolato immediatamente utilizzando la formula:
 *       indirizzo_elemento = indirizzo_base + (indice * dimensione_elemento)
 *   - Non è necessario iterare sugli elementi per trovare quello richiesto.
 * - **Complessità:**
 *   - Poiché l'accesso è diretto e calcolabile con un'operazione aritmetica,
 *     la complessità è **O(1)** (tempo costante).
 *
 * 2. Pop e Append: O(n) nel caso peggiore, ma O(1) in media
 * ----------------------------------------------------------
 * - **Append:**
 *   - Aggiungere un elemento alla fine di una lista è generalmente un'operazione a tempo costante (**O(1)**),
 *     perché l'elemento viene semplicemente aggiunto alla fine dell'array.
 *   - **Caso peggiore:**
 *     - Se l'array dinamico ha raggiunto la sua capacità massima, deve essere riallocato. Durante la riallocazione:
 *         1. Viene allocato un nuovo array più grande (generalmente il doppio della capacità attuale).
 *         2. Tutti gli elementi dell'array originale vengono copiati nel nuovo array.
 *     - Questa operazione di riallocazione ha complessità **O(n)**, dove `n` è il numero di elementi presenti nell'array.
 *   - **In media:**
 *     - La riallocazione non avviene ad ogni operazione di `append`. Di solito, avviene solo quando l'array
 *       si riempie completamente.
 *     - Quindi, il costo della riallocazione è "ammortizzato" su molte operazioni di `append`.
 *       In media, ogni operazione costa tempo costante **O(1)**.
 *
 * - **Pop:**
 *   - Rimuovere l'ultimo elemento di una lista è un'operazione a tempo costante (**O(1)**),
 *     poiché non è necessario spostare altri elementi. Si riduce semplicemente la dimensione logica della lista.
 *
 * 3. Inserimento e Cancellazione: O(n) nel caso peggiore
 * ------------------------------------------------------
 * - **Inserimento:**
 *   - Per inserire un elemento in una posizione specifica all'interno di un array dinamico, è necessario:
 *       1. Spostare tutti gli elementi a destra della posizione di inserimento per fare spazio al nuovo elemento.
 *       2. Questo richiede un numero di operazioni proporzionale al numero di elementi da spostare.
 *     - **Caso migliore:** Inserire un elemento alla fine richiede **O(1)**, se non è necessario riallocare.
 *     - **Caso peggiore:** Inserire un elemento all'inizio richiede di spostare tutti gli `n` elementi già presenti
 *       (complessità **O(n)**).
 *
 * - **Cancellazione:**
 *   - Rimuovere un elemento da una posizione specifica richiede:
 *       1. Spostare tutti gli elementi a destra di quella posizione per riempire lo spazio lasciato vuoto.
 *       2. Questo richiede un numero di operazioni proporzionale al numero di elementi da spostare.
 *     - **Caso migliore:** Rimuovere l'ultimo elemento richiede **O(1)**.
 *     - **Caso peggiore:** Rimuovere il primo elemento richiede di spostare tutti gli `n-1` elementi (complessità **O(n)**).
 */

/*
 * 4.**Ricerca generica di na chiave
 * ----------------------------------------------------
 * - **Ricerca di una chiave generica: O(n)**
 *   - Quando si cerca un elemento in una lista dinamica senza conoscere la sua posizione (es. "l'elemento X appartiene?"),
 *     è necessario confrontare ogni elemento della lista con il valore cercato.
 *   - Questo richiede di iterare su tutti gli elementi della lista fino a trovare il valore (o confermare che non esiste).
 *     - **Caso migliore:** Se l'elemento si trova al primo posto, richiede **O(1)**.
 *     - **Caso peggiore:** Se l'elemento non esiste, è necessario confrontare tutti gli `n` elementi della lista.
 *   - **Complessità:** **O(n)**.



 * Riepilogo delle complessità
 * ------------------------------------------------------
 * | Operazione               | Complessità             | Note                                                                                           |
 * |--------------------------|-------------------------|------------------------------------------------------------------------------------------------|
 * | **Ricerca per posizione**| **O(1)**                | Accesso diretto grazie all'indirizzamento in memoria contigua.                                 |
 * | **Append**               | **O(1)** in media       | Può essere **O(n)** durante la riallocazione, ma il costo è ammortizzato.                      |
 * | **Pop (ultimo elemento)**| **O(1)**                | Rimuove semplicemente l'ultimo elemento.                                                       |
 * | **Inserimento**          | **O(n)** nel peggiore   | Richiede lo spostamento di elementi per fare spazio al nuovo elemento.                         |
 * | **Cancellazione**        | **O(n)** nel peggiore   | Richiede lo spostamento di elementi per chiudere lo spazio lasciato vuoto.                     |
 *
 * Approfondimento sulla riallocazione e costo ammortizzato
 * ---------------------------------------------------------
 * - Quando la capacità dell'array è esaurita, viene effettuata una riallocazione. La nuova capacità dell'array
 *   è generalmente il doppio di quella precedente.
 * - Esempio:
 *     1. Inizialmente, la capacità dell'array è 4. Inserisco 5 elementi.
 *     2. Quando il quinto elemento viene inserito:
 *         - Viene creato un nuovo array di capacità 8.
 *         - Gli elementi del vecchio array vengono copiati nel nuovo array (costo **O(4)**).
 *     3. Nei successivi 3 inserimenti, non sarà necessario riallocare.
 *
 * - **Costo totale di n operazioni `append`:**
 *   - La riallocazione avviene solo per capacità crescenti: 1, 2, 4, 8, ... fino a `n`.
 *   - Il costo totale delle copie è:
 *       1 + 2 + 4 + 8 + ... + n = 2n - 1
 *   - Dividendo per il numero totale di operazioni, il costo medio per operazione è **O(1)**.
 *
 * Questo dimostra perché la complessità di `append` è **O(1) in media**, ma **O(n)** nel caso peggiore.
 */
//###################################################################################################################################################################################################################################################################

 /*
 * - **Ricerca di una chiave generica: O(n)**
 *   - Quando si cerca un elemento in una lista dinamica senza conoscere la sua posizione (es. "l'elemento X appartiene?"),
 *     è necessario confrontare ogni elemento della lista con il valore cercato.
 *   - Questo richiede di iterare su tutti gli elementi della lista fino a trovare il valore (o confermare che non esiste).
 *     - **Caso migliore:** Se l'elemento si trova al primo posto, richiede **O(1)**.
 *     - **Caso peggiore:** Se l'elemento non esiste, è necessario confrontare tutti gli `n` elementi della lista.
 *   - **Complessità:** **O(n)**.
 *
 * ===================================================================================================
 * DIZIONARI
 * ===================================================================================================
 * - **Ricerca di una chiave (accesso o verifica esistenza):**
 *   - I dizionari in Python sono implementati come **tabelle hash**.
 *     - Ogni chiave è mappata a una posizione nella memoria utilizzando una funzione di hashing.
 *     - Questo permette di accedere al valore associato alla chiave in tempo costante, nella maggior parte dei casi.
 *
 *   - **Caso medio: O(1)**
 *     - La funzione di hashing distribuisce uniformemente le chiavi, e il valore può essere trovato direttamente.
 *   - **Caso peggiore: O(n)**
 *     - Se ci sono **collisioni** nella tabella hash (più chiavi che vengono mappate alla stessa posizione),
 *       può essere necessario cercare linearmente tra le chiavi con la stessa posizione hash.
 *     - Questo avviene raramente, poiché i dizionari ridimensionano automaticamente la tabella hash per ridurre
 *       le collisioni.
 *   - **Complessità:**
 *     - **Caso medio:** **O(1)**.
 *     - **Caso peggiore:** **O(n)** (ma raro).
 *
 * ===================================================================================================
 * RIEPILOGO COMPLESSITÀ
 * ===================================================================================================
 * | Struttura dati             | Ricerca per posizione | Pop e Append      | Inserimento e Cancellazione | Ricerca di una chiave                    |
 * |----------------------------|-----------------------|-------------------|-----------------------------|------------------------------------------|
 * | **Liste (array dinamici)** | **O(1)**              | **O(n)**          | **O(n)** nel caso peggiore  | **O(n)** nel caso peggiore               |
 * | **Dizionari**              | **N/A**               | **N/A**           | **O(1)** in media           | **O(1)** in media, **O(n)** nel peggiore |
 *
 * ===================================================================================================
 * APPROFONDIMENTO SUI DIZIONARI E FUNZIONI HASH
 * ===================================================================================================
 * - **Funzione hash:**
 *   - I dizionari utilizzano una funzione hash per calcolare una posizione basata sulla chiave.
 *   - Ad esempio, se la chiave è una stringa, la funzione hash converte la stringa in un valore numerico
 *     e lo mappa a una posizione nella memoria.
 *
 * - **Collisioni:**
 *   - Quando due chiavi diverse producono lo stesso valore hash, si verifica una collisione.
 *   - Le collisioni vengono risolte utilizzando tecniche come:
 *     - **Catene (chaining):** Memorizzare tutte le chiavi con lo stesso hash in una lista.
 *     - **Indirizzamento aperto:** Cercare un'altra posizione disponibile nella tabella hash.
 *
 * - **Ridimensionamento automatico:**
 *   - Quando la tabella hash diventa troppo piena (fattore di carico alto), viene ridimensionata
 *     (generalmente raddoppiando la capacità) e tutti gli elementi vengono reinseriti.
 *   - Questo assicura che le collisioni rimangano basse e il tempo medio rimanga costante (**O(1)**).
 *
 * ===================================================================================================
 */
//##########################################################################################################################################################################################################################################################################
/*
 *
 * ===================================================================================================
 * DIZIONARI (Tabelle hash)
 * ===================================================================================================
 *
 *
 *
 * - **Inserimento e aggiornamento:**
 *   - Aggiungere o aggiornare un valore associato a una chiave richiede il calcolo dell'hash e,
 *     in caso di collisioni, la gestione tramite chaining o probing.
 *     - **Caso medio:** **O(1)**.
 *     - **Caso peggiore:** **O(n)**, in caso di molte collisioni.
 *
 * - **Cancellazione:**
 *   - Per eliminare un elemento, è necessario:
 *     1. Calcolare l'hash della chiave.
 *     2. Rimuovere la chiave e il valore associato.
 *   - Complessità: **O(1)** in media, **O(n)** nel caso peggiore (collisioni).
 *
 * - **Ricerca di una chiave:**
 *   - I dizionari in Python utilizzano una funzione hash per calcolare una posizione basata sulla chiave.
 *     Questo consente di accedere direttamente al valore associato alla chiave.
 *     - **Caso medio:** **O(1)**, grazie alla funzione hash e alla distribuzione uniforme.
 *     - **Caso peggiore:** **O(n)**, se ci sono molte collisioni (ad esempio, tutte le chiavi mappate alla stessa posizione).
 * ===================================================================================================
 * RIEPILOGO COMPLESSITÀ
 * ===================================================================================================
 * | Struttura dati         | Ricerca per posizione | Pop e Append      | Inserimento e Cancellazione | Ricerca di una chiave                    |
 * |------------------------|-----------------------|-------------------|-----------------------------|------------------------------------------|
 * | **Liste (array dinamici)** | **O(1)**            | **O(1)** in media | **O(n)** nel caso peggiore  | **O(n)** nel caso peggiore               |
 * | **Dizionari**          | **N/A**              | **N/A**           | **O(1)** in media           | **O(1)** in media, **O(n)** nel peggiore |
 *
 * ===================================================================================================
 * APPROFONDIMENTO SUI DIZIONARI E FUNZIONI HASH
 * ===================================================================================================
 * - **Funzione hash:**
 *   - Una funzione hash converte la chiave in un valore numerico che viene utilizzato per calcolare la posizione
 *     nella tabella.
 *   - Se due chiavi producono lo stesso valore hash, si verifica una collisione.
 *
 * - **Collisioni:**
 *   - Le collisioni vengono gestite tramite tecniche come:
 *     - **Chaining:** Memorizzare più chiavi in una lista collegata alla stessa posizione.
 *     - **Probing:** Cercare una nuova posizione libera nella tabella hash.
 *
 * - **Ridimensionamento dinamico:**
 *   - Quando la tabella hash diventa troppo piena, viene ridimensionata (generalmente raddoppiando la capacità).
 *     Questo riduce le collisioni e mantiene la complessità media di accesso costante.
 *
 * ===================================================================================================
 */



// Dizionari
//contengono delle coppie, composte
// - Una struttura contenente coppie ( key,values)
// - le chiavi sono univoche, (ko,vo) e (k,v) sono appartengono a D  sono uguale  ko, k , le chiavi sono univoche
// - il dizionario : ha una  e'una mappa  uguale ai valori k -> v
// le operazioni sono :
// - di aggiornamento (k,v) -> D { ci sono  due possibili casi : - se k gia'appartiene  al dizionario allora -> il suo valore di k  e'v
//                                                              - se invece k non appartiene al dizionario : allora aggiungiamo la nuova coppia al dizionario (k,v)
// k e D ricerca
// Rimuove ka da i  : { - se k appartiene a d rimuovi la coppia (k,v)
//                      - altrimenti nulla

/*
* Assunzioni
 * - le chaivi  sono stringhe (che sono una sequenza di byte e caratteri) : non perdo di generalita' perche' e'' di lunghezza arbitraria , ossia che possono essere qualunque cosa
 * - i valori sono interi
 * -
 * */

/*Indice
* - creo una relazione 1 a 1 tra chiavi e indici di un array(ossia che associo in maniera univoca una posizione)
 * - allora creo un array al quale corrisponde 1 e solo un chiave
 *      |         |
 *    O |---------|
 *      |         |            a p corrisonde una  ed una sola chiave k
 *      |         |
 *      |         |         ricerca vertice del valore  di d[p] in O(1) nel caso peggiore
 *    p |---------|     se corrisonde risonde True, in caso contrario False d[p]
 *      |         |
 *      |         |
 *  m-1 |         |
 *
 * d deve contendere tutte le stringhe di lunghezza composte da n byte  (10 btye = 80 byte)
 *
 * assumiamo che le chiavi siano composte da 10 byte ->  quale e'numero delle possibili chiavi  e' 80 btye
 *
 *   1 tera e'2 alla 40 (2^40)
 *  */


// eliminiamo il rapporto 1 a 1 tra le chaivi e  definiamo  il valore di m in numero frattabile -> cio'implica che su una posizione potranno ricadere chiavi
/*          0 |         |
              |         |
              |         | { potranno confluire diverse chivi  , in questo caso avro'un conflitto quando piu'chiavi ricadono nello stesso indice
           p  |---------|           d[p] contiene un insieme  di elemnti del dizionario
              |         |
          m-1 |---------|

sie m la dimensione dellárray d  "n il numero di elemnti (di chivi ) del dizionario "

-> allora le chiavi saranno distribuite in maniera uniforme tra tutti gli elmenti dell'array

-> Indice [p] ricerca in media  n/m chiavi
la ricerca avra' costo  O(1) costante per ottenere p  + costo O(n/m) per trovare k nellínsieme delle chiavi in d[p]

- n/m e'costante se n e' uguale ad una costane ad m ( n = c m )

deve garantire  che da k e' una potenziale chiave, la funzione  che da k calcola la posiz. p in cui deve trovarsi , k deve avere costo O(1)

h(k, m) ->  p  hash
o < p< m-1

           |     |
           |     |
h(k) -> p  |-----|  -> insiemi (k,v) delle chiavi k tale che h(k) = p
           |     |
           |     |

Se línsieme e'piccolo, non ci interessa che sia implentato bene nella ricerca ma che faccia una ricerca lineare



 */

































