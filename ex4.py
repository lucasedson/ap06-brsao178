# Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL).
# O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP),
# e o programa deve exibir o valor atual, máximo e mínimo da cotação, 
# além da data e hora da última atualização.
# Utilize a API da AwesomeAPI para obter os dados de cotação.​

import requests

def consultar_cotacao(moeda, formato="text"):
    moeda = moeda.upper()
    cotacao_final = {
        "cotacao": "",
        "maximo": "",
        "minimo": ""
    }
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        cotacao = response.json()
        # print(cotacao[f"{moeda}BRL"]['bid'])
        cotacao_final["cotacao"] = cotacao[f"{moeda}BRL"]["bid"]
        cotacao_final["maximo"] = cotacao[f"{moeda}BRL"]["high"]
        cotacao_final["minimo"] = cotacao[f"{moeda}BRL"]["low"]

        if formato == "json":
            return cotacao_final
        return f'''
        Moeda: {moeda} - BRL
        Valor Atual: {cotacao_final["cotacao"]}
        Valor Máximo: {cotacao_final["maximo"]}
        Valor Mínimo: {cotacao_final["minimo"]}
        '''
    else:
        return "Moeda inválida."
    
if __name__ == "__main__":
    moeda = input("Informe a moeda desejada (ex: USD, EUR, GBP): ")
    cotacao = consultar_cotacao(moeda)

    print(cotacao)