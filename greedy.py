import networkx as nx
import sys
from math import sqrt
from random import sample, uniform
import typing


def generate_thresholds(n: int, threshold: str):
    if threshold == "linear":
        thrs = [uniform(0, 1) for _ in range(n)]
    elif threshold == "concave":
        thrs = [uniform(0, 1)**2 for _ in range(n)]
    elif threshold == "convex":
        thrs = [sqrt(uniform(0, 1)) for _ in range(n)]
    else:
        thrs = [0.5 for _ in range(n)]
    return thrs


def simulate_time_step(S_t: set, G: typing.Union[nx.Graph, nx.DiGraph], deg):
    S_next = S_t | {v for v in set(G.nodes()) - S_t
                    if len(set(G.neighbors(v)) & S_t)/deg[v] >= G.nodes[v]["threshold"]}
    return S_next


def simulate_diffusion(S_0: set, G: typing.Union[nx.Graph, nx.DiGraph], graph_type: str):
    if graph_type == "D":
        deg = G.in_degree
    else:
        deg = G.degree

    S_n = S_0.copy()
    for _ in range(G.number_of_nodes()):
        S_new = simulate_time_step(S_n, G, deg)
        if len(S_new) == len(S_n):
            break
        S_n = S_new

    return S_n


def find_k_best(k: int, G: typing.Union[nx.Graph, nx.DiGraph], graph_type: str):
    S = set()
    nodes = []
    sigma_prev = 0  # for empty start set we will always get 0
    for i in range(k):
        sigmas = [(v, len(simulate_diffusion((S | {v}), G, graph_type))) for v in set(G.nodes())-S]
        top_node = sorted(sigmas, key=lambda x: x[1] - sigma_prev, reverse=True)[0]
        S |= {top_node[0]}
        sigma_prev = top_node[1] - sigma_prev
        nodes.append(top_node)

    return nodes

def main(argv):
    f = open(sys.argv[1], 'r').readlines()[1:]

    if sys.argv[3] == 'D':
        G = nx.read_edgelist(f, nodetype=int, create_using=nx.DiGraph())

        if sys.argv[1] == 'Data/Epinions.txt':
            G = G.reverse()
    else:
        G = nx.read_edgelist(f, nodetype=int)

    k = int(sys.argv[2])

    thresholds = {v: {"threshold": threshold} for (v, threshold) in zip(G.nodes(), generate_thresholds(G.number_of_nodes(), "linear"))}
    nx.set_node_attributes(G, thresholds)

    S = {1, 2, 3, 4, 5}
    nodes = find_k_best(k, G, sys.argv[3])
    nodes_sorted = sorted(nodes, key=lambda x: x[1], reverse=True)
    for key, value in nodes_sorted:
        print(key, value)

if __name__ == "__main__":
    main(sys.argv)
