
In this repository you can find the code to reproduce the results from the following paper:

Yu Zhang and Yan Zhang. 2017. Top-K Influential Nodes in Social Networks: A Game Perspective. In Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '17). Association for Computing Machinery, New York, NY, USA, 1029–1032. DOI: https://doi.org/10.1145/3077136.3080709

Git-repo of the authors: https://github.com/yuzhimanhua/Influence-Maximization

The script to produce the nodes, which are the best as influencer:
`python experiment.py #1 #2 -t #3 #4 -fs #5 -it #6`

<ins>Meaning of the arguments</ins>:<br>
#1 algorithm to calculate the most influential nodes (`Random/Greedy++/Degree/PageRank`), <br>
#2 input graph (find all in folder Data), <br>
#3 threshold (`linear/concave/convex/majority`), <br>
#4 = `D` for directed graph or `U` for undirected graph, <br>
#5 = number of the most influential nodes (seed set size),<br>
#6 = number of interations

A documentation of the meaning of the thresholds is to be found in the paper (section 4). There you can also find which graphes are directed or undirected. 

The parameters #5 and #6 (incl. `fs` and `it` flags) are optimal. If not set, the chosen setting runs for every seed set size between 1 and 20. If the parameters are defined, the chosen setting runs only for the defined seed set size (`fs` flag), but more times (number of iterations = `it` flag)

_Examples_:<br>
`python experiment.py Degree Data/Epinions.txt -t linear D`<br>
`python experiment.py Random Data/NetHept.txt -t linear U -fs 5 -it 50`

Use `python experiment.py -h` to retrieve a description of the parameters in the command line.

The results are then written to folder `Results`. In each subfolder labelled `<algorithm>_output_<dataset>_<threshold>` under `Results` there is a file named `Influence.csv` which documents the influence score and runtimes (for finding the most promising node set and for calculating the influence) for each given size of seed set. The files `out<n>.txt` document the IDs of the `n` nodes computed to be the most influential under the given setting.

Slides: https://de.overleaf.com/3845151781fmpmzjnmdhkg
