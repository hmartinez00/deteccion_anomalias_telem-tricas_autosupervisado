### **FASE 1: Mapeo de Entidades (Análisis)**

* **Dominio:** Aprendizaje Autosupervisado y Arquitectura de Redes Profundas Embarcadas (Modelado Probabilístico de Series Temporales).
* **Componentes clave del LaTeX:** Ventanas deslizantes de telemetría multivariada, *Encoder* temporal (Conv1D + BiLSTM), Espacio Latente Variacional (*Reparameterization Trick*), Mecanismo de Atención Multi-Cabeza (Inter-variable y temporal), Rama de Aprendizaje Contrastivo (con *Data Augmentations* específicas como ruido, *masking*, escalado y permutación), *Decoder* Simétrico de Reconstrucción.
* **Nivel de Abstracción:** Arquitectura de red neuronal compleja (Flujo lógico de tensores y optimización multiobjetivo).

---

### **FASE 2: Auditoría y Reporte de Hallazgos Críticos**

1. **Contraste de Coherencia:** El prompt base asume una secuencia puramente lineal. Sin embargo, el texto describe una función de pérdida compuesta por tres términos basándose en la ecuación (\ref{eq:total_loss}). La arquitectura propuesta no es una tubería simple; es un modelo con **bifurcaciones paralelas** (una rama generativa/reconstructiva y una rama contrastiva) que convergen matemáticamente en la optimización.
2. **LISTA DE DISCREPANCIAS (Elementos vitales del LaTeX ausentes en el prompt base):**
* **La Bifurcación Dual Posterior al Espacio Latente (Crítico):** El prompt base sugiere que el módulo de atención va antes de la rama contrastiva de manera lineal. El texto técnico indica que el modelo "combina autoencoders variacionales con un módulo contrastivo". Estructuralmente, del Espacio Latente deben nacer dos ramas paralelas independientes: la rama superior va hacia el *Decoder* (pasando por el mecanismo de atención temporal/inter-variable) para calcular $\mathcal{L}_{rec}$, y la rama inferior va hacia el *Módulo Contrastivo* (donde se aplican las *augmentations* físicas de series de tiempo) para calcular $\mathcal{L}_{contrastive}$.
* **El Bloque del Reparameterization Trick:** Al ser un VAE, el espacio latente no es un vector estático. Debe representarse visualmente la separación analítica entre los vectores de media ($\mu$) y varianza ($\sigma$), los cuales convergen en un nodo de muestreo estocástico antes de alimentar los módulos posteriores.
* **El Mecanismo de Atención Multi-Cabeza Dual:** El texto explicita que la atención opera "tanto a nivel temporal como entre variables". Un solo bloque es insuficiente; el gráfico debe denotar una estructura bidimensional u horizontal/vertical cruzada para reflejar esta propiedad de atención indexada.


