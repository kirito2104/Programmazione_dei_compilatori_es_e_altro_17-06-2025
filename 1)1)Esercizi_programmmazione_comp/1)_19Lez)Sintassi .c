
// Radice_quadrata_e_altro
#include <stdio.h>




// In c a differenza di python, bisogna compilarlo a differenza di python che viene interpretato
// il c e' compilato ossia che tira fuori un eseguibile
// il main ossia il corpo della funzione a differenzza di python che
// in c un blocco inizia con la parentesi e si conclude con essa, con la graffa
// per andare a capo bisogna usare /n
// abs e' una funzione che calcola una funzione assoluta usando la libreria math
//#include <math.h>

// la variabile in c e' un riferimento in uno spazio di memoria

//======================================================================================================================



// implementazione della funzione abs
// per l'if rimane la stessa sintassi di python l'unica cosa che cambia e' che bisogna mettere i blocco
// lo stesso pure copn else

// In questo caso faccio ritornare un valore float e lo dichiaro anche all'inizio mettendo il float
// a differenza del main che metto un int perche' vorro un valore intero

float my_abs(float a) {
    // 1. La funzione 'my_abs' restituisce il valore assoluto di un numero
    //    in virgola mobile (float) passato come argomento 'a'.

    if (a < 0) {
        // 2. Controlla se il valore di 'a' è negativo.
        //    Se 'a' è minore di zero, il suo valore assoluto è dato
        //    dal numero opposto, quindi restituisce '-a'.
        return -a;
    } else {
        // 3. Se 'a' è maggiore o uguale a zero, il valore assoluto
        //    è il numero stesso, quindi restituisce 'a'.
        return a;
    }

    // Nota: La funzione è semplice e non fa uso di librerie standard come
    //       <math.h>, che fornisce una funzione predefinita 'fabs' per calcolare
    //       il valore assoluto di un numero float. Questo rende la funzione
    //       utile in contesti dove non si vogliono o non si possono usare
    //       librerie esterne.
}



int main(){

    float x = 20 ; /* Dichiarazione ed inizializzazione delle variabili */
    float g ; // dichiaro la variabile g

    g = 5; // inizializzazione separata

    // il while sia in c che python funzionanop allo stesso modo, fin tanto che una condizione e' vera cicla
    // a differenza bisogna mettere le parentesi


     while (my_abs(g * g - x) > 0.00001) {
         // 1. Calcola la differenza tra il quadrato di 'g' e 'x'.
         //    Questa differenza rappresenta quanto l'approssimazione attuale
         //    di 'g' è vicina alla radice quadrata di 'x'.
         //    'my_abs' è una funzione che restituisce il valore assoluto.
         //    La condizione del ciclo controlla se questa differenza è maggiore
         //    di una tolleranza molto piccola (0.00001).
         //    Finché la differenza è maggiore di questa tolleranza, il ciclo continua.

         g = (g + x / g) / 2;
         // 2. Aggiorna il valore di 'g' usando il metodo di Newton-Raphson.
         //    Il metodo approssima iterativamente la radice quadrata di 'x'.
         //    Formula: g = (g + x / g) / 2.
         //    'g' rappresenta l'attuale stima della radice quadrata.
         //    In ogni iterazione, il valore di 'g' si avvicina sempre di più alla
         //    radice quadrata esatta di 'x'.
     }

     // 3. Una volta che il valore assoluto di (g*g - x) è minore o uguale a 0.00001,
     //    il ciclo termina. A questo punto, 'g' è una buona approssimazione della
     //    radice quadrata di 'x'.




    // gli metto %f perche' voglio far ritornare un valore float

    printf(" la radice quadrata di %d e' = %f\n",x, g); // stampa l'ouput
    // quindi facendo cosi' uscira' cosi': la radice quadrata di 20.000000 = 4.472136
     // infatti mettendo %f che sarebbe la dichiarazione della variabile x, gli dico di stamparla e poi di stampare
    // il suo risultato ossia g  che sarebbe il ris, dell main su e della funzione
    // x e' un intero quindi gli andiamo a mettere %d, altrimenti con %f metterebbe anche gli 0
}