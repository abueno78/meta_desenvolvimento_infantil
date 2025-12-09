"""
Módulo para gráficos e visualizações
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from config.settings import INDICATORS, COLORS


def criar_grafico_indicadores(df: pd.DataFrame) -> go.Figure:
    """
    Cria gráfico de barras com conformidade de cada indicador.
    
    Args:
        df: DataFrame com os dados processados
        
    Returns:
        Figura Plotly
    """
    # Calcular percentuais
    total = len(df)
    percentuais = [
        (df["Indicador_A"].sum() / total * 100) if total > 0 else 0,
        (df["Indicador_B"].sum() / total * 100) if total > 0 else 0,
        (df["Indicador_C"].sum() / total * 100) if total > 0 else 0,
        (df["Indicador_D"].sum() / total * 100) if total > 0 else 0,
        (df["Indicador_E"].sum() / total * 100) if total > 0 else 0,
    ]
    
    indicadores = ["A", "B", "C", "D", "E"]
    nomes = [
        INDICATORS["A"]["nome"],
        INDICATORS["B"]["nome"],
        INDICATORS["C"]["nome"],
        INDICATORS["D"]["nome"],
        INDICATORS["E"]["nome"],
    ]
    cores = [
        INDICATORS["A"]["cor"],
        INDICATORS["B"]["cor"],
        INDICATORS["C"]["cor"],
        INDICATORS["D"]["cor"],
        INDICATORS["E"]["cor"],
    ]
    
    fig = go.Figure(
        data=[
            go.Bar(
                x=nomes,
                y=percentuais,
                marker=dict(color=cores),
                text=[f"{p:.1f}%" for p in percentuais],
                textposition="auto",
                hovertemplate="<b>%{x}</b><br>Conformidade: %{y:.1f}%<extra></extra>",
            )
        ]
    )
    
    fig.update_layout(
        title="Conformidade por Indicador",
        xaxis_title="Indicador",
        yaxis_title="Conformidade (%)",
        yaxis=dict(range=[0, 100]),
        hovermode="x unified",
        template="plotly_white",
        height=400,
    )
    
    return fig


def criar_grafico_indicadores_bolsa_familia(df: pd.DataFrame) -> go.Figure:
    """
    Cria grafico de barras agrupadas com conformidade de indicadores por Bolsa Familia.
    
    Args:
        df: DataFrame com os dados processados
        
    Returns:
        Figura Plotly
    """
    indicadores = ["A", "B", "C", "D", "E"]
    nomes_indicadores = [
        INDICATORS["A"]["nome"],
        INDICATORS["B"]["nome"],
        INDICATORS["C"]["nome"],
        INDICATORS["D"]["nome"],
        INDICATORS["E"]["nome"],
    ]
    
    # Calcular conformidade para cada grupo de Bolsa Familia
    grupos = ["Sim", "Não"]
    dados_grafico = {ind: {grupo: 0 for grupo in grupos} for ind in indicadores}
    
    for grupo in grupos:
        df_grupo = df[df["Beneficiário do programa Bolsa Família"] == grupo]
        total_grupo = len(df_grupo)
        
        if total_grupo > 0:
            for i, ind in enumerate(indicadores):
                col = f"Indicador_{ind}"
                percentual = (df_grupo[col].sum() / total_grupo * 100)
                dados_grafico[ind][grupo] = percentual
    
    # Criar barras para cada grupo
    fig = go.Figure()
    
    cores_grupo = {"Sim": "#28a745", "Não": "#dc3545"}
    
    for grupo in grupos:
        valores = [dados_grafico[ind][grupo] for ind in indicadores]
        label_grupo = "Com Bolsa Família" if grupo == "Sim" else "Sem Bolsa Família"
        fig.add_trace(go.Bar(
            x=nomes_indicadores,
            y=valores,
            name=label_grupo,
            marker=dict(color=cores_grupo[grupo]),
            text=[f"{v:.1f}%" for v in valores],
            textposition="auto",
            hovertemplate="<b>%{x}</b><br>" + label_grupo + "<br>Conformidade: %{y:.1f}%<extra></extra>",
        ))
    
    fig.update_layout(
        title="Conformidade por Indicador - Agrupado por Bolsa Família",
        xaxis_title="Indicador",
        yaxis_title="Conformidade (%)",
        yaxis=dict(range=[0, 100]),
        barmode="group",
        hovermode="x unified",
        template="plotly_white",
        height=400,
        legend=dict(x=1.05, y=1)
    )
    
    return fig


def criar_grafico_status_geral(df: pd.DataFrame) -> go.Figure:
    """
    Cria gráfico de pizza com status geral (conforme/não-conforme).
    
    Args:
        df: DataFrame com os dados processados
        
    Returns:
        Figura Plotly
    """
    conformes = (df["Pontuacao_total"] == 100).sum()
    nao_conformes = (df["Pontuacao_total"] < 100).sum()
    
    labels = ["Conforme", "Não-conforme"]
    valores = [conformes, nao_conformes]
    cores_status = [COLORS["success"], COLORS["danger"]]
    
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=valores,
                marker=dict(colors=cores_status),
                textposition="inside",
                textinfo="label+percent",
                hovertemplate="<b>%{label}</b><br>Quantidade: %{value}<br>Percentual: %{percent}<extra></extra>",
            )
        ]
    )
    
    fig.update_layout(
        title="Status Geral das Crianças",
        height=400,
    )
    
    return fig


def criar_grafico_distribuicao_idade(df: pd.DataFrame) -> go.Figure:
    """
    Cria gráfico de distribuição por faixa etária.
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        Figura Plotly
    """
    distribuicao = df["Faixa_etaria"].value_counts().sort_index()
    
    fig = go.Figure(
        data=[
            go.Bar(
                x=distribuicao.index,
                y=distribuicao.values,
                marker=dict(color=COLORS["primary"]),
                text=distribuicao.values,
                textposition="auto",
                hovertemplate="<b>%{x}</b><br>Quantidade: %{y}<extra></extra>",
            )
        ]
    )
    
    fig.update_layout(
        title="Distribuição por Faixa Etária",
        xaxis_title="Faixa Etária",
        yaxis_title="Quantidade de Crianças",
        hovermode="x unified",
        template="plotly_white",
        height=400,
    )
    
    return fig


def criar_grafico_sexo(df: pd.DataFrame) -> go.Figure:
    """
    Cria gráfico de distribuição por sexo.
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        Figura Plotly
    """
    distribuicao = df["Sexo"].value_counts()
    cores_sexo = {
        "Masculino": "#3498db",
        "Feminino": "#e74c3c",
        "Não informado": "#95a5a6",
    }
    
    fig = go.Figure(
        data=[
            go.Pie(
                labels=distribuicao.index,
                values=distribuicao.values,
                marker=dict(colors=[cores_sexo.get(x, COLORS["light"]) for x in distribuicao.index]),
                textposition="inside",
                textinfo="label+percent",
                hovertemplate="<b>%{label}</b><br>Quantidade: %{value}<br>Percentual: %{percent}<extra></extra>",
            )
        ]
    )
    
    fig.update_layout(
        title="Distribuição por Sexo",
        height=400,
    )
    
    return fig


def criar_heatmap_indicadores(df: pd.DataFrame) -> go.Figure:
    """
    Cria heatmap de conformidade dos indicadores por faixa etária.
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        Figura Plotly
    """
    # Criar matriz de conformidade
    faixas = df["Faixa_etaria"].unique()
    indicadores = ["A", "B", "C", "D", "E"]
    
    matriz = []
    for faixa in sorted(faixas):
        df_faixa = df[df["Faixa_etaria"] == faixa]
        linha = []
        for ind in indicadores:
            col = f"Indicador_{ind}"
            percentual = (df_faixa[col].sum() / len(df_faixa) * 100) if len(df_faixa) > 0 else 0
            linha.append(percentual)
        matriz.append(linha)
    
    fig = go.Figure(
        data=go.Heatmap(
            z=matriz,
            x=indicadores,
            y=sorted(faixas),
            colorscale="RdYlGn",
            text=[[f"{v:.0f}%" for v in linha] for linha in matriz],
            texttemplate="%{text}",
            textfont={"size": 12},
            hovertemplate="<b>Indicador %{x}</b><br>Faixa: %{y}<br>Conformidade: %{z:.1f}%<extra></extra>",
        )
    )
    
    fig.update_layout(
        title="Heatmap de Conformidade por Indicador e Faixa Etária",
        xaxis_title="Indicador",
        yaxis_title="Faixa Etária",
        height=400,
    )
    
    return fig


def criar_tabela_crianças(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepara DataFrame para exibição em tabela.
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        DataFrame formatado para exibição
    """
    colunas_exibicao = [
        "Nome",
        "Data de nascimento",
        "Idade",
        "Sexo",
        "Raça/cor",
        "Bairro",
        "Indicador_A",
        "Indicador_B",
        "Indicador_C",
        "Indicador_D",
        "Indicador_E",
        "Pontuacao_total",
        "Status_geral",
    ]
    
    df_exibicao = df[colunas_exibicao].copy()
    
    # Renomear colunas para exibição
    df_exibicao = df_exibicao.rename(
        columns={
            "Indicador_A": "A",
            "Indicador_B": "B",
            "Indicador_C": "C",
            "Indicador_D": "D",
            "Indicador_E": "E",
            "Pontuacao_total": "Pontuação",
            "Status_geral": "Status",
        }
    )
    
    # Converter booleanos para símbolos
    for col in ["A", "B", "C", "D", "E"]:
        df_exibicao[col] = df_exibicao[col].apply(lambda x: "✓" if x else "✗")
    
    return df_exibicao


