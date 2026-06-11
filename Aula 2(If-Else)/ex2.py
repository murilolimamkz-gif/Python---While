nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
tipo_cliente = input("Digite o tipo de cliente (PREMIUM, GOLD ou REGULAR): ").upper()
peso_bagagem = float(input("Digite o peso da bagagem despachada (em kg): "))

if tipo_cliente == "PREMIUM" or tipo_cliente == "GOLD" or tipo_cliente == "REGULAR":

    if (tipo_cliente == "PREMIUM" and peso_bagagem <= 40) or \
       (tipo_cliente == "GOLD" and peso_bagagem <= 30) or \
       (tipo_cliente == "REGULAR" and peso_bagagem <= 20):

        print(f"Parabens {nome} ! Sua bagagem esta dentro do limite permitido.")

    else:
        if tipo_cliente == "PREMIUM":
            excesso = peso_bagagem - 40

        elif tipo_cliente == "GOLD":
            excesso = peso_bagagem - 30

        else: 
            excesso = peso_bagagem - 20

        valor = excesso * 2

        print(f"Atencao, {nome} . Voce excedeu o limite em {excesso} kg.")
        print(f"Sera necessario pagar R$ {valor} no balcao.")

else:
    print("Erro: tipo de cliente invalido. Digite PREMIUM, GOLD ou REGULAR.")