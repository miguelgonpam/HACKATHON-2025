import math


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

    for x in range(s + d // 2, lote_w - s - d // 2 + 1, d + e):
        for y in range(s + d // 2, lote_h - s - d // 2 + 1, d + e):
            if all((x - px) ** 2 + (y - py) ** 2 >= (d + e) ** 2 for px, py in posiciones):
                posiciones.append((round(x, 2), round(y, 2)))
                backtracking(lote_w, lote_h, d, e, s, posiciones, max_posiciones)
                posiciones.pop()

    return max_posiciones


def distribucion_hexagonal_neumaticos(ancho_lote, largo_lote, diametro_neumatico, espacio_entre_neumaticos, separacion_bordes):
    coordenadas = []

    # Radio del neumático
    radio = diametro_neumatico / 2

    # Distancia entre centros (considerando espacio entre neumáticos)
    distancia_x = diametro_neumatico + espacio_entre_neumaticos
    distancia_y = math.sqrt(3) * radio + espacio_entre_neumaticos

    # Ajustar límites considerando separación de bordes
    x_inicio = separacion_bordes + radio
    y_inicio = separacion_bordes + radio
    x_fin = ancho_lote - separacion_bordes
    y_fin = largo_lote - separacion_bordes

    # Iniciar en las coordenadas del primer neumático
    x, y = x_inicio, y_inicio
    fila = 0

    while y + radio <= y_fin:
        # Desplazamiento horizontal alternado (efecto panal)
        x = x_inicio + (fila % 2) * (distancia_x / 2)

        while x + radio <= x_fin:
            # Añadir coordenadas del centro del neumático
            coordenadas.append((round(x, 2), round(y, 2)))
            x += distancia_x

        # Avanzar a la siguiente fila
        y += distancia_y
        fila += 1

    return coordenadas


def distribucion_maxima_densidad(ancho_lote, largo_lote, diametro_neumatico, espacio_entre_neumaticos,
                                 separacion_bordes):
    radio = diametro_neumatico / 2

    # Distancia entre centros de neumáticos
    paso_x = diametro_neumatico + espacio_entre_neumaticos
    paso_y = diametro_neumatico + espacio_entre_neumaticos

    # Ajustar límites considerando separación de bordes
    x_inicio = separacion_bordes + radio
    y_inicio = separacion_bordes + radio
    x_fin = ancho_lote - separacion_bordes
    y_fin = largo_lote - separacion_bordes

    coordenadas = []

    y = y_inicio
    fila = 0

    while y + radio <= y_fin:
        x = x_inicio

        # Desplazamiento alternado para máxima densidad
        if fila % 2 != 0:
            x += paso_x / 2

        while x + radio <= x_fin:
            # Verificar que el neumático esté completamente dentro del lote
            coordenadas.append((round(x, 2), round(y, 2)))

            x += paso_x

        y += paso_y
        fila += 1

    return coordenadas


def optimizar_distribucion_neumaticos(ancho_lote, largo_lote, diametro_neumatico, espacio_entre_neumaticos,
                                      separacion_bordes):
    radio = diametro_neumatico / 2

    # Ajustar límites considerando separación de bordes
    x_inicio = separacion_bordes + radio
    y_inicio = separacion_bordes + radio
    x_fin = ancho_lote - separacion_bordes
    y_fin = largo_lote - separacion_bordes

    # Calcular paso considerando radio y espacio
    paso_x = diametro_neumatico + espacio_entre_neumaticos
    paso_y = diametro_neumatico + espacio_entre_neumaticos

    coordenadas = []

    # Comenzar desde el borde
    y = y_inicio
    while y + radio <= y_fin:
        x = x_inicio

        while x + radio <= x_fin:
            # Verificaciones de límites y colisiones
            if no_hay_colision(coordenadas, x, y, radio):
                coordenadas.append((x, y))

            x += paso_x

        y += paso_y

    return coordenadas


def no_hay_colision(coordenadas_existentes, x_nuevo, y_nuevo, radio):
    for x, y in coordenadas_existentes:
        distancia = math.sqrt((x - x_nuevo) ** 2 + (y - y_nuevo) ** 2)
        if distancia < 2 * radio:
            return False
    return True