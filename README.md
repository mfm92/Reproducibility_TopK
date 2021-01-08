In diesem Repository liegt der Code um die Ergebnisse aus folgendem Paper zu reproduzieren:

Yu Zhang and Yan Zhang. 2017. Top-K Influential Nodes in Social Networks: A Game Perspective. In Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '17). Association for Computing Machinery, New York, NY, USA, 1029–1032. DOI: https://doi.org/10.1145/3077136.3080709

Link zum Git-Repo der Autoren: https://github.com/yuzhimanhua/Influence-Maximization


Mit diesem Skript werden die Knoten bestimmt die sich als beste Influencer eignen:

`python experiment.py #1 #2 -t #3 #4 -fs #5 -it #6`

Bedeutung der Argumente: #1 = Algorithmus zur Berechnung der einflussreichsten Knoten (_Random/Greedy++/Degree/PageRank_), #2 = Inputgraph (liegen alle im Ordner `Data`), #3 = Threshold (_linear/concave/convex/majority_), #4 = `D` (für gerichteter Graph) oder `X` für ungerichteter Graph, #5 = Größe der Menge der einflussreichsten Knoten (`seed set size`), #6 = Anzahl der Iterationen.

Im Paper ist eine Dokumentation was die Thresholds genau bedeuten (Sektion 4). Ebenso steht drinnen welche Graphen gerichtet sind und welche nicht (Sektion 4).

Die Parameter #5 und #6 (inklusive `fs` und `it` flags) sind optional. Wenn diese Parameter nicht gesetzt sind wird das gewählte Setting im CLI für alle Seed Set sizes zwischen 1 und 20 jeweils einmal ausgeführt. Wenn diese Parameter definiert sind wird das gewählte Setting nur für die benutzerdefinierte Seed Set Size (`fs` flag) durchgeführt, dafür aber mehrmals (Anzahl der Iterationen = `it` flag).

Beispielaufrufe:

`python experiment.py Degree Data/Epinions.txt -t linear D`
`python experiment.py Random Data/NetHept.txt -t linear U -fs 5 -it 50`

Slides: https://de.overleaf.com/3845151781fmpmzjnmdhkg
