import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="Manager Dashboard", layout="wide")

st.title("📊 Manager Dashboard - Suivi des Agents")

# Données des agents
agents = ["Toky", "Isaia", "Zara", "Ny Haingo", "Jy Ny Aina", "Vanja"]

# Données exemple
data = {
    "Agent": agents,
    "Heures": [45.5, 38.0, 52.0, 41.2, 35.5, 48.0],
    "Tâches": [12, 10, 15, 11, 9, 14],
    "Pause": [3.2, 2.5, 4.0, 3.0, 2.8, 3.5]
}

df = pd.DataFrame(data)

# KPIs
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("⏱️ Temps total", f"{df['Heures'].sum():.0f}h")
with col2:
    st.metric("📋 Tâches totales", df['Tâches'].sum())
with col3:
    st.metric("☕ Pause totale", f"{df['Pause'].sum():.0f}h")
with col4:
    st.metric("👥 Agents", len(agents))

# Graphique
fig = px.bar(df, x="Agent", y="Heures", color="Agent", 
             title="Temps de travail par agent")
st.plotly_chart(fig, use_container_width=True)

# Tableau
st.subheader("📋 Détail des agents")
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.caption(f"🔄 Dernière mise à jour: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
