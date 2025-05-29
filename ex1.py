import random

def gerar_senha(tamanho_senha=8):
	senha = '' 
	for i in range(0, tamanho_senha):
		senha += str(chr(random.randrange(32, 126)))
	return senha
 


if __name__ == "__main__":
    quantidade = int(input("Informe a quantidade de caracteres da senha: "))
    print(gerar_senha(quantidade))

# Crie um programa que gera uma senha aleatória com o módulo random,
#  utilizando caracteres especiais, 
# possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória. ​