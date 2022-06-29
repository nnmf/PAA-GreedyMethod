

##https://www.youtube.com/watch?v=ARvQcqJ_-NY
def simpleOne():
    print("Bicicleta: 300h\nCarro: 50h\nTrem-bala: 10h\nAvião: 5h\n")
    seq = [300, 150, 50, 5]
    x = 300
    for i in range(len(seq)):
        if x > seq[i]:
            x=seq[i]
    print("A locomoção mais rápida é: ", x, "horas")

    ##https://www.youtube.com/watch?v=ARvQcqJ_-NY




##https://www.youtube.com/watch?v=QvSIAB27Vdk&t=328s
##https://docs.google.com/presentation/d/1kO7-GTgkQpWBki6azzrQM-H-gKn_udfkn1xfNppZDV0/edit#slide=id.p
def simpleTwo():

    tasks = [6, 3, 2, 7, 5, 5]
    print(tasks)
    print("\n")
    workers = []
    tasks = sorted(tasks)

    if len(tasks) % 2 == 1:
        workers.append((tasks[-1],))
        tasks.pop()

    for i in range(len(tasks) // 2):
        workers.append((tasks[i], tasks[~i]))
        print(tasks[i], tasks[~i])


def simpleChoice():
    op = input("Digite a opcao desejada:\n1-Locomoção Mais Rápida\n2-Trabalho Rápido\nEscolha: ")
    op = int(op)
    if op == 1:
        simpleOne()
    elif op == 2:
        simpleTwo()
    else:
        print('opção inexistente!')