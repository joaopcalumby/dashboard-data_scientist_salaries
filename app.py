import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)


@st.cache_data
def carregar_dados():
    url = "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"
    df = pd.read_csv(url)
    return df

df = carregar_dados()

st.sidebar.header("🔍 Filtros Globais")

anos_selecionados = st.sidebar.multiselect(
    "Ano", sorted(df['ano'].unique()), default=sorted(df['ano'].unique())
)

senioridades_selecionadas = st.sidebar.multiselect(
    "Senioridade", sorted(df['senioridade'].unique()), default=sorted(df['senioridade'].unique())
)

df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas))
]

st.title("🎲 Dashboard de Salários na Área de Dados")
st.markdown("Dashboard interativo para exploração de tendências no mercado de dados durante o período de 2020 a 2025.")

aba1, aba2, aba3 = st.tabs(["📊 Visão Geral", "🌍 Mapa Global", "📋 Tabela de Dados"])

with aba1:
    col1, col2, col3, col4 = st.columns(4)
    if not df_filtrado.empty:
        col1.metric("Salário Médio", f"${df_filtrado['usd'].mean():,.0f}")
        col2.metric("Salário Máximo", f"${df_filtrado['usd'].max():,.0f}")
        col3.metric("Registros", f"{df_filtrado.shape[0]:,}")
        col4.metric("Cargo Principal", df_filtrado["cargo"].mode()[0])
    
    st.markdown("---")
    
    col_dir, col_esq = st.columns(2)
    
    with col_dir:
        st.subheader("Top 10 Cargos (USD)")
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        fig_barra = px.bar(top_cargos, x='usd', y='cargo', orientation='h', 
                           color_discrete_sequence=['#E63946']) 
        st.plotly_chart(fig_barra, use_container_width=True)

    with col_esq:
        st.subheader("Tendência Temporal")
        tendencia = df_filtrado.groupby('ano')['usd'].mean().reset_index()
        fig_linha = px.line(tendencia, x='ano', y='usd', markers=True,
                            color_discrete_sequence=['#E63946'], title="Média Salarial por Ano")
        st.plotly_chart(fig_linha, use_container_width=True)

with aba2:
    st.subheader("Distribuição Geográfica por Cargo")
    lista_cargos = sorted(df_filtrado['cargo'].unique())
    cargo_selecionado = st.selectbox("Selecione um cargo para ver no mapa:", lista_cargos)
    
    df_mapa = df_filtrado[df_filtrado['cargo'] == cargo_selecionado]
    media_pais = df_mapa.groupby('residencia_iso3')['usd'].mean().reset_index()
    
    if not media_pais.empty:
        fig_mapa = px.choropleth(
            media_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='Oranges',
            title=f'Salário Médio: {cargo_selecionado}'
        )
        st.plotly_chart(fig_mapa, use_container_width=True)
    else:
        st.info("Selecione filtros na lateral para visualizar o mapa.")

with aba3:
    st.subheader("Exploração de Dados Brutos")
    st.write("Utilize a tabela abaixo para realizar pesquisas específicas nos registros filtrados.")
    st.dataframe(df_filtrado, use_container_width=True)