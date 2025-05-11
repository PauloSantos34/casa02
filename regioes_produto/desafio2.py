from datetime import datetime

# Ano atual
ANO_ATUAL = 2025

# Lista para armazenar os candidatos válidos
candidatos = []

print("=== Cadastro de Candidatos ===")

# Loop para cadastrar até 10 candidatos válidos
while len(candidatos) < 10:
    print(f"\nCadastro do candidato {len(candidatos) + 1}:")
    nome = input("Nome: ")
    ano_nascimento = int(input("Ano de nascimento (ex: 2006): "))
    
    idade = ANO_ATUAL - ano_nascimento
    if idade < 18:
        print("Candidato menor de 18 anos. Cadastro não permitido.")
        continue  # Volta para o início do loop, sem contar esse candidato

    telefone = input("Telefone: ")
    email = input("E-mail: ")
    formacao = input("Formação acadêmica: ")
    experiencia = input("Experiência profissional: ")

    candidato = {
        "Nome": nome,
        "Idade": idade,
        "Telefone": telefone,
        "E-mail": email,
        "Formação Acadêmica": formacao,
        "Experiência Profissional": experiencia
    }

    candidatos.append(candidato)
    print("Candidato cadastrado com sucesso!")

# Exibe todos os candidatos cadastrados
print("\n=== Lista de Candidatos Cadastrados ===")
for i, c in enumerate(candidatos, start=1):
    print(f"\nCandidato {i}:")
    for chave, valor in c.items():
        print(f"{chave}: {valor}")
print("\n=== Cadastro encerrado ===")