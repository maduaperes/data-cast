# =======================================================================
# SISTEMA DE RH: CÁLCULO DE FOLHA DE PAGAMENTO COM FUNÇÕES
# ======================================================================

# --- ÁREA DE CRIAÇÃO DAS NOSSAS FERRAMENTAS (FUNÇÕES) ---


def calcular_salario_base(valor_hora, horas_normais):
    return valor_hora * horas_normais


def calcular_hora_extra(valor_hora, horas_extras):
    """Calcula a hora extra com adicional de 50% (multiplica por 1.5)"""
    valor_hora_extra = valor_hora * 1.5
    return valor_hora_extra * horas_extras


def calcular_desconto_inss(salario_bruto):
    """Simulação simples de desconto de INSS (10% fixo para o exemplo)"""
    desconto = salario_bruto * 0.10
    return desconto


# --- ÁREA DE EXECUÇÃO DO PROGRAMA PRINCIPAL ---
print("=" * 50)
print(" 💰 GERADOR DE HOLERITE AUTOMÁTICO")
print("=" * 50)

# 1. Coletando os dados do funcionário
nome_func = input("Nome do Colaborador: ")
valor_hr = float(input("Valor da hora de trabalho (R$): "))
hr_normais = float(input("Horas normais trabalhadas no mês: "))
hr_extras = float(input("Horas extras trabalhadas no mês: "))

print("\nProcessando folha de pagamento...")

# 2. Invocando as nossas funções (jogando a matéria-prima e pegando o resultado)
salario_base = calcular_salario_base(valor_hr, hr_normais)
pagamento_extra = calcular_hora_extra(valor_hr, hr_extras)

# Somando os ganhos
salario_bruto = salario_base + pagamento_extra

# Passando o salário total pela função de desconto
desconto_imposto = calcular_desconto_inss(salario_bruto)

# Calculando o que vai pingar na conta
salario_liquido = salario_bruto - desconto_imposto

# 3. Imprimindo holerite
print("\n" + "=" * 40)
print(f" HOLERITE: {nome_func.upper()}")
print("=" * 40)
print(f" (+) Salário base:   R${salario_bruto:.2f}")
print(f" (+) Horas extras:   R${pagamento_extra:.2f}")
print(f" (-) Desconto INSS:   R${desconto_imposto:.2f}")
print("=" * 40)
print(f" (=) Salário liquido:   R${salario_liquido:.2f}")
print("=" * 40)
