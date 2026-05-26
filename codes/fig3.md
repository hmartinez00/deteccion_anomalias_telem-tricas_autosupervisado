### **FASE 1: Mapeo de Entidades (Análisis)**

* **Dominio:** Ingeniería de Software de Vuelo / Pipelines de Aprendizaje Automático en Edge para Sistemas Satelitales.
* **Componentes clave del LaTeX:** Limpieza e interpolación de telemetría bruta, división en ventanas deslizantes (*Windowing* con 50% de solapamiento), rama de *Data Augmentations* (Jitter, Masking, Escalado, Permutación), bucle/etapa de entrenamiento híbrido multiobjetivo ($\mathcal{L}_{rec} + \beta\mathcal{L}_{KL} + \lambda\mathcal{L}_{contrastive}$), optimización de modelo (*Pruning* estructurado y cuantización INT8) y despliegue final en hardware embebido (*Edge Inferencia*) asistido por un mecanismo de parada temprana (*Early Stopping*) basado en el *Anomaly Score*.
* **Nivel de Abstracción:** Tubería de datos arquitectónica y de ciclo de vida (*End-to-End MLOps Pipeline* en sistemas embebidos críticos).

---

### **FASE 2: Auditoría y Reporte de Hallazgos Críticos**

1. **Contraste de Coherencia:** El prompt base asume una secuencia lineal uniforme de izquierda a derecha. Sin embargo, el texto técnico describe procesos que rompen esta linealidad: las *Augmentations* alimentan la pérdida contrastiva del entrenamiento pero no la reconstructiva del VAE de forma directa, y la inferencia embebida incluye un lazo de control crítico de ahorro de energía (*Early Stopping*) que altera el flujo regular.
2. **LISTA DE DISCREPANCIAS (Elementos vitales del LaTeX ausentes en el prompt base):**
* **El Lazo de Retroalimentación de Early Stopping (Crítico):** La sección 4.3 menciona explícitamente "técnicas de early stopping basado en puntuaciones de anomalía para ahorrar ciclos de cómputo en periodos nominales". El prompt base carece de esta lógica condicional. Debe existir un lazo físico (flecha de retorno) que conecte el bloque del *Anomaly Score* final de vuelta al inicio del procesamiento de la ventana o al módulo de inferencia para simbolizar la detención prematura/salto de ciclo.
* **Visualización Geométrica del Solapamiento (50% Windowing):** El bloque de preprocesamiento no puede ser un rectángulo plano genérico. Para reflejar la precisión técnica del texto, debe graficarse la descomposición de la serie temporal continua en una pila de bloques horizontales desfasados exactamente a la mitad de su longitud.
* **Bucle de Optimización del Modelo:** El paso de "Training" a "Optimized Model" implica que las optimizaciones (*Pruning* estructurado y *Quantization-Aware Training*) se ejecutan en concordancia con el entrenamiento. Se requiere un bloque de transición que muestre una reducción o compresión geométrica antes de la inferencia edge.


