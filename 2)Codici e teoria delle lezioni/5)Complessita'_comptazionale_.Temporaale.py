
#Complessita' computazionale:

# possiamo assumere che ogni op elemtare richiede un costo di tempo,


#  costante ossia che va comparato ad una grandezza presa in considerazione nell'input
#nel caso di un stringa va presa in considerazione la lunghezza della stringa dei suoi cvaratteri 

# I nostri algortmi devo essere efficienti per input elevati 

#se l'input e' grande ed ho una funz. del tempo ossia delle operazioni che e' composta da termini sommati tra di essi 
#dove possono comparire un quadrato della lunghezza della stringa ,uno con cui compare il termine semplice lineare 
#della stringa l'input compare 

# se il termine  e' dato dda un termine di funzioni , mateniamo con noi soltanto la funzione piu' grande 
#ossia quella che cresce piu' velocemente 





# una volta levate tute le costanti additivi che sono di ordine inferiori 
# rispetto al massimo avro' un termine dove compare che puo' essere moltiplicaro da una costante 

# se un operazione invece di vale in modo costante , a noi interessa come cresce la funzione 

# QUINDI QUAALQUE SIAA IL VALORE RESTITISCE SEMPRE N 
 

#==============================================================================================================================

#ECCO TUTTO CIO SCRITTO PRECEDENTEMENTE IN MODO MIGLIORE 


# Complessità computazionale:

# 1. Definizione di costo delle operazioni:
#    - Ogni operazione elementare (ad esempio un confronto o un'assegnazione) ha un costo costante.
#    - Questo significa che richiede sempre lo stesso tempo, indipendentemente dalla lunghezza dell'input.

# 2. Cosa influenza il costo complessivo?
#    - Nel caso di una stringa, la lunghezza della stringa (numero di caratteri) è la principale grandezza
#      che determina la complessità computazionale.
#    - Algoritmi efficienti devono essere progettati per funzionare bene anche con input molto lunghi.

# 3. Crescita del tempo di esecuzione:
#    - Se il costo del tempo di esecuzione è rappresentato da una funzione composta da più termini
#      (ad esempio, un termine quadratico e uno lineare rispetto alla lunghezza della stringa),
#      ci concentriamo solo sul termine che cresce più velocemente.
#
#    - Esempio: Se abbiamo una funzione T(n) = n^2 + 5n + 10:
#      - Il termine n^2 cresce più velocemente rispetto a 5n e 10, quindi trascuriamo gli altri termini.
#      - Questo perché, per input grandi (n molto grande), il termine n^2 domina sugli altri.

# 4. Eliminazione delle costanti:
#    - Anche i coefficienti moltiplicativi (costanti) vengono ignorati nell'analisi della complessità.
#    - Questo perché la complessità si occupa solo di come cresce la funzione, non dei valori precisi.
#    - Ad esempio, T(n) = 3n^2 e T(n) = n^2 hanno la stessa complessità O(n^2).

# 5. Concetto di crescita della funzione:
#    - Se il comportamento dell'algoritmo dipende dalla lunghezza dell'input (n),
#      la complessità descrive come cresce il tempo di esecuzione al crescere di n.
#    - Anche se ogni operazione ha un costo costante, ciò che importa è il numero totale di operazioni rispetto all'input.

# 6. Conclusione:
#    - Una volta eliminate tutte le costanti e i termini di ordine inferiore,
#      il risultato finale descrive la complessità asintotica dell'algoritmo.
#    - Questo è rappresentato dalla notazione O-grande:
#      - Ad esempio, O(n), O(n^2), O(log n), ecc.

# Sintesi:
# - Gli algoritmi devono essere valutati in base alla loro efficienza per input di grandi dimensioni.
# - Concentriamoci sul termine che cresce più velocemente in una funzione di costo.
# - Ignoriamo costanti additive o moltiplicative per ottenere una rappresentazione pulita della complessità.
# - Alla fine, l'importante è capire come il tempo cresce rispetto alla dimensione dell'input.


#============================================================================================================================

# PUNTO 6

 
# Complessità computazionale:

# Una volta eliminate tutte le costanti e i termini di ordine inferiore, 
# il risultato finale descrive la complessità asintotica dell'algoritmo.
# Questo è rappresentato dalla notazione O-grande (es: O(n), O(n^2), O(log n), ecc.).

# Cosa significa eliminare costanti e termini di ordine inferiore?

