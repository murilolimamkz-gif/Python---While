nome = input("Digite seu nome: ")
saldo = float(input("Digite o seu saldo inicial(em R$): "))

quantidade_saques = 0
total_sacado = 0

while saldo > 0:
    saque = float(input("\nDigite o valor do saque (0 para encerrar): "))
    
    if saque == 0:
        print("Atendimento encerrado pelo cliente.")
        break

    elif saque < 0:
        print("Valor inválido, não é permitido sacar valores negativos.")

    elif saque > saldo:
        print("Saldo insuficiente, não é possícel realizar o saque")

    else:
        saldo = saldo - saque
        quantidade_saques = quantidade_saques + 1
        total_sacado = total_sacado + saldo

        print("Seu saque foi realizado com sucesso!")
        print("Seu saldo atual é de R$", saldo)

        if saldo == 0:
            print("Saldo zerado. Seu atendimento será ecerrado atuamaticamente.")
            break

print("\nResumo do Atendimento:")
print("Cliente:", nome)
print("Quantidades de saques efetuados:", quantidade_saques)
print("Total sacadoo:", total_sacado)
print("Saldo final:", saldo)

    
