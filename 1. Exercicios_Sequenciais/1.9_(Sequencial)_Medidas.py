print('''
-------------------------------------------------------------------------------------------------
                     ███╗   ███╗███████╗██████╗ ██╗██████╗  █████╗ ███████╗
                     ████╗ ████║██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██╔════╝
                     ██╔████╔██║█████╗  ██║  ██║██║██║  ██║███████║███████╗
                     ██║╚██╔╝██║██╔══╝  ██║  ██║██║██║  ██║██╔══██║╚════██║
                     ██║ ╚═╝ ██║███████╗██████╔╝██║██████╔╝██║  ██║███████║
                     ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝                                                                                                                                 
-------------------------------------------------------------------------------------------------
Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
com quatro casas decimais):
a) a área do quadrado que tem lado A
b) a área do triângulo retângulo que base A e altura B
c) a área do trapézio que tem bases A e B, e altura C                                                 
''')

iMedidaA = float(input("Medida A: "))
iMedidaB = float(input("Medida B: "))
iMedidaC = float(input("Medida C: "))

iResolucao_A = iMedidaA * iMedidaA
iResolucao_B = (iMedidaA * iMedidaB) / 2
iResolucao_C = ((iMedidaA + iMedidaB) * iMedidaC) / 2

print('\nÁrea do Quadrado: ',format(iResolucao_A,'.4f'))
print('Área do Triângulo: ',format(iResolucao_B,'.4f'))
print('Área do Trapézio: ',format(iResolucao_C,'.4f'),'\n')
