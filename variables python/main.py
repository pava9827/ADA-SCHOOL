# variables python
edad = 29
grados = 3.1455
esta_caliente = True
mid = "Faker"
cam = "Campeon"


suma = edad * (edad + 10)
resulConcatenacion = cam +(" ") + mid  + str(edad) + str(grados)  + str(esta_caliente) + ("+")+str(suma) 



# Límite de los enteros en Python:
# El tamaño de los enteros en Python no tiene límite teórico, ya que Python 3.x utiliza una representación de enteros de longitud variable.
# Sin embargo, el límite práctico está determinado por la cantidad de memoria disponible en la máquina.

# Ejemplo de enteros grandes:
# entero_grande = 10**18
# print(f"Ejemplo de entero grande: {entero_grande}")

# # Límite de los flotantes en Python:
# # Los números de punto flotante en Python siguen el estándar IEEE 754 y tienen límites específicos en términos de rango y precisión.

# # Ejemplo de flotante grande:
# flotante_grande = 1.0e308
# print(f"Ejemplo de flotante grande: {flotante_grande}")

# # Ejemplo de flotante cercano a cero:
# flotante_cercano_a_cero = 1.0e-308
# print(f"Ejemplo de flotante cercano a cero: {flotante_cercano_a_cero}")

print(resulConcatenacion )
