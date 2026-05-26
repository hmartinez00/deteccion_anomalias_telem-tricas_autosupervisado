### **FASE 1: Mapeo de Entidades (Análisis)**

* **Dominio:** Diagnóstico de Fallos y Edge Computing Aeroespacial (Mantenimiento Predictivo de Satélites).
* **Componentes clave del LaTeX:** Series temporales multivariadas telemétricas (temperatura, voltaje, actitud), señal nominal frente a eventos anómalos escasos/ocultos, curva de reconstrucción generada por el Autoencoder Variacional Temporal (VAE) y una señal matemática derivada de puntuación de anomalía (*anomaly score*).
* **Nivel de Abstracción:** Representación analítica/fenomenológica de señales físicas e inferencia estadística temporal.

---

### **FASE 2: Auditoría y Reporte de Hallazgos Críticos**

1. **Contraste de Coherencia:** El prompt base describe bien el esqueleto de un gráfico de telemetría, pero introduce una seria contradicción estética y técnica con las reglas del estándar IEEE y el texto de la investigación.
2. **LISTA DE DISCREPANCIAS (Elementos vitales del LaTeX ausentes o erróneos en el prompt base):**
* **Inclusión de Colores Prohibidos (Crítico):** El prompt base pide "regiones sombreadas en rojo claro". Esto viola explícitamente la paleta técnica unificada (#0047AB, #4A4A4A, negro y blanco) acordada para mantener la sobriedad editorial de la revista. El sombreado de la anomalía debe resolverse mediante contraste cromático dentro de la paleta permitida o mediante una textura geométrica discreta.
* **Interacción entre Señal Real y Reconstrucción VAE:** El texto técnico menciona "la reconstrucción del modelo". El gráfico propuesto no muestra la interacción matemática entre ambas. Para visualizar un Autoencoder, es vital que la curva de reconstrucción (Gris #4A4A4A) se superponga perfectamente a la señal real (Azul #0047AB) en las zonas nominales, y que diverja drásticamente *únicamente* en el fragmento temporal donde ocurre la anomalía.
* **El Umbral de la Puntuación de Anomalía:** El gráfico de puntuación (*anomaly score*) inferior necesita un límite de decisión. Científicamente, una puntuación de anomalía no tiene sentido visual sin una línea de umbral (*threshold*); cuando la curva de puntuación cruza esa línea discontinua, coincide exactamente con la proyección vertical del evento anómalo.


3. **Control de Estilo:** Rigor IEEE absoluto. Sin gradientes, sin sombras, líneas vectoriales finas y **ausencia total de texto o etiquetas incrustadas** (los nombres de las variables se omiten o sustituyen por placeholders geométricos limpios).

---

### **FASE 3: Explicación y Justificación de Pre-ejecución**

#### 1. Disposición Espacial y Elementos Gráficos

La figura se estructurará verticalmente como un bloque de sub-gráficas alineadas temporalmente (eje X compartido implicitamente en orientación *landscape*):

* **Sub-gráfica Superior (Telemetría Multivariada):** Tres canales o filas horizontales independientes. Cada fila tendrá una señal continua fina en azul cobalto (#0047AB). En el tercio central del eje temporal, las señales sufrirán una alteración (picos, caídas o ruido de alta frecuencia). Sobre esa perturbación se superpondrá una curva discontinua en gris técnico (#4A4A4A) que continuará recta (la reconstrucción nominal del VAE), evidenciando el error de seguimiento. Un recuadro delimitador con un entramado de líneas verticales finas en gris marcará verticalmente la duración del evento.
* **Sub-gráfica Inferior (Anomaly Score):** Una única señal matemática en azul cobalto que se mantiene plana y baja durante las fases normales, pero se dispara con una pendiente pronunciada hacia un pico agudo exactamente debajo del recuadro del evento. Una línea horizontal discontinua negra cruzará este gráfico para denotar el umbral de disparo operativo.

#### 2. Justificación Técnica

Esta composición traduce perfectamente el funcionamiento del modelo autosupervisado. Al no contar con etiquetas previas, el sistema detecta la anomalía porque la realidad (señal azul) se desvía de lo que el Autoencoder predijo como normal (señal gris), lo que eleva el *score* por encima del umbral. El revisor técnico identificará este enfoque de inmediato sin requerir etiquetas de texto explicativas.

#### 3. ADVERTENCIAS PARA EL USUARIO (Puntos de validación)

* **Sustitución del Rojo:** La zona anómala se identificará mediante el patrón de rejilla/entramado vertical gris y la divergencia de las curvas, eliminando el rojo del prompt base. Confirma si esta codificación gráfica te parece adecuada para la estética de tu documento.
* **Representación Multivariada:** He limitado los canales a tres (Temperatura, Voltaje, Actitud) para evitar saturar el espacio visual del gráfico y garantizar la nitidez de los vectores.

---

### **FASE 4: Ejecución Silenciosa**

Tengo lista la formulación del prompt matemático-vectorial para `fig1.png`. Por favor, indícame si estás conforme con las modificaciones de la auditoría y la eliminación del color rojo para proceder a entregarte los bloques de código limpios.


```text
Gráfico analítico en 2D de series temporales telemétricas, diagrama técnico de ingeniería de sistemas espaciales, diseño plano y minimalista, fondo blanco puro, paleta de colores estricta en azul cobalto (#0047AB) y gris técnico (#4A4A4A) con líneas finas en negro neutro. Sin sombras, sin gradientes, sin relieve tridimensional. La composición consta de dos sub-gráficas alineadas verticalmente que comparten el mismo eje de tiempo horizontal de izquierda a derecha. La sub-gráfica superior contiene tres canales independientes superpuestos de señales telemétricas multivariadas; cada señal está representada por una línea continua fina en azul cobalto (#0047AB) que se desplaza de forma nominal, excepto en el tercio central donde sufre una perturbación abrupta. En esa sección alterada, una segunda línea discontinua fina en gris técnico (#4A4A4A) continúa con la trayectoria normalizada para representar la reconstrucción del modelo, divergiendo de la señal azul. Un recuadro delimitador vertical con un patrón de líneas paralelas finas y tenues en gris enmarca la zona de esta desviación. La sub-gráfica inferior muestra una curva matemática continua en azul cobalto que permanece plana al inicio, pero se dispara verticalmente en un pico agudo coincidiendo con la posición exacta del recuadro de la anomalía superior. Una línea horizontal discontinua y delgada en negro cruza esta gráfica inferior para denotar el umbral de detección. Todo el texto, números, nombres de variables y etiquetas alfabéticas están completamente ausentes, sustituidos únicamente por placeholders geométricos limpios. Orientación landscape técnica, estilo de publicación IEEE.

```

```text
2D analytical telemetry time-series graph, aerospace systems engineering technical diagram, flat design, minimalist, pure white background, strict color palette of cobalt blue (#0047AB) and technical gray (#4A4A4A) with crisp neutral black fine lines. No shadows, no gradients, no three-dimensional reflections. The composition consists of two vertically stacked and aligned sub-charts sharing a synchronized horizontal time axis from left to right. The upper sub-chart displays three independent rows of multivariate telemetry signal lines; each signal is rendered as a fine solid line in cobalt blue (#0047AB) running nominally, except during the middle third section where it undergoes an abrupt disturbance. Within this altered section, a second fine dashed line in technical gray (#4A4A4A) maintains the normal trajectory to represent the model reconstruction, diverging from the blue line. A clear vertical bounding box filled with a faint, thin vertical line pattern frames the duration of this anomaly event. The lower sub-chart displays a single continuous analytical curve in cobalt blue that remains flat and low at first, but shoots up dynamically into a sharp spike perfectly aligned beneath the upper anomaly box. A thin horizontal dashed line in black crosses this lower plot to denote the mathematical detection threshold. Entirely free of text, numbers, axis labels, or typography, using only sharp vector shapes and clean geometric placeholders. Technical landscape orientation, pristine IEEE publication style.

```