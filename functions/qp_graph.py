import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Usa il backend TkAgg per interattività
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import logging
import os

# Configurazione del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Funzione per calcolare la distanza dall'origine in coordinate cartesiane
def f(x, y):
    return np.sqrt(x**2 + y**2)

# Funzione principale per plottare la capability curve V/Q
def plot_qp_graph(csv_inverter_data, csv_qp_points):
    try:
        # Caricamento dei dati dell'inverter da CSV
        df_inverter = pd.read_csv(csv_inverter_data)
        logging.info("Dati dell'inverter caricati correttamente.")
        # Caricamento dei dati dei punti QP da CSV
        df_points = pd.read_csv(csv_qp_points)
        logging.info("Dati dei punti QP caricati correttamente.")
    except Exception as e:
        logging.error(f"Errore nel caricamento dei dati da CSV: {e}")
        return
    
    # Setup del plot
    fig, ax = plt.subplots(figsize=(10, 9))
    
    # Assegnazione dei valori estratti dal dataframe
    first_row = df_inverter.iloc[0]
    pnd = first_row["Pnd"]
    qmax_plus = first_row["Qmax_plus"]
    qmax_minus = first_row["Qmax_minus"]
    smax = first_row["Smax"]
    qmax_med = (qmax_plus + qmax_minus) / 2
    qmax_radius = (qmax_plus - qmax_minus) / 2
    
    # Impostazione dei limiti degli assi
    x_max = max(abs(qmax_plus), abs(qmax_minus)) * 1.1
    y_max = max(abs(qmax_plus), abs(qmax_minus))
    ax.set_xlim(-x_max, x_max)
    ax.set_ylim(-y_max * 0.2, y_max * 1.8)
    logging.info("Limiti degli assi impostati.")
    
    # Aggiunta degli assi cartesiani
    ax.axhline(0, color='black', lw=1, alpha=0.5)
    ax.axvline(0, color='black', lw=1, alpha=0.5)
    logging.info("Assi cartesiani aggiunti.")
    
    # Labeling degli assi
    ax.set_xlabel('-Q (induttiva), +Q (capacitiva)')
    ax.set_ylabel('P')
    ax.set_xticks([-pnd * 0.35, pnd * 0.35, qmax_minus, qmax_plus])
    ax.set_xticklabels(['-35% Pnd', '35% Pnd', 'Qmin', 'Qmax'])
    ax.set_yticks([pnd * 0.1, pnd])
    ax.set_yticklabels(['10% Pnd', 'Pnd'])
    logging.info("Etichette degli assi impostate.")
    
    # Disegno della capability curve
    theta = np.linspace(0, np.pi, 1000)
    x_semicircle = qmax_med + qmax_radius * np.cos(theta)
    y_semicircle = qmax_radius * np.sin(theta)
    ax.plot(x_semicircle, y_semicircle, color='red', linestyle='-')
    
    # Colorazione dell'area sotto la capability curve
    upper_limit = np.minimum(y_semicircle, pnd)
    ax.fill_between(x_semicircle, 0.1 * pnd, upper_limit, where=(upper_limit >= 0.1 * pnd), color='red', alpha=0.15)
    logging.info("Semicirconferenza aggiunta.")

    # Disegno delle linee verticali tratteggiate e orizzontali per Pnd
    ax.axvline(-pnd * 0.35, color='black', lw=1, linestyle='--', alpha=0.25)
    ax.axvline(pnd * 0.35, color='black', lw=1, linestyle='--', alpha=0.25)
    ax.axhline(pnd, color='black', lw=1, linestyle='--', alpha=0.5)
    ax.axhline(0.1 * pnd, color='black', lw=1, linestyle='--', alpha=0.5)
    logging.info("Linee verticali e orizzontali tratteggiate aggiunte.")
    
    # Plottaggio dei punti QP
    for index, row in df_points.iterrows():
        ax.plot(row['q'], row['p'], marker='o', markersize=5, label=row['nome'])
    logging.info("Punti del CSV plottati.")

    # Personalizzazione dei tick
    ax.tick_params(axis='both', direction='out', length=4, width=1, colors='black', grid_color='black', grid_alpha=0.5)
    
    # Aggiunta della legenda
    ax.legend()
    logging.info("Legenda aggiunta.")
    
    # Visualizzazione del grafico
    plt.show()
    logging.info("Grafico visualizzato.")
