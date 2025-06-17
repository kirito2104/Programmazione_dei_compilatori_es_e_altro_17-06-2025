// Created by Enzo on 23/01/2025.
#include <stdio.h>
#include <stdlib.h>


// Definizione della struttura 'elemento', che rappresenta un singolo dato nella lista
// Ogni elemento può essere di tipo intero ('i'), float ('f') o stringa ('s')
// 'dato' è un puntatore void che permette di contenere qualsiasi tipo di dato
typedef struct {
    char tipo; /* 'i' per intero; 'f' per float; 's' per stringa */
    void *dato; // Puntatore generico al dato contenuto (che può essere un int, float o char*)
} elemento;

// Struttura che rappresenta una lista dinamica
// La lista è implementata come un array dinamico che può crescere o diminuire
struct lista {
    elemento *a;  // Puntatore a un array di 'elemento'
    int c;        // Capacità attuale dell'array (quanti elementi può contenere senza ridimensionarsi)
    int n;        // Numero di elementi attuali nella lista
};
typedef struct lista lista; // Alias per la struttura lista

// Funzioni dichiarate nel programma
lista init();                      // Funzione per inizializzare la lista
lista append(lista, elemento);     // Funzione per aggiungere un elemento alla lista
void mostra(lista);                // Funzione per visualizzare i contenuti della lista
lista pop(lista);                  // Funzione per rimuovere l'ultimo elemento dalla lista

lista insert(lista, elemento, int );


// Funzioni che creano un elemento specifico di tipo intero, float o stringa
elemento intero(int);
elemento fpoint(float);
elemento stringa(char*);
char cerca_tipo(char *b)
{
    /*
     * Questa funzione determina il tipo di contenuto della stringa `b` e restituisce un carattere
     * rappresentativo del tipo:
     * - Restituisce `'i'` se la stringa contiene solo cifre decimali (quindi rappresenta un numero intero).
     * - Restituisce `'f'` se la stringa contiene solo cifre decimali e **esattamente un punto** ('.'),
     *   il che indica che rappresenta un numero in virgola mobile.
     * - Restituisce `'s'` in tutti gli altri casi (ad esempio, se contiene caratteri non numerici,
     *   più di un punto o altri simboli).
     */

    int i = 0;            // Variabile per scorrere i caratteri della stringa.
    int numero_punti = 0; // Contatore per i punti ('.') trovati nella stringa.

    // Ciclo per analizzare ogni carattere della stringa `b`.
    while (b[i] != '\0')  // Continua finché non si raggiunge il terminatore di stringa '\0'.
    {
        if (b[i] == '.'|| b[i] == ',')  // Controlla se il carattere corrente è un punto ('.').
        {
            if (numero_punti > 0)
            {
                /*
                 * Se è stato già trovato un punto, significa che ci sono più punti nella stringa.
                 * Una stringa con più di un punto non è valida né come numero intero né come float.
                 * Restituisco 's' poiché la stringa non rappresenta un numero valido.
                 */
                return 's';
            }
            else
            {
                /*
                 * Se è il primo punto trovato, lo conto incrementando il contatore `numero_punti`.
                 * La stringa potrebbe ancora essere un numero in virgola mobile.
                 */
                numero_punti++;
            }
        }
        else if (b[i] < '0' || b[i] > '9')
        {
            /*
             * Controlla se il carattere corrente non è una cifra decimale (tra '0' e '9').
             * Se si trova un carattere non numerico (escluso il punto), la stringa non rappresenta
             * né un numero intero né un numero in virgola mobile.
             * Restituisco 's' poiché la stringa contiene caratteri non validi.
             */
            return 's';
        }
        else
        {
            /*
             * Se il carattere corrente è una cifra decimale, si passa al carattere successivo.
             */
            i++;
        }
    }

    /*
     * Dopo aver esaminato tutti i caratteri della stringa, determino il tipo in base al numero di punti trovati:
     */
    if (numero_punti == 0)
    {
        /*
         * Se non ci sono punti nella stringa, significa che la stringa contiene solo cifre decimali
         * e rappresenta un numero intero. Restituisco 'i'.
         */
        return 'i';
    }
    else
    {
        /*
         * Se c'è esattamente un punto nella stringa, significa che contiene cifre decimali
         * e un solo punto. La stringa rappresenta un numero in virgola mobile. Restituisco 'f'.
         */
        return 'f';
    }
}

int main()
{
    lista L = init ();

    char buffer [1024]; // di un kb
    scanf("%s", buffer);
    printf("%c\n", cerca_tipo(buffer));

}

