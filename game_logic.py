from secret_number import *
from response import *

semilla = int(input("Enter a seed number:\n"))
seed_secret_numbers(semilla)

secreto = generate_secret_number()

intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("What is your guess:\n"))
    intentos += 1
    
    mensaje, adivinado = input_response(secreto, intento)
    print(mensaje)

print(f"It took you {intentos} tries!")