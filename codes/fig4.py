# === IMPORTS ===
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# === PARÁMETROS DEL GRÁFICO ===
figsize = (12, 10)
color_datos = "#0047AB"
color_baseline = "#808080"
color_ground_truth = "#FF0000"
estilo_linea = "-"
grosor_linea = 1.5

# === DATOS ===
t = np.linspace(0, 100, 200)
# Series temporales sintéticas
sig1 = np.sin(t/5) + np.random.normal(0, 0.1, 200)
sig2 = np.cos(t/5) + np.random.normal(0, 0.1, 200)
sig3 = np.sin(t/10) + np.random.normal(0, 0.1, 200)

# Datos de desempeño
noise_levels = np.linspace(0, 100, 10)
f1_prop = 0.8 - (noise_levels * 0.005)
f1_base = 0.75 - (noise_levels * 0.006)

# === FIGURA ===
fig = plt.figure(figsize=figsize)
gs = gridspec.GridSpec(3, 2, width_ratios=[1, 1], height_ratios=[1, 1, 1])

# Panel Izquierdo: Series temporales
labels_left = ['Temperature (C)', 'Voltage (V)', 'Attitude (deg)']
signals = [sig1, sig2, sig3]
for i in range(3):
    ax = fig.add_subplot(gs[i, 0])
    ax.plot(t, signals[i], color=color_datos, lw=grosor_linea)
    ax.set_ylabel(labels_left[i])
    ax.grid(True, linestyle='--', alpha=0.5)

# Panel Derecho Superior: Score
ax4 = fig.add_subplot(gs[0, 1])
ax4.set_title("Anomaly Score & Ground Truth")
ax4.plot(t, 0.5 + 0.2*np.sin(t/5), label="Anomaly Score", color=color_datos)
# ASUNCIÓN: Dibujo de cajas para Ground Truth
ax4.add_patch(plt.Rectangle((20, 0.3), 20, 0.4, color=color_ground_truth, alpha=0.2))
ax4.set_ylim(0, 1)

# Panel Derecho Medio/Inferior: Robustez
ax5 = fig.add_subplot(gs[1:, 1])
ax5.set_title("Robustness to Noise")
ax5.plot(noise_levels, f1_prop, label="Proposed Method", color=color_datos, marker='o', markersize=4)
ax5.plot(noise_levels, f1_base, label="Baseline LSTM", color=color_baseline, linestyle='--')
ax5.set_xlabel("Noise %")
ax5.set_ylabel("F1 Score")
ax5.legend()
ax5.grid(True, linestyle='--', alpha=0.5)

# === RENDER ===
plt.tight_layout()
plt.show()