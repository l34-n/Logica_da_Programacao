print('''
-------------------------------------------------------------------------------------------------
                     ██████╗██╗██████╗  ██████╗██╗   ██╗██╗      ██████╗ 
                    ██╔════╝██║██╔══██╗██╔════╝██║   ██║██║     ██╔═══██╗
                    ██║     ██║██████╔╝██║     ██║   ██║██║     ██║   ██║
                    ██║     ██║██╔══██╗██║     ██║   ██║██║     ██║   ██║
                    ╚██████╗██║██║  ██║╚██████╗╚██████╔╝███████╗╚██████╔╝
                     ╚═════╝╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ 
-------------------------------------------------------------------------------------------------
Fazer um programa para ler o valor "r" do raio de um círculo, e depois mostrar o valor da área do
círculo com três casas decimais. 𝜋 = 3.14159                                                           
''')

iRaio = float(input("\nValor do Raio do Círculo: "))

iArea = 3.14 * (iRaio * iRaio)

print("\nA Área é de:",format(iArea,".3f"),'\n')
