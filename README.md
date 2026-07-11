# HIDROSED_V1

Primera base modular consolidada.

## Versiones seleccionadas del chat

1. **Módulo de cuencas:** `HidroSed Foja Cero v3 tramo útil`, usando la lógica que dio mejor resultado para doble punto de control, eje obligatorio, tramo útil y curvas asociadas al eje.
2. **Módulo de eje/secciones:** `HidroSed · Eje Cauce y Secciones v15 · geometría ajustada a extremos`, integrado como módulo independiente.

## Criterio aplicado

No se reconstruyó la lógica de cuencas. Se encapsuló Foja Cero v3 como módulo y solo se agregaron reportes morfométricos, imagen de cuenca y salida JSON para módulos futuros.

## Streamlit Cloud

- Main file path: `app.py`
- Python version: `3.11`
- Después de subir: `Manage app → Clear cache and reboot`
