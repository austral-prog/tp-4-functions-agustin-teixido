# ---- Funciones provistas (NO modificar) ----

def apply_discount(price, discount_pct):
    """Dado un precio y un porcentaje de descuento, retorna el precio con el descuento aplicado."""
    return price * (1 - discount_pct / 100)

def apply_tax(price, tax_pct):
    """Dado un precio y un porcentaje de impuesto, retorna el precio con el impuesto aplicado."""
    return price * (1 + tax_pct / 100)

# ---- Funciones a implementar ----


def final_price(presio, cantidad, descuento, impuesto):
    """
    Calculates final price:
    1. subtotal = price * quantity
    2. apply discount
    3. apply tax
    4. round to 2 decimals
    """
    subtotal = presio * cantidad
    con_descuento = apply_discount(subtotal, descuento)
    con_impuesto = apply_tax(con_descuento, impuesto)
    return round(con_impuesto, 2)


def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    """
    Returns "A" or "B" depending on which final price is lower.
    If equal, returns "A".
    """
    a = final_price(price_a, qty_a, disc_a, tax_pct)
    b = final_price(price_b, qty_b, disc_b, tax_pct)

    if a <= b:
        return "A"
    else:
        return "B"


