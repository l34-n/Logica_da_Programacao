print('''
--------------------------------------------------------------------------------------------------------

                             ██████╗  █████╗ ██████╗ ██████╗  ██████╗ 
                             ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗
                             ██║  ██║███████║██████╔╝██║  ██║██║   ██║
                             ██║  ██║██╔══██║██╔══██╗██║  ██║██║   ██║
                             ██████╔╝██║  ██║██║  ██║██████╔╝╚██████╔╝
                             ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝                                                                                                      
--------------------------------------------------------------------------------------------------------
No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual
foi a maior.                       
''')

iDistancia_1 = float(input("Primeira Distância: "))
iDistancia_2 = float(input("Segunda Distância: "))
iDistancia_3 = float(input("Terceira Distância: "))

if iDistancia_1 > iDistancia_2 and iDistancia_1 > iDistancia_3:
   print("\nMaior Distância:",iDistancia_1,"\n")

elif iDistancia_2 > iDistancia_3:
   print("\nMaior Distância:",iDistancia_2,"\n")    

else:
   print("\nMaior Distância:",iDistancia_3,"\n")