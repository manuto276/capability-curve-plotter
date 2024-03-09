# Importazione delle librerie necessarie
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Usa il backend TkAgg per interattività

def plot_equation(ax, func, x_range, label=None, line_style='-', color='blue'):
    x = np.linspace(x_range[0], x_range[1], 500)
    y = func(x)
    ax.plot(x, y, label=label, linestyle=line_style, color=color) 

def plot_area_between_functions(ax, func1, func2, x_range, color_above='green', color_below='red'):
    x = np.linspace(x_range[0], x_range[1], 500)
    y1 = func1(x)
    y2 = func2(x)
    ax.fill_between(x, y1, y2, where=(y1>y2), facecolor=color_above, alpha=0.5, interpolate=True)  # Trasparenza modificata per visibilità
    ax.fill_between(x, y1, y2, where=(y1<=y2), facecolor=color_below, alpha=0.5, interpolate=True)  # Trasparenza modificata per visibilità

def plot_points(ax, points, point_labels=None, marker='o', color='black'):
    x, y = zip(*points)  # Estrae le coordinate x e y
    ax.scatter(x, y, marker=marker, color=color)  
    if point_labels:
        for (i, (px, py)) in enumerate(points):
            ax.text(px, py, point_labels[i])  