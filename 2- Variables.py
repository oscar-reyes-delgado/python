print('- Saludo personalizado -')
nombre = input("Ingresa tu nombre por favor: ")
print(f"\nHola {nombre}, espero que te encuentres bien el dia de hoy\n")

#Las entradas que hagas con input siempre seraan strings, tu puedes convertirlos con las funciones de int(), float(), string(), 
# que son funciones que ya estan integradas en python, no necesitas importar algun tipo de libreria. Igual el print y el input.

print(f"- Calculadora -\nVamos a realizar la suma de dos numeros, que ingresaras a continuacion\n")
numero1 = float(input("Escribe el primer numero: "))
numero2 = float(input("Escribe el segundo numero: "))

print(f"El resultado es: {numero1 + numero2}")

#En el codigo que acabo de escribir use una entrada para guardar datos en variables, lo esperado es que se meta un numero, pero si
# entra algun string que no sea convertible a float(numeros con decimales), el codigo tronara. Para evitar esto se usan excepciones
# que evitan que el codigo truene seleccionando errores especificos; pero esas se veran en el futuro.


