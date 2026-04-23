# ---- Funciones provistas (NO modificar) ----

def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

# ---- Funciones a implementar ----

def total_letters(text):
    """Retorna la cantidad total de letras. Debe USAR count_vowels y count_consonants."""
    return count_vowels(text) + count_consonants(text)


def vowel_percentage(text):
    """Retorna el porcentaje de vocales sobre el total de letras, redondeado a 1 decimal.
    Si no hay letras, retorna 0.0. Debe USAR count_vowels y total_letters."""
    total = total_letters(text)
    if total == 0:
        return 0.0
    vowels = count_vowels(text)
    return round((vowels * 100) / total, 1)


def analyze_text(text):
    """Retorna un string con formato: "V:{vowels} C:{consonants} T:{total} P:{percentage}%"
    Debe USAR todas las funciones anteriores."""
    vowels = count_vowels(text)
    consonants = count_consonants(text)
    total = total_letters(text)
    percentage = vowel_percentage(text)

    return f"V:{vowels} C:{consonants} T:{total} P:{percentage}%"
