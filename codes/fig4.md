### **FASE 1: Mapeo de Entidades (Análisis)**

* **Dominio:** Validación Fenomenológica de Detección de Anomalías / Procesamiento de Telemetría Satelital On-board.
* **Componentes clave del LaTeX:** Estructura secuencial de arriba a abajo (`de arriba abajo` según la descripción de la leyenda de la figura). 1) Señal original multivariada (proveniente del benchmark OPS-SAT), 2) Puntuación de anomalía calculada en inferencia optimizada (<4.7 ms, <1.8W) y 3) Línea base de *Ground Truth* (Verdad de Terreno). El texto enfatiza la capacidad de aislar anomalías sutiles y contextuales.
* **Nivel de Abstracción:** Validación fenomenológica comparativa (Alineación temporal de variables físicas e índices de inferencia).

---

### **FASE 2: Auditoría y Reporte de Hallazgos Críticos**

1. **Contraste de Coherencia:** El prompt base asume una disposición genérica ("Paneles verticales o en grid"), lo cual introduce ambigüedad. El texto de la descripción (`\caption`) exige un orden estrictamente vertical descendente. Además, al igual que en la figura 1, el prompt base vuelve a arrastrar el error analítico de introducir el color rojo ("línea roja con umbral"), rompiendo el acuerdo cromático institucional.
2. **LISTA DE DISCREPANCIAS (Elementos vitales del LaTeX ausentes en el prompt base):**
* **Violación de la Restricción de Color (Rojo):** El uso de "línea roja" en el prompt base está prohibido bajo la paleta estricta de la IEEE solicitada (#0047AB, #4A4A4A). La puntuación de anomalía debe resolverse en azul cobalto con su umbral en línea discontinua negra.
* **Ausencia de Alineación Síncrona Temporal:** El prompt base pide "ejemplos de anomalías sutiles y evidentes" sin estructurar su correlación. Científicamente, los tres paneles deben compartir un eje X implícito idéntico (tiempo). Si la señal original sufre una perturbación sutil en la coordenada $X_1$, la curva de puntuación del panel intermedio debe registrar un pico que cruce el umbral exactamente en $X_1$, y la barra del *Ground Truth* en el panel inferior debe cubrir con precisión la misma ventana temporal $X_1$.
* **Representación de la Anomalía Sutil frente a la Evidente:** El texto destaca el éxito en anomalías contextuales y sutiles. La serie multivariada inicial debe mostrar dos eventos: uno obvio (un pico masivo fuera de rango) y uno sutil (un cambio de fase o pérdida de correlación donde los valores se mantienen dentro del rango normal pero alteran su frecuencia), demostrando la robustez del mecanismo de atención frente al simple análisis de umbrales estáticos de la *Tabla I*.


3. **Control de Estilo:** Estricto cumplimiento de la norma IEEE. Gráficos planos en 2D, rejillas de coordenadas muy tenues, formas vectoriales nítidas y **remoción absoluta de cualquier etiqueta, número o carácter alfabético incrustado**.

---

### **FASE 3: Explicación y Justificación de Pre-ejecución**

#### 1. Disposición Espacial y Elementos Gráficos

La figura se estructurará como una columna vertical de tres sub-gráficas rectangulares idénticas y alineadas horizontalmente (*Landscape*):

* **Panel Superior (Señal Original):** Dos canales telemétricos (líneas continuas finas). El canal 1 (azul cobalto #0047AB) mostrará una anomalía evidente (un pulso cuadrado o pico extremo). El canal 2 (gris técnico #4A4A4A) mostrará una anomalía sutil (una oscilación sinusoidal repetitiva que cambia bruscamente de frecuencia en la misma ventana temporal sin alterar su amplitud máxima).
* **Panel Intermedio (Puntuación de Anomalía):** Una línea analítica en azul cobalto. Registrará un pico masivo que satura el gráfico durante la anomalía evidente y un pico más moderado pero claramente definido que cruza una línea horizontal discontinua negra (el umbral) durante la anomalía sutil.
* **Panel Inferior (Ground Truth):** Una barra de estado horizontal segmentada. El fondo es blanco puro y dos bloques rectangulares sólidos en gris técnico (#4A4A4A) marcarán las ventanas de tiempo exactas donde ocurrieron los dos fenómenos, validando el acierto del modelo.

#### 2. Justificación Técnica

Esta disposición en tres etapas indexadas por el tiempo es el estándar riguroso de visualización en la literatura de procesamiento de señales e inteligencia artificial aeroespacial. Permite demostrar visualmente cómo el *Framework propuesto* logra convertir perturbaciones físicas complejas en el dominio del tiempo en clasificaciones binarias discretas correctas sin depender de explicaciones textuales complejas.

#### 3. ADVERTENCIAS PARA EL USUARIO (Puntos de validación)

* **Reemplazo Cromático Definitivo:** Toda identificación de zonas críticas se delega a la alineación geométrica vertical y al cambio de estado de la barra inferior del *Ground Truth*. No existirá el color rojo en el lienzo final.
* **Simplificación Multivariada:** Se reducen a dos los canales de señales en el panel superior para evitar el solapamiento caótico de vectores en la generación automática, manteniendo la legibilidad de la sutil anomalía de frecuencia.

---

### **FASE 4: Ejecución Silenciosa**

Tengo normalizada la configuración geométrica y espacial para `fig4.png`. Por favor, facilítame tu confirmación para proceder con el despliegue de los códigos de prompt correspondientes.


```text
Gráfico analítico en 2D de series temporales alineadas, diagrama técnico de evaluación de algoritmos aeroespaciales, diseño plano y minimalista, fondo blanco puro, paleta de colores estricta en azul cobalto (#0047AB) y gris técnico (#4A4A4A) con líneas finas en negro neutro. Sin sombras, sin gradientes, sin relieve tridimensional. La composición consiste en tres sub-gráficas rectangulares idénticas apiladas en una columna vertical exacta, compartiendo un eje horizontal de tiempo síncrono de izquierda a derecha. El panel superior ("Señal Original") muestra dos líneas de canales telemétricos: la primera en azul cobalto presenta un pico masivo extremo fuera de rango en el primer tercio del tiempo, y la segunda en gris técnico muestra una oscilación constante que altera bruscamente su frecuencia en el segundo tercio del tiempo. El panel intermedio ("Puntuación de Anomalía") muestra una línea continua en azul cobalto que genera un pico vertical muy alto debajo del primer evento y un segundo pico moderado pero claro debajo del segundo evento; una línea horizontal discontinua y delgada en negro cruza todo este panel para marcar el umbral matemático. El panel inferior ("Ground Truth") consiste en una barra horizontal limpia donde dos bloques rectangulares sólidos en gris técnico (#4A4A4A) delimitan exactamente los dos intervalos temporales de los eventos anómalos. Todo el texto, etiquetas de ejes, números y caracteres alfabéticos están completamente ausentes, sustituidos únicamente por formas vectoriales nítidas y placeholders geométricos limpios. Orientación landscape técnica, estilo de publicación IEEE.

```

```text
2D analytical aligned time-series graph, aerospace algorithm evaluation technical diagram, flat design, minimalist, pure white background, strict color palette of cobalt blue (#0047AB) and technical gray (#4A4A4A) with crisp neutral black fine lines. No shadows, no gradients, no three-dimensional reflections. The composition consists of three identical rectangular sub-charts stacked in a precise vertical column, sharing a synchronized horizontal time axis from left to right. The upper panel ("Original Signal") displays two telemetry channel lines: the first in cobalt blue features an extreme, out-of-range massive spike during the first third of the timeline, and the second in technical gray displays a steady oscillation that abruptly changes frequency during the second third of the timeline. The middle panel ("Anomaly Score") shows a single continuous curve in cobalt blue that shoots up into a very high vertical spike under the first event and a second moderate but distinct spike under the second event; a thin horizontal dashed line in black crosses this entire plot to denote the mathematical threshold. The lower panel ("Ground Truth") consists of a clean horizontal bar where two solid rectangular blocks in technical gray (#4A4A4A) precisely delimit the two temporal intervals of the anomalous events. Entirely free of text, axis labels, numbers, or alphabetical characters, using only sharp vector shapes and clean geometric placeholders. Technical landscape orientation, pristine IEEE publication style.

```