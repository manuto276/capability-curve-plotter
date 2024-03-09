import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Usa il backend TkAgg per interattività
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import logging

# Configurazione del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def plot_qv_graph(csv_path):
    try:
        # Tentativo di lettura del file CSV
        df_points = pd.read_csv(csv_path)
        logging.info("File CSV letto correttamente.")
    except FileNotFoundError:
        logging.error(f"Il percorso del file non è valido: {csv_path}")
        return
    except pd.errors.EmptyDataError:
        logging.error("Il file è vuoto.")
        return
    except pd.errors.ParserError:
        logging.error("Il contenuto del file non è valido.")
        return
    except Exception as e:
        logging.error(f"Si è verificato un errore nella lettura del file: {e}")
        return

    # Inizio della creazione del grafico
    fig, ax = plt.subplots(figsize=(10, 9))
    logging.info("Inizializzazione della figura matplotlib.")

    # Impostazione dei limiti degli assi
    ax.set_xlim(-0.55, 0.55)
    ax.set_ylim(0.85, 1.15)
    logging.info("Limiti degli assi impostati.")

    # Aggiunta degli assi cartesiani con trasparenza
    ax.axhline(1, color='black', lw=1, alpha=0.5)
    ax.axvline(0, color='black', lw=1, alpha=0.5)
    logging.info("Assi cartesiani aggiunti.")

    # Aggiunta delle linee orizzontali tratteggiate
    ax.axhline(1.05, color='black', lw=1, linestyle='--', alpha=0.25)
    ax.axhline(0.95, color='black', lw=1, linestyle='--', alpha=0.25)
    logging.info("Linee orizzontali tratteggiate aggiunte.")

    # Nomi degli assi
    ax.set_xlabel('Q/Pnd')
    ax.set_ylabel('V/Vnom')
    ax.set_xticks([-0.35, 0, 0.3])
    ax.set_xticklabels(['-0.35', '0', '0.3'])
    ax.set_yticks([0.9, 0.95, 1, 1.05, 1.1])
    ax.set_yticklabels(['0.9', '0.95', '1', '1.05', '1.1'])
    logging.info("Etichette degli assi impostate.")

    # Aggiunta del poligono con colore rosso e bordo opaco
    vertices = [(0.3, 0.9), (0.3, 1.05), (0, 1.1), (-0.35, 1.1), (-0.35, 0.95), (0, 0.9)]
    polygon = patches.Polygon(vertices, closed=True, facecolor=(1, 0, 0, 0.15), edgecolor='red', linewidth=1)
    ax.add_patch(polygon)
    logging.info("Poligono aggiunto.")

    # Plottare i punti letti dal file CSV
    for index, row in df_points.iterrows():
        ax.plot(row['q'], row['v'], marker='o', markersize=5, label=row['nome'])
    logging.info("Punti del CSV plottati.")

    # Aggiungere legenda per identificare i punti
    ax.legend()
    logging.info("Legenda aggiunta.")

    # Visualizzazione del grafico
    plt.show()
    logging.info("Grafico visualizzato.")