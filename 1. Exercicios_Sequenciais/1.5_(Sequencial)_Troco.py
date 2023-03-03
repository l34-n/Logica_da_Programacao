print('''
-------------------------------------------------------------------------------------------------
                           ████████╗██████╗  ██████╗  ██████╗ ██████╗ 
                           ╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝██╔═══██╗
                              ██║   ██████╔╝██║   ██║██║     ██║   ██║
                              ██║   ██╔══██╗██║   ██║██║     ██║   ██║
                              ██║   ██║  ██║╚██████╔╝╚██████╗╚██████╔╝
                              ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝            
-------------------------------------------------------------------------------------------------
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia. 
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto, 
e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve 
mostrar o valor do troco a ser devolvido ao cliente.                                                             
''')

iPreco = float(input("Preço Unitário do Produto: "))
iQuantidade = int(input("Quantidades Compradas: "))
iValor_Recebido = float(input("Valor Recebido pelo Cliente: "))

iTroco = iValor_Recebido - (iPreco * iQuantidade) 

print("O Troco é de:",format(iTroco,".2f"),"\n")