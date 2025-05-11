# entrar com os dados de 10 estudantes
# Lista para armazenar os dados dos estudantes
estudantes = []

# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)
# Coletar os dados de 10 estudantres
for i in range(10):
    nome = input(f"Digite o nome do estudante {i + 1}: ")
    notas = []
    for j in range(4): # Supondo que cada estudante tenha 4 notas
        nota = float(input(f"Digite a nota {j +1} de {nome}: "))
        notas.append(nota)

    media = calcular_media(notas)
    status = "Aprovado" if media >= 7 else "Em Recuperação" if 5 <= media < 7 else "Reprovado"
    estudantes.append({'Nome': nome, 'media': media, 'status': status})

    # Exibir os dados dos estudantes
for estudante in estudantes:
    print(f"Nome: {estudante['Nome']}, Média: {estudante['media']:.2f}, status: {estudante['status']}")
    
    