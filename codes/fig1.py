# === IMPORTS ===
import matplotlib.pyplot as plt
import numpy as np

# === PARÁMETROS DEL GRÁFICO ===
# Dimensiones y colores
figsize = (10, 10)
color_linea = "#2365a6"
color_anomalia = "#ffcccc"
color_score = "#808080"
color_umbral = "red"
alpha_sombreado = 0.5

# Datos temporales
t = np.linspace(0, 100, 500)
# ASUNCIÓN: Generación de señales sintéticas que emulan la estructura de picos y valles de la imagen
y_temp = 5 + 0.5 * np.sin(t/5)
y_volt = 5 + 0.5 * np.cos(t/5)
y_att = 0.5 * np.sin(t/10)
y_score = 0.5 + 0.1 * np.random.normal(size=len(t))

# Picos artificiales para anomalías
y_temp[100:150] += 5; y_temp[200:250] -= 5
y_volt[100:150] -= 5; y_volt[300:350] += 5
y_score[100:150] = 10; y_score[300:350] = 10

# === FIGURA ===
fig, axs = plt.subplots(4, 1, figsize=figsize, sharex=True, gridspec_kw={'hspace': 0.2})
fig.suptitle('Multivariate System Anomaly Detection', fontsize=16, fontweight='bold')

# Función para añadir sombreado
def add_shading(ax):
    ax.axvspan(20, 40, color=color_anomalia, alpha=alpha_sombreado)
    ax.axvspan(70, 90, color=color_anomalia, alpha=alpha_sombreado)

# Plotting
axs[0].plot(t, y_temp, color=color_linea)
axs[0].set_ylabel('Temperature (C)')
add_shading(axs[0])

axs[1].plot(t, y_volt, color=color_linea)
axs[1].set_ylabel('Voltage (V)')
add_shading(axs[1])

axs[2].plot(t, y_att, color=color_linea)
axs[2].set_ylabel('Attitude (deg)')
add_shading(axs[2])

axs[3].plot(t, y_score, color=color_score)
axs[3].axhline(y=5, color=color_umbral, linestyle='--', label='Critical Threshold')
axs[3].set_ylabel('Anomaly Score')
axs[3].set_xlabel('Time (s)')

# Configuración estética
for ax in axs:
    ax.grid(axis='y', linestyle='-', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# === RENDER ===
plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.show()