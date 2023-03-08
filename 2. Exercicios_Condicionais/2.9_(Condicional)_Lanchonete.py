print('''
--------------------------------------------------------------------------------------------------------

        ██╗      █████╗ ███╗   ██╗ ██████╗██╗  ██╗ ██████╗ ███╗   ██╗███████╗████████╗███████╗
        ██║     ██╔══██╗████╗  ██║██╔════╝██║  ██║██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██╔════╝
        ██║     ███████║██╔██╗ ██║██║     ███████║██║   ██║██╔██╗ ██║█████╗     ██║   █████╗  
        ██║     ██╔══██║██║╚██╗██║██║     ██╔══██║██║   ██║██║╚██╗██║██╔══╝     ██║   ██╔══╝  
        ███████╗██║  ██║██║ ╚████║╚██████╗██║  ██║╚██████╔╝██║ ╚████║███████╗   ██║   ███████╗
        ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝  
                                                                     
--------------------------------------------------------------------------------------------------------
Uma lanchonete possui vários produtos. Cada produto possui um código e um preço. 
Você deve fazer um programa para ler o código e a quantidade comprada de um produto 
(suponha um código válido), e daí informar qual o valor a ser pago, com duas casas decimais, conforme
tabela:

Código do Produto  |  Preço do Produto
       1                 R$5.00
       2                 R$3.50
       3                 R$4.80
       4                 R$8.90
       5                 R$7.32
''')

iCodigo = int(input("Código do Produto Comprado: "))
iQuantidade = int(input("Quantidade Comprada: "))

if iCodigo == 1:
    print("\nValor a Pagar: ",format(5 * iQuantidade,'.2f'),"\n")

elif iCodigo == 2:
    print("\nValor a Pagar: ",format(3.50 * iQuantidade,'.2f'),"\n")    

elif iCodigo == 3:
    print("\nValor a Pagar: ",format(4.80 * iQuantidade,'.2f'),"\n")    

elif iCodigo == 4:
    print("\nValor a Pagar: ",format(8.90 * iQuantidade,'.2f'),"\n")    

elif iCodigo == 5:
    print("\nValor a Pagar: ",format(7.32 * iQuantidade,'.2f'),"\n")    