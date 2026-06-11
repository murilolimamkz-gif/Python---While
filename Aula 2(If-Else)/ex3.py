nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
idade = int(input("Digite sua idade: "))
plano = input("Digite seu plano (bronze, prata ou ouro): ").lower()

print("DADOS DO CLIENTE")
print("Nome:", nome)
print("CPF:", cpf)
print("Idade:", idade)
print("Plano:", plano)

print("FILMES DISPONÍVEIS")

if plano == "bronze":
    print("- Forrest Gump")
    print("- Toy Story")
    print("- O Rei Leão")
    print("- Jurassic Park")
    print("- Titanic")
    print("- Harry Potter e a Pedra Filosofal")
    print("- De Volta para o Futuro")

elif plano == "prata":
    print("- Forrest Gump")
    print("- Toy Story")
    print("- O Rei Leão")
    print("- Jurassic Park")
    print("- Titanic")
    print("- Harry Potter e a Pedra Filosofal")
    print("- De Volta para o Futuro")
    print("- Matrix")
    print("- Gladiador")
    print("- Os Vingadores")

    if idade >= 18:
        print("- O Exorcista")
        print("- It — A Coisa")

elif plano == "ouro":
    print("- Forrest Gump")
    print("- Toy Story")
    print("- O Rei Leão")
    print("- Jurassic Park")
    print("- Titanic")
    print("- Harry Potter e a Pedra Filosofal")
    print("- De Volta para o Futuro")
    print("- Matrix")
    print("- Gladiador")
    print("- Os Vingadores")
    print("- Interestelar")
    print("- Clube da Luta")
    print("- A Origem")

    if idade >= 18:
        print("- O Exorcista")
        print("- It — A Coisa")

else:
    print("Plano inválido! Digite bronze, prata ou ouro.")