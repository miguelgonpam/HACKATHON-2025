def voraz(lote_w, lote_h, d, e, s):
    """
    lote_w: Ancho del lote
    lote_h: Alto del lote
    d     : Diámetro del lote
    e     : Separación entre neumáticos
    s     : Separación entre los neumáticos y los bordes del lote 
    """
    posiciones = []
    
    # Coordenadas iniciales
    x = s + d // 2
    while x + d // 2 <= lote_w - s:
        y = s + d // 2
        while y + d // 2 <= lote_h - s:
            posiciones.append((x, y))
            y += d + e  # Moverse en la dirección Y (vertical)
        x += d + e  # Moverse en la dirección X (horizontal)

    return posiciones

def backtracking(lote_w, lote_h, d, e, s, posiciones=[], max_posiciones=[]):
    """
    lote_w: Ancho del lote
    lote_h: Alto del lote
    d     : Diámetro del lote
    e     : Separación entre neumáticos
    s     : Separación entre los neumáticos y los bordes del lote 
    """
    if len(posiciones) > len(max_posiciones):
        max_posiciones[:] = posiciones[:]

    for x in range(s + d//2, lote_w - s - d//2 + 1, d + e):
        for y in range(s + d//2, lote_h - s - d//2 + 1, d + e):
            if all((x - px)**2 + (y - py)**2 >= (d + e)**2 for px, py in posiciones):
                posiciones.append((x, y))
                backtracking(lote_w, lote_h, d, e, s, posiciones, max_posiciones)
                posiciones.pop()

    return max_posiciones

