# 06 Stringhe -creare una stringa, parlare di apici doppi singoli 
# # -mandare a schermo stringa e variabile stringa 
# # -stringhe multi riga """prova""" 
# # -trattare stringhe come array (prendere carattere, lenght, loop) 11 12 
# # -prendere parte di stringa str[:5], str[2:], str[-5:-2]
# # -modificare stringa con upper() lower() strip() split() e replace() -concatenare stringhe 
# # -usare format() per combinare stringhe e numeri
# # -escape dei caratteri 


#LE STRINGHE 
# LE SSTRINGHE NON PERMETTONO DI ANDARE A CAPO MA DEVE ESSERE SCRITTO SU UNA SINGOLA RIGA 
#UNA STRINGA PUO' ESSERE SCRITTA IN DUE DIVERSE MANIERE, NON FA DIFFERENZA:
'''
x = "ciao"
y='ciao'
xy = x+""+y
 
print(xy)
'''
# facendo cosi' concateno piu stringe in una singola 

# LE STRINGHE SI POSSONO COMPORTARE/TRATTATE COME DEGLI ARRAY
# ( GLI ARRAY NOJN ESISTONO IN PYTHON PERO', CHE POSSONO ESSERE IMPLEMENTATE CON UNA LIBRERIA ESTERNA)

#UNA STRINGA PER SI CHE SIA SIMILE AD UN ARRAY BISOGNA VEDERLA COME UN INSIEME DI SINGOLI CARATTERI
# AVENDO CIO POSSO ACCEDERE AD OGNI SIGOLO TIPO DI CARATTERE
'''
x = "prova bbb"
y='ciao'
print(x[0]) 
'''

#CIO' Permette di prendere da x la lettera p, siccome in una lista, 
#Siccome ogni carattere ha un indice, ossia l'indirizzo a cui troviamo ogni singolo carattere e' partono sempre con 0  
#anche lo spazio viene contato come un carattere

#NEL CASO IN CUI SIA :
'''
x = "prova bbb"
y='ciao'
print(x[-1]) 
'''
#NEL CASO IN CUI SIA COSI' USCIRA' B SICOME LE STRINGHE QUANDO 
# GLI DICI COME IN QUESTO CASO CON IL MENO RIPRENDONO DAL L'ULTIMA PARTE DELLA STRINGA
'''
x = "prova bbb"
y='ciao'

for carattere  in "computer":
  print(x[-1])   
'''
#facendo cosi puoi sapere la lunghezza di ogni singolo carattere

#LA LUNGHEZZA CHE E` LA SOMMA DEI CARATTERI 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#PER METTERE PER PRENDERE PARTI DI STRINGA BISOGNA FARE:
'''
X='CIAO SONO LUCA0'

print(X[2:3])'''
#facendo cosi` ci prendera` a schermo "CIA" 

#LA DIFFERENZA SOSTANZIALE E` PRINCIPALMENTE CHE SENSA I DOPPI PUNTI PRENDERA` SOLO UN CARATTERE, IN QUESTO CASO SOLO " O "
# QUINDI PRENDERA I NUMERI DA 0 A 3, 3 NON E` COMPRESO 
#MENTRE FACENDO COSI` print(X[2:3]) " PRENDERA I NUMERI DA 2 A 3, SI PUO FARE ANCHE VICE VERSA [2:] , ED USCIRA` AO SO LUCA.

# SI PUO FARE LO STESSO AL CONTRAIO , [-4] E ANCHE INVERSO IL NOME [-4:]


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#MODIFICARE UNA STRINGA CON upper() , lower() , strip() , slit()  e replace()

'''
X=' ciao sono luca 0'

 
print(X.upper())''' # QUI SI HA UNA STRINGA CHE HA DEI METODI, in questo  caso UPPER cambiera` carattere ossia lo rendera maiuscolo


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#MENTRE SE SI VORRA` FARE IN MINUSCOLO BISOGNERA` METTERE LOWER
'''
X='CCIAO SONO LUCA ' # e`  eutto cio diventera minuscolo 
print(X.lower())'''


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# il metodo STRIP PERMETTERA` DI  LEVARE gli spazzi all'inizio e alla fine della stringa 
'''
X='    CCIAO SONO LUCA ' 
print(X.strip())'''# permette di levare gli spazzi sulla stringa 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# per sostituire una stringa invece bisognera` usare il metodo REPLACE che sostituira la stringa con il carattere scelto da noi

'''
X='CCIAO SONO LUCA ' 
print(X.replace("O","w")) '''# questo metodo permette di scambiare il carattere


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Per concetenare una stringa una stringa bisognera`
'''
X='CCIAO SONO LUCA ' 

Y= "luca  bino"

print(X+Y.lower())''' # CIO PERMETTE DI CASTARE LE DUE STRINGHE IN UNA SOLA 



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
X='CCIAO SONO LUCA ' 

Y= "luca  bino"

prova= "ciao eeeiiiii" + 15

print(X+Y.lower()) '''
#cio non si potra` fare, per farlo bisogna usare  il metodo format

#QUINDI PER POTER COMBINARE LE STRIGHE ED I NUMERI BISOGNERA USARE ' fromat() '


'''
X='CCIAO SONO LUCA ' 

Y= "luca  bino"

prova= "io sono nato il {}, peso {}kg e sono alto{}" # le grafe permettono di di aggiungere con la funzione format un num. intero, 
#si puo aggiungere anche un altra grafa per aggiungere altri valori

print(prova.format(15,70, 1.80))''' # questo metodo format permette di aggiungere il num intero, si puo anche aggiungere direttamente una variabile gia` esistente `

#si puo aggiungere nella grafa il numero delle stringhe che si vogliono aggiungere 
   
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Per fare un escape dei caratteri bisognera` invece fare 

X='CCIAO SONO LUCA e sono piu` alto di un\'altro' # cio permette di mettere l'accento su una lettera un\'altro


prova= "ciao sono luc e sono \"bello\"" # per aggiungere le virgolette in una stringa bisognera` mettere \"bello\" che permette di stamparle a schermo sensa errori
# la stessa cosa conl'apostrofo '\bello\'

print(prova+X)














