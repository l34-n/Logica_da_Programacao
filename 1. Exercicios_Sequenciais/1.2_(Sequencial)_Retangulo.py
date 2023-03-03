import math

print('''
-------------------------------------------------------------------------------------------------
             ██████╗ ███████╗████████╗ █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗██╗      ██████╗ 
             ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗████╗  ██║██╔════╝ ██║   ██║██║     ██╔═══██╗
             ██████╔╝█████╗     ██║   ███████║██╔██╗ ██║██║  ███╗██║   ██║██║     ██║   ██║
             ██╔══██╗██╔══╝     ██║   ██╔══██║██║╚██╗██║██║   ██║██║   ██║██║     ██║   ██║
             ██║  ██║███████╗   ██║   ██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝███████╗╚██████╔╝
             ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ 
-------------------------------------------------------------------------------------------------
Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
da área, perímetro e diagonal deste retângulo, com quatro casas decimais.                                                             
''')

iBase = float(input("Base do Retângulo: "))
iAltura = float(input("Altura do Retângulo: "))

iArea = iBase * iAltura
iPerimetro = (iBase * 2) + (iAltura * 2)
iDiagonal = math.sqrt(iBase ** 2 + iAltura ** 2)

print("\nA Área do Retângulo é de: ",format(iArea,'.4f'))
print("O Valor do Terreno é de: ",format(iPerimetro,'.4f'))
print("A Medida da Diagonal é de: ",format(iDiagonal,'.4f'),'\n')