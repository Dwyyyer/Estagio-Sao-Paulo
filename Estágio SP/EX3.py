import json

def calcular_faturamento():

    with open('faturamento.json', 'r') as file:
        faturamento_diario = json.load(file)

    faturamento_validos = [dia["faturamento"] for dia in faturamento_diario if dia["faturamento"] > 0]
    
    if not faturamento_validos:
        print("Não há dados de faturamento para calcular.")
        return

    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)
    dias_acima_da_media = len([f for f in faturamento_validos if f > media_mensal])

    print(f"Menor faturamento: {menor_faturamento}")
    print(f"Maior faturamento: {maior_faturamento}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

calcular_faturamento()