import networkx as nx
import sys

def main(argv):
    f = open(sys.argv[1], 'r').readlines()[1:]

    if sys.argv[4] == 'D':
        G = nx.read_edgelist(f, nodetype=int, create_using=nx.DiGraph())

        if sys.argv[1] == 'Data/Epinions.txt':
            G = G.reverse()
    else:
        G = nx.read_edgelist(f, nodetype=int)

    page_rank = nx.pagerank(G, alpha=float(sys.argv[3]))
    page_rank_sorted = sorted(page_rank.items(),
                              key=lambda t: t[1],
                              reverse=True)

    for key, value in page_rank_sorted[:(int(sys.argv[2]))]:
        print(key, value)

if __name__ == "__main__":
    main(sys.argv)