def criar_grafico_conformidade_por_variavel(df: pd.DataFrame, variavel: str, indicador: str = "Indicador_A") -> go.Figure:
    """
    Cria gráfico de barras agrupadas comparando Conforme vs Não-conforme para uma variável.
    
    Args:
        df: DataFrame com os dados processados
        variavel: Nome da coluna para agrupar (ex: "Sexo", "Raça/cor", etc)
        indicador: Coluna do indicador a analisar (padrão: "Indicador_A")
        
    Returns:
        Figura Plotly
    """
    # Obter valores únicos da variável
    valores = df[variavel].dropna().unique()
    
    conformes = []
    nao_conformes = []
    labels = []
    percentuais_conf = []
    percentuais_nao_conf = []
    
    for valor in valores:
        df_valor = df[df[variavel] == valor]
        total = len(df_valor)
        
        if total > 0:
            conf = int(df_valor[indicador].sum())
            nao_conf = total - conf
            perc_conf = (conf / total * 100)
            perc_nao_conf = (nao_conf / total * 100)
            
            conformes.append(conf)
            nao_conformes.append(nao_conf)
            percentuais_conf.append(perc_conf)
            percentuais_nao_conf.append(perc_nao_conf)
            labels.append(str(valor))
    
    fig = go.Figure(
        data=[
            go.Bar(
                x=labels,
                y=conformes,
                name="Conforme",
                marker=dict(color="#28a745"),
                text=[f"{c}<br>({p:.1f}%)" for c, p in zip(conformes, percentuais_conf)],
                textposition="auto",
                hovertemplate="<b>%{x}</b><br>Conforme: %{y} (%{customdata:.1f}%)<extra></extra>",
                customdata=percentuais_conf,
            ),
            go.Bar(
                x=labels,
                y=nao_conformes,
                name="Não-conforme",
                marker=dict(color="#dc3545"),
                text=[f"{nc}<br>({p:.1f}%)" for nc, p in zip(nao_conformes, percentuais_nao_conf)],
                textposition="auto",
                hovertemplate="<b>%{x}</b><br>Não-conforme: %{y} (%{customdata:.1f}%)<extra></extra>",
                customdata=percentuais_nao_conf,
            ),
        ]
    )
    
    fig.update_layout(
        title=f"Conformidade por {variavel}",
        xaxis_title=variavel,
        yaxis_title="Quantidade de Crianças",
        barmode="group",
        hovermode="x unified",
        template="plotly_white",
        height=400,
    )
    
    return fig


