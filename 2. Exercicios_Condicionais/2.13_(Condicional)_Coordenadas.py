print('''
--------------------------------------------------------------------------------------------------------

       ██████╗ ██████╗  ██████╗ ██████╗ ██████╗ ███████╗███╗   ██╗ █████╗ ██████╗  █████╗ ███████╗
       ██╔════╝██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝
       ██║     ██║   ██║██║   ██║██████╔╝██║  ██║█████╗  ██╔██╗ ██║███████║██║  ██║███████║███████╗
       ██║     ██║   ██║██║   ██║██╔══██╗██║  ██║██╔══╝  ██║╚██╗██║██╔══██║██║  ██║██╔══██║╚════██║
       ╚██████╗╚██████╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║ ╚████║██║  ██║██████╔╝██║  ██║███████

--------------------------------------------------------------------------------------------------------
Leia os valores das coordenadas X e Y de um ponto no plano cartesiano. A seguir, determine qual o quadrante 
ao qual pertence o ponto (Q1, Q2, Q3 ou Q4). Se o ponto estiver na origem, escreva a mensagem “Origem”. 
Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

            |y
   Q2       |     Q1
            |
------------------------- X
            |
   Q3       |     Q4
            |
''')

i_X = float(input("Insira o Valor de X: "))
i_Y = float(input("Insira o Valor de Y: "))

if i_X > 0 and i_Y > 0:
    print("\nQuadrante 1\n")

elif i_X < 0 and i_Y > 0:
    print("\nQuadrante 2\n")

elif i_X > 0 and i_Y < 0:
    print("\nQuadrante 4\n")

elif i_X < 0 and i_Y < 0:
    print("\nQuadrante 3\n")    

elif i_X == 0 and i_Y == 0:
    print("\nOrigem\n")  

elif i_X != 0 and i_Y == 0:
    print("\nEixo X\n")  

elif i_X == 0 and i_Y != 0:
    print("\nEixo Y\n")  