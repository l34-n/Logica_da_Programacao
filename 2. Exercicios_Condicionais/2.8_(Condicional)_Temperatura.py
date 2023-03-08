print('''
--------------------------------------------------------------------------------------------------------

      ████████╗███████╗███╗   ███╗██████╗ ███████╗██████╗  █████╗ ████████╗██╗   ██╗██████╗  █████╗ 
      ╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██╔══██╗
         ██║   █████╗  ██╔████╔██║██████╔╝█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝███████║
         ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗██╔══██║
         ██║   ███████╗██║ ╚═╝ ██║██║     ███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║██║  ██║
         ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═                                                                         
--------------------------------------------------------------------------------------------------------
Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para
isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser
informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com
duas casas decimais.                     
''')

iTemperatura = input("Qual a Escala da Temperatura (C ou F): ")

if iTemperatura == "C":
    iCelsius = float(input("\nDigite a Temperatura em Celsius: "))

    iCalculo_Celsius = (((iCelsius * 9) / 5) + 32)

    print("Temperatura Equivalente em Celsius: ",format(iCalculo_Celsius,'.2f'),"\n")

else:
    iFahrenheit = float(input("\nDigite a Temperatura em Fahrenheit: "))

    iCalculo_Fahrenheit = (((iFahrenheit - 32) * 5) / 9)

    print("Temperatura Equivalente em Celsius: ",format(iCalculo_Fahrenheit,'.2f'),"\n")
