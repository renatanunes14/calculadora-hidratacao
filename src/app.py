tarefas = []

def adicionar_consumo(quantidade):
    if quantidade <= 0:
        raise ValueError("Quantidade inválida")
    tarefas.append(quantidade)

def total_consumido():
    return sum(tarefas)

def main():
    while True:
        print("\n1 - Registrar água")
        print("2 - Ver total")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                qtd = float(input("Quantidade em ml: "))
                adicionar_consumo(qtd)
                print("Registrado!")
            except ValueError:
                print("Erro ao registrar.")
        
        elif opcao == "2":
            print(f"Total consumido: {total_consumido()} ml")
        
        elif opcao == "3":
            break

if __name__ == "__main__":
    main()