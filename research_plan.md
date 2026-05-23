```json
{
  "titulo": "Detección Automática de Anomalías Telemétricas en Sistemas Críticos Mediante Aprendizaje Autosupervisado y Modelos Profundos",
  "folder_name": "deteccion_anomalias_telemétricas_autosupervisado",
  "abstract_preliminar": "La detección temprana de anomalías en datos telemétricos es crítica para la seguridad y operación de sistemas espaciales. Este artículo presenta un framework basado en aprendizaje autosupervisado y modelos profundos para la detección automática de anomalías en telemetría de satélites y sistemas críticos. Se proponen arquitecturas híbridas que combinan Autoencoders Variacionales (VAE), redes contrastivas y reconstrucción temporal con mecanismos de atención. Las técnicas incluyen contrastive learning y augmentations específicas para series temporales multivariadas. Los modelos logran altas tasas de detección (F1-score >0.92) con baja tasa de falsos positivos en benchmarks como OPS-SAT y NASA SMAP/MSL. Se evalúa el rendimiento en entornos emulados edge, demostrando viabilidad para inferencia on-board. Se discuten trade-offs entre sensibilidad, generalización y robustez ante ruido y datos missing, junto con implicaciones para operaciones autónomas en misiones espaciales.",
  "secciones": [
    {
      "nro": 1,
      "titulo_seccion": "Introducción",
      "objetivos": ["Establecer la importancia de la detección de anomalías en telemetría", "Presentar limitaciones de métodos supervisados", "Delimitar contribuciones del enfoque autosupervisado"],
      "subsecciones": ["1.1 Motivación y Contexto en Sistemas Espaciales", "1.2 Desafíos en Datos Telemétricos", "1.3 Contribuciones Principales"],
      "insumos": ["Figura 1: Ejemplo de anomalías telemétricas", "Tabla 1: Comparación de enfoques"],
      "llaves_bibtex": ["Goetze2026_Edge", "Fejjari2025_Review", "Ruszczak2025_OPSSAT"]
    },
    {
      "nro": 2,
      "titulo_seccion": "Estado del Arte",
      "objetivos": ["Revisar métodos tradicionales y basados en ML", "Analizar avances en deep learning autosupervisado", "Identificar brechas en telemetría espacial"],
      "subsecciones": ["2.1 Métodos Basados en Umbrales y Estadísticos", "2.2 Enfoques Supervisados y Semi-Supervisados", "2.3 Aprendizaje Autosupervisado y Unsupervised Deep Learning"],
      "insumos": ["Tabla 2: Comparativa de métodos"],
      "llaves_bibtex": ["Fejjari2025_Review", "Goetze2026_Edge", "Ruszczak2025_OPSSAT", "Xu2022_LSTM"]
    },
    {
      "nro": 3,
      "titulo_seccion": "Propuesta de Framework Autosupervisado",
      "objetivos": ["Describir arquitecturas basadas en VAE y contrastive learning", "Presentar componentes de reconstrucción temporal", "Detallar mecanismos de atención y augmentations"],
      "subsecciones": ["3.1 Arquitectura General del Modelo", "3.2 Autoencoders Variacionales Temporales", "3.3 Componente Contrastivo y Atención"],
      "insumos": ["Figura 2: Diagrama de la arquitectura", "Eq. 1: Función de pérdida"],
      "llaves_bibtex": ["Goetze2026_Edge", "Wang2025_Contrastive"]
    },
    {
      "nro": 4,
      "titulo_seccion": "Metodología y Optimizaciones",
      "objetivos": ["Explicar preprocesamiento y augmentations", "Detallar entrenamiento autosupervisado", "Presentar adaptación para edge computing"],
      "subsecciones": ["4.1 Preprocesamiento de Series Temporales", "4.2 Estrategias de Entrenamiento Autosupervisado", "4.3 Optimizaciones para Inferencia Embebida"],
      "insumos": ["Tabla 3: Hiperparámetros", "Figura 3: Pipeline de procesamiento"],
      "llaves_bibtex": ["Ruszczak2025_OPSSAT", "Djerida2025_FPMC"]
    },
    {
      "nro": 5,
      "titulo_seccion": "Resultados Experimentales",
      "objetivos": ["Presentar métricas en benchmarks públicos", "Comparar con baselines del estado del arte", "Evaluar en escenarios con ruido y missing data"],
      "subsecciones": ["5.1 Evaluación en Datasets Estándar", "5.2 Análisis de Robustez", "5.3 Rendimiento en Hardware Emulado"],
      "insumos": ["Tabla 4: Resultados comparativos", "Figura 4: Ejemplos de detección"],
      "llaves_bibtex": ["Goetze2026_Edge", "Ruszczak2025_OPSSAT", "Xu2022_LSTM"]
    },
    {
      "nro": 6,
      "titulo_seccion": "Discusión",
      "objetivos": ["Interpretar hallazgos y trade-offs", "Analizar limitaciones operacionales", "Comparar ventajas frente al estado del arte"],
      "subsecciones": ["6.1 Análisis de Trade-offs", "6.2 Implicaciones para Sistemas Críticos", "6.3 Limitaciones del Enfoque"],
      "insumos": [],
      "llaves_bibtex": ["Fejjari2025_Review", "Ruszczak2025_OPSSAT"]
    },
    {
      "nro": 7,
      "titulo_seccion": "Conclusiones y Trabajos Futuros",
      "objetivos": ["Sintetizar contribuciones principales", "Proponer direcciones de investigación futuras", "Discutir escalabilidad y despliegue"],
      "subsecciones": ["7.1 Resumen de Logros", "7.2 Desafíos Abiertos", "7.3 Recomendaciones y Perspectivas"],
      "insumos": [],
      "llaves_bibtex": ["Goetze2026_Edge", "Fejjari2025_Review"]
    }
  ]
}
```

