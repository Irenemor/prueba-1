"""Calculadora simple: suma, resta, multiplicacion y division."""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


OPERACIONES = {
    "1": ("Sumar", sumar),
    "2": ("Restar", restar),
    "3": ("Multiplicar", multiplicar),
    "4": ("Dividir", dividir),
}

SIMBOLOS = {"1": "+", "2": "-", "3": "*", "4": "/"}


def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Eso no es un numero valido. Intenta de nuevo.")


def main():
    print("=== Calculadora simple ===")
    while True:
        print("\nElige una opcion:")
        for clave, (nombre, _) in OPERACIONES.items():
            print(f"  {clave}. {nombre}")
        print("  5. Salir")

        opcion = input("Opcion: ").strip()

        if opcion == "5":
            print("Hasta luego!")
            break

        if opcion not in OPERACIONES:
            print("Opcion no valida. Elige un numero del 1 al 5.")
            continue

        a = pedir_numero("Primer numero: ")
        b = pedir_numero("Segundo numero: ")

        _, funcion = OPERACIONES[opcion]
        try:
            resultado = funcion(a, b)
        except ZeroDivisionError as error:
            print(f"Error: {error}")
            continue

        print(f"Resultado: {a} {SIMBOLOS[opcion]} {b} = {resultado}")


if __name__ == "__main__":
    main()
