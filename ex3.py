# Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário,
#  utilizando a API ViaCEP. 
# O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.

import requests

def consultar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        endereco = response.json()
        print(f"Logradouro: {endereco['logradouro']}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Cidade: {endereco['localidade']}")
        print(f"Estado: {endereco['uf']}")
    else:
        print("CEP inválido.")

if __name__ == "__main__":
    cep = input("Informe o CEP: ")
    consultar_endereco(cep)