print('''
--------------------------------------------------------------------------------------------------------

                           ██████╗ ██╗     ██╗ ██████╗ ██████╗ ███████╗███████╗
                          ██╔════╝ ██║     ██║██╔════╝██╔═══██╗██╔════╝██╔════╝
                          ██║  ███╗██║     ██║██║     ██║   ██║███████╗█████╗  
                          ██║   ██║██║     ██║██║     ██║   ██║╚════██║██╔══╝  
                          ╚██████╔╝███████╗██║╚██████╗╚██████╔╝███████║███████╗
                           ╚═════╝ ╚══════╝╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝                                                                                                       
--------------------------------------------------------------------------------------------------------
Fazer um programa para ler a quantidade de glicose no sangue de uma pessoa e depois mostrar na tela a
classificação desta glicose.                          
''')

iGlicose = float(input("Medida da Glicose: "))

if iGlicose <= 100:
    print("\nClassificação: Normal\n")

elif iGlicose > 100 and iGlicose <= 140:
    print("\nClassificação: Elevado\n")

else: 
    print("\nClassificação: Diabetes\n")