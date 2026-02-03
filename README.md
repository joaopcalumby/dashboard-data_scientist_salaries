# 📊 Dashboard de Salários na Área de Dados (2020-2025)

Este projeto é um dashboard interativo desenvolvido durante a **Imersão de Dados com Python da Alura**. O objetivo é explorar e visualizar as tendências salariais globais no setor de dados, permitindo análises por cargo, senioridade e localização geográfica.

---

## 🚀 Funcionalidades

O dashboard oferece três visões principais organizadas por abas:

1. **Visão Geral:** * Exibição de KPIs (Salário Médio, Máximo e Cargo mais frequente).
   * Gráfico de barras com o Top 10 cargos mais bem pagos.
   * Análise de tendência temporal da média salarial ano a ano.
2. **Mapa Global:** * Distribuição geográfica dos salários baseada na residência do profissional.
   * Filtro dinâmico por cargo específico para visualização no mapa.
3. **Exploração de Dados:**
   * Tabela interativa com os dados brutos filtrados para inspeção detalhada.

---

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem base para o processamento de dados.
* **Streamlit**: Framework utilizado para a criação da interface web interativa.
* **Pandas**: Biblioteca para manipulação e limpeza do dataset.
* **Plotly Express**: Biblioteca para geração de gráficos dinâmicos e mapas.

---

## 📂 Como executar o projeto

Para rodar este dashboard localmente, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   ```
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Execute o aplicativo:**
   ```bash
   streamlit run app.py
   ```

---

## 📈 Aprendizados Principais

Este foi meu primeiro contato prático com as bibliotecas **Streamlit** e **Plotly**. Durante o desenvolvimento, pude aprofundar conhecimentos em:

* Estruturação de dashboards multipáginas (abas).
* Implementação de filtros dinâmicos na barra lateral (sidebar).
* Uso de `@st.cache_data` para otimizar a performance da aplicação.
* Customização de visualizações geográficas (Choropleth Maps).

Reutilizei o código do dashboard original da atividade e resolvi ampliar meus estudos direcionando isso à apresentação dos dados. A divisão em abas e o uso de cache pra melhorar a performance foram implementadas como formas de tentar ir além ao que foi visto na imersão
