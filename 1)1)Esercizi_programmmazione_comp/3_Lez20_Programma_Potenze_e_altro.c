//
// Created by Enzo on 18/01/2025.
//
// 3)Potenze e array


#include <stdio.h>

// in c abbaimo due  modi per definire delle sequenze ossia quello di definire : degli array che sono, dei vettori che hanno una dimensione
// hanno degli elementi  che ognuno di essi nella sequenza ha lo stesso tipo, gli array di char sono stringhe
// con essi si ci si puo' fare poco
// si puo creare un elemento , modificare le stringhe (ps: in python non si puo )
// non si possono ne allungare ne ristringere
// quindi sono piu' statici rispetto alle liste python



/*Scrivere una funzione C avente il seguente prototipo:

    float potenza(float x, int e);
        che ritorna il valore x^e

*/

float potenza(float x, int e);


/*
 *
 * x^e = x *x*x*x ..... *x              E>0
 *-------------------------
 *  E VOLTE
 *
 *  1                                   E=0
 *
 *I/POTENZA(X;E                         E<0
 */
#include <stdio.h> // Inclusione della libreria necessaria per l'input/output, in particolare per la funzione printf
float potenza(float x, int e);
int main() {
    // Test della funzione potenza con vari input per verificarne la correttezza
    printf("%f\n", potenza(2, 4));  // Calcola 2^4 = 16.000000
    printf("%f\n", potenza(2, -4)); // Calcola 2^(-4) = 0.062500
    printf("%f\n", potenza(2, 49)); // Calcola 2^49 (risultato molto grande)
    printf("%f\n", potenza(2, 0));  // Calcola 2^0 = 1.000000

    // Ecco alcuni esempi di come e' formato un array
    int a [10];/* QUESTA E' LA DIMENSIONE DEGLI ARRAY  INDEFINITI */
    int b [6] = {0,1,5,1,2,4}; // come prima cosa gli definisco la lunghezza,array interi definiti

    int c [] = {4,1,4}; // qui invece definisco un'array sensa dirgli di che dimensione e'
    int d [101] = { 0,1,2}; // definisco esplicitamente i primi tre elementi, da d[3] in poi gli elementi sono 0

    // un array di puo anche modificare facendo come qui sotto:
     a [10] = 9 ;


    //dell'array e poi succesivamente i valori dell'array

    // gli array ci consentono di creare un tipo di dato o modificarlo
    /**
     *
     *  ARRAY : SONO UNA SEGUENZA DI ELEMENTI TUTTI DELLO STESSO TIPO, QUI SOPRA ECCO UN ES. DI COME E' FATTO UN ARRAY
     *
     *
     */

    int i = 0;
    while (i < 10 ) { // stampera' da elemento 0 in poi
        printf("%d\n",d[i]);
        i++;
    }

// il for invece ha piu' ho meno la  stessa struttura, l'unica cosa che cambia e'
// che al suo interno si puo' definire una variabile contatore  e che a differenza
// del while che finche' la condizione non e' verificata continua ciclare.
// il for invece, ci sono tre dischiarazioni rispetto a python


    for (i=0; i<10;i++) { // ci sono tre dichiarazioni, la prima definisco i,
            //poi do una condizione fintanto che e' vera , esguo il blocco del for e dopo poi la incremento

        printf("%d\n",d[i]); // stampa gli elementi dell'array da 0 a 10
    }

    /* Entrambi i cicli sono simili, mentre l'utilizzo dipende da cio che bisogna fare, sono equivalenti praticamente */

    return 0; // Termina il programma con successo

}







// Definizione della funzione potenza per calcolare x elevato alla potenza e
float potenza(float x, int e) {


    // Dichiarazione delle variabili
    int pe; // Variabile per l'esponente positivo (necessaria per gestire esponenti negativi)
    float pow = 1; // Variabile che accumula il risultato della potenza

    // Verifica se l'esponente è negativo
    if (e < 0) {
        pe = -e; // Se negativo, prendi il valore assoluto
    } else {
        pe = e; // Se positivo, usalo direttamente
    }

    // Calcolo della potenza tramite moltiplicazioni ripetute
    while (pe > 0) {
        pow *= x; // Moltiplica il risultato corrente per la base x
        pe--;     // Decrementa l'esponente positivo per avvicinarsi allo zero
    }

    // Se l'esponente originale era negativo, restituisci l'inverso della potenza calcolata
    if (e < 0) {
        pow = (1.0)/pow;
    } else {
        return pow; // Altrimenti restituisci il risultato calcolato
    }
}