/*
 * La funzione `sscanf` fa parte della libreria standard del linguaggio C (inclusa in <stdio.h>).
 * È una variante della funzione `scanf` e viene utilizzata per leggere dati formattati da una stringa
 * in memoria anziché dall'input standard (come la tastiera).
 *
 * **A cosa serve `sscanf`:**
 * - Serve a **estrarre valori formattati** da una stringa, analizzandola in base a uno specificatore di formato.
 * - È utile quando si desidera ottenere dati già presenti in una stringa e convertirli in variabili di tipo diverso
 *   (ad esempio, interi, float o stringhe).
 * - Permette di processare stringhe di input con un controllo più flessibile rispetto a `scanf`.
 *
 * **Principali differenze rispetto a `scanf`:**
 * - `scanf`: Legge direttamente dall'input standard (es. tastiera).
 * - `sscanf`: Analizza una stringa esistente e ne estrae i valori.
 *
 * **Sintassi di `sscanf`:**
 * ```c
 * int sscanf(const char *str, const char *format, ...);
 * ```
 * - `str`: La stringa sorgente da cui estrarre i dati.
 * - `format`: Una stringa di formato che specifica il tipo e la sequenza dei dati da leggere (es. "%d", "%f").
 * - `...`: Variabili (passate come puntatori) in cui memorizzare i valori estratti dalla stringa.
 * - **Valore di ritorno**: Restituisce il numero di valori letti con successo.
 *   Se non riesce a leggere alcun valore, restituisce 0. Se c'è un errore nella stringa o nei formati, restituisce EOF.
 *
 * **Quando viene usata `sscanf`:**
 * 1. **Parsing di stringhe formattate:**
 *    - Quando è necessario leggere valori specifici da una stringa complessa (ad esempio, estrarre dati numerici da un file o stringhe di log).
 * 2. **Elaborazione di dati ricevuti:**
 *    - Utile per analizzare dati da buffer o stringhe ricevute da un socket, file, o altra fonte di input in memoria.
 * 3. **Situazioni dove non è pratico usare `scanf`:**
 *    - Se i dati sono già in memoria, `sscanf` evita di usare l'input standard, permettendo un controllo più preciso.
 *
 * **Esempio 1: Lettura di numeri da una stringa**
 * ```c
 * char input[] = "123 456";
 * int a, b;
 * sscanf(input, "%d %d", &a, &b); // Legge due interi dalla stringa
 * printf("a = %d, b = %d\n", a, b); // Output: a = 123, b = 456
 * ```
 *
 * **Esempio 2: Parsing di una stringa complessa**
 * ```c
 * char input[] = "(3.14,2.71)";
 * float x, y;
 * sscanf(input, "(%f,%f)", &x, &y); // Legge due float separati da una virgola e racchiusi tra parentesi
 * printf("x = %f, y = %f\n", x, y); // Output: x = 3.140000, y = 2.710000
 * ```
 *
 * **Esempio 3: Estrazione di una sottostringa**
 * ```c
 * char input[] = "Nome: Enzo, Età: 30";
 * char nome[50];
 * int eta;
 * sscanf(input, "Nome: %s, Età: %d", nome, &eta); // Legge una stringa e un intero dalla stringa
 * printf("Nome: %s, Età: %d\n", nome, eta); // Output: Nome: Enzo, Età: 30
 * ```
 *
 * **Vantaggi di `sscanf`:**
 * 1. Analizza i dati direttamente da una stringa senza bisogno di input manuale.
 * 2. Supporta il parsing di formati complessi con grande precisione.
 * 3. Permette di separare la logica di acquisizione e di analisi dei dati.
 *
 * **Limitazioni di `sscanf`:**
 * 1. Come `scanf`, è vulnerabile a errori se i dati non rispettano esattamente il formato specificato.
 * 2. Non è progettata per leggere grandi quantità di dati o stringhe non strutturate.
 * 3. Richiede un'attenzione particolare per evitare buffer overflow (es. specificare la lunghezza massima per `%s`).
 *
 * **Nota sulla sicurezza:**
 * - Quando si usano specificatori come `%s`, specificare sempre la dimensione del buffer per evitare problemi
 *   di sicurezza. Ad esempio:
 * ```c
 * char buffer[10];
 * sscanf(input, "%9s", buffer); // Limita la lettura a 9 caratteri per evitare buffer overflow
 * ```
 */

