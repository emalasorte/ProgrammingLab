def sum_list(my_list):
    risultato = 0
    if (len(my_list)==0):
        return None
    for x in my_list:
        risultato = risultato + x
    return risultato
   


lista = [456,43,6778,54,72,100000000, 4728372647274283198]

print(lista)
r = sum_list(lista)
print(r)
