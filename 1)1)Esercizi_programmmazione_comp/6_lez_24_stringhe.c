//
// Created by Enzo on 19/01/2025.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h> // include diverse funzioni per le stringhe
/*
    * LE STRINGHE IN C:
 * Una stringa e' una sequenza di caratteri che termina con un carattere speciale, chiamato stringa.
 * In c questa sequenza  e' memorizzata in un array di caratteri, che contiene ad un certo punto  i carattere speciale di fine stringa sara' una stringa
 *  E' un array di char che contiene il carattere di fine stringa
 * */

/*
 * Gli array sono sequenze  di elemenri che hanno la stessa dimensione
 *
 *
 */


int str_len(char *a) // Funzione per calcolare la lunghezza di una stringa
{
    int c = 0; // Inizializza il contatore a 0

    // Itera sulla stringa finché non incontra il terminatore '\0'
    // '\0' indica la fine della stringa in C

    while (a[c] != '\0') // lo incrementiamo fintanto che non incrementiamo il carattere di fine stringa
        c++; // Incrementa il contatore per ogni carattere trovato

    return c; // Restituisce la lunghezza della stringa (escluso '\0')
}/*ha complessita' temporale lineare nella lunghezza della stringa  O(n) */



int str_cmp(char *a,char *b);

int main(){
  /* '\0' CARATTERE DI FINE STRINGA*/
  char  a[] = "Una stringa";   // arry composto dai caratteri mostrati + carattere \0
  // e' un array di char, cosi' e' un'allocazione staitca

    char b0[1000];

    char *b1;
  char stringa_vuota [] = ""; /*l'array contiene \0 in posizione 0*/




  printf("%d\n",sizeof(a)); // i byte sono 12 ossia ogni carattere della stringa, incluso quello di chiusura della stringa
  printf("%s\n",a);
  a[3] = '\0'; // definisce una  stringa "ana"
    // cosi' modifica la stringa , ponendo il caratere di fine stringa alla posizione 3

    printf("%s\n",a); //stampera' una e' il carettere di fine stringa sara' la posiz. 3

    printf("str_len(%s) = %d\n",a,str_len(a)) ; // facendo cosi' dira' la grandezza della stringa e
    printf("str_len(\"%s\") = %d\n",a,str_len(a)); // facendo cosi' stampera' anche gli apici
    // Se a e' = None, quale e' la lunghezza della stringa, la lunghezza
    printf("str_len(\"%s\") = %d\n",a,strlen(a));   /* FUNZIONE DI string */
    // e' otterro' lo stesso risultato di sopra

/* Altre funzioni delle libreria string :*/
    strcpy(b0,a);/* prende la stringa da copiare , copia una stringa dentro un'altra a sua volta, e ritorna il puntatore alla stringa, ci deve essere memoria allocata quindi libera*, sufficiente per contenere la memoria corrente */
    // copia pure il carattere di fine stringa, e la memoria deve essere allocata, se si sovrappongono
    // una copia ossia l'indirizzo di
    printf("str_len(\"%s\") = %d\n",b0,strlen(b0));

    // MEntre qui e' allocata dinamicamente :
    b1 = malloc(sizeof(char)*(strlen(a)+1)); // moltipicato per tutti i caratteri che mi servono, strlen midice di quanti caratteri e' composto, per consentire al carattere di fine stringa
    // deve essere sempre definita, perche potrebbe scrivere  su della memoria non allocata
    strcpy(b1,a); /* HA COSTO TEMPORALE LINEARE NELLA LUNGHEZZA DELLA STRINGA A */

    printf("str_len(\"%s\") = %d\n",b1,strlen(b1));

    char c[] = "programmazione";
    char d[] = "programma";
    char e[] = "prolog";
    printf("%d\n", str_cmp(c,d));
    printf("%d\n", str_cmp(d,e));

}

