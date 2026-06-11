quantidade_de_vendedores = int(input("Quantos vendedores fazem parte da equipe? "))
quantidade_de_dias = int(input("Quantos dias serão analisados? "))

total_da_equipe = 0
maior_venda_do_dia = 0
maior_vendedor = ""
maior_total_do_vendedor = 0


for vendedor in range(quantidade_de_vendedores):
    nome = input("\nNome do vendedor: ")

    total_de_vendas = 0
    dias_de_folga = 0

    for dia in range(quantidade_de_dias):
        venda = float(input("Valor vendido no dia " + str(dia+1) + ": R$"))

        if venda < 0:
            continue

        if venda == 0:
            dias_de_folga = dias_de_folga + 1
            continue

        total_de_vendas = total_de_vendas + venda

        if venda > maior_venda_do_dia:
            maior_venda_do_dia = venda

    media_vendas = total_de_vendas / quantidade_de_dias

    print("\nResumo do Vendedor")
    print("\nNome: ", nome)
    print("Total vendido na semana: R$", total_de_vendas)
    print("Média diária: R$", media_vendas)
    print("Dias de folga: ", dias_de_folga)

    total_da_equipe = total_da_equipe + total_de_vendas

    if total_de_vendas > maior_total_do_vendedor:
        maior_total_do_vendedor = total_de_vendas
        maior_vendedor = nome

print("\nRelatório da equipe")
print("\nTotal vendido pela equipe: R$", total_da_equipe)
print("Vendedor que mais vendeu:", maior_vendedor)
print("Maior venda registrada em um único dia: R$", maior_venda_do_dia)