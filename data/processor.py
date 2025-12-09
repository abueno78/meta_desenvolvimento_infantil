"""
Módulo para processamento de dados
"""

import pandas as pd
from datetime import datetime
from data.loader import extrair_idade_meses


def processar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Processa os dados adicionando colunas calculadas.
    
    Args:
        df: DataFrame com dados brutos
        
    Returns:
        DataFrame processado com colunas adicionais
    """
    df = df.copy()
    
    # Converter colunas de data para datetime
    colunas_data = [
        "Data de nascimento",
        "Data da primeira consulta",
        "Data da primeira visita domiciliar",
        "Data da segunda visita domiciliar",
        "Data da ultima medição de peso e altura",
    ]
    
    for col in colunas_data:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], format='%d/%m/%Y', errors='coerce')
    
    # Calcular idade em meses
    df["Idade_meses"] = df["Idade"].apply(extrair_idade_meses)
    
    # Calcular faixa etária
    df["Faixa_etaria"] = df["Idade_meses"].apply(_calcular_faixa_etaria)
    
    # Calcular indicadores
    df["Indicador_A"] = df.apply(_calcular_indicador_a, axis=1)
    df["Indicador_B"] = df.apply(_calcular_indicador_b, axis=1)
    df["Indicador_C"] = df.apply(_calcular_indicador_c, axis=1)
    df["Indicador_D"] = df.apply(_calcular_indicador_d, axis=1)
    df["Indicador_E"] = df.apply(_calcular_indicador_e, axis=1)
    
    # Calcular pontuação total
    df["Pontuacao_total"] = (
        df["Indicador_A"].astype(int) * 20 +
        df["Indicador_B"].astype(int) * 20 +
        df["Indicador_C"].astype(int) * 20 +
        df["Indicador_D"].astype(int) * 20 +
        df["Indicador_E"].astype(int) * 20
    )
    
    # Status geral
    df["Status_geral"] = df["Pontuacao_total"].apply(
        lambda x: "Conforme" if x == 100 else "Não-conforme"
    )
    
    return df


def _calcular_faixa_etaria(idade_meses: int) -> str:
    """Calcula a faixa etária baseada na idade em meses."""
    if pd.isna(idade_meses):
        return "Desconhecida"
    if idade_meses < 6:
        return "0-6 meses"
    elif idade_meses < 12:
        return "6-12 meses"
    elif idade_meses <= 24:
        return "12-24 meses"
    else:
        return "Acima de 24 meses"


def _calcular_indicador_a(row) -> bool:
    """
    Indicador A: 1ª consulta presencial até 30º dia de vida.
    """
    if pd.isna(row["Data de nascimento"]) or pd.isna(row["Data da primeira consulta"]):
        return False
    
    try:
        dias_para_consulta = (row["Data da primeira consulta"] - row["Data de nascimento"]).days
        return dias_para_consulta <= 30
    except:
        return False


def _calcular_indicador_b(row) -> bool:
    """
    Indicador B: Mínimo 9 consultas presenciais ou remotas até 2 anos.
    """
    try:
        consultas = row["Quantidade de consultas até 24 meses"]
        # Converter para número se for string
        if isinstance(consultas, str):
            consultas = float(consultas.replace(',', '.'))
        return pd.notna(consultas) and consultas >= 9
    except:
        return False


def _calcular_indicador_c(row) -> bool:
    """
    Indicador C: Mínimo 9 registros simultâneos de peso e altura até 2 anos.
    """
    try:
        registros = row["Quantidade de medições de peso/altura simultâneas até 24 meses"]
        # Converter para número se for string
        if isinstance(registros, str):
            registros = float(registros.replace(',', '.'))
        return pd.notna(registros) and registros >= 9
    except:
        return False


def _calcular_indicador_d(row) -> bool:
    """
    Indicador D: Mínimo 2 visitas domiciliares (ACS/TACS).
    - 1ª visita: até 30 dias de vida
    - 2ª visita: até 6 meses de vida
    """
    try:
        # Verificar quantidade mínima de visitas
        visitas = row["Quantidade de visitas domiciliares até os 24 meses de idade"]
        
        # Converter para número se for string
        if isinstance(visitas, str):
            visitas = float(visitas.replace(',', '.'))
        
        if pd.isna(visitas) or visitas < 2:
            return False
        
        # Verificar datas das visitas
        data_nasc = row["Data de nascimento"]
        data_primeira_visita = row["Data da primeira visita domiciliar"]
        data_segunda_visita = row["Data da segunda visita domiciliar"]
        
        # Se não tem datas, não pode validar
        if pd.isna(data_nasc):
            return False
        
        # 1ª visita deve ser até 30 dias
        if pd.notna(data_primeira_visita):
            dias_primeira = (data_primeira_visita - data_nasc).days
            if dias_primeira > 30:
                return False
        else:
            return False  # 1ª visita é obrigatória
        
        # 2ª visita deve ser até 6 meses
        if pd.notna(data_segunda_visita):
            meses_segunda = (data_segunda_visita - data_nasc).days / 30.44
            if meses_segunda > 6:
                return False
        else:
            return False  # 2ª visita é obrigatória
        
        return True
    except:
        return False


def _calcular_indicador_e(row) -> bool:
    """
    Indicador E: Vacinação completa conforme Calendário Nacional.
    - Penta (DTP + Hib + HB): 3 doses
    - VIP (Poliomielite): 3 doses
    - VPC10 (Pneumocócica): 3 doses
    - SCR (Sarampo, Caxumba, Rubéola): 1 dose
    """
    try:
        # Colunas de vacinação
        col_penta = "Difteria, Tétano, Pertusis, Hepatite B, Haemophilus Influenza B"
        col_vip = "Poliomielite"
        col_scr = "Sarampo, Caxumba, Rubéola"
        col_vpc10 = "Pneumocócica"
        
        # Verificar se as colunas existem
        if col_penta not in row.index or col_vip not in row.index or col_scr not in row.index or col_vpc10 not in row.index:
            return False
        
        # Contar doses de cada vacina
        def contar_doses(texto_vacina):
            """Conta o número de doses em um texto de vacinação."""
            if pd.isna(texto_vacina) or texto_vacina == "-" or texto_vacina == "":
                return 0
            
            texto = str(texto_vacina).upper()
            # Contar ocorrências de D1, D2, D3 (doses) e D (dose ao nascer)
            doses = 0
            if "D -" in texto or "D1 -" in texto:
                doses += 1
            if "D2 -" in texto:
                doses += 1
            if "D3 -" in texto:
                doses += 1
            
            return doses
        
        # Validar doses de cada vacina
        penta_doses = contar_doses(row[col_penta])
        vip_doses = contar_doses(row[col_vip])
        scr_doses = contar_doses(row[col_scr])
        vpc10_doses = contar_doses(row[col_vpc10])
        
        # Verificar se atende aos requisitos mínimos
        penta_ok = penta_doses >= 3
        vip_ok = vip_doses >= 3
        scr_ok = scr_doses >= 1
        vpc10_ok = vpc10_doses >= 3
        
        return penta_ok and vip_ok and scr_ok and vpc10_ok
    except:
        return False


def calcular_estatisticas(df: pd.DataFrame) -> dict:
    """
    Calcula estatísticas gerais dos indicadores.
    
    Args:
        df: DataFrame processado
        
    Returns:
        Dicionário com estatísticas
    """
    total_criancas = len(df)
    
    stats = {
        "total_criancas": total_criancas,
        "conformes": (df["Pontuacao_total"] == 100).sum(),
        "nao_conformes": (df["Pontuacao_total"] < 100).sum(),
        "percentual_conforme": ((df["Pontuacao_total"] == 100).sum() / total_criancas * 100) if total_criancas > 0 else 0,
        "indicador_a": {
            "conformes": df["Indicador_A"].sum(),
            "percentual": (df["Indicador_A"].sum() / total_criancas * 100) if total_criancas > 0 else 0,
        },
        "indicador_b": {
            "conformes": df["Indicador_B"].sum(),
            "percentual": (df["Indicador_B"].sum() / total_criancas * 100) if total_criancas > 0 else 0,
        },
        "indicador_c": {
            "conformes": df["Indicador_C"].sum(),
            "percentual": (df["Indicador_C"].sum() / total_criancas * 100) if total_criancas > 0 else 0,
        },
        "indicador_d": {
            "conformes": df["Indicador_D"].sum(),
            "percentual": (df["Indicador_D"].sum() / total_criancas * 100) if total_criancas > 0 else 0,
        },
        "indicador_e": {
            "conformes": df["Indicador_E"].sum(),
            "percentual": (df["Indicador_E"].sum() / total_criancas * 100) if total_criancas > 0 else 0,
        },
    }
    
    return stats
