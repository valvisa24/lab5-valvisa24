def obtener_total(pasos):
    return sum(pasos) 

def obtener_promedio(pasos):
    return sum(pasos) // len(pasos)

def obtener_maximo(pasos):
    return max(pasos)

def obtener_minimo(pasos):
    return min(pasos)

def verificar_metas(pasos):
    return [p >= 10000 for p in pasos]

entrada = input("Ingresa tus pasos diarios durante 7 días (separados por espacios): ")
pasos_diarios = [int(x) for x in entrada.split()]

total = obtener_total(pasos_diarios)
promedio = obtener_promedio(pasos_diarios)
max_pasos = obtener_maximo(pasos_diarios)
min_pasos = obtener_minimo(pasos_diarios)
cumple_metas = verificar_metas(pasos_diarios)

print(f"Total steps: {total}")
print(f"Average daily steps: {promedio}")
print(f"Highest steps in a day: {max_pasos}")
print(f"Lowest steps in a day: {min_pasos}")
print(f"Goal met each day: {cumple_metas}")