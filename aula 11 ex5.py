def calcular_idade(ano_nascimento, ano_atual):
    """Calcula a idade baseada no ano de nascimento e ano atual"""
    idade = ano_atual - ano_nascimento
    return idade

print(calcular_idade(1970, 2025)) 