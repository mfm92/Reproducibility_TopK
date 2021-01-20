In this repository you can find the code to reproduce the results from the following paper:

Yu Zhang and Yan Zhang. 2017. Top-K Influential Nodes in Social Networks: A Game Perspective. In Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '17). Association for Computing Machinery, New York, NY, USA, 1029–1032. DOI: https://doi.org/10.1145/3077136.3080709

Git-repo of the authors: https://github.com/yuzhimanhua/Influence-Maximization

The script to produce the nodes, which are the best as influencer:
python experiment.py #1 #2 -t #3 #4 -fs #5 -it #6

Meaning of the arguments:
#1 = algorithm to calculate the most influential nodes (Random/Greedy++/Degree/PageRank), 
#2 = input graph (find all in folder Data), 
#3 = threshold (linear/concave/convex/majority), 
#4 = D for directed graph or X for undirected graph, 
#5 = number of the most influential nodes (seed set size),
#6 = number of interations

A documentation of the meaning of the thresholds is to be found in the paper (section 4). There you can also find which graphes are directed or undirected. 

The parameters #5 and #6 (incl. fs and it flags) are optimal. If not set, the chosen setting runs for every seed set size between 1 and 20. If the parameters are defined, the chosen setting runs only for the defined seed set size (fs flag), but more times (number of iterations = it flag)

Examples:
python experiment.py Degree Data/Epinions.txt -t linear D 
python experiment.py Random Data/NetHept.txt -t linear U -fs 5 -it 50

Slides: https://de.overleaf.com/3845151781fmpmzjnmdhkg
