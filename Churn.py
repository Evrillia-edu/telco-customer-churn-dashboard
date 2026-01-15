import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. SETTING HALAMAN ---
st.set_page_config(page_title="Telco Churn Dashboard", layout="wide")

# --- 2. LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
    # Ubah TotalCharges ke numerik (kadang ada yang kosong/string)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(inplace=True)
    return df

df = load_data()

# --- 3. SIDEBAR FILTER ---
st.sidebar.header("Filter Pelanggan")

# Filter Jenis Kontrak
contract_type = st.sidebar.multiselect(
    "Pilih Jenis Kontrak:",
    options=df["Contract"].unique(),
    default=df["Contract"].unique()
)

# Filter Metode Pembayaran
payment_method = st.sidebar.multiselect(
    "Metode Pembayaran:",
    options=df["PaymentMethod"].unique(),
    default=df["PaymentMethod"].unique()
)

# Terapkan Filter
df_selection = df[
    (df["Contract"].isin(contract_type)) & 
    (df["PaymentMethod"].isin(payment_method))
]

# --- 4. DASHBOARD HEADER & KPI ---
st.title("Telco Customer Churn Analysis")
st.markdown("##")

# Hitung KPI
total_cust = df_selection.shape[0]
churn_rate = (df_selection[df_selection["Churn"] == "Yes"].shape[0] / total_cust) * 100
avg_monthly = df_selection["MonthlyCharges"].mean()

c1, c2, c3 = st.columns(3)
c1.metric("Total Pelanggan", f"{total_cust:,}")
c2.metric("Churn Rate", f"{churn_rate:.1f}%")
c3.metric("Rata-rata Biaya/Bulan", f"${avg_monthly:.2f}")

st.markdown("---")

# --- 5. GRAFIK ANALISIS ---
col_left, col_right = st.columns(2)

with col_left:
    # Grafik Churn berdasarkan Masa Langganan (Tenure)
    st.subheader("Distribusi Masa Langganan (Tenure)")
    fig_tenure = px.histogram(
        df_selection, x="tenure", color="Churn", 
        nbins=30, barmode="group",
        title="Berapa lama pelanggan bertahan?"
    )
    st.plotly_chart(fig_tenure, use_container_width=True)

with col_right:
    # Grafik Churn berdasarkan Jenis Kontrak
    st.subheader("Churn Berdasarkan Jenis Kontrak")
    fig_contract = px.sunburst(
        df_selection, path=['Contract', 'Churn'], 
        values='MonthlyCharges',
        title="Kontrak mana yang paling berisiko?"
    )
    st.plotly_chart(fig_contract, use_container_width=True)

# Grafik Bar: Biaya Bulanan vs Churn
st.subheader("Biaya Bulanan vs Churn")
fig_monthly = px.box(df_selection, x="Churn", y="MonthlyCharges", color="Churn", points="all")
st.plotly_chart(fig_monthly, use_container_width=True)