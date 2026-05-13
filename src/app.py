import requests

tarefas = []

def obter_clima(cidade):
    url = f"https://wttr.in/{cidade}?format=j1"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        temperatura = dados["current_condition"][0]["temp_C"]
        return temperatura

    return None


def adicionar_consumo(quantidade):
    if quantidade <= 0:
        raise ValueError("Quantidade inválida")
    tarefas.append(quantidade)


def total_consumido():
    return sum(tarefas)


def main():

    cidade = input("Digite sua cidade: ")
    temperatura = obter_clima(cidade)

    if temperatura:
        print(f"\nTemperatura atual em {cidade}: {temperatura}°C")

        if int(temperatura) >= 30:
            print("Está quente! Beba mais água hoje.\n")

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