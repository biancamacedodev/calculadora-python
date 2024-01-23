saldo = 2000.00

while True:
    print("\n Caixa Eletrônico")
    print("1 - Verificar saldo(extrato)")
    print("2 - Depositar Dinheiro")
    print("3 - Sacar Dinheiro")
    print("4 - Sair")

    opcao = input('Escolha uma opção (1-4):')
    
    if opcao == "1":
        print(f"Seu saldo é: R$ {saldo: .2f}")

    elif opcao == "2":
        deposito = float(input('Digite o valor do depósito: R$ '))

        if deposito > 0:
            saldo += deposito

            print(f"Seu deposito de: R$ {deposito: .2f} foi realizado com sucesso!")
        
        else:
            print("Deposito inválido!")
          
    elif opcao == "3":
        saque = float(input('Digite o valor do Saque: R$ '))

        if saque > 0 and saque <= saldo:
            saldo -= deposito
            print(f"Saque de: R$ {saque: .2f} foi realizado com sucesso!")
        
        else:
            print("Saque inválido ou saldo insuficiente!")
   
    elif opcao == "4":
        print(f"Obrigada por utilizar nossos serviços. Volte sempre!")

        break

    else: 
        print('opção inválida!')

