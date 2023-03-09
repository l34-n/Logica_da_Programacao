print('''
--------------------------------------------------------------------------------------------------------

             ██████╗██████╗ ███████╗███████╗ ██████╗███████╗███╗   ██╗████████╗███████╗
            ██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔════╝
            ██║     ██████╔╝█████╗  ███████╗██║     █████╗  ██╔██╗ ██║   ██║   █████╗  
            ██║     ██╔══██╗██╔══╝  ╚════██║██║     ██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  
            ╚██████╗██║  ██║███████╗███████║╚██████╗███████╗██║ ╚████║   ██║   ███████╗
             ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝

--------------------------------------------------------------------------------------------------------
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma
mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O
programa deve finalizar quando forem digitados dois valores iguais.
''')

iNumero_1 = int(input("Digite o Primeiro Número: "))
iNumero_2 = int(input("Digite o Segundo Número: "))

while iNumero_1 != iNumero_2:
    if iNumero_1 < iNumero_2:
       print("\nOrdem Crescente\n")
    else:
        print("\nOrdem Decrescente\n")

    print("Digite Outros Dois Números: ")
    iNumero_1 = int(input())
    iNumero_2 = int(input())