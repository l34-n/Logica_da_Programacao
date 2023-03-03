print('''
-------------------------------------------------------------------------------------------------
              ██████╗ ██████╗  ██████╗ ██████╗ ██╗     ███████╗███╗   ███╗ █████╗    
              ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║     ██╔════╝████╗ ████║██╔══██╗██╗
              ██████╔╝██████╔╝██║   ██║██████╔╝██║     █████╗  ██╔████╔██║███████║╚═╝
              ██╔═══╝ ██╔══██╗██║   ██║██╔══██╗██║     ██╔══╝  ██║╚██╔╝██║██╔══██║██╗
              ██║     ██║  ██║╚██████╔╝██████╔╝███████╗███████╗██║ ╚═╝ ██║██║  ██║╚═╝
              ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝   
                                                                       
                   ████████╗███████╗██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗        
                   ╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔═══██╗       
                      ██║   █████╗  ██████╔╝██████╔╝█████╗  ██╔██╗ ██║██║   ██║       
                      ██║   ██╔══╝  ██╔══██╗██╔══██╗██╔══╝  ██║╚██╗██║██║   ██║       
                      ██║   ███████╗██║  ██║██║  ██║███████╗██║ ╚████║╚██████╔╝       
                      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝        
-------------------------------------------------------------------------------------------------
Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular, 
bem como o valor do metro quadrado do terreno. Em seguida, o programa deve mostrar o 
valor da área do terreno, bem como o valor do preço do terreno, ambos com duas casas decimais.                                                                  
''')

iLargura = float(input("Largura do Terreno: "))
iComprimento = float(input("Comprimento do Terreno: "))
iMetroQuadrado = float(input("Metro Quadrado: "))

iArea = iLargura * iComprimento
iValor = iArea * iMetroQuadrado

print("\nA Área do Terreno é de: ",format(iArea,'.2f'))
print("O Valor do Terreno é de: ",format(iValor,'.2f'),'\n')

