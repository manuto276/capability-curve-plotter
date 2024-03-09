import os
import logging
from tkinter import Tk, Label, Button
from tkinter.ttk import Style
from ttkthemes import ThemedTk
from functions.qp_graph import plot_qp_graph
from functions.qv_graph import plot_qv_graph
from functions.test_graph import plot_test_graph

# Configurazione del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def display_qp_graph():
    try:
        inverter_data_csv = os.path.join(os.path.dirname(__file__), "data/inverter_data.csv")
        qp_points_csv = os.path.join(os.path.dirname(__file__), "data/qp_points.csv")
        plot_qp_graph(inverter_data_csv, qp_points_csv)
    except Exception as e:
        logging.error(f"Errore durante la visualizzazione del grafico della capability curve P/Q: {e}")

def display_qv_graph():
    try:
        qv_points_csv = os.path.join(os.path.dirname(__file__), "data/qv_points.csv")
        plot_qv_graph(qv_points_csv)
    except Exception as e:
        logging.error(f"Errore durante la visualizzazione del grafico della capability curve V/Q: {e}")

def display_test_graph():
    try:
        plot_test_graph()
    except Exception as e:
        logging.error(f"Errore durante la visualizzazione del grafico test: {e}")

def create_menu_window():
    window = ThemedTk(theme="arc")  # Usa il tema 'arc' che è vicino al Material Design
    window.title("Capability Curve Visualizer")

    style = Style(window)
    style.configure('TButton', padding=6, font=('Roboto', 10))
    style.configure('TLabel', padding=6, font=('Roboto', 12))

    Label(window, text="Seleziona il grafico da visualizzare:").pack(pady=10)
    
    Button(window, text="Mostra il grafico della capability curve P/Q", command=display_qp_graph).pack(fill='x', padx=20, pady=5)
    Button(window, text="Mostra il grafico della capability curve V/Q", command=display_qv_graph).pack(fill='x', padx=20, pady=5)
    Button(window, text="Mostra il grafico test", command=display_test_graph).pack(fill='x', padx=20, pady=5)
    Button(window, text="Termina lo script", command=window.destroy).pack(fill='x', padx=20, pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_menu_window()
