from g_choice import greedChoice


print("###### PROGRAMA INICIADO ######")

sair = 1
while sair !=0:
    op = input("\nDigite a opcao desejada:\n1-Exemplo simples\n2-Knapsack Problem\n3-Deadline "
               "Job Problem\n4-Optimal Merge Patern\n5-Huffman\n6-Kruskal\n7-Prim\n8-Dijkstra\n0-Sair\nEscolha:")
    op = int(op)
    sair = op
    print('\n')
    greedChoice(op)
    print('\n')

print("###### PROGRAMA FINALIZADO ######")