print('''
-------------------------------------------------------------------------------------------------
                 ██████╗ ██╗   ██╗██████╗  █████╗  ██████╗ █████╗  ██████╗ 
                 ██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔═══██╗
                 ██║  ██║██║   ██║██████╔╝███████║██║     ███████║██║   ██║
                 ██║  ██║██║   ██║██╔══██╗██╔══██║██║     ██╔══██║██║   ██║
                 ██████╔╝╚██████╔╝██║  ██║██║  ██║╚██████╗██║  ██║╚██████╔╝
                 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝                                                                                                                               
-------------------------------------------------------------------------------------------------
Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
formato horas:minutos:segundos.                                           
''')

iSegundos = int(input("Insira a Quantidade de Segundos: "))

def convert(iSegundos):
    minuto, segundo = divmod(iSegundos, 60)
    horas, minuto = divmod(minuto, 60)
    return '%d:%02d:%02d' % (horas, minuto, segundo)

print("'\nHoras - Minutos - Segundos")
print(convert(iSegundos),'\n')