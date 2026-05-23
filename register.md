```markdown
**Title**: Detección Automática de Anomalías Telemétricas en Sistemas Críticos Mediante Aprendizaje Autosupervisado y Modelos Profundos

**Description**: El proyecto desarrolla un framework basado en aprendizaje autosupervisado para la detección automática de anomalías en datos telemétricos de satélites y sistemas críticos. La arquitectura híbrida combina Autoencoders Variacionales Temporales (VAE), aprendizaje contrastivo y mecanismos de atención multi-cabeza, permitiendo aprender representaciones ricas del comportamiento nominal sin requerir etiquetas de anomalías. El modelo logra F1-score superior a 0.92 en benchmarks como OPS-SAT, con robustez ante ruido y datos faltantes, y optimizaciones específicas (pruning y cuantización) para inferencia embebida on-board en entornos con recursos limitados.

**General Objective**: Desarrollar y validar un framework de aprendizaje autosupervisado basado en modelos profundos para la detección automática y robusta de anomalías en telemetría de sistemas críticos espaciales.

**Specific Objectives**: 
- Diseñar una arquitectura híbrida que integre VAE temporales, aprendizaje contrastivo y atención multi-cabeza para series temporales multivariadas.
- Implementar estrategias de augmentations específicas del dominio y optimizaciones para inferencia en edge computing.
- Evaluar el rendimiento del modelo en precisión, robustez y eficiencia computacional utilizando benchmarks públicos (OPS-SAT y similares).
- Analizar trade-offs entre sensibilidad, tasa de falsos positivos y viabilidad on-board.
- Proponer recomendaciones para escalabilidad y despliegue en misiones espaciales reales.

**Justification**: La telemetría de satélites genera volúmenes masivos de datos donde las anomalías son raras pero potencialmente catastróficas. Los métodos tradicionales y supervisados fallan ante la escasez de etiquetas y la variabilidad entre misiones. Un sistema autosupervisado habilita detección temprana on-board, reduciendo la dependencia de ground segment, mejorando la autonomía, la seguridad operacional y la respuesta ante fallos. Esto es estratégico para constelaciones satelitales, misiones de larga duración y sistemas críticos, contribuyendo a mayor confiabilidad y sostenibilidad de las operaciones espaciales.

**Methodology**: Se adopta un enfoque experimental iterativo con aprendizaje autosupervisado. Se implementa un framework híbrido VAE + Contrastive Learning con augmentations especializadas para series temporales. La validación se realiza en benchmarks públicos (OPS-SAT), con pruebas de robustez ante ruido y missing data, y evaluación en hardware emulado (Jetson Orin NX). Se utilizan métricas estándar (Precision, Recall, F1-Score, AUC-ROC) y mediciones de latencia y consumo energético.

**Scope**: Diseño, implementación y validación en hardware emulado de un framework autosupervisado para detección de anomalías en telemetría multi-variada con énfasis en viabilidad on-board (máximo 100 caracteres).

**Activities**: 
1. Revisión del estado del arte y definición de requisitos. 
2. Diseño e implementación de la arquitectura híbrida VAE-Contrastiva. 
3. Desarrollo de preprocesamiento, augmentations y optimizaciones edge. 
4. Experimentación y evaluación en benchmarks y escenarios de ruido. 
5. Análisis de resultados, discusión de trade-offs y elaboración de recomendaciones.

**Resources**: 
- Benchmarks públicos de telemetría (OPS-SAT, NASA SMAP/MSL). 
- Plataformas de hardware emulado (NVIDIA Jetson Orin NX). 
- Frameworks de deep learning (PyTorch) con soporte para cuantización y pruning. 
- Herramientas de simulación de series temporales y fault injection.

**Limitations**: 
- Validación limitada a entornos emulados (sin pruebas en órbita real). 
- Dependencia de la disponibilidad y representatividad de datos nominales de entrenamiento. 
- Desafíos de generalización entre diferentes plataformas satelitales y misiones. 
- Requerimientos de certificación para sistemas de alta criticidad.
```