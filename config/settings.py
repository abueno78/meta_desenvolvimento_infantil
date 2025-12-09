"""
Configurações globais do dashboard
"""

# Cores e tema
COLORS = {
    "primary": "#1f77b4",
    "success": "#2ca02c",
    "warning": "#ff7f0e",
    "danger": "#d62728",
    "info": "#17a2b8",
    "light": "#f8f9fa",
    "dark": "#343a40",
}

# Indicadores (Metas)
INDICATORS = {
    "A": {
        "nome": "1ª Consulta Presencial",
        "descricao": "1ª consulta presencial realizada até 30º dia de vida",
        "pontos": 20,
        "cor": COLORS["success"],
    },
    "B": {
        "nome": "Consultas Presenciais/Remotas",
        "descricao": "Mínimo 9 consultas presenciais ou remotas até 2 anos",
        "pontos": 20,
        "cor": COLORS["info"],
    },
    "C": {
        "nome": "Medições Peso/Altura",
        "descricao": "Mínimo 9 registros simultâneos de peso e altura até 2 anos",
        "pontos": 20,
        "cor": COLORS["warning"],
    },
    "D": {
        "nome": "Visitas Domiciliares",
        "descricao": "Mínimo 2 visitas domiciliares (ACS/TACS) - 1ª até 30 dias, 2ª até 6 meses",
        "pontos": 20,
        "cor": COLORS["primary"],
    },
    "E": {
        "nome": "Vacinação Completa",
        "descricao": "Penta (3 doses), VIP (3 doses), VPC10 (3 doses), SCR (1 dose)",
        "pontos": 20,
        "cor": COLORS["danger"],
    },
}

# Limites dos indicadores
INDICATOR_LIMITS = {
    "A": {"dias": 30},  # Dias para 1ª consulta
    "B": {"consultas": 9},  # Mínimo de consultas
    "C": {"registros": 9},  # Mínimo de registros peso/altura
    "D": {
        "visitas": 2,
        "primeira_visita_dias": 30,  # 1ª visita até 30 dias
        "segunda_visita_meses": 6,   # 2ª visita até 6 meses
    },
    "E": {
        "penta_doses": 3,      # Penta: 3 doses
        "vip_doses": 3,        # VIP: 3 doses
        "vpc10_doses": 3,      # VPC10: 3 doses
        "scr_doses": 1,        # SCR: 1 dose
    },
}

# Faixas etárias
FAIXAS_ETARIAS = {
    "0-6 meses": (0, 6),
    "6-12 meses": (6, 12),
    "12-24 meses": (12, 24),
}

# Opções de filtros
FILTROS = {
    "sexo": ["Todos", "Masculino", "Feminino"],
    "raca_cor": ["Todos", "BRANCA", "PARDA", "PRETA", "INDÍGENA", "AMARELA"],
    "bolsa_familia": ["Todos", "Sim", "Não"],
    "status": ["Todos", "Conforme", "Não-conforme"],
}

# Parâmetros de Avaliação
PARAMETROS = {
    "otimo": {"min": 75, "max": 100, "label": "Ótimo", "cor": "#27ae60"},
    "bom": {"min": 50, "max": 75, "label": "Bom", "cor": "#3498db"},
    "suficiente": {"min": 25, "max": 50, "label": "Suficiente", "cor": "#f39c12"},
    "regular": {"min": 0, "max": 25, "label": "Regular", "cor": "#e74c3c"},
}

# Configurações de página
PAGE_CONFIG = {
    "page_title": "Dashboard - Desenvolvimento Infantil",
    "page_icon": "👶",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

# Configurações de dados
DATA_CONFIG = {
    "csv_path": "dados_utf8.csv",
    "skiprows": 24,
    "sep": ";",
    "encoding": "utf-8",
}

# Textos da Sidebar
SIDEBAR_TEXTS = {
    "apresentacao": """Bem-vindo ao Dashboard de Monitoramento de Desenvolvimento Infantil!
    
Esta ferramenta foi desenvolvida para avaliar e acompanhar indicadores de qualidade do cuidado 
no desenvolvimento infantil, baseado na Nota Metodológica C2 do Ministério da Saúde.
    
Você pode analisar dados de crianças de 0 a 2 anos e acompanhar 5 indicadores principais de saúde.""",
    
    "passo_a_passo": """**Como usar:**
1. Faça upload do seu arquivo CSV
2. Selecione os filtros desejados
3. Analise as metas e indicadores
4. Visualize gráficos e relatórios
5. Exporte os dados se necessário""",
}