def criar_mapa_conformidade(df: pd.DataFrame, indicador: str = "Indicador_A") -> go.Figure:
    """
    Cria mapa de localização com marcadores de conformidade.
    
    Args:
        df: DataFrame com os dados processados
        indicador: Coluna do indicador a analisar (padrão: "Indicador_A")
        
    Returns:
        Figura Plotly
    """
    # Separar conforme e não-conforme
    df_conforme = df[df[indicador] == True]
    df_nao_conforme = df[df[indicador] == False]
    
    # Criar figura
    fig = go.Figure()
    
    # Adicionar marcadores para conforme (verde)
    if len(df_conforme) > 0:
        fig.add_trace(go.Scattergeo(
            lon=df_conforme.get("Longitude", [0] * len(df_conforme)),
            lat=df_conforme.get("Latitude", [0] * len(df_conforme)),
            mode="markers",
            name="Conforme",
            marker=dict(
                size=10,
                color="#28a745",
                opacity=0.7,
                line=dict(width=2, color="darkgreen")
            ),
            text=df_conforme.get("Nome", ""),
            hovertemplate="<b>%{text}</b><br>Conforme<extra></extra>",
        ))
    
    # Adicionar marcadores para não-conforme (vermelho)
    if len(df_nao_conforme) > 0:
        fig.add_trace(go.Scattergeo(
            lon=df_nao_conforme.get("Longitude", [0] * len(df_nao_conforme)),
            lat=df_nao_conforme.get("Latitude", [0] * len(df_nao_conforme)),
            mode="markers",
            name="Não-conforme",
            marker=dict(
                size=10,
                color="#dc3545",
                opacity=0.7,
                line=dict(width=2, color="darkred")
            ),
            text=df_nao_conforme.get("Nome", ""),
            hovertemplate="<b>%{text}</b><br>Não-conforme<extra></extra>",
        ))
    
    fig.update_layout(
        title="Mapa de Conformidade - Localização das Crianças",
        geo=dict(
            scope="south america",
            projection_type="mercator",
            showland=True,
            landcolor="rgb(243, 243, 243)",
            coastcolor="rgb(204, 204, 204)",
        ),
        height=500,
        hovermode="closest",
    )
    
    return fig


