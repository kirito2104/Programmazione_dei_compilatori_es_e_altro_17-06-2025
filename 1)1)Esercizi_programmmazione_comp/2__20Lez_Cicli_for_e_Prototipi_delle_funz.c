//
// Created by Enzo on 18/01/2025.
//
// Fond_C/_2)cicli_for_e_prototipi



#include <stdio.h>
/*
 * CONTIENE IL PROTOTIPO DEL FILE PRINTF
 *
 */



//PROTOTIPI DELLA FUNZ
float my_abs(float a);
float my_sqrt(float x, int max_iter  );

char maiuscola_to_minuscola(char c);


int main(void) {
    // si possono dichiarare due variabili nella stessa riga di tipo intero

    int a = 3 , b = 2;
    float c = a/b; // che sarebbe la divisione tra a e b
    //  a/b e' intero perche' a e b lo sono
    // se detro un operazione c'e' un float diventa float anche se ci sono operazioni intere
    //quindi l'int se non viene dichiarato un altro variabile che non sia int, rimane int altrimenti cambia
    // ad es: quando ci sta un float


    // in c se si mette int sulle due variabili che si vogliono dividere
    // anche quella dopo dovras essere di tipo intero

    float d = 1.0 * a / b;
    // 1. L'operazione '1.0 * a / b' viene eseguita come segue:
    //    - '1.0' è un numero in virgola mobile (float), quindi tutta l'espressione
    //      viene promossa al tipo float per evitare il troncamento di valori decimali.
    //    - 'a' e 'b' sono utilizzati nell'operazione di divisione, con 'a / b' calcolato
    //      come divisione tra i due valori.
    //    - Il risultato della divisione viene moltiplicato per '1.0', garantendo che il
    //      valore finale sia trattato come float, anche se 'a' e 'b' fossero interi.
    // 2. Il risultato viene assegnato alla variabile 'd', che conterrà il risultato
    //    della divisione come numero in virgola mobile.

    float e = (a / b) * 1.0;
    // 1. L'operazione '(a / b) * 1.0' viene eseguita come segue:
    //    - Prima viene calcolata la divisione 'a / b'.
    //      Se 'a' e 'b' sono interi, questa divisione viene eseguita come
    //      divisione intera, troncando eventuali decimali.
    //    - Successivamente, il risultato della divisione intera viene moltiplicato per '1.0',
    //      promuovendo il risultato al tipo float.
    // 2. Il risultato finale, in virgola mobile, viene assegnato alla variabile 'e'.


    float f = (float)a/b; // questa sara' un'operazione esplicita', ossia di casting esplicito
    // in modo implicito e' quando viene fatto in modo fatto in maniera automatica e non in modo itenzionale
    /* tipo qui, che viene usato un casting implicito :
     *
     *  float c = a/b
     */

    printf("%f,%f,%f\n",c,d,e);

    printf("radice quadrata di 2: %f\n",2,my_sqrt(2,2));
    printf("radice quadrata di 2 : %f\n",2,my_sqrt(2,200));



    // Questo sara' il ris :1.000000,1.500000,1.000000

    // nelle funz bisogna inidicare anche i parametri, ossia il tipo di ogni funz.
    // In C in rimane tutto uguale tranne la potenza

    /*
     *  Operazini aritmetiche
     *
     *  +, - , * , /, %
     *
     *
     *
     **/

    /*
     *  Operazini relazionali
     *
     *  <, > , == ,<=,>=, !=
     *  minore,maggiore, uguale, min uguale, magg. uguale, diverso
     *
     *
     */

    /*
         *  Operazini logiche
         *
         *  && AND
         *  || OR
         *  ! NOT
         *
         *
         */

     char ch = 'h';
    printf("%c, %c, %c,%c\n",ch, ch +1, ch,ch+1 ); //%c serve per far stampare un carattere, ossia per dirgli che e' un carattere
    // i caratteri vengono codificati attraverso il codice asci, quindi sarebbero degli interi
    // ogni carattere ha quindi un tipo di codifica diversa, in base al tipo di carattere, come anche le maiscole


    //====================================================================================================================================
    printf("%c", maiuscola_to_minuscola(('G'))); // trasformera' in lettera minuscola
    return 0;

}


// in c abbaimo due  modi per definire delle sequenze ossia quello di definire : degli array che sono, dei vettori che hanno una dimensione
// hanno degli elementi  che ognuno di essi nella sequenza ha lo stesso tipo, gli array di char sono stringhe
// con essi si ci si puo' fare poco
// si puo creare un elemento , modificare le stringhe (ps: in python non si puo )
// non si possono ne allungare ne ristringere
// quindi sono piu' statici rispetto alle liste python



float my_sqrt(float x, int max_iter  ) {
    float g = x/2;
    int c =0; // conta il numero di operazioni, che aggiornaniamo all'interno di ogni ciclo


    while (my_abs(g * g - x) > 0.00001 && c< max_iter) { // && sarebbe and
        g = (g + x / g) / 2;
        c++ ;// equivalente a c = C+1 oppure c+=1
    }
    return g ;
}

float my_abs(float a) {
    if (a < 0) {

        return -a;
    } else {

        return a;
    }
}
// IN C QUANDO COME NEL CASO QUI SOPRA SI INVERTONO LE DUE FUNZ DARA' ERRORE PERCHE' VIENE DICHIARATA PIU' SOTTO, QUINDI E' OTTIMALE METTERE
// UN PROTOTIPO DELLA FUNZIONE, PER EVITARE ERRORI : float my_sqrt(float x, int max_iter  );
//

char maiuscola_to_minuscola(char c) {

    if ( c >= 'A'&& c <= 'Z') { // c'e' una lettera maiscola
        int d = c-'A'; // voglio trovare la distanza che c'e tra c e' 'A'
        return 'a' + d; // questa sara' proglietta sul range delle minuscole e questo e cio' che riporto

    }
    return -1 ;// che significa che c'e una anomalia

}

