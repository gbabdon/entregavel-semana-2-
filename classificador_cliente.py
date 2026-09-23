idade = int(input("Digite a idade: "))

renda = float(input("Digite a renda mensal: "))

if idade < 18:
    categoria = "Bronze"
elif renda < 3000:
    categoria = "Prata"
elif renda < 10000:
    categoria = "Ouro"
else:
    categoria = "Diamante"

print(f"Categoria do cliente: {categoria}")
