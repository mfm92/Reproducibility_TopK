import networkx as nx
import sys

from random import sample

def page_rank(G):
    page_rank = nx.pagerank(G, alpha=float(sys.argv[3]))
    page_rank_sorted = sorted(page_rank.items(),
                              key=lambda t: t[1],
                              reverse=True)

    for key, value in page_rank_sorted[:(int(sys.argv[2]))]:
        print(key, value)


def random(G):
    for node in sample(list(G.nodes()), (int)(sys.argv[2])):
        print(node, 1) # doesn't matter


def degree(G):
    if sys.argv[4] == 'D':
        degree_sort = sorted(G.out_degree, key=lambda x: x[1], reverse=True)
    else:
        degree_sort = sorted(G.degree, key=lambda x: x[1], reverse=True)
    for key, value in degree_sort[:(int(sys.argv[2]))]:
         print(key, value)


def main(argv):
    f = open(sys.argv[1], 'r').readlines()[1:]

    if sys.argv[4] == 'D':
        G = nx.read_edgelist(f, nodetype=int, create_using=nx.DiGraph())

        if sys.argv[1] == 'Data/Epinions.txt' and sys.argv[5] == "PageRank":
            G = G.reverse()
    else:
        G = nx.read_edgelist(f, nodetype=int)

    if sys.argv[5] == "PageRank":
        page_rank(G)
    elif sys.argv[5] == "Random":
        random(G)
    elif sys.argv[5] == "Degree":
        degree(G)

if __name__ == "__main__":
    main(sys.argv)
