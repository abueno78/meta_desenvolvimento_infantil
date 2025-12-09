"""
Módulo para carregamento e limpeza de dados
"""

import pandas as pd
from pathlib import Path
from config.settings import DATA_CONFIG


def carregar_dados(caminho_csv: str = None) -> pd.DataFrame:
    """
    Carrega o arquivo CSV e realiza limpeza inicial.
    
    Args:
        caminho_csv: Caminho para o arquivo CSV. Se None, usa o padrão de config.
        
    Returns:
        DataFrame com os dados carregados e limpos
    """
    if caminho_csv is None:
        caminho_csv = DATA_CONFIG["csv_path"]
    
    # Verificar se arquivo existe
    if not Path(caminho_csv).exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_csv}")
    
    # Carregar CSV
    df = pd.read_csv(
        caminho_csv,
        skiprows=DATA_CONFIG["skiprows"],
        sep=DATA_CONFIG["sep"],
        encoding=DATA_CONFIG["encoding"],
    )
    
    # Limpeza inicial
    df = limpar_dados(df)
    
    return df


def limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza limpeza e normalização dos dados.
    
    Args:
        df: DataFrame a ser limpo
        
    Returns:
        DataFrame limpo
    """
    # Remover linhas completamente vazias
    df = df.dropna(how="all")
    
    # Normalizar nomes de colunas
    df.columns = df.columns.str.strip()
    
    # Converter colunas de data
    colunas_data = [
        "Data de nascimento",
        "Data da primeira consulta",
        "Data da primeira visita domiciliar",
        "Data da segunda visita domiciliar",
        "Data da ultima medição de peso e altura",
    ]
    
    for col in colunas_data:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], format="%d/%m/%Y", errors="coerce")
    
    # Converter colunas numéricas
    colunas_numericas = [
        "Dias desde o último atendimento médico",
        "Meses desde o último atendimento médico",
        "Dias desde o último atendimento de enfermagem",
        "Meses desde o último atendimento de enfermagem",
        "Dias desde o último atendimento odontológico",
        "Meses desde o último atendimento odontológico",
        "Dias desde a última visita domiciliar",
        "Meses desde a última visita domiciliar",
        "Última medição de peso",
        "Última medição de altura",
        "Quantidade de consultas até 24 meses",
        "Quantidade de medições de peso/altura simultâneas até 24 meses",
        "Quantidade de visitas domiciliares até os 24 meses de idade",
    ]
    
    for col in colunas_numericas:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    
    # Preencher valores faltantes em colunas categóricas
    df["Sexo"] = df["Sexo"].fillna("Não informado")
    df["Raça/cor"] = df["Raça/cor"].fillna("Não informado")
    
    return df


def extrair_idade_meses(idade_str: str) -> int:
    """
    Extrai a idade em meses a partir da string de idade.
    
    Args:
        idade_str: String no formato "X anos e Y meses e Z dias"
        
    Returns:
        Idade em meses (inteiro)
    """
    if pd.isna(idade_str) or idade_str == "-":
        return None
    
    try:
        idade_str = str(idade_str).lower()
        
        # Extrair anos
        anos = 0
        if "ano" in idade_str:
            anos = int(idade_str.split("ano")[0].strip().split()[-1])
        
        # Extrair meses
        meses = 0
        if "mês" in idade_str:
            partes = idade_str.split("mês")
            meses_str = partes[0].strip().split()[-1]
            meses = int(meses_str)
        
        return anos * 12 + meses
    except (ValueError, IndexError):
        return None
