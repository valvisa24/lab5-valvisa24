from utils import *

mensaje = input("Please type your message\n")
invertido = flip(mensaje)
conteo = count_letters(mensaje)

print(f"Your encoded message is: {invertido}{conteo}")