int main2()
{
    int t, n;
    char buffer [1024]; // di un kb
    t = scanf("%s", buffer); // sara' la stringa sufficientemente grande che dovra' contenere l'intero input
// la funzione sscanf invece di legere gli input da tastiera,  legge una stringa
    // il suo formato e' una stringa, una stringa di formato, poi copiare l'indirizzo dell'intero che ho estrapolato da buffer
    if (sscanf(buffer,"%d",&n) ==1 )
    {
        // se l'output e' 1 allora, l'utente ha inserito un intero
        printf("%s\n", n);
    }
}
// La Funzione SCANF:
/*
 * 'scanf' è una funzione della libreria standard del linguaggio C, inclusa in <stdio.h>,
 * utilizzata per leggere dati formattati dall'input standard (solitamente la tastiera).
 *
 * **Funzionalità principali:**
 * 1. **Lettura di vari tipi di dati:**
 *    - 'scanf' permette di leggere diversi tipi di dati come interi, numeri in virgola mobile,
 *      caratteri e stringhe. Utilizza specificatori di formato per determinare il tipo di dato da leggere.
 *      Ad esempio:
 *        - `%d` per interi (`int`).
 *        - `%f` per numeri in virgola mobile (`float`).
 *        - `%c` per singoli caratteri (`char`).
 *        - `%s` per stringhe (array di `char` terminati da '\0').
 *        - `%lf` per numeri in virgola mobile a doppia precisione (`double`).
 *
 * 2. **Input formattato e parsing:**
 *    - 'scanf' utilizza stringhe di formato che specificano la sequenza e il tipo dei dati da leggere.
 *      Può leggere più valori contemporaneamente, separati da spazi, tabulazioni o a capo.
 *      Ad esempio:
 *        - `scanf("%d %f", &x, &y);` leggerà un intero e un float, separati da uno spazio o un invio.
 *
 * 3. **Assegnazione diretta:**
 *    - I valori letti dall'input vengono automaticamente assegnati alle variabili fornite come argomenti,
 *      utilizzando i loro indirizzi di memoria. Questo è fondamentale: bisogna passare i puntatori
 *      alle variabili (`&variabile`), altrimenti il programma non funzionerà correttamente.
 *
 * 4. **Ritorno del numero di valori letti:**
 *    - 'scanf' restituisce un valore intero che rappresenta il numero di elementi letti con successo.
 *      Questo permette di controllare se l'input è avvenuto correttamente.
 *      Ad esempio:
 *        - `if (scanf("%d", &x) == 1)` verifica che un intero sia stato letto con successo.
 *      - Se il formato dell'input non corrisponde, 'scanf' restituisce un valore inferiore al numero
 *        di specificatori presenti.
 *
 * **Specificatori di formato principali:**
 * - `%d` : Intero decimale con segno.
 * - `%u` : Intero decimale senza segno.
 * - `%f` : Numero in virgola mobile (float).
 * - `%lf`: Numero in virgola mobile a doppia precisione (double).
 * - `%c` : Singolo carattere (inclusi spazi e caratteri speciali).
 * - `%s` : Stringa di caratteri (terminata da '\0', ignora spazi).
 * - `%x` : Intero esadecimale.
 * - `%o` : Intero ottale.
 * - `%p` : Puntatore (stampa o legge l'indirizzo di memoria).
 *
 * **Caratteristiche di 'scanf':**
 * 1. **Separatori predefiniti:**
 *    - 'scanf' utilizza spazi, tabulazioni o a capo come separatori di input.
 *    - Non richiede esplicitamente che l'input sia nello stesso formato visualizzato.
 *      Ad esempio, `scanf("%d %d", &x, &y)` funzionerà correttamente se l'utente inserisce
 *      "10 20", "10\n20" o "10\t20".
 *
 * 2. **Lettura di stringhe:**
 *    - Quando si usa `%s` per leggere stringhe, 'scanf' si ferma al primo spazio, tabulazione o a capo.
 *      Per leggere stringhe contenenti spazi, è necessario usare funzioni come `fgets`.
 *
 * 3. **Sicurezza:**
 *    - 'scanf' non verifica automaticamente i limiti di memoria per tipi di dato come stringhe.
 *      Usare `%s` senza specificare la dimensione del buffer può causare overflow del buffer,
 *      portando a potenziali vulnerabilità di sicurezza.
 *      Ad esempio:
 *        - `char nome[10]; scanf("%s", nome);` può causare problemi se l'utente inserisce
 *          una stringa più lunga di 9 caratteri (10 include il terminatore '\0').
 *      - Per evitare questo problema, è possibile specificare una dimensione massima:
 *        - `scanf("%9s", nome);` legge fino a 9 caratteri e aggiunge '\0'.
 *
 * 4. **Gestione di errori:**
 *    - Se l'input non è nel formato richiesto, 'scanf' fallisce e lascia le variabili
 *      in uno stato non definito.
 *      - Ad esempio, se si usa `%d` ma l'utente inserisce "abc", l'input non sarà interpretato
 *        e la funzione restituisce 0 (nessun valore letto).
 *
 * 5. **Efficienza e semplicità:**
 *    - 'scanf' è rapido e semplice per operazioni basilari di input, ma non è ideale
 *      per operazioni più complesse o per situazioni in cui è necessaria una rigorosa
 *      gestione dell'input.
 *
 * **Esempi di utilizzo:**
 *
 * 1. **Lettura di un singolo valore intero:**
 *    ```c
 *    int x;
 *    printf("Inserisci un numero: ");
 *    scanf("%d", &x); // Legge un intero dall'input e lo assegna a 'x'.
 *    ```
 *
 * 2. **Lettura di più valori di tipi diversi:**
 *    ```c
 *    int x;
 *    float y;
 *    printf("Inserisci un numero intero e un float: ");
 *    scanf("%d %f", &x, &y); // Legge un intero in 'x' e un float in 'y'.
 *    ```
 *
 * 3. **Lettura di una stringa:**
 *    ```c
 *    char nome[20];
 *    printf("Inserisci il tuo nome: ");
 *    scanf("%19s", nome); // Legge una stringa di massimo 19 caratteri in 'nome'.
 *    ```
 *
 * 4. **Verifica dell'input:**
 *    ```c
 *    int x;
 *    printf("Inserisci un numero: ");
 *    if (scanf("%d", &x) == 1) {
 *        printf("Numero inserito correttamente: %d\n", x);
 *    } else {
 *        printf("Errore: input non valido.\n");
 *    }
 *    ```
 *
 * **Considerazioni e limitazioni:**
 * - 'scanf' non è sempre la scelta migliore per gestire l'input, specialmente in situazioni complesse.
 * - Per leggere intere righe di input (inclusi spazi), è consigliabile utilizzare funzioni come `fgets`.
 * - Per garantire la sicurezza, usare sempre controlli sull'input e specificare limiti nei specificatori (%d, %s, ecc.).
 */

