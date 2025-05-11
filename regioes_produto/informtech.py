codigo = int(input("Digite o código da Compra: "))
vl_compra = float(input("Digite o valor da compra: "))

match codigo:
    case 1:
        print("Você escolheu a forma de pagamento: PIX e o Preço é normal.")
        vl_compra = vl_compra + 0
        print(f'O Valor final da compra é: {vl_compra}')
    case 2:
        print("Você escolheu a forma de pagamento: À vista (dinheiro) e receberá 10'%' de desconto")
        vl_compra = vl_compra - (vl_compra * 0.10)
        print(f'O Valor final da compra é: {vl_compra}')
    case 3:
        print("Você escolheu a forma de pagamento: Débito e sofrerá 5'%' de juros")
        vl_compra = vl_compra + (vl_compra * 0.05)
        print(f'O Valor final da compra é: {vl_compra}')
    case 4:
        print("Você escolheu a forma de pagamento: Cartão de crédito e sofrerá 8'%' de juros")
        vl_compra = vl_compra + (vl_compra * 0.08)
        print(f'O Valor final da compra é: {vl_compra}')
    case 5:
        print("Você escolheu a forma de pagamento: Cheque e sofrerá 12'%' de juros")
        vl_compra = vl_compra + (vl_compra * 0.12)
        print(f'O Valor final da compra é: {vl_compra}')
    case _:
        print("Modalidade de compra inválida não efetuar cálculo")
        codigo = 'codigo inválido'
        print('Não foi possível calcular o valor da compra')

    
        
        