/*
 * esercizio : scrivere una funzione col seguente prototipo
 *
 * char *clona(che *a)
 *
 * che copia a in una stringa nuova allocata dinamicamente e ne ritorna l'indirizzo
 *
 * ritorna NUll se l'operazione non e' possibile
 */

/*
 * Testare se a e b0 sono uguali: ( solo l'ultimo carattere lo e' )
 *  a e b sono diversi come array ma uguali come stringhe
 *
 *  testare la stringa  e' uguale alla stringa b0
 *
 *  a == b ?? , non funziona perche' conforntiamo i puntatori, ed e' no confronto tra indirizzi sono diversi
 *
 *
 *
 *
*/

//char *clona_stringa(char *a,v );



int str_cmp(char *a,char *b)
{
    /*
     * a e b sono due stringhe , Ritorna -1 se a precede b nell'ordinamento lessicografico
     * ovvero se i e' la prima posizione in cui a e b divergono allora a[i] < b[i]
     *
     * ritorna +1 , nel caso opposto , quando b precede a
     *
     * ritorna  0 quando  a e b sono uguali
     */

                // che ci permette di scorrere tra le stringhe
    int i = 0; // Inizializza un indice per scorrere le stringhe

    // Ciclo che confronta i caratteri di `a` e `b` finché:
    // 1. Non si raggiunge la fine di entrambe le stringhe.
    // 2. I caratteri corrispondenti di `a` e `b` sono uguali.

    while (i < strlen(a) && i < strlen(b) && a[i] == b[i]) // !!!!!!! Attenzione vedere commento sotto

        /* deve quindi rispettare queste tre condizioni i , deve essere piu' piccolo di a e b e poi misura l'indice di i con quello a e di b*/
    {
        i++; // Incrementa l'indice per confrontare il carattere successivo
    }

    // Se sono stati confrontati tutti i caratteri di entrambe le stringhe
    // e i caratteri corrispondenti sono uguali
    if (i == strlen(a) && i == strlen(b))
    {
        return 0; // Le stringhe sono uguali
    }

    // Se si è raggiunta la fine della stringa `a` ma non di `b`
    // significa che `a` è un prefisso di `b`
    if (i == strlen(a))
    {
        return -1; // `a` precede `b`
    }

    // Se si è raggiunta la fine della stringa `b` ma non di `a`
    // significa che `b` è un prefisso di `a`
    if (i == strlen(b))
    {
        return +1; // `b` precede `a`
    }

    // Se i caratteri corrispondenti a `i` di `a` e `b` sono diversi,
    // ritorna -1 o +1 a seconda di quale stringa precede l'altra
    if (a[i] < b[i])
    {
        return -1; // Il carattere di `a` è minore di quello di `b`
    }
    else
    {
        return +1; // Il carattere di `b` è minore di quello di `a`
    }

/*
 *Attenzione !!!
 *
 *Costo' Temporale quadratico  dovuto alle esecuzioni  strlen al'interno del while
 *
 * Come  riparare ??
 *
 * int na = strlen(a), nb = strlen(b)
 *
 * e usare  na e nb dove serve
 *
 * In string c'e' strcmp che fa la stessa cosa
 */


}
 /*
      * Questa funzione confronta due stringhe `a` e `b` e restituisce un valore
      * in base al loro ordinamento lessicografico:
      *
      * - Ritorna -1: se `a` precede `b` nell'ordinamento lessicografico.
      *   Ciò accade se esiste un indice `i` in cui `a[i] < b[i]` o se `a` è un prefisso di `b`.
      *
      * - Ritorna +1: se `b` precede `a` nell'ordinamento lessicografico.
      *   Ciò accade se esiste un indice `i` in cui `a[i] > b[i]` o se `b` è un prefisso di `a`.
      *
      * - Ritorna 0: se `a` e `b` sono uguali, ovvero ogni carattere coincide e le due stringhe
      *   hanno la stessa lunghezza.
      */


