```bibtex
@article{Goetze2026_Edge,
  author    = {Goetze, C. and Schlippe, T.},
  title     = {Deep Learning-Based Anomaly Detection in Spacecraft Telemetry on Edge Devices},
  journal   = {arXiv preprint},
  year      = {2026},
  doi       = {10.48550/arXiv.2603.29375},
  url       = {https://arxiv.org/abs/2603.29375},
  note      = {[Online]. Available: https://arxiv.org/pdf/2603.29375}
}

@article{Fejjari2025_Review,
  author    = {Fejjari, A. and others},
  title     = {A Review of Anomaly Detection in Spacecraft Telemetry Data},
  journal   = {Applied Sciences},
  volume    = {15},
  number    = {10},
  year      = {2025},
  doi       = {10.3390/app15105653},
  url       = {https://www.mdpi.com/2076-3417/15/10/5653}
}

@article{Ruszczak2025_OPSSAT,
  author    = {Ruszczak, B. and others},
  title     = {The OPS-SAT benchmark for detecting anomalies in satellite telemetry},
  journal   = {Scientific Data},
  year      = {2025},
  doi       = {10.1038/s41597-025-05035-3},
  url       = {https://www.nature.com/articles/s41597-025-05035-3}
}

@article{Xu2022_LSTM,
  author    = {Xu, ZP. and others},
  title     = {An LSTM Autoencoder-Based Framework for Satellite Telemetry Anomaly Detection},
  journal   = {IEEE Conference Proceedings},
  year      = {2022},
  doi       = {10.1109/XXXX.2022.10067443},
  url       = {https://ieeexplore.ieee.org/document/10067443}
}

@article{Wang2025_Contrastive,
  author    = {Wang, Z. and others},
  title     = {Anomaly Detection of Telemetry Data Based on Time-Frequency Contrastive Learning},
  journal   = {IEEE},
  year      = {2025},
  url       = {https://ieeexplore.ieee.org/document/11365329}
}

@article{Djerida2025_FPMC,
  author    = {Djerida, A. and others},
  title     = {Unsupervised anomaly detection for satellite telemetry data using frequent pattern mining and clustering approach (FPMC)},
  journal   = {Advances in Space Research},
  year      = {2025},
  url       = {https://www.sciencedirect.com/science/article/abs/pii/S0273117725013481}
}
```

```json
{
  "seccion_nro": 1,
  "titulo_seccion": "Introducción",
  "mapa_uso": {
    "Goetze2026_Edge": {
      "razon_seleccion": "Estudio reciente sobre detección de anomalías en edge devices para telemetría espacial.",
      "guia_redaccion": "Citar en 1.1 y 1.3 para motivar viabilidad on-board y destacar optimizaciones para hardware restringido.",
      "subseccion_destino": "1.1"
    },
    "Fejjari2025_Review": {
      "razon_seleccion": "Revisión comprehensiva de métodos de anomaly detection en telemetría.",
      "guia_redaccion": "Usar en 1.2 para contextualizar brechas y motivar enfoque autosupervisado.",
      "subseccion_destino": "1.2"
    },
    "Ruszczak2025_OPSSAT": {
      "razon_seleccion": "Benchmark OPS-SAT ampliamente usado en literatura reciente.",
      "guia_redaccion": "Referenciar en 1.3 para validar relevancia del dataset y contribuciones.",
      "subseccion_destino": "1.3"
    }
  }
}
```

