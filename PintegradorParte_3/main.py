import os
from readchar import readkey, key


def clear_print(n):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Contador: {n}")

# El contador inica en valor cero
contador = 0

print(input("Por favor presiona la tecla 'n' para el contador: ")

while True:
    k = readkey()
    if k == key.UP:
        print("Oh!! has presionado 🡩  para detener ")
        break
    elif k == 'n':

        contador += 1
        clear_print(contador)

        if contador == 50:
            print("Has llegado al número 50, el programa se detendrá.")
            break

