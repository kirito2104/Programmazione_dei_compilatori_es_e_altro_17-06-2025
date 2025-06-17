
def ricerca_intervallo(a, k):
    # Ciclo di ricerca binaria
    lx, rx = 0, len(a) - 1  # lx = primo indice (sinistro), rx = ultimo indice (destro)
    
    if k < a[0]:  # Controllo se il valore cercato k è minore del primo elemento dell'array
        return ('-if', a[0])  
    # Restituiamo un messaggio per indicare che k è fuori 
    #dai limiti inferiori e il primo valore nell'array

    if k < a[-1]:  # Controllo se il valore cercato k è minore dell'ultimo elemento dell'array
        return (a[-1], '+if') 
    # Restituiamo l'ultimo valore dell'array e 
    #un messaggio per indicare che k è compreso nell'intervallo superiore
 
    while lx <= rx:  
        cx = int((lx + rx) / 2)  # Calcolo del punto medio come media tra lx e rx
        
        if k == a[cx]:  # Se il valore cercato k è uguale al valore al punto medio
            return (a[cx], a[cx+1])  # Stampiamo il valore trovato e quello successivo
           
        elif k < a[cx]:  # Se k è minore del valore al punto medio
            rx = cx - 1  # Restringiamo l'intervallo alla metà sinistra escludendo il punto medio
        
        else:  # Se k è maggiore del valore al punto medio
            lx = cx + 1  # Restringiamo l'intervallo alla metà destra escludendo il punto medio
            
    # Controllo finale dopo la fine del ciclo
    if k < a[cx]:  # Se il valore cercato è minore del valore al punto medio
        return (a[cx-1], a[cx])  # Stampiamo lx e cx per indicare l'intervallo in cui k si troverebbe
    elif k > a[cx]:  # Se il valore cercato è maggiore del valore al punto medio
        return (a[cx], a[cx+1])  # Stampiamo cx e rx per indicare l'intervallo in cui k si troverebbe


a = [-2, 3, 9, 12, 13]  # Lista ordinata di elementi su cui fare la ricerca
k = 13                   # Elemento da cercare nell'array

print(ricerca_intervallo(a, k))