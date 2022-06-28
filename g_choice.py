from dijkstra_algorithm import dijkstraSSSP
from huffman_coding import huffmanCoding
from job_sequencing_problem import jobSequencing
from knapsack_problem import knapsackProblemEscolha
from optimal_merge_pattern import optimaMergePatern
from kruskals_algorithms import kruskalC
from prims__algorithms import primC
from simple import simpleChoice


def greedChoice(opc):
    match opc:
        case 0:
            return print("Saindo.....\n")
        case 1:
            return simpleChoice()
        case 2:
            return knapsackProblemEscolha()
        case 3:
            return jobSequencing()
        case 4:
            return optimaMergePatern()
        case 5:
            return huffmanCoding()
        case 6:
            return kruskalC()
        case 7:
            return primC()
        case 8:
            return dijkstraSSSP()
        case default:
            return print("Entrada inválida")
