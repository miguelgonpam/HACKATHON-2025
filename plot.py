import matplotlib.pyplot as plt
import numpy as np

def plot_neumaticos(lote_w, lote_h, d, posiciones):
    """
    Genera un gráfico de un lote con neumáticos en posiciones dadas.
    
    :param lote_w: Ancho del lote.
    :param lote_h: Alto del lote.
    :param d: Diámetro de los neumáticos.
    :param posiciones: Lista de tuplas con las coordenadas de los centros de los neumáticos.
    """
    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(6, 12))
    ax.set_xlim(0, lote_w)
    ax.set_ylim(0, lote_h)
    ax.set_xticks(np.arange(0, lote_w + 10, 10))
    ax.set_yticks(np.arange(0, lote_h + 10, 10))
    ax.grid(True, linestyle="--", alpha=0.5)

    # Dibujar el lote como un rectángulo
    ax.add_patch(plt.Rectangle((0, 0), lote_w, lote_h, fill=False, edgecolor="black", linewidth=2))

    # Dibujar los neumáticos
    for (x, y) in posiciones:
        ax.add_patch(plt.Circle((x, y), d / 2, fill=True, color="blue", alpha=0.5, edgecolor="black"))
        ax.plot(x, y, 'ro')  # Marcar el centro con un punto rojo
        ax.text(x, y, f"({x},{y})", fontsize=10, ha='right', color="red")

    # Agregar etiquetas de dimensiones
    ax.annotate("", xy=(lote_w, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="<->", color="black"))
    ax.text(lote_w / 2, -10, f"Ancho: {lote_w}", ha='center', fontsize=12, color="black")

    ax.annotate("", xy=(0, lote_h), xytext=(0, 0), arrowprops=dict(arrowstyle="<->", color="black"))
    ax.text(-15, lote_h / 2, f"Alto: {lote_h}", va='center', rotation=90, fontsize=12, color="black")

    # Mostrar el gráfico
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Distribución de neumáticos en el lote")
    plt.show()