# 1. Costanti additive:
#    - Supponiamo che la funzione che descrive il tempo di esecuzione di un algoritmo sia:
#      T(n) = n^2 + 5n + 10
#    - Qui:
#      - n^2: Termine quadratico.
#      - 5n: Termine lineare.
#      - 10: Costante additiva.
#    - Per valori di n molto grandi (es: n = 1.000.000), il termine n^2 diventa dominante:
#      - n^2 = 1.000.000^2 = 10^12
#      - 5n = 5 * 1.000.000 = 5 * 10^6 (trascurabile rispetto a 10^12).
#      - 10: Ancora più trascurabile rispetto agli altri.
#    - Quindi, eliminiamo i termini 5n e 10, perché il loro contributo è insignificante per n grandi.

# 2. Costanti moltiplicative:
#    - Supponiamo che il termine dominante sia:
#      T(n) = 3n^2
#    - Anche il coefficiente 3 viene eliminato. Questo perché non influisce sulla crescita relativa 
#      del tempo di esecuzione rispetto a n.
#    - Rimane solo il termine:
#      T(n) = n^2

# 3. Risultato finale:
#    - Una volta rimasto il termine più significativo (senza costanti additive e moltiplicative),
#      abbiamo una rappresentazione pulita della crescita del tempo di esecuzione, che chiamiamo
#      complessità asintotica.
#    - La complessità asintotica è scritta usando la notazione O-grande:
#      - Ad esempio, O(n^2), O(n), O(log n), ecc.

# Cos'è la notazione O-grande?

# La notazione O-grande (O) descrive la crescita asintotica di un algoritmo rispetto alla dimensione
# del suo input n. 

# 1. Significato:
#    - Rappresenta il limite superiore del tempo di esecuzione dell'algoritmo, ignorando costanti
#      e termini di ordine inferiore.
#    - Dice come cresce il tempo di esecuzione all'aumentare di n.

# 2. Esempi:
'''--------------------------------------------------------------------------------------------------'''
#    - O(1): Tempo costante, indipendente dalla dimensione dell'input.
#    - O(n): Tempo lineare, cresce proporzionalmente alla dimensione dell'input.
#    - O(n^2): Tempo quadratico, cresce proporzionalmente al quadrato della dimensione dell'input.
#    - O(log n): Tempo logaritmico, cresce lentamente all'aumentare di n.
'''---------------------------------------------------------------------------------------------------'''
# 3. Interpretazione pratica:
#    - Se n = 10:
#      - O(1): 1 operazione.
#      - O(n): 10 operazioni.
#      - O(n^2): 100 operazioni.
#      - O(log n): Circa 3 operazioni (log_2(10) ≈ 3.3).
#    - Se n = 1.000.000:
#      - O(1): 1 operazione.
#      - O(n): 1.000.000 operazioni.
#      - O(n^2): 1.000.000.000.000 operazioni.
#      - O(log n): Circa 20 operazioni (log_2(1.000.000) ≈ 20).
'''---------------------------------------------------------------'''
# Perché eliminiamo costanti e termini inferiori?

# 1. Costanti non influenzano la crescita relativa:
#    - Il coefficiente moltiplicativo non cambia come cresce il tempo per valori grandi di n. 
#    - Esempio: T(n) = 3n^2 e T(n) = 100n^2 hanno entrambe complessità O(n^2).

# 2. Termini inferiori sono trascurabili:
#    - Per valori grandi di n, i termini come n o 1 diventano insignificanti rispetto a n^2, n^3, ecc.

# Esempio Applicato:

# Funzione di Costo:
# T(n) = n^2 + 5n + 10

# Passaggi:
# 1. Identifica il termine dominante:
#    - n^2 domina su 5n e 10.

# 2. Elimina termini inferiori:
#    - Rimuovi 5n e 10.

# 3. Elimina costanti moltiplicative:
#    - Rimuovi il coefficiente di n^2 (se presente).
'''------------------------------------------------------------------------------------------------------------------'''

# 4. Risultato:
#    - Complessità finale: O(n^2).
'''------------------------------------------------------------------------------------------------------------------'''
# Conclusione:
# - La complessità asintotica (O) rappresenta il comportamento del tempo di esecuzione per input molto grandi.
# - Serve a confrontare algoritmi senza preoccuparsi dei dettagli implementativi 
# (come costanti o ottimizzazioni specifiche).
# - È un'indicazione della scalabilità dell'algoritmo.

'''------------------------------------------------------------------------------------------------------------------'''