int main1 ()
{
    float f0 = 0.0, f1 = 0.0;
    int t;
     /*scanf("%f",&f) ;*/
    // come l;a funzione printf, prende come primo parametro una stringa di formato, ossia una stringa che descrive non come deve essere fatto l'output, ma come l'input deve essere scritto da cio: ""
    // se si vuole scrive un float %f
    // il secondo, terzo , possono  tradurre nei tipi di dato messi nel primo dato
    // bisognera' mettere &, come in questo caso qui sopra per far si che stampi il float

        /**
         * Chiedo all'utente di inserire due numeri separati da una virgola.
         * L'output include una descrizione della formattazione richiesta ("(%%f,%%f)").
         * Le doppie virgolette e i backslash sono necessari per includere i caratteri speciali nella stringa.
         */
        printf("Inserisci un numero: \"(%%f,%%f) \": ");

        /**
         * Uso `scanf` per leggere due numeri in virgola mobile separati esattamente da una virgola.
         * `scanf` si aspetta che l'input dell'utente segua esattamente il formato specificato:
         * un numero, una virgola, e un altro numero.
         * Se l'utente non rispetta questa formattazione (es. non mette la virgola o aggiunge spazi),
         * il parsing fallisce.
         */

         //* Uso `scanf` per leggere due numeri in virgola mobile nel formato specifico con parentesi.
         //* `scanf` si aspetta:
         //* - Un carattere `(` all'inizio.
         //* - Un numero in virgola mobile.
         //* - Una virgola `,`.
         //* - Un secondo numero in virgola mobile.
         //* - Un carattere `)` alla fine.

        t = scanf("(%f,%f)", &f0, &f1);

        /**
         * Controllo il valore di ritorno di `scanf` per verificare se l'input è stato letto correttamente.
         * `scanf` restituisce il numero di valori letti con successo. Se i due numeri sono stati inseriti
         * correttamente, il valore di ritorno sarà 2. Qui, però, controllo solo se è uguale a 1, il che
         * potrebbe essere un errore perché voglio verificare se entrambi i numeri sono stati letti.
         */
        if (t == 2) {
            /**
             * Se almeno un numero è stato letto correttamente (anche se non è la situazione ideale per questo codice),
             * calcolo il prodotto dei due numeri e lo stampo.
             */
            printf("%f * %f = %f\n", f0, f1, f0 * f1);
        } else {
            /**
             * Se il valore di ritorno di `scanf` non è 1, significa che l'input non era nel formato corretto.
             * Stampo un messaggio di errore.
             */
            printf("Formato errato\n");
        }


    /* questo sara' il risultato , del codice compilato:
     *Inserisci un numero: "(%f,%f) ":(3.5,2.1)
     *3.500000 * 2.100000 = 7.349999*/

    return 0;
}




