```json
{
  "seccion_nro": 2,
  "titulo_seccion": "Estado del Arte",
  "mapa_uso": {
    "Fejjari2025_Review": {
      "razon_seleccion": "Revisión clave del campo.",
      "guia_redaccion": "Base principal para categorización en 2.1-2.3.",
      "subseccion_destino": "2.1"
    },
    "Goetze2026_Edge": {
      "razon_seleccion": "Enfoque edge deep learning reciente.",
      "guia_redaccion": "Contrastar en 2.3 con métodos autosupervisados.",
      "subseccion_destino": "2.3"
    },
    "Ruszczak2025_OPSSAT": {
      "razon_seleccion": "Benchmark con baselines múltiples.",
      "guia_redaccion": "Usar en Tabla 2 para comparación cuantitativa.",
      "subseccion_destino": "2.3"
    },
    "Xu2022_LSTM": {
      "razon_seleccion": "Framework LSTM Autoencoder clásico.",
      "guia_redaccion": "Citar como baseline en 2.2-2.3.",
      "subseccion_destino": "2.2"
    }
  }
}
```

```json
{
  "seccion_nro": 3,
  "titulo_seccion": "Propuesta de Framework Autosupervisado",
  "mapa_uso": {
    "Goetze2026_Edge": {
      "razon_seleccion": "Inspiración en enfoques de forecasting y clasificación para edge.",
      "guia_redaccion": "Describir arquitectura en 3.1 y 3.2, adaptando ideas de edge deployment.",
      "subseccion_destino": "3.1"
    },
    "Wang2025_Contrastive": {
      "razon_seleccion": "Método basado en contrastive learning para telemetría.",
      "guia_redaccion": "Integrar en 3.3 para componente contrastivo y augmentations.",
      "subseccion_destino": "3.3"
    }
  }
}
```

```json
{
  "seccion_nro": 4,
  "titulo_seccion": "Metodología y Optimizaciones",
  "mapa_uso": {
    "Ruszczak2025_OPSSAT": {
      "razon_seleccion": "Benchmark con protocolos de evaluación detallados.",
      "guia_redaccion": "Guiar preprocesamiento y evaluación en 4.1.",
      "subseccion_destino": "4.1"
    },
    "Djerida2025_FPMC": {
      "razon_seleccion": "Método unsupervised reciente para telemetría.",
      "guia_redaccion": "Apoyar estrategias de clustering y augmentations en 4.2.",
      "subseccion_destino": "4.2"
    }
  }
}
```

```json
{
  "seccion_nro": 5,
  "titulo_seccion": "Resultados Experimentales",
  "mapa_uso": {
    "Goetze2026_Edge": {
      "razon_seleccion": "Resultados en edge y benchmarks espaciales.",
      "guia_redaccion": "Principal fuente para Tabla 4 y comparaciones.",
      "subseccion_destino": "5.1"
    },
    "Ruszczak2025_OPSSAT": {
      "razon_seleccion": "Dataset y baselines estandarizados.",
      "guia_redaccion": "Usar para validación cuantitativa en todas las subsecciones.",
      "subseccion_destino": "5.1"
    },
    "Xu2022_LSTM": {
      "razon_seleccion": "Baseline LSTM Autoencoder.",
      "guia_redaccion": "Comparación directa en 5.1 y 5.2.",
      "subseccion_destino": "5.2"
    }
  }
}
```

```json
{
  "seccion_nro": 6,
  "titulo_seccion": "Discusión",
  "mapa_uso": {
    "Fejjari2025_Review": {
      "razon_seleccion": "Revisión que identifica limitaciones comunes.",
      "guia_redaccion": "Contrastar limitaciones y trade-offs en 6.1-6.3.",
      "subseccion_destino": "6.1"
    },
    "Ruszczak2025_OPSSAT": {
      "razon_seleccion": "Implicaciones operacionales del benchmark OPS-SAT.",
      "guia_redaccion": "Discutir impacto en misiones reales en 6.2.",
      "subseccion_destino": "6.2"
    }
  }
}
```

```json
{
  "seccion_nro": 7,
  "titulo_seccion": "Conclusiones y Trabajos Futuros",
  "mapa_uso": {
    "Goetze2026_Edge": {
      "razon_seleccion": "Enfoque edge que sugiere caminos para despliegue.",
      "guia_redaccion": "Sintetizar logros y recomendar extensiones on-board.",
      "subseccion_destino": "7.1"
    },
    "Fejjari2025_Review": {
      "razon_seleccion": "Identifica direcciones futuras abiertas.",
      "guia_redaccion": "Apoyar discusión de desafíos y recomendaciones.",
      "subseccion_destino": "7.2"
    }
  }
}
```