'''======================================================================================================================='''
# t(N) E' IL TEMPO DI CALCOLO DELLE OPERAZIONI DA A CON L'INPUT DDATO 


# T(N ) = 2 N^2 + N/4 + 9  ---->>>>> L'ORDINE MAGGIORE  E 2 n^2  PERCHE' n^2 E' MAGGIORE DEGLI ALTRI 

# E' DIVENTA T(N) DI  O(N^2) DIVENTANDO COSI' L'ANOTAZIONE MAGGIORE DIVENTAA COSI' 

# ( E UNA LIMITAZIONI T(N) PERCHE' O(N^2) E' SEMPRE PIU' GRANDE )

# T(N) E O(N^2) E' UNA LIMITAZIONE PERCHE' PUO' ESSERE  T(N) E O(N^3) 


# T (N) =  3n^2 SE........................
# T (N) = n^3 SE..........................
'''======================================================================================================================='''

#=================================================================================================================================

# t(N) rappresenta il tempo di esecuzione di un algoritmo in funzione della dimensione dell'input (N).

# Esempio di funzione del tempo di esecuzione:
# T(N) = 2N^2 + N/4 + 9
# ---> L'ordine di grandezza dominante è N^2, perché il termine N^2 cresce più velocemente rispetto agli altri.
# ---> I termini N/4 e 9 diventano trascurabili per valori grandi di N.

# Notazione asintotica:
# La complessità T(N) si esprime come O(N^2), indicando che il tempo di 
# esecuzione cresce al massimo come il quadrato di N.

# Perché consideriamo solo il termine dominante?
# - Per input molto grandi (N → infinito), i termini di ordine inferiore e le costanti 
# moltiplicative diventano insignificanti.



# - Esempio:
#     - Per N = 1.000.000:
#       - 2N^2 = 2 * 10^12 (dominante).
#       - N/4 = 250.000 (trascurabile rispetto a 10^12).
#       - 9 = una costante (ancora più trascurabile).

# Limitazione della notazione O-grande:
# O(N^2) rappresenta il limite superiore della complessità.
# Questo significa che T(N) cresce al massimo come N^2, ma potrebbe crescere più lentamente.

# Esempio di funzioni di costo che rientrano in O(N^2):
# T(N) = 3N^2
# ---> Complessità asintotica: O(N^2)

# Esempio di una funzione con complessità maggiore:
# T(N) = N^3
# ---> Complessità asintotica: O(N^3)

# Nota importante:
# - La notazione O-grande descrive il **limite superiore** della crescita del tempo di esecuzione.
# - Se un algoritmo ha complessità O(N^2), potrebbe anche rientrare in O(N^3), poiché N^3 cresce più velocemente.

# - Tuttavia, scegliamo sempre la complessità **più stretta possibile** per 
# rappresentare il comportamento reale dell'algoritmo.

# Conclusione:
# - T(N) = 2N^2 + N/4 + 9 ---> Complessità O(N^2).
# - Se il termine dominante cambia (es. T(N) = N^3), la complessità asintotica diventa O(N^3).

#=============================================================================================================================================


''' # Differenza tra O(N²) e Θ(N²): '''


# O(N²) - Limite Superiore Asintotico:

''' # - O(N²) rappresenta il limite superiore del tempo di esecuzione. '''

# - Indica che l'algoritmo non crescerà mai più velocemente di N², ma potrebbe crescere più lentamente.
''' # - È una garanzia di crescita massima. '''

# Esempio per O(N²):
# Se T(N) = N² + N, possiamo dire che T(N) ∈ O(N²) perché:
# - N² + N ≤ c * N² per un opportuno valore di c e N > N₀.
# - Il termine N (lineare) è trascurabile rispetto al termine dominante N².

# Usi di O(N²):
# - Serve per garantire che l'algoritmo non diventi inefficiente per input grandi.
# - Si usa quando vogliamo una stima superiore, senza preoccuparci di quanto strettamente 
# il limite superiore descrive l'algoritmo.


''' MENTRE CON THETHAA '''

# Θ(N²) - Limite Teso Asintotico:
# - Θ(N²) rappresenta sia il limite superiore che il limite inferiore del tempo di esecuzione.
# - Indica che l'algoritmo cresce esattamente come N², né più lentamente né più velocemente.
# - È una garanzia di crescita esatta.

# Esempio per Θ(N²):
# Se T(N) = 2N² + 5, possiamo dire che T(N) ∈ Θ(N²) perché:
# - Esistono costanti c₁, c₂, N₀ tali che:
#   c₁ * N² ≤ T(N) ≤ c₂ * N² per ogni N > N₀.
# - Il comportamento dell'algoritmo è dominato esattamente da N².

# Usi di Θ(N²):
# - Si usa per descrivere il comportamento preciso dell'algoritmo.
# - Indica che N² rappresenta sia un limite superiore che inferiore, 
# quindi il tempo di esecuzione è strettamente proporzionale a N².

# Differenza Chiave tra O(N²) e Θ(N²):
# - O(N²): Limite superiore (crescita massima). Può crescere più lentamente di N².
# - Θ(N²): Limite superiore e inferiore (crescita esatta). Cresce esattamente come N².

# Esempio di Confronto:
# 1. Caso O(N²):
#    - Algoritmo con T(N) = N² + N:
#      - Cresce al massimo come N², ma il termine lineare N è trascurabile per N grandi.
#      - Complessità: O(N²).
# 2. Caso Θ(N²):
#    - Algoritmo con T(N) = 2N² + 5:
#      - Cresce esattamente come N², senza termini inferiori significativi.
#      - Complessità: Θ(N²).

# Differenza Pratica:
# - O(N²): Include tutti gli algoritmi che crescono al massimo come N² (ma possono crescere più lentamente, es. N).
# - Θ(N²): Include solo gli algoritmi che crescono esattamente come N².

# Conclusione:
# - O(N²) è più generale e garantisce solo un limite superiore.
# - Θ(N²) è più specifico e descrive il comportamento esatto di un algoritmo.

#=========================================================================================================================

# x e' una stringa , tale che len (x) = n

# c in x 

# T(n) =  i + 1 dove i  taale che 
               # x[1] == c

            # n se c non appartiene ad x 
            
#nel casoo peggiore T(n) = Θ (n)


#def 0()

#t(n) e 0 (f(n))               t(n) < f (n) + d n  c0 sono costanti 
                                # se n > n0 




# T( n ) = 6 n + 4 e 0 (n)           e 0 (n)
# T ( n ) < c n  per  n > n0 




#==============================================================================================================================

'''========================================================================================================================'''
# Spiegazione del problema:

# 1. Input:
#    - x: Una stringa di lunghezza n (len(x) = n).
#    - c: Un carattere che vogliamo cercare all'interno della stringa x.

# 2. Obiettivo:
#    - Determinare la posizione di c nella stringa x (se presente).
#    - Se c non è presente, eseguire un'operazione corrispondente al numero massimo di controlli, cioè n.

# Comportamento della funzione:

# 1. Caso 1: c è presente in x:
#    - La funzione effettua un controllo sequenziale sui caratteri della stringa x.
#    - Si ferma non appena trova il carattere c.
#    - Il costo del tempo di esecuzione è proporzionale alla posizione i di c nella stringa:
#      T(n) = i + 1, dove i è l'indice (0-based) della prima occorrenza di c.

# 2. Caso 2: c non è presente in x:
#    - La funzione esegue un controllo su tutti i caratteri della stringa x senza trovare una corrispondenza.
#    - In questo caso, il numero di controlli è uguale alla lunghezza della stringa n.
#    - T(n) = n, che rappresenta il costo massimo dell'algoritmo.

# Complessità Computazionale:

# 1. Caso Migliore (Best Case):
#    - c è il primo carattere di x (i = 0).
#    - Tempo di esecuzione: T(n) = 1.
#    - Complessità: O(1), poiché è un'operazione costante.

# 2. Caso Peggiore (Worst Case):
#    - c non è presente in x o si trova all'ultimo indice (i = n-1).
#    - Tempo di esecuzione: T(n) = n.
#    - Complessità: O(n), poiché il numero di controlli cresce linearmente con la lunghezza della stringa.

# 3. Caso Medio (Average Case):
#    - Supponendo che c abbia la stessa probabilità di essere trovato in qualsiasi posizione,
#      in media verranno effettuati n/2 controlli.
#    - Tempo di esecuzione medio: T(n) = n/2.
#    - Complessità: O(n), poiché il termine n/2 è comunque lineare rispetto a n.

# Riassunto:
# - La funzione esegue una ricerca sequenziale sulla stringa x per trovare il carattere c.
# - Complessità Asintotica:
#   - Caso migliore: O(1) (se il carattere è al primo posto).
#   - Caso medio e peggiore: O(n) (se il carattere è alla fine o non è presente).

'''========================================================================================================================'''






































