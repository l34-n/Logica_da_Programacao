print('''
-------------------------------------------------------------------------------------------------
                           ███╗   ██╗ ██████╗ ████████╗ █████╗ ███████╗
                           ████╗  ██║██╔═══██╗╚══██╔══╝██╔══██╗██╔════╝
                           ██╔██╗ ██║██║   ██║   ██║   ███████║███████╗
                           ██║╚██╗██║██║   ██║   ██║   ██╔══██║╚════██║
                           ██║ ╚████║╚██████╔╝   ██║   ██║  ██║███████║
                           ╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝                                                                                                                                                           
-------------------------------------------------------------------------------------------------
Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no
ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a
mensagem "REPROVADO",                                       
''')

iNota1 = float(input("Primeira Nota: "))
iNota2 = float(input("Segunda Nota: "))

iNota_final = iNota1 + iNota2

if iNota_final >= 60.00:
    print("\nAluno Aprovado - Nota Final: ",iNota_final,"\n")

else:
    print("\nAluno Reprovado - Nota Final: ",iNota_final,"\n")    