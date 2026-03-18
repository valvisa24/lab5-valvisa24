import os
import math

directorio = os.getcwd()
print(f"Current working directory: {directorio}")

entrada = int(input("Enter an integer: "))
valor_log = math.log2(entrada)
print(f"Log base 2 of {entrada} is: {valor_log}")

val_piso = math.floor(valor_log)
val_techo = math.ceil(valor_log)
print(f"Floor: {val_piso}")
print(f"Ceiling: {val_techo}")