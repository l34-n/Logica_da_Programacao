print('''
-------------------------------------------------------------------------------------------------
                         ██╗██████╗  █████╗ ██████╗ ███████╗███████╗
                         ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
                         ██║██║  ██║███████║██║  ██║█████╗  ███████╗
                         ██║██║  ██║██╔══██║██║  ██║██╔══╝  ╚════██║
                         ██║██████╔╝██║  ██║██████╔╝███████╗███████║
                         ╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
-------------------------------------------------------------------------------------------------
Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os 
nomes e a idade média entre essas pessoas, com uma casa decimal.                                                             
''')

iNome_Pessoa1 = input("Nome da Primeira Pessoa: ")
iIdade_Pessoa1 = int(input("Idade da Primeira Pessoa: "))
iNome_Pessoa2 = input("Nome da Segunda Pessoa: ")
iIdade_Pessoa2 = int(input("Idade da Segunda Pessoa: "))

iMedia = (iIdade_Pessoa1 + iIdade_Pessoa2) / 2

print("\nDados da Primeira Pessoa")
print("Nome: ",iNome_Pessoa1)
print("Idade: ",iIdade_Pessoa1,"\n")

print("Dados da Segunda Pessoa")
print("Nome: ",iNome_Pessoa2)
print("Idade: ",iIdade_Pessoa2,"\n")

print("A Média de Idades é de:",format(iMedia,'.1f'),"\n")