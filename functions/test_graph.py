# Importazione delle librerie necessarie
import numpy as np
import matplotlib
import logging
matplotlib.use('TkAgg')  # Usa il backend TkAgg per interattività
import matplotlib.pyplot as plt
from functions.common import plot_equation, plot_area_between_functions, plot_points
# Configurazione di matplotlib per utilizzare il backend TkAgg per l'interattività
matplotlib.use('TkAgg')

# Configurazione del logging per registrare informazioni utili durante l'esecuzione
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def f(x):
    """ Funzione che rappresenta y = sin(x). """
    return np.sin(x)

def g(x):
    """ Funzione che rappresenta y = cos(x). """
    return np.cos(x)

# Funzione principale per disegnare il grafico di test
def plot_test_graph():
    # Configurazione del plot con titoli degli assi e limiti
    logging.info("Configurazione del grafico in corso...")
    fig, ax = plt.subplots()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.axhline(0, color='black', lw=1, alpha=0.5)  # Asse orizzontale
    ax.axvline(0, color='black', lw=1, alpha=0.5)  # Asse verticale

    # Plottaggio delle funzioni sin(x) e cos(x) usando funzioni helper dalla libreria common
    logging.info("Plottaggio delle equazioni sin(x) e cos(x).")
    plot_equation(ax, f, (-2, 2), label='sin(x)', line_style='-', color='blue')
    plot_equation(ax, g, (-2, 2), label='cos(x)', line_style='--', color='orange')

    # Plottaggio dell'area tra le due funzioni
    logging.info("Plottaggio dell'area tra le funzioni.")
    plot_area_between_functions(ax, f, g, (-2, 2))

    # Definizione e plottaggio dei punti esemplificativi sul grafico
    points = [(1, 2), (2, 3), (3, 1)]
    point_labels = ['A', 'B', 'C']
    logging.info("Plottaggio dei punti esemplificativi.")
    plot_points(ax, points, point_labels=point_labels, marker='o', color='red')

    # Aggiunta delle frecce agli assi
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    ax.annotate('', xy=(xlim[1], 0), xytext=(xlim[1] - 0.1, 0),
                arrowprops=dict(facecolor='black', shrink=0.05, alpha=0.5))
    ax.annotate('', xy=(0, ylim[1]), xytext=(0, ylim[1] - 0.1),
                arrowprops=dict(facecolor='black', shrink=0.05, alpha=0.5))

    # Aggiunta delle etichette degli assi
    ax.text(xlim[1], 0.1, 'x', ha='center', va='center', alpha=0.5)
    ax.text(0.1, ylim[1], 'y', ha='center', va='center', alpha=0.5)

    # Visualizzazione della legenda e del grafico
    ax.legend()
    logging.info("Visualizzazione del grafico.")
    plt.show()
