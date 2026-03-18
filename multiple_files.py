from utils import *
mensaje = input("Please type your message\n")

mensaje_invertido = flip(mensaje)
cantidad_aes = count_letters(mensaje, 'a')

mensaje_codificado = str(mensaje_invertido) + str(cantidad_aes)
print(f"Your encoded message is: {mensaje_codificado}")