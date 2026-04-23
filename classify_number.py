


# ---- Funciones provistas (NO modificar) ----

def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    if n % 2 == 0:
        return True
    else:
        return False


def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    if n > 0:
        return True
    else:
        return False


# ---- Función a implementar ----

def classify_number(num):
    """
    Dado un número entero n, retorna un string que lo clasifica.
    Debe USAR las funciones is_even e is_positive.
    """

    # Caso especial primero
    if num == 0:
        return "zero"

    iseven = is_even(num)
    ispositive = is_positive(num)

    if ispositive and iseven:
        return "positive even"
    elif ispositive and not iseven:
        return "positive odd"
    elif not ispositive and iseven:
        return "negative even"
    else:
        return "negative odd"