3. **Control de Estilo:** Cumplimiento riguroso de la especificación técnica IEEE. Paleta de colores hermética (#0047AB, #4A4A4A, negro y fondo blanco puro), vectores planos bidimensionales y **exclusión absoluta de cualquier carácter textual o etiqueta alfabética**.

---

### **FASE 3: Explicación y Justificación de Pre-ejecución**

#### 1. Disposición Espacial y Conectores de Flujo

El diagrama se presentará en formato horizontal extenso (*Landscape*), estructurado de la siguiente manera:

* **Módulo A: Preprocesamiento (Izquierda):** Una señal continua entra a un primer sub-bloque de normalización, el cual se conecta a una representación abstracta de ventanas deslizantes (tres rectángulos horizontales escalonados y superpuestos al 50%).
* **Módulo B: Núcleo de Entrenamiento (Centro):** El flujo se divide. Una rama recta va al bloque del VAE (representado por una forma trapezoidal de compresión/descompresión latente); una rama paralela inferior se bifurca hacia tres iconos de líneas distorsionadas (las *augmentations*), las cuales se conectan a un bloque de pérdida contrastiva. Ambas ramas se consolidan en un nodo de optimización unificado.
* **Módulo C: Compresión e Inferencia Edge (Derecha):** El modelo entrenado pasa a través de un icono de filtrado/podado (mallas de nodos que pierden conexiones) hacia el bloque de hardware embebido (un microcontrolador/CPU plano simplificado).
* **Módulo D: Lazo Condicional de Salida:** La salida genera una curva con un pico (el *score*). Desde este nodo terminal, nace una flecha técnica fina en gris (#4A4A4A) que viaja de regreso en sentido inverso (lazo inferior) hacia el bloque de hardware embebido, denotando el desvío/parada de cómputo (*Early Stopping*).

#### 2. Justificación Técnica

Este diseño no es una simple lista de pasos; es la representación funcional del software de vuelo propuesto. Explicitar el solapamiento al 50% y, sobre todo, el bucle de retroalimentación del *Early Stopping* justifica de forma visual cómo el sistema logra mitigar las restricciones energéticas estrictas de los CubeSats descritas en la metodología.

#### 3. ADVERTENCIAS PARA EL USUARIO (Puntos de validación)

* **Ausencia de Texto:** Conceptos complejos como "TensorRT", "VAE" o "INT8 Quantization" se expresarán mediante morfología de formas (por ejemplo, el reescalado del bloque del modelo para INT8). Al compilar tu documento en LaTeX, el texto de la `\caption{}` deberá detallar exhaustivamente la leyenda visual de estos módulos.
* **Flujo de Early Stopping:** El lazo de retorno se ha diseñado hacia el bloque de inferencia para representar el ahorro de ciclos de reloj de la CPU a bordo. Confirma si esta lógica de arquitectura de computadoras espaciales se alinea perfectamente con tu desarrollo de software.

---

### **FASE 4: Ejecución Silenciosa**

Tengo configurada la gramática geométrica definitiva para `fig3.png`. Por favor, facilítame tu aprobación para proceder a redactar los dos bloques de código con los prompts optimizados.


```text
Diagrama de flujo técnico y arquitectónico en 2D, esquema de pipeline de datos e ingeniería de software para sistemas espaciales, diseño plano y minimalista, fondo blanco puro, paleta de colores estricta en azul cobalto (#0047AB) y gris técnico (#4A4A4A) con líneas finas en negro neutro. Sin sombras, sin gradientes, sin reflejos tridimensionales. Disposición horizontal en orientación landscape que se lee de izquierda a derecha. En el extremo izquierdo, una línea de señal continua entra a un bloque de preprocesamiento estructurado como una pila vertical de tres rectángulos horizontales desfasados y solapados exactamente al 50%. A continuación, el flujo se bifurca en dos caminos paralelos en el centro: la rama superior entra a un bloque trapezoidal simétrico de compresión central, y la rama inferior entra a un nodo que se divide en tres líneas distorsionadas e interrumpidas de forma aleatoria, convergiendo ambas ramas en un nodo cuadrado unificado. El flujo avanza hacia la derecha cruzando un icono de red de nodos donde varias conexiones internas son eliminadas con líneas discontinuas finas, conectando directamente con un bloque plano con el patrón geométrico de una CPU o microcontrolador embebido. Del bloque de hardware nace la señal de salida final en forma de una curva analítica delgada con un pico agudo. Desde el punto terminal de esta curva, una flecha técnica fina en gris técnico (#4A4A4A) forma un lazo de retorno inferior continuo en sentido inverso que se reconecta directamente con el lateral del bloque de la CPU, indicando un bucle condicional de parada. Todo el texto, números y etiquetas alfabéticas están completamente ausentes, sustituidos únicamente por formas vectoriales nítidas y placeholders geométricos limpios, bajo el estándar de publicación IEEE.

```

```text
2D technical and architectural flowchart, data pipeline and software engineering schematic for space systems, flat design, minimalist, pure white background, strict color palette of cobalt blue (#0047AB) and technical gray (#4A4A4A) with crisp neutral black fine lines. No shadows, no gradients, no three-dimensional reflections. Horizontal landscape orientation layout reading from left to right. On the far left, a continuous signal line enters a preprocessing block structured as a vertical stack of three horizontal rectangles, offset and overlapped exactly at 50%. Next, the flow bifurcates into two parallel paths in the center: the upper branch enters a symmetrical trapezoidal block with central pinching, and the lower branch enters a node that splits into three randomly distorted, broken lines, with both branches then converging into a unified square node. The flow proceeds to the right, passing through a node network icon where several internal connections are removed with thin dashed lines, connecting directly into a flat block styled as an embedded CPU or microcontroller. From this hardware block emerges the final output signal rendered as a fine analytical curve with a sharp spike. From the terminal point of this curve, a thin technical gray (#4A4A4A) arrow forms a continuous lower feedback loop running in the reverse direction, reconnecting directly into the side of the CPU block to indicate a conditional stopping loop. Entirely free of text, numbers, or alphabetical labels, using only sharp vector shapes and clean geometric placeholders. Pristine IEEE publication style.

```