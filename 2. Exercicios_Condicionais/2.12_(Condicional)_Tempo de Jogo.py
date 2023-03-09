print('''
--------------------------------------------------------------------------------------------------------

████████╗███████╗███╗   ███╗██████╗  ██████╗     ██████╗ ███████╗         ██╗ ██████╗  ██████╗  ██████╗ 
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔═══██╗    ██╔══██╗██╔════╝         ██║██╔═══██╗██╔════╝ ██╔═══██╗
   ██║   █████╗  ██╔████╔██║██████╔╝██║   ██║    ██║  ██║█████╗           ██║██║   ██║██║  ███╗██║   ██║
   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║   ██║    ██║  ██║██╔══╝      ██   ██║██║   ██║██║   ██║██║   ██║
   ██║   ███████╗██║ ╚═╝ ██║██║     ╚██████╔╝    ██████╔╝███████╗    ╚█████╔╝╚██████╔╝╚██████╔╝╚██████╔╝
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝      ╚═════╝     ╚═════╝ ╚══════╝     ╚════╝  ╚═════╝  ╚═════╝  ╚═════╝ 

--------------------------------------------------------------------------------------------------------
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo
pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24
horas.
''')

iInicial = int(input("Insira a Hora Inicial: "))
iTermino = int(input("Insira a Hora Final: "))

if iInicial < iTermino:

   iCalculo = iTermino - iInicial 

   print("\nO jogo durou:",iCalculo,"horas\n")

else:

   iCalculo = (24 - iInicial) + iTermino

   print("\nO jogo durou:",iCalculo,"horas \n")