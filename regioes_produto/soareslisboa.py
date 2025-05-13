# Nesta escola os estudantes realizam duas avaliações principais ao longo do semestre.
# Além disso, eles têm a opção de realizar uma prova optativa, que pode ser utilizada
# para substituir a menor nota das avaliações principais.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
optativa = float(input("Digite a nota da prova optativa, caso não haja, digite '-1': "))

# Substitui a menor nota pela optativa, se ela for válida
if optativa != -1:
    menor = min(nota1, nota2)
    maior = max(nota1, nota2)
    media = (optativa + maior) / 2
else:
    media = (nota1 + nota2) / 2

# Exibe a média e o status do aluno
print(f"A média do aluno é: {media:.2f}")

if media >= 6.0:
    print("Situação: Aprovado!")
elif 3.0 <= media < 6.0:
    print("Situação: Em exame.")
else:
    print("Situação: Reprovado.")
