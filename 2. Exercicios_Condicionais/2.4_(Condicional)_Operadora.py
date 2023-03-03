print('''
--------------------------------------------------------------------------------------------------------

                 ██████╗ ██████╗ ███████╗██████╗  █████╗ ██████╗  ██████╗ ██████╗  █████╗ 
                ██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗
                ██║   ██║██████╔╝█████╗  ██████╔╝███████║██║  ██║██║   ██║██████╔╝███████║
                ██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║██║  ██║██║   ██║██╔══██╗██╔══██║
                ╚██████╔╝██║     ███████╗██║  ██║██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║
                 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝                                                                                                                               
--------------------------------------------------------------------------------------------------------
Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.                                   
''')

iMinutos = int(input("Quantidade de Minutos Consumida: "))

iCalculo = ((iMinutos - 100) * 2) + 50.00

if iMinutos < 100:
    print("\nQuantidade dentro do plano - Consumo:",iMinutos,"Minutos - Valor de: R$50,00\n")

elif iMinutos > 100:
    print("\nQuantidade fora do plano - Consumo:",iMinutos,"Minutos - Valor de: R$",format(iCalculo,'.2f'),"\n")