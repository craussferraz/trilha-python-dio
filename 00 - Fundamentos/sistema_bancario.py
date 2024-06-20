saldo = 0
extrato = ""
LIMITE_VALOR_SAQUE = 500
numero_saques = 0
LIMITE_SAQUES = 3

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """ 

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print("Valores disponiveis: 5, 10, 20, 50, 100")
        valor = int(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > LIMITE_VALOR_SAQUE

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite saque. Seu limte é R$ {LIMITE_VALOR_SAQUE} por operação")

        elif excedeu_saques:
            print(f"Operação falhou! Número máximo de saques excedido. Seu limte diario é {LIMITE_SAQUES} saques")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")