/*
#include <stdio.h>
#include <string.h>
*/

/*Programmazione dei calcolatori con laboratorio
26 settembre 2022

Consegna
Fare reply all’email ricevuta allegando i codici C e Python (una unica email con i due sorgenti). I formati ammessi sono:

per Python: .py, .ipynb, export html
per C: .c
NB. Verranno sottratti punti in proporzione ai minuti di ritardo dalla scadenza.

1) C
Si considerino le strutture dati definite dal seguente frammento di codice:
*/



struct point {
    float x, y;
};
typedef struct point point;

struct segment {
    point *a;
    point *b;
};
typedef struct segment segment;



//Si scriva una funzione che abbia il seguente prototipo

segment *new_segment(float ax, float ay, float bx, float by);


void free_segment(segment *s);


int main (){

}



/*e restituisca un puntatore ad un nuovo segment tale che i due point che lo compongono 
abbiano coordinate ax e ay per il primo e bx e by per il secondo.*/