def criar_tabela_contatos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepara DataFrame com informações de contato para exibição.
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        DataFrame formatado para exibição
    """
    colunas_exibicao = [
        "Nome",
        "CPF",
        "CNS",
        "Telefone celular",
        "Telefone residencial",
        "Telefone de contato",
    ]
    
    # Verificar quais colunas existem
    colunas_exibicao = [c for c in colunas_exibicao if c in df.columns]
    
    df_exibicao = df[colunas_exibicao].copy()
    
    return df_exibicao


def contar_doses_vacina(texto_vacina):
    """
    Conta o número de doses em um texto de vacinação.
    
    Args:
        texto_vacina: String com informações de doses
        
    Returns:
        Número de doses encontradas
    """
    if pd.isna(texto_vacina) or texto_vacina == "-" or texto_vacina == "":
        return 0
    
    texto = str(texto_vacina).upper()
    doses = 0
    if "D -" in texto or "D1 -" in texto:
        doses += 1
    if "D2 -" in texto:
        doses += 1
    if "D3 -" in texto:
        doses += 1
    
    return doses


def criar_tabela_analise_vacinas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria tabela detalhada com análise de vacinas por criança.
    
    Args:
        df: DataFrame com os dados processados
        
    Returns:
        DataFrame formatado com análise de vacinas
    """
    col_penta = "Difteria, Tétano, Pertusis, Hepatite B, Haemophilus Influenza B"
    col_vip = "Poliomielite"
    col_scr = "Sarampo, Caxumba, Rubéola"
    col_vpc10 = "Pneumocócica"
    
    dados_vacinas = []
    
    for idx, row in df.iterrows():
        penta_doses = contar_doses_vacina(row.get(col_penta, "-"))
        vip_doses = contar_doses_vacina(row.get(col_vip, "-"))
        scr_doses = contar_doses_vacina(row.get(col_scr, "-"))
        vpc10_doses = contar_doses_vacina(row.get(col_vpc10, "-"))
        
        # Calcular faltantes
        penta_falta = max(0, 3 - penta_doses)
        vip_falta = max(0, 3 - vip_doses)
        scr_falta = max(0, 1 - scr_doses)
        vpc10_falta = max(0, 3 - vpc10_doses)
        
        # Status de conformidade
        penta_status = "✓" if penta_doses >= 3 else "✗"
        vip_status = "✓" if vip_doses >= 3 else "✗"
        scr_status = "✓" if scr_doses >= 1 else "✗"
        vpc10_status = "✓" if vpc10_doses >= 3 else "✗"
        
        dados_vacinas.append({
            "Nome": row.get("Nome", ""),
            "Penta (3D)": f"{penta_doses}/3 {penta_status}",
            "Falta": penta_falta if penta_falta > 0 else "-",
            "VIP (3D)": f"{vip_doses}/3 {vip_status}",
            "Falta.1": vip_falta if vip_falta > 0 else "-",
            "SCR (1D)": f"{scr_doses}/1 {scr_status}",
            "Falta.2": scr_falta if scr_falta > 0 else "-",
            "VPC10 (3D)": f"{vpc10_doses}/3 {vpc10_status}",
            "Falta.3": vpc10_falta if vpc10_falta > 0 else "-",
        })
    
    df_vacinas = pd.DataFrame(dados_vacinas)
    
    return df_vacinas


