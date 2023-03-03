print('''
--------------------------------------------------------------------------------------------------------

███╗   ███╗███████╗███╗   ██╗ ██████╗ ██████╗     ██████╗ ███████╗    ████████╗██████╗ ███████╗███████╗
████╗ ████║██╔════╝████╗  ██║██╔═══██╗██╔══██╗    ██╔══██╗██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝██╔════╝
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║██████╔╝    ██║  ██║█████╗         ██║   ██████╔╝█████╗  ███████╗
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║██╔══██╗    ██║  ██║██╔══╝         ██║   ██╔══██╗██╔══╝  ╚════██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝██║  ██║    ██████╔╝███████╗       ██║   ██║  ██║███████╗███████║                                                                                                                                 
--------------------------------------------------------------------------------------------------------
Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
números lidos. Em caso de empate, mostrar apenas uma vez.                                     
''')

iNumero_1 = int(input("Primeiro Número: "))
iNumero_2 = int(input("Segundo Número: "))
iNumero_3 = int(input("Terceiro Número: "))

if iNumero_1 < iNumero_2 and iNumero_1 < iNumero_3:
   print("\nMenor Número:",iNumero_1,"\n")

elif iNumero_2 < iNumero_3:
   print("\nMenor Número:",iNumero_2,"\n")    

else:
   print("\nMenor Número:",iNumero_3,"\n")