3. **Control de Estilo:** Adherencia estricta a la norma IEEE. Paleta de colores restringida (#0047AB, #4A4A4A, negro y blanco), líneas vectoriales finas y **ausencia total de texto incrustado** (se emplearán iconos matemáticos y geométricos limpios).

---

### **FASE 3: Explicación y Justificación de Pre-ejecución**

#### 1. Disposición Espacial y Flujo de Datos

El diagrama se organizará horizontalmente (*Landscape*), estructurando el flujo en tres secciones principales:

* **Sección de Entrada y Codificación (Izquierda):** Una cuadrícula de líneas horizontales (series multivariadas) entra a un bloque compuesto por dos capas consecutivas (rejillas densas que representan Conv1D y celdas LSTM bidireccionales con flechas de doble sentido).
* **Sección Latente (Centro):** El *Encoder* diverge en dos pequeños contenedores paralelos: uno con el símbolo matemático de media ($\mu$) y otro con el de desviación ($\sigma$). Ambos conectan con un nodo circular de suma/muestreo (representando el *reparameterization trick*).
* **Sección de Bifurcación Híbrida (Derecha):** Desde el nodo de muestreo, el flujo se divide en dos caminos paralelos:
* **Rama Superior (Generativa):** El vector latente entra en un bloque matricial segmentado (Atención Multi-Cabeza temporal e inter-variable) y de ahí pasa al *Decoder* simétrico, finalizando en una cuadrícula que emula la telemetría reconstruida.
* **Rama Inferior (Contrastiva):** El vector latente pasa por un nodo que rompe el flujo en múltiples líneas paralelas que sufren distorsiones geométricas (las *augmentations* de ruido y *masking*), convergiendo en un bloque de pérdidas comparativas (pares positivos/negativos).



#### 2. Justificación Técnica

Esta composición dual es la única manera de justificar visualmente la función de pérdida unificada de la ecuación (\ref{eq:total_loss}). Permite al revisor de la IEEE entender de un vistazo cómo coexisten el objetivo probabilístico (Divergencia KL en el centro), el objetivo reconstructivo (arriba) y el aprendizaje por contraste (abajo), resolviendo el cuello de botella de la caja negra.

#### 3. ADVERTENCIAS PARA EL USUARIO (Puntos de validación)

* **Iconografía en Lugar de Texto:** Siguiendo tus restricciones de estilo, conceptos como "Encoder", "Decoder" o "Contrastive Loss" se suprimirán. Se usarán abstracciones: redes de nodos para el encoder, una estructura en espejo para el decoder, y diagramas de vectores opuestos/alineados para la pérdida contrastiva. ¿Es conforme para tu pipeline de compilación en LaTeX?
* **Simetría del VAE:** El decoder se dibujará con la orientación matemática inversa al encoder para denotar la simetría estructural que mencionas en la sección 3.2.

---

### **FASE 4: Ejecución Silenciosa**

Tengo lista la estructura taxonómica para optimizar el renderizado de `fig2.png`. Por favor, facilítame tu confirmación para proceder con la generación de los prompts técnicos definitivos.


```text
Diagrama técnico vectorial en 2D, esquema de arquitectura de red neuronal compleja y flujo de tensores, diseño plano y minimalista, fondo blanco puro, paleta de colores estricta en azul cobalto (#0047AB) y gris técnico (#4A4A4A) con líneas finas en negro neutro. Sin sombras, sin gradientes, sin reflejos tridimensionales. Disposición horizontal en orientación landscape que fluye de izquierda a derecha. En el extremo izquierdo, una cuadrícula de líneas horizontales paralelas entra en un bloque de codificación compuesto por una rejilla densa y celdas con flechas bidireccionales. Este bloque se conecta en el centro con dos contenedores rectangulares pequeños en paralelo que muestran los símbolos matemáticos griegos mu y sigma; ambos convergen en un nodo circular central de muestreo. A partir de este nodo de muestreo, el flujo se bifurca limpiamente en dos ramas paralelas en el lado derecho. La rama superior se dirige a un bloque matricial de atención bidireccional cruzada y luego a un bloque de decodificación simétrico invertido, terminando en una cuadrícula de salida. La rama inferior se dirige a un nodo que divide la señal en tres líneas distorsionadas geométricamente con patrones de líneas discontinuas, que convergen en un bloque terminal con dos vectores opuestos. Todo el texto, etiquetas y caracteres alfabéticos están completamente ausentes, sustituidos únicamente por símbolos matemáticos limpios, placeholders geométricos y formas vectoriales nítidas según el estándar de publicación IEEE.

```

```text
2D technical vector diagram, complex neural network architecture and tensor flow schematic, flat design, minimalist, pure white background, strict color palette of cobalt blue (#0047AB) and technical gray (#4A4A4A) with crisp neutral black fine lines. No shadows, no gradients, no three-dimensional reflections. Horizontal landscape orientation layout flowing from left to right. On the far left, an input grid of parallel horizontal lines enters an encoding block composed of a dense matrix grid and stacked cells with bidirectional arrows. This block connects in the center to two small parallel rectangular containers displaying the Greek mathematical symbols mu and sigma; both converge into a central circular sampling node. From this sampling node, the workflow cleanly bifurcates into two distinct parallel branches on the right side. The upper branch leads into a segmented matrix block representing cross-attention and then into an inverted symmetrical decoding block, ending in a reconstructed output grid. The lower branch leads to a node that splits the signal into three geometrically distorted lines with dashed line patterns, which then converge into a terminal block featuring two opposing vectors. Entirely free of text, alphabetical labels, or words, utilizing only clean mathematical symbols, geometric placeholders, and sharp vector shapes. Pristine IEEE publication style.

```