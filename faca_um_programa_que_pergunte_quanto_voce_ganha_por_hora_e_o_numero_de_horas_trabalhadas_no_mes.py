# Solicitar o valor ganho por hora e o número de horas trabalhadas
valor_por_hora = float(input("Informe quanto você ganha por hora: "))
horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))

# Calcular o salário bruto
salario_bruto = valor_por_hora * horas_trabalhadas

# Calcular os descontos
ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto

# Calcular o salário líquido
salario_liquido = salario_bruto - ir - inss - sindicato

# Exibir os resultados
print(f"Salário Bruto : R$ {salario_bruto:.2f}")
print(f"IR (11%) : R$ {ir:.2f}")
print(f"INSS (8%) : R$ {inss:.2f}")
print(f"Sindicato (5%) : R$ {sindicato:.2f}")
print(f"Salário Líquido : R$ {salario_liquido:.2f}")
