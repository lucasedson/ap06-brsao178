# Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
# O programa deve exibir o nome, email e país do usuário gerado."

import requests

def gerar_perfil_aleatorio():
    usuario = {
        "nome": "",
        "email": "",
        "pais": ""
    }
    response = requests.get("https://randomuser.me/api/")
    data = response.json()
    user = data["results"][0]

    usuario["nome"] = user["name"]["first"] + " " + user["name"]["last"]
    usuario["email"] = user["email"]
    usuario["pais"] = user["location"]["country"]

    return usuario

if __name__ == "__main__":
    perfil = gerar_perfil_aleatorio()
    print(f"Nome: {perfil['nome']}")
    print(f"Email: {perfil['email']}")
    print(f"Pais: {perfil['pais']}")