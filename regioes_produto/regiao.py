codigo = int(input("Digite o código do produto: "))

match codigo:
    case 1:
        print("Produto oriundo da Região Sul")
    case 2:
        print("Produto oriundo da Região Norte")
    case 3:
        print("Produto oriundo da Região Leste")
    case 4:
        print("Prdoduto oriundo da Região Oeste")
    case c if c == 5 or c == 6:
        print("Produto oriundo da Região Nordeste")
    case 7 | 8 | 9:
        print("Produto oriundo da Região Sudeste")
    case 10:
        print("Produto oriundo da Região Centro-Oeste")
    case 11:
        print("Prodduto oriundo da REgião Noroeste")
    case _:
        print("produto Importado")