# -*- coding: utf-8 -*-
from __future__ import annotations

import json
from datetime import datetime
import streamlit as st

st.set_page_config(
    page_title="HIDROSED_V1",
    page_icon="💧",
    layout="wide",
)

st.sidebar.title("HIDROSED_V1")
st.sidebar.caption("Base modular: Foja Cero v3 + Eje/Secciones v15")

modulo = st.sidebar.radio(
    "Seleccionar módulo",
    [
        "1 · Cuencas y morfometría · Foja Cero v3 tramo útil",
        "2 · Eje cauce y secciones · v15 geometría ajustada a extremos",
        "3 · Base técnica integrada",
    ],
    index=0,
)

if modulo.startswith("1"):
    from modules import foja_cero_v3_tramo_util
    foja_cero_v3_tramo_util.run()
elif modulo.startswith("2"):
    from modules import eje_cauce_secciones_v15
    eje_cauce_secciones_v15.run()
else:
    st.title("🧩 HIDROSED_V1 · Base técnica integrada")
    st.markdown(
        "Esta vista resume lo que ya quedó disponible en sesión para módulos futuros de hidrología, hidráulica, sedimentos y socavación."
    )
    foja = st.session_state.get("foja_cero_v3_summary")
    eje = st.session_state.get("eje_result")
    data = {
        "fecha_consulta": datetime.utcnow().isoformat() + "Z",
        "modulo_cuencas_disponible": foja is not None,
        "modulo_eje_secciones_disponible": eje is not None,
        "cuencas_morfometria_foja_cero_v3": foja,
        "eje_secciones_v15": None if eje is None else {
            "crs_proyectado": str(eje.get("crs_proj")),
            "perfil_longitudinal_filas": int(len(eje.get("profile_df", []))) if eje.get("profile_df") is not None else 0,
            "numero_secciones": int(len(eje.get("sections", []))) if eje.get("sections") is not None else 0,
            "dem_download_info": eje.get("dem_download_info"),
            "conectividad_hecras": "Disponible dentro del módulo v15 mediante LOB / Channel / ROB, bancos y talweg.",
        },
    }
    c1, c2 = st.columns(2)
    c1.metric("Cuencas/morfometría", "Disponible" if foja is not None else "No ejecutado")
    c2.metric("Eje/secciones", "Disponible" if eje is not None else "No ejecutado")
    st.json(data)
    st.download_button(
        "Descargar base técnica integrada JSON",
        json.dumps(data, ensure_ascii=False, indent=2, default=str).encode("utf-8"),
        file_name="HIDROSED_V1_base_tecnica_integrada.json",
        mime="application/json",
    )