/*
=======================================================================================================================================================================================================================================================================================
 */




int main0(){
    lista L = init(); // Inizializzazione della lista vuota

    // Aggiunta di vari elementi alla lista con tipi misti (intero, float, stringa)
    L = append(L, intero(10));
    L = append(L, fpoint(3.14));
    L = append(L, stringa("programma"));
    L = append(L, fpoint(2.71));
    L = append(L, stringa("lista"));
    L = append(L, intero(7));

    // Aggiunta di altri elementi per testare la lista con diversi tipi
    L = append(L, intero(10));
    L = append(L, fpoint(3.14));
    L = append(L, stringa("programma"));
    L = append(L, fpoint(2.71));
    L = append(L, stringa("lista"));
    L = append(L, intero(7));

    // Mostra la lista corrente
    mostra(L);
	L = insert(L, stringa("nuovo elemento 0"), 4 );
    L = insert(L, stringa("nuovo elemento 1"), 0 );
    L = insert(L, stringa("nuovo elemento 2"), 1000 );

    mostra(L);



    /*
    // Popolare la lista rimuovendo un elemento alla volta fino a quando non è vuota
    while(L.n > 0){
        L = pop(L);  // Rimuove l'ultimo elemento
        mostra(L);   // Mostra la lista aggiornata
    }*/
}

// Funzione di inizializzazione della lista
// Restituisce una lista vuota con dimensioni iniziali 0
lista init(){
    lista lista_vuota = {NULL, 0, 0};  // Inizializzazione con array NULL, capacità 0 e numero di elementi 0
    return lista_vuota;
}

// Funzione per aggiungere un elemento alla lista
// Se la lista è piena, raddoppia la sua capacità usando realloc
lista append(lista L, elemento e){
    if (L.n == L.c) {  // Se la lista è piena (numero di elementi == capacità)
        L.c = 2*(L.c + 1); // Raddoppia la capacità della lista
        L.a = realloc(L.a, L.c * sizeof(elemento)); // Rialloco la memoria per il nuovo array più grande
    }

    L.a[L.n] = e;  // Aggiunge l'elemento alla fine della lista
    L.n++;         // Incrementa il numero di elementi

    return L;
}


lista insert(lista L , elemento e , int p ){
    // aumento la dimensione dell'array poi sposto tutti gli elementi di i a destra e poi, inserisco il nuovo elemnto in i
    // possiamo usare la funzione append come strumento per insert
    int i;
	if (p < 0){
 		p = 0 ;
    }
    // Utilizzo la funzione append per aggiungere l'elemento alla fine della lista.
    // Questo passaggio gestisce anche il possibile aumento della capacità dell'array se la lista è piena.
    // In altre parole, se la capacità attuale della lista non è sufficiente per contenere un elemento in più,
    // la funzione append raddoppia la capacità dell'array e copia i vecchi elementi nel nuovo array più grande.
    L = append(L, e); // facendo così significa che si trova qui, risolve tutti i problemi di memoria

    // Dopo aver aggiunto l'elemento alla fine della lista, iniziamo a spostare gli elementi per fare spazio alla posizione desiderata 'p'.
    // Il ciclo for inizia dall'ultimo elemento inserito (ora alla posizione L.n-1, che è l'indice dell'elemento appena aggiunto)
    // e continua fino a quando non raggiunge la posizione 'p'. In ogni iterazione, l'elemento corrente viene spostato a destra.
    for (i = L.n-1; i > p; i--) { // i sarà la posizione di e
        // si scambia l'elemento in posizione i con i in -1
        L.a[i] = L.a[i-1]; // sposto a sinistra tutti gli elementi in posizione nell'elemento in posiz -1

        L.a[p] = e; /* Inserisco 'e' in posizione 'p' ad ogni iterazione per garantire che 'e' sia presente in 'p'
                 * anche se il ciclo viene interrotto prematuramente. Questo assicura che 'e' sia almeno
                 * inserito in 'p' una volta, a prescindere da eventuali interruzioni o errori durante l'esecuzione. */
    }

    // Dopo aver fatto spazio, inseriamo l'elemento 'e' nella posizione 'p'.
    // Questo passaggio sovrascrive l'elemento che era precedentemente spostato in quella posizione durante l'ultimo ciclo del for.

    return L;
}

// complessita' temporale : O(l.n - p) e quindi  O(n) nel caso peggiore
// Complessita'


/*Analisi del processo e delle scelte di implementazione:

Gestione della memoria: Utilizzi append per aggiungere un elemento alla lista prima di effettivamente inserirlo nella posizione desiderata.
Questo approccio è efficiente in termini di gestione della memoria poiché ti assicuri che ci sia spazio sufficiente nella lista per un nuovo
elemento senza dover riallocare e copiare manualmente gli elementi ogni volta.

Spostamento degli elementi: Il ciclo for che sposta gli elementi è essenziale per mantenere l'ordine corretto degli elementi dopo l'inserimento.
Sposti ogni elemento di una posizione a destra fino a raggiungere la posizione dove deve essere inserito il nuovo elemento.
Questo metodo è comune quando si lavora con array dinamici.

Inserimento diretto: Una volta che hai creato spazio nella posizione desiderata, inserisci direttamente il nuovo elemento.
Questo è un passaggio critico perché assicura che l'elemento sia collocato esattamente dove l'utente desidera.

La funzione è progettata per essere robusta e gestire automaticamente le questioni di capacità dell'array,
il che è vantaggioso per evitare errori di overflow dell'array e per semplificare
l'uso della funzione insert in vari contesti.
*/


// Funzione per visualizzare gli elementi della lista
// La funzione stampa ogni elemento a seconda del suo tipo
void mostra(lista L){
    int i;

    printf("==================================\n");

    // Itera su tutti gli elementi nella lista e li stampa
    for(i = 0; i < L.n; i++){
        // A seconda del tipo dell'elemento, stampa il dato in modo appropriato
        switch(L.a[i].tipo) {
            case 'i': // Se l'elemento è di tipo intero
                printf("%d\n", *((int*)L.a[i].dato));
                break;
            case 'f': // Se l'elemento è di tipo float
                printf("%f\n", *((float*)L.a[i].dato));
                break;
            case 's': // Se l'elemento è di tipo stringa
                printf("%s\n", (char*)L.a[i].dato);
                break;
        }
    }

    // Stampa la dimensione attuale e la capacità della lista
    printf("dimensione %d, capacita' %d\n", L.n, L.c);
}

// Funzione per rimuovere l'ultimo elemento dalla lista
// Se la lista è troppo vuota, la capacità viene ridotta
lista pop(lista L){
    if(L.n > 0){
        L.n--;  // Riduce il numero di elementi nella lista
        if (L.n < L.c / 4){ // Se la lista è meno di un quarto della sua capacità
            L.c = L.c / 2; // Riduce la capacità della lista
            L.a = realloc(L.a, L.c * sizeof(elemento)); // Rialloco la memoria per il nuovo array più piccolo
        }

        // Se l'elemento rimosso è un tipo non stringa (int o float), libero la memoria associata al dato
        if (L.a[L.n].tipo != 's')
            free(L.a[L.n].dato);
    }
    return L;
}

// Funzione per creare un elemento di tipo intero
// Alloca memoria per un intero, lo imposta con il valore dato e restituisce l'elemento
elemento intero(int d){
    elemento e = {'i', NULL};

    e.dato = malloc(sizeof(int)); // Allocazione della memoria per un intero
    *((int*)e.dato) = d;          // Imposta il valore dell'intero

    return e;
}

// Funzione per creare un elemento di tipo float
// Alloca memoria per un float, lo imposta con il valore dato e restituisce l'elemento
elemento fpoint(float d){
    elemento e = {'f', NULL};

    e.dato = malloc(sizeof(float)); // Allocazione della memoria per un float
    *((float*)e.dato) = d;          // Imposta il valore del float

    return e;
}

// Funzione per creare un elemento di tipo stringa
// Restituisce un elemento con il puntatore alla stringa passata come argomento
elemento stringa(char *d){
    elemento e = {'s', NULL};

    e.dato = d; // La stringa viene passata direttamente senza bisogno di allocare memoria

    return e;
}
