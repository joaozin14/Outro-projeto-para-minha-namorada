import streamlit as st
from datetime import *

data_atual = datetime.now()
data_passada = datetime(2022, 7, 3)
diferenca = data_atual - data_passada 
total_segundos = diferenca.total_seconds()
minutos_totais = int(total_segundos // 60) 
segundos_totais = int(diferenca.total_seconds())
formatado_minutos = f"{minutos_totais:,}".replace(",", ".")
formatado_segundos = f"{segundos_totais:,}".replace(",", ".")

st.markdown("""
    <h1 class="titulo">Contador dos nossos dias juntos ❤</h1> 
    <style>
    .titulo{
        text-align: center;
        color: pink;
        text-shadow: 2px 2px 5px pink;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
        .contador {
            font-size: 24px;
            color: #DA70D6;
            text-align: center;
            margin-top: 100px;
            text-shadow: 2px 2px 5px pink;
        }
        .dias {
            font-weight: bold;
            color: pink;
            text-shadow: 2px 2px 5px #DA70D6;
        }

        .minutos {
            font-weight: bold;
            color: pink; 
            text-shadow: 2px 2px 5px #DA70D6;   
        }

        .segundos {
            font-weight: bold;
            color: pink;
            text-shadow: 2px 2px 5px #DA70D6;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class="contador">
        Estamos juntos há <span class="dias">{diferenca.days}</span> dias, <span class="minutos">{formatado_minutos}</span> minutos e <span class="segundos">{formatado_segundos}</span> segundos juntos e seguimos contando ❤.
    </div>
""", unsafe_allow_html=True)

