from datetime import datetime, date

def calcular_idade(data_nascimento):
    hoje = date.today()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

def calcular_tempo_contribuicao(data_contribuicao):
    hoje = date.today()
    return hoje.year - data_contribuicao.year - ((hoje.month, hoje.day) < (data_contribuicao.month, data_contribuicao.day))

def verificar_aposentadoria():
    print("=== Verificador de Aposentadoria ===")
    
    genero = input("Informe seu gênero (M para masculino, F para feminino): ").strip().upper()
    if genero not in ['M', 'F']:
        print("Gênero inválido.")
        return

    data_nascimento_str = input("Informe sua data de nascimento (DD/MM/AAAA): ")
    data_contribuicao_str = input("Informe a data da sua primeira contribuição (DD/MM/AAAA): ")

    try:
        data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
        data_contribuicao = datetime.strptime(data_contribuicao_str, "%d/%m/%Y").date()
    except ValueError:
        print("Formato de data inválido. Use DD/MM/AAAA.")
        return

    idade = calcular_idade(data_nascimento)
    tempo_contribuicao = calcular_tempo_contribuicao(data_contribuicao)

    if genero == 'M':
        idade_minima = 65
        contribuicao_minima = 20
    else:
        idade_minima = 62
        contribuicao_minima = 15

    print(f"\nIdade atual: {idade} anos")
    print(f"Tempo de contribuição: {tempo_contribuicao} anos\n")

    falta_idade = max(0, idade_minima - idade)
    falta_contribuicao = max(0, contribuicao_minima - tempo_contribuicao)

    if falta_idade == 0 and falta_contribuicao == 0:
        print("🎉 Parabéns! Você já pode se aposentar.")
    else:
        print("⏳ Você ainda não pode se aposentar.")
        if falta_idade > 0:
            print(f" - Faltam {falta_idade} ano(s) para atingir a idade mínima.")
        if falta_contribuicao > 0:
            print(f" - Faltam {falta_contribuicao} ano(s) de contribuição.")

# Executa o programa
verificar_aposentadoria()
# teste com dados ficticios