def criar_grafico_cobertura_vacinal(df: pd.DataFrame) -> go.Figure:
    """
    Cria gráfico de cobertura vacinal por tipo de vacina.
    
    Args:
        df: DataFrame com os dados processados
        
    Returns:
        Figura Plotly
    """
    col_penta = "Difteria, Tétano, Pertusis, Hepatite B, Haemophilus Influenza B"
    col_vip = "Poliomielite"
    col_scr = "Sarampo, Caxumba, Rubéola"
    col_vpc10 = "Pneumocócica"
    
    total = len(df)
    
    # Contar crianças com doses completas por vacina
    penta_completo = sum(1 for _, row in df.iterrows() if contar_doses_vacina(row.get(col_penta, "-")) >= 3)
    vip_completo = sum(1 for _, row in df.iterrows() if contar_doses_vacina(row.get(col_vip, "-")) >= 3)
    scr_completo = sum(1 for _, row in df.iterrows() if contar_doses_vacina(row.get(col_scr, "-")) >= 1)
    vpc10_completo = sum(1 for _, row in df.iterrows() if contar_doses_vacina(row.get(col_vpc10, "-")) >= 3)
    
    # Calcular percentuais
    penta_perc = (penta_completo / total * 100) if total > 0 else 0
    vip_perc = (vip_completo / total * 100) if total > 0 else 0
    scr_perc = (scr_completo / total * 100) if total > 0 else 0
    vpc10_perc = (vpc10_completo / total * 100) if total > 0 else 0
    
    vacinas = ["Penta\n(3 doses)", "VIP\n(3 doses)", "SCR\n(1 dose)", "VPC10\n(3 doses)"]
    percentuais = [penta_perc, vip_perc, scr_perc, vpc10_perc]
    cores = ["#28a745", "#17a2b8", "#ffc107", "#dc3545"]
    
    fig = go.Figure(
        data=[
            go.Bar(
                x=vacinas,
                y=percentuais,
                marker=dict(color=cores),
                text=[f"{p:.1f}%" for p in percentuais],
                textposition="auto",
                hovertemplate="<b>%{x}</b><br>Cobertura: %{y:.1f}%<extra></extra>",
            )
        ]
    )
    
    fig.update_layout(
        title="Cobertura Vacinal por Tipo de Vacina",
        xaxis_title="Tipo de Vacina",
        yaxis_title="Cobertura (%)",
        yaxis=dict(range=[0, 100]),
        hovermode="x unified",
        template="plotly_white",
        height=400,
    )
    
    return fig


def criar_grafico_doses_faltantes(df: pd.DataFrame) -> go.Figure:
    """
    Cria gráfico com distribuição de doses faltantes.
    
    Args:
        df: DataFrame com os dados processados
        
    Returns:
        Figura Plotly
    """
    col_penta = "Difteria, Tétano, Pertusis, Hepatite B, Haemophilus Influenza B"
    col_vip = "Poliomielite"
    col_scr = "Sarampo, Caxumba, Rubéola"
    col_vpc10 = "Pneumocócica"
    
    # Contar doses faltantes por vacina
    penta_faltantes = sum(max(0, 3 - contar_doses_vacina(row.get(col_penta, "-"))) for _, row in df.iterrows())
    vip_faltantes = sum(max(0, 3 - contar_doses_vacina(row.get(col_vip, "-"))) for _, row in df.iterrows())
    scr_faltantes = sum(max(0, 1 - contar_doses_vacina(row.get(col_scr, "-"))) for _, row in df.iterrows())
    vpc10_faltantes = sum(max(0, 3 - contar_doses_vacina(row.get(col_vpc10, "-"))) for _, row in df.iterrows())
    
    vacinas = ["Penta", "VIP", "SCR", "VPC10"]
    doses_faltantes = [penta_faltantes, vip_faltantes, scr_faltantes, vpc10_faltantes]
    
    fig = go.Figure(
        data=[
            go.Bar(
                x=vacinas,
                y=doses_faltantes,
                marker=dict(color="#dc3545"),
                text=doses_faltantes,
                textposition="auto",
                hovertemplate="<b>%{x}</b><br>Doses faltantes: %{y}<extra></extra>",
            )
        ]
    )
    
    fig.update_layout(
        title="Total de Doses Faltantes por Tipo de Vacina",
        xaxis_title="Tipo de Vacina",
        yaxis_title="Quantidade de Doses Faltantes",
        hovermode="x unified",
        template="plotly_white",
        height=400,
    )
    
    return fig
