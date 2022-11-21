def sum_list(my_list):
    risultato = 0
    if (len(my_list)==0):
        return None
    for item in my_list:
        risultato = risultato + item
    return risultato
   


lista = [1,2]

print(lista)
r = sum_list(lista)
print(r)
