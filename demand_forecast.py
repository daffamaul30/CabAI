
import streamlit as st
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objects as go
import gdown
import os

def forecast():
    # Download model dan scaler jika belum ada
    if not os.path.exists('lstm_model_cabai_gpu.h5'):
        gdown.download('https://drive.google.com/uc?id=13G3MA4Zyeajca-BNjjQuj5MCmI7__gIn', 'lstm_model_cabai_gpu.h5', fuzzy=True)
    if not os.path.exists('scaler.gz'):
        gdown.download('https://drive.google.com/uc?id=1XzO8v3KGG8m9LG9DYCWY5ryYL0OHH4iL', 'scaler.gz', fuzzy=True)

    # Nama file lokal
    model_path = 'lstm_model_cabai_gpu.h5'
    scaler_path = 'scaler.gz'

    # Load model dan scaler
    model = load_model(model_path, compile=False)
    scaler = joblib.load(scaler_path)

    # Load data
    file_path = "https://drive.google.com/uc?export=download&id=1tZTzs9RK6Sg_FRyP-rDJfqbznUAGDjUQ"
    df_raw = pd.read_excel(file_path)

    # Filter data
    df = df_raw[df_raw['Jenis Cabai'] == 'Cabai Keriting'].copy()
    df['Tanggal'] = pd.to_datetime(dict(year=df['Tahun'], month=df['Bulan'], day=1))
    df = df.sort_values(by='Tanggal')
    df.set_index('Tanggal', inplace=True)

    # Ambil kebutuhan dan scaling
    kebutuhan_asli = df['Kebutuhan']
    kebutuhan_scaled = scaler.transform(kebutuhan_asli.values.reshape(-1, 1)).flatten()

    # Session state
    if 'prediksi_scaled' not in st.session_state:
        st.session_state.prediksi_scaled = []
        st.session_state.input_scaled = kebutuhan_scaled[-12:].tolist()
        st.session_state.tanggal_terakhir = kebutuhan_asli.index[-1]

    st.write("Prediksi dilakukan per bulan berdasarkan 12 bulan terakhir.")

    # Tombol prediksi bulan selanjutnya
    left, middle, right = st.columns(3)
    if middle.button("Prediksi Kebutuhan Bulan Selanjutnya", type="primary"):
        input_model = np.array(st.session_state.input_scaled).reshape(1, 12, 1)
        pred_scaled = model.predict(input_model)[0][0]

        # Simpan prediksi
        st.session_state.prediksi_scaled.append(pred_scaled)
        st.session_state.input_scaled.pop(0)
        st.session_state.input_scaled.append(pred_scaled)
        st.session_state.tanggal_terakhir += pd.DateOffset(months=1)

    # Data input asli (12 bulan terakhir)
    input_asli = scaler.inverse_transform(np.array(st.session_state.input_scaled).reshape(-1, 1)).flatten()
    tanggal_input = pd.date_range(end=st.session_state.tanggal_terakhir, periods=12, freq='MS')

    # Data prediksi
    if st.session_state.prediksi_scaled:
        pred_aktual = scaler.inverse_transform(
            np.array(st.session_state.prediksi_scaled).reshape(-1, 1)
        ).flatten()
        tanggal_prediksi = pd.date_range(
            start=kebutuhan_asli.index[-1] + pd.DateOffset(months=1),
            periods=len(pred_aktual),
            freq='MS'
        )
    else:
        pred_aktual = []
        tanggal_prediksi = []

    # Gabungkan semua untuk ditampilkan dalam satu grafik
    fig = go.Figure()

    # Garis input (aktual 12 bulan terakhir)
    # Garis input (aktual 12 bulan terakhir)
    fig.add_trace(go.Scatter(
        x=tanggal_input,
        y=input_asli,
        mode='lines+markers',
        name='Input Aktual (12 Bulan)',
        line=dict(color='blue', width=3),
        marker=dict(symbol='circle', size=8, color='blue'),
        hovertemplate='Aktual: %{y:.2f} Ton<br>Tanggal: %{x|%b %Y}<extra></extra>'
    ))

    # Garis prediksi
    # Garis prediksi
    if len(pred_aktual) > 0:
        fig.add_trace(go.Scatter(
            x=tanggal_prediksi,
            y=pred_aktual,
            mode='lines+markers',
            name='Prediksi',
            line=dict(color='orange', dash='dot', width=3),
            marker=dict(symbol='diamond', size=10, color='orange'),
            hovertemplate='Prediksi: %{y:.2f} Ton<br>Tanggal: %{x|%b %Y}<extra></extra>'
        ))


    fig.update_layout(
        xaxis_title="Tanggal",
        yaxis_title="Kebutuhan (Ton)",
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    )

    st.plotly_chart(fig, use_container_width=True)
