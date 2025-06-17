'''
### 1 Analizza sempre se la domanda riguarda la memoria statica o dinamica
'''
# - Memoria statica → Si riferisce alla dimensione della struttura stessa 
# (misurata con `sizeof()`).

# - Memoria dinamica → Dipende da eventuali allocazioni (`malloc`, `calloc`, `realloc`).
# - Accortezza: Se una struttura contiene solo puntatori, `sizeof()`
#   non misura la memoria occupata dagli elementi puntati.

'''
### 2 Identifica subito il tipo di dati e i suoi effetti sulla complessità
'''
# - Strutture che contengono solo tipi primitivi (int, float, char) → O(1)
# - Strutture con puntatori a dati dinamici (array dinamici, liste collegate) → O(n) 
#                                                          per il contenuto puntato.
# - Accortezza: Non confondere la memoria occupata dalla struttura con la
#   memoria totale usata dal programma.

'''
### 3 Usa il concetto di accesso diretto vs scansione
'''
# - Accesso diretto (esempio: `arr[i]`, `struct.field`, `sizeof()`) → O(1)
# - Scansione completa di una lista o array → O(n)
# - Accortezza: Quando analizzi una funzione, chiediti "quante volte 
#   viene visitato un elemento?".

'''
### 4 Riconosci le strutture dati e le operazioni comuni
'''
# | Struttura Dati  | Accesso | Inserimento  | Cancellazione | Ordinamento |
# |-----------------|---------|--------------|---------------|-------------|
# | Array           | O(1)    | O(n) (shift) | O(n) (shift)  | O(n log n)  |
# | Lista Collegata | O(n)    | O(1) in testa| O(1) in testa | O(n log n)  |
# | Hash Table      | O(1)    | O(1)         | O(1)          | N/A         |
# | Albero Binario  | O(log n)| O(log n)     | O(log n)      | O(n log n)  |
#     Bilanciato 
# - Accortezza: Se la domanda coinvolge operazioni su strutture dati, 
#   chiediti "quale struttura stiamo usando?".

'''
### 5 Controlla se ci sono cicli annidati
'''
# - Singolo ciclo → O(n)
# - Doppio ciclo annidato → O(n²)
# - Ricorsione che dimezza il problema (tipo ricerca binaria) → O(log n)
# - Accortezza: Se il codice ha più cicli, prova a stimare quanti elementi 
#   vengono visitati in totale.

'''
### 6 Memorizza alcune regole di base per `sizeof()`
'''
# - `sizeof(int)` → 4 byte su molti sistemi
# - `sizeof(char)` → 1 byte
# - `sizeof(float)` → 4 byte
# - `sizeof(double)` → 8 byte
# - Strutture con solo puntatori → O(1) (i puntatori occupano memoria fissa)
# - Strutture con array dinamici → Dipende dagli elementi allocati
# - Accortezza: Se hai una struttura con puntatori,
#   `sizeof()` misura solo lo spazio dei puntatori, 
#   non lo spazio effettivamente usato per i dati.

'''
### 7 Fai sempre esempi pratici
'''
# - Se hai un dubbio sulla complessità, scrivi un piccolo programma e stampa `sizeof()`, oppure prova a contare le operazioni eseguite in un ciclo.

# Esempio:
# ```c
# #include <stdio.h>
#
# struct esempio {
#     int a;
#     char b;
#     double c;
# };
#
# int main() {
#     printf("Dimensione struct: %lu bytes\n", sizeof(struct esempio));
#     return 0;
# }
# ```
# - Accortezza: Se vedi padding nella dimensione (`sizeof()` più grande della somma dei membri), la memoria può essere riallineata.

'''
### 8 Controlla sempre il contesto della domanda
'''
# - Se si parla di `sizeof()` → La risposta è sempre O(1).
# - Se si parla di operazioni su una struttura → Dipende da cosa fa il codice.
# - Se si parla di memoria usata → Controlla se ci sono allocazioni dinamiche.

# Seguendo queste accortezze, sarai in grado di rispondere nel modo corretto e di evitare errori di interpretazione. 🚀 Se vuoi approfondire qualcosa, dimmelo!
