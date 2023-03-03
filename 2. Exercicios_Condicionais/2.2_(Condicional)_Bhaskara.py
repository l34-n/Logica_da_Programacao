print('''
-------------------------------------------------------------------------------------------------
                ██████╗ ██╗  ██╗ █████╗ ███████╗██╗  ██╗ █████╗ ██████╗  █████╗ 
                ██╔══██╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗
                ██████╔╝███████║███████║███████╗█████╔╝ ███████║██████╔╝███████║
                ██╔══██╗██╔══██║██╔══██║╚════██║██╔═██╗ ██╔══██║██╔══██╗██╔══██║
                ██████╔╝██║  ██║██║  ██║███████║██║  ██╗██║  ██║██║  ██║██║  ██║
                ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                                                                                                                                                
-------------------------------------------------------------------------------------------------
Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais,
conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem.                                 
''')

iCoeficiente_a =float(input("Coeficiente 'a': "))
iCoeficiente_b =float(input("Coeficiente 'b': "))
iCoeficiente_c =float(input("Coeficiente 'c': "))

iDelta = (((iCoeficiente_b) * iCoeficiente_b) - 4 * iCoeficiente_a * iCoeficiente_c)

iX1 = ((-(iCoeficiente_b)) + (iDelta**0.5)) / (2 * iCoeficiente_a)
iX2 = ((-(iCoeficiente_b)) - (iDelta**0.5)) / (2 * iCoeficiente_a)

if iDelta > 0:
 print("\nO Valor de Delta é de: ",iDelta)
 print("O Valor da Primeira Raiz é: ",format(iX1,'.4f'))
 print("O Valor da Segunda Raiz é: ",format(iX2,'.4f'),"\n")

else:
  print("\nNão há Raízes Reais.\n")

