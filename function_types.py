def list_shift(lista, valor_flotante):
   
    for i in range(len(lista)):
        lista[i] += valor_flotante

def calc_avg(lista):
   
    return sum(lista) / len(lista)

def print_normalized(lista):
    
    print(lista)