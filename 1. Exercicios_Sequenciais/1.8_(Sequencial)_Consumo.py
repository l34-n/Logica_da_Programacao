print('''
-------------------------------------------------------------------------------------------------
                 ██████╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗███╗   ███╗ ██████╗ 
                ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║   ██║████╗ ████║██╔═══██╗
                ██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██╔████╔██║██║   ██║
                ██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║╚██╔╝██║██║   ██║
                ╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝
                 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝                                                                                                                                    
-------------------------------------------------------------------------------------------------
Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
médio do carro, com três casas decimais.                                                     
''')

iDistancia_Total = float(input("Distância Total percorrida: "))
iCombustivel = float(input("Combustivel gasto: "))

iConsumo = iDistancia_Total / iCombustivel 

print("\nO Consumo Médio do Carro é de: ",format(iConsumo,'.3f'),'\n')