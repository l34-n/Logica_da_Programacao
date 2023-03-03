print('''
-------------------------------------------------------------------------------------------------
        ██████╗  █████╗  ██████╗  █████╗ ███╗   ███╗███████╗███╗   ██╗████████╗ ██████╗ 
        ██╔══██╗██╔══██╗██╔════╝ ██╔══██╗████╗ ████║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗
        ██████╔╝███████║██║  ███╗███████║██╔████╔██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║
        ██╔═══╝ ██╔══██║██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   ██║   ██║
        ██║     ██║  ██║╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   ╚██████╔╝
        ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝                                                                               
-------------------------------------------------------------------------------------------------
Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário.                                                      
''')

iNome = input("Nome do Funcionário: ")
iValor_Hora = float(input("Valor por Hora: "))
iHoras_Trabalhadas = int(input("Quantidade de Horas Trabalhadas: "))

iCalculo = iValor_Hora * iHoras_Trabalhadas

print("\nO Valor Total para Pagamento é de: ",format(iCalculo,'.2f'),'\n')