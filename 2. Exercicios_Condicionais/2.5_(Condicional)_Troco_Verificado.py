print('''
--------------------------------------------------------------------------------------------------------

                          ████████╗██████╗  ██████╗  ██████╗ ██████╗                  
                          ╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝██╔═══██╗                 
                             ██║   ██████╔╝██║   ██║██║     ██║   ██║                 
                             ██║   ██╔══██╗██║   ██║██║     ██║   ██║                 
                             ██║   ██║  ██║╚██████╔╝╚██████╗╚██████╔╝                 
                             ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝                  
                                                                        
               ██╗   ██╗███████╗██████╗ ██╗███████╗██╗ ██████╗ █████╗ ██████╗  ██████╗ 
               ██║   ██║██╔════╝██╔══██╗██║██╔════╝██║██╔════╝██╔══██╗██╔══██╗██╔═══██╗
               ██║   ██║█████╗  ██████╔╝██║█████╗  ██║██║     ███████║██║  ██║██║   ██║
               ╚██╗ ██╔╝██╔══╝  ██╔══██╗██║██╔══╝  ██║██║     ██╔══██║██║  ██║██║   ██║
                ╚████╔╝ ███████╗██║  ██║██║██║     ██║╚██████╗██║  ██║██████╔╝╚██████╔╝
                 ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝                                                                                                                          
--------------------------------------------------------------------------------------------------------
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
valor restante.                              
''')

iPreco_Produto = float(input("Valor do Produto: "))
iQuantidade = int(input("Quantidade Comprada: "))
iPagamento = float(input("Valor Pago: "))

iCompra = iPreco_Produto * iQuantidade
iTroco = iPagamento - iCompra

if iPagamento >= iCompra:
    print("\nTroco: ",iTroco,"\n")

else:
    print("\nPagamento Insuficiente - Faltam:",-(iTroco),"\n")