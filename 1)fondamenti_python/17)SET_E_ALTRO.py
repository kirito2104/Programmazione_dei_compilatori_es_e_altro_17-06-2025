# 17 set

# - Collezioni di dati non ordinate, non indicizzate, non modificabili e non permettono duplicati
# - Creare una tupla, normale e mischiata
# - Vediamo len(), type() e set()

# - Accedere agli elementi con loop
# - Modificare elementi non è possibile, possiamo solo aggiungere e rimuovere
# - Aggiungere elementi con add(), update()
# - Rimuovere elementi con remove(), discard(), pop(), clear(), del
# - Unire con union() e update(), intersection_update(), intersection(), symmetric_difference_update(), symmetric_difference()

#------------------------------------------------------------------------------------------------------------------------------
# I set di dati sono delle : 
# - Collezioni di dati non ordinate, non indicizzate, non modificabili e non permettono duplicati
'''PERO' E' POSSIBILE AGGIUNGERE DEGLI ELEMENTI'''


X = {'PISA','MILANO','ROMA','NAPOLI'} # questo e' un set 
Y = {'MILANO',89,True} # si possono anche mettere piu' valori insieme 

#-----------------------------------------------------------------------------------------------------------------------------------
# 'Set{} ' usando : 
# la funz. Type
# - Vediamo len(), type() e set()

x = {'milano','firenze','verona'}

print(type(x))  # leggera di che tipo e' x ossia un set

#-------------------------------------------------------------------------------------------------------------------------
# 'Set{} ' usando : 
# la funz. len, che leggera' la graandezza del set 
x = {'milano','firenze','verona'}
y = set(('milano','rm','napoli')) # con il costruttore set, crea un set di elementi 

print(len(x)) # leggera' la lunghezza di x che sara' di 3  


#----------------------------------------------------------------------------------------------------------------------------------------------------
#nei set per accedere agli elementi, bisogna enevitabilmente usare i loop

# - Accedere agli elementi con loop

x = {'milano','firenze','verona'}

'''print(x[0])'''# facendo cosi' dara' errore 

print(x) # facendo cosi' stampera gli elemnti in modo casuale, perche' non e' ordinato il set
#cio dimostra che gli eeeeeeelemnti non sono ordinati e quindi non indicizzati 

#---------------------------------------------------------------------------------------------------------------------------
x = {'milano','firenze','verona'}

for citta in x :
    print(citta)
# facendo cosi' non cambiera nulla l'ordinamento sara' sempre casuale
#-----------------------------------------------------------------------------------------------------------------------------------------------


x = {'milano','firenze','verona'}
print('milano' in x )   # facendo cosi' verifica che un elemnto sia presente nel set di x 

# e stampera che e' true 
'''
# Cio' non si potra' fare : 
x = {'milano','firenze','verona'}

x [0] = 'venezia' # facendo cosi' dara' errore perche non si puo' modificare 


'''
#-----------------------------------------------------------------------------------------------------------------------------------------------
# l'unica cosa che si puo' fare con un set, si puo' aggiungere o rimuove un elemento 

# per aggiungere un elemnto si dobvra usare add , che aggiungera' un elemnto in x 
# a differenza della lista che si usava append , qui si usa add
# che accodera'  'venezi' al set di elemnti 

x = {'milano','firenze','verona'}

x.add('venezia') # add accoda degli elementi al set x 
# e diventera' : {'firenze', 'milano', 'verona', 'venezia'} che sara' sempre casuale l'ordinamento pero'

print(x)

#------------------------------------------------------------------------------------------------------------------------------

# la funzione  ' update ' , aggiorna un set, ossia aggiunge gli elementi di un altro set, unendoli a sua volta 
# come qui sotto infatti il set di x diventera' cosi': sempre scaasuale l'ordinamento, 
#{'genova', 'milano', 'verona', 'firenze'} gli elemnti usguali , non saranno inseriti 

x = {'milano','firenze','verona'}

y = {'genova','milano','firenze','verona'}

x.update(y) # aggiungera' gli elementi di y in x , aggiornando quindi il set di x 

print(x)

#--------------------------------------------------------------------------------------------------------------------------------------
#nei set si puo' anche :
# - Rimuovere elementi con remove(), discard(), pop(), clear(), del

#con ilmetodo remove :
# usando remove e discard : rimuovero' un determinato elemento dal set di elementi 

x = {'milano','firenze','verona'}

y = {'genova','milano','firenze','verona'}

x.remove('milano') # usando questo metodo rimuovera' 'milano' dal set 
x.discard ('roma')
print(x)

#--------------------------------------------------------------------------------------------------------------------------
# LA DIFFERENZA TRAI DUE E' PRICIPALMENTE CHE QUANDO UN ELEMENTO NON ESISTE NEL SET DI ELEMENTI  :
#  ' REMOVE() ' DARA' ERRORE , MENTRE ' DISCARD ' NON DARA' NULLA  STAMPERA COMUNQUE IL SET DI ELEMENTI 

x = {'milano','firenze','verona'}

y = {'genova','milano','firenze','verona'}

#x.remove('UDINE') # usando questo metodo rimuovera' 'milano' dal set, LA DIFFERENZA E CHE CON RIMOVE SE L'ELEMENTO 
# DA RIMUOVERE NON E' PRESENTE, DARA' ERRORE IL CODICE 

x.discard ('UDINE') # ANCHE SE L'ELEMENTO NON E' PRESENTE STAMPERA' COMUNQUE A SCHERMO GLI ELEMENTI, PASSERA OLTRE 
print(x)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# MENTRE USANDO LA FUNZIONE POP, ELIMINERA L'ULTIMO ELEMENTO NEL  SET, L'UNICA COSA CHE 
# SICCOME GLI ELEMNTI NON SONO ORDINATI, ELIMINERA CASUALMENTE UN ELEMENTO 


x = {'milano','firenze','verona'}

y = {'genova','milano','firenze','verona'}

x.pop() # ELIMINA L'ULTIMO ELEMENTO , L'UNICA COSA E' CHE CON IL SET L'ORIDINAMENTO E' CASUALE 

print(x)

#--------------------------------------------------------------------------------------------------------------------------

#USANDO ' CLEAR() ' IL SET E QUINDI NON RIMARA' NULLA 

x = {'milano','firenze','verona'}

y = {'genova','milano','firenze','verona'}

x.clear() # PULISCE IL SET E RITORNA VUOTO 

print(x)

#USDANDO IL METODO ' DEL ' INVECE ELIMINERA' TUTTO DANDO PERO' ERRORE 
# del x 

#-------------------------------------------------------------------------------------------------------------------------------------
# - Unire con union() e update(), intersection_update(), intersection(), symmetric_difference_update(),
# symmetric_difference()

# usando il metodo 'union'  unira e creara' un nuovo set , che sara' l'unione di x e y 
x = {'milano','firenze','verona'}

y = {'genova','milano','firenze','verona'}


z = x.union (y)

print(z) # unira' i due set x e y 
#sia updete che union,  andranno ad eliminare gli elementi duplicati 
# UNION --->>>> UNISCE DUE SET DI DATI 
#UPDATE --->>>> INVECE AGGIORNA I DATI DEL SET 
'''x = {'milano','firenze','verona'}

y = {'genova','milano','firenze','verona'}

x.update(y) # aggiungera' gli elementi di y in x , aggiornando quindi il set di x 

print(x)
'''
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# NEL CASO IN CUI  SI VOGLIANO AGGIUNGERE ANCHE GLI ELEMENTI DUPLICATI 
# BISOGNA USARE :intersection_update(), intersection()

#intersection_update() ---->>>>>> lavora sugli elementi in comune tra i due set, aggiorna pero' un set che si ha gia' 



x = {'milano','firenze','verona'}

y = {'genova','milano','firenze','verona'}

x.intersection_update(y) # lavora sugli elementi in comune tra i due set, 
#ossia solo cio che e' duplicato in entrambi 

print(x)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Mentre
#intersection() crea un copia tra i due set e li unisce tra di loro, creando a sua volta un nuovo set

#intersection() ---->>>>>> bisogna creare un nuovo set che sara' l'unione dei due set 


x = {'milano','firenze','verona'}

y = {'genova','milano','firenze','verona'}

z = x.intersection(y) # unice i due set x e y in un unico set 

print(z)

#---------------------------------------------------------------------------------------------------------------------------
# Creazione di due set di caratteri
set1 = {'a', 'b', 'c', 'd'}
set2 = {'c', 'd', 'e', 'f'}

# symmetric_difference() ---->>>>>> da tutto tranne che i valori uguali 

# Restituisce un nuovo set con i caratteri che sono in uno solo dei due set
symmetric_diff = set1.symmetric_difference(set2)
print("Risultato di symmetric_difference():", symmetric_diff)
# Output atteso: {'a', 'b', 'e', 'f'}

# symmetric_difference_update() ----->>>>> lavorano su un diverso set unendoli e creandone uno nuovo 
#con i valori uguali 

# Aggiorna il set chiamante (set1) con la differenza simmetrica rispetto a un altro set
set1.symmetric_difference_update(set2)
print("Risultato di symmetric_difference_update():", set1)
# Output atteso: {'a', 'b', 'e', 'f'}

# set2 rimane invariato
print("Set2 rimane invariato:", set2)
# Output atteso: {'c', 'd', 'e', 'f'}




'''
Spiegazione:
Set iniziali:
set1 = {'a', 'b', 'c', 'd'}
set2 = {'c', 'd', 'e', 'f'}
Operazioni:
symmetric_difference():

Confronta i due set e restituisce un nuovo set contenente i caratteri che sono presenti in uno solo dei due set (non in entrambi).
Non modifica set1 o set2.
Risultato: {'a', 'b', 'e', 'f'}.
symmetric_difference_update():

Aggiorna il set chiamante (set1) con la differenza simmetrica rispetto a set2.
Modifica direttamente il contenuto di set1.
Risultato: set1 diventa {'a', 'b', 'e', 'f'}.
set2 non viene modificato:

set2 rimane invariato con i suoi valori originali: {'c', 'd', 'e', 'f'}. '''