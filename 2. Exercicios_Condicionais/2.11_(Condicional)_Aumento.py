print('''
--------------------------------------------------------------------------------------------------------

                    █████╗ ██╗   ██╗███╗   ███╗███████╗███╗   ██╗████████╗ ██████╗ 
                   ██╔══██╗██║   ██║████╗ ████║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗
                   ███████║██║   ██║██╔████╔██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║
                   ██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   ██║   ██║
                   ██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   ╚██████╔╝
                   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ 

--------------------------------------------------------------------------------------------------------
Uma empresa vai conceder um aumento percentual de salário aos seus funcionários dependendo de quanto
cada pessoa ganha, conforme tabela abaixo. Fazer um programa para ler o salário de uma pessoa, daí mostrar
qual o novo salário desta pessoa depois do aumento, quanto foi o aumento e qual foi a porcentagem de aumento.

     Salário Atual     |     Aumento
      Até R$1000,00          20%
 
      Acima de R$1000        15%
        até R$3000        

      Acima de R$3000        10%
         até 8000

      Acima de R$8000         5%   

''')

iSalario = float(input("Insira o Salário: "))



if iSalario < 1000:

    iCalculo = (iSalario * 20) / 100
    iTotal = iCalculo + iSalario

    print("\nO valor do novo salário é de: ",iTotal)
    print("O valor do aumento foi de: ",iCalculo)
    print("A porcentagem foi de: 20%")

elif iSalario >= 1000 and iSalario < 3000:

    iCalculo = (iSalario * 15) / 100
    iTotal = iCalculo + iSalario

    print("\nO valor do novo salário é de: ",iTotal)
    print("O valor do aumento foi de: ",iCalculo)
    print("A porcentagem foi de: 15%")

    print()

elif iSalario >= 3000 and iSalario < 8000:

    iCalculo = (iSalario * 10) / 100
    iTotal = iCalculo + iSalario

    print("\nO valor do novo salário é de: ",iTotal)
    print("O valor do aumento foi de: ",iCalculo)
    print("A porcentagem foi de: 10%")

elif iSalario > 8000:

    print("\nO valor do novo salário é de: ",iTotal)
    print("O valor do aumento foi de: ",iCalculo)
    print("A porcentagem foi de: 5%")
