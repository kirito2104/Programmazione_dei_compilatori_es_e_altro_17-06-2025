

#8 operatori Aritmetici

#- opoeratori artimetici
#- operatori di asssegnamento 
#- precedenza operatori 
#- metodi minx, max, abs , pow

# +, -, /, %, **, // 

#__________________________________________________________________________________________________________________________________
# Addizzione, si fa x+y
x=  5
y= 9

print(x+y)

#-------------------------------------------------------------------------------------------------------------------

#SOTTRAZIONE
#Sottrae x ed y
x= 5
y= 9

print(x-y)

#--------------------------------------------------------------------------------------------------------------------
#Moltiplicazione , moltiplica x* y

x=  5
y= 9

print(x*y)

#--------------------------------------------------------------------------------------------------------------------
#Divisione, divide x/y

x=  5
y= 9

print(x/y)

#--------------------------------------------------------------------------------------------------------------------
#Il modulo di x % y

x=  5
pi= 9

print(x%pi)

#--------------------------------------------------------------------------------------------------------------------
#Potenza , base elevata a sestessa o ad un altro numero ad es: x**2

x=  5
y= 9

print(x**x)
#---------------------------------------------------------------------------------------------------------------------
#Floor division -> ossia ////
#Da esclusivamente il valorearotondato per difetto

x=  15
y= 7

print(x//y)
#usicra' 2 , arrotondando
#--------------------------------------------------------------------------------------------------------------------
# si possono anche fare piu' operazioni insieme,mettendo la parentesi cambia totalmente il risultato (x+Y)*2

x=25
y= 32

print(x+y*2*2//2)
#------------------------------------------------------------------------------------------------------------------
#Si puo anche riassegnare un valore ad una variabile simile come qui sotto, per poi richiamarla e' sommarla a sua volta

x=  15
x = x +2

y= 8

print(x)
# facendo cosi pero' risulta essere troppo lungo 

#e si puo anche fare cosi' che risulta piu veloce, e un po piu' logico 
x=15
x += 2 # che significa uguale a se stesso + e' = a due, ed il risultato sara' 17

y=7
print (x)

#vale la stessa cosa per :
#  -=
#  *=
#  /=

#---------------------------------------------------------------------------------------------------------------------
# ci sono diversi metodi come: Min , Max , Abs , Pow
# abs -> che sta per absolute
#pow  -> che sta per potenza


x = min  (5,10,29) # con min permette di definere il valore piu' piccolo 
 
y="ciaaoo, il num e' "
new_val = str(x)
print (y+ str(x))
#--------------------------------------------------------------------------------------------------------------------
#Mentre con la variabile Max
#definisce il valore piu grande e lo stampa a schermo 
x = max (5,10,29) 
# con max permette di definere il valore piu' grande

y="ciaaoo, il num piu' grande e' "
new_val = str(x)
print (y+ str(x))

#--------------------------------------------------------------------------------------------------------------------
#Mentre con la variabile Abs
#definisce il valore Assoluto di numero e poi lo stampa a schermo 
x = abs (-5) 
# con abs permette di definere il valore assoluto del num, negativo(in questo caso levando il meno)

y="ciaaoo, il num assoluto e' "
new_val = str(x)
print (y+ str(x))

#-------------------------------------------------------------------------------------------------------------------
#Pow , ossia potenza
#permette di fARE LA potenza tra due numeri, tra parentesi

x = pow (4,0) # pertmette di fare elevare a potenza e dare risultato 
y="ciaaoo, LA POTENZA E' "
new_val = str(x)
print (y+ str(x))


