import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Manager Dashboard", layout="wide")

st.title("📊 Manager Dashboard - Suivi des Agents")

# Données des agents
agents = ["Toky", "Isaia", "Zara", "Ny Haingo", "Jy Ny Aina", "Vanja"]
heures = [45.5, 38.0, 52.0, 41.2, 35.5, 48.0]
taches = [12, 10, 15, 11, 9, 14]
pauses = [3.2, 2.5, 4.0, 3.0, 2.8, 3.5]

# Calcul des totaux
total_heures = sum(heures)
total_taches = sum(taches)
total_pauses = sum(pauses)

# KPIs
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("⏱️ Temps total", f"{total_heures:.0f}h")
with col2:
    st.metric("📋 Tâches totales", total_taches)
with col3:
    st.metric("☕ Pause totale", f"{total_pauses:.0f}h")
with col4:
    st.metric("👥 Agents", len(agents))

# Tableau
st.subheader("📋 Détail des agents")

# Créer un tableau simple
table_data = []
for i in range(len(agents)):
    table_data.append({
        "Agent": agents[i],
        "Heures": f"{heures[i]:.1f}h",
        "Tâches": taches[i],
        "Pause": f"{pauses[i]:.1f}h"
    })

st.table(table_data)

st.markdown("---")
st.caption(f"Dernière mise à jour: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
