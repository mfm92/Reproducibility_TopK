In diesem Repository liegt der Code um die Ergebnisse aus folgendem Paper zu reproduzieren:

Yu Zhang and Yan Zhang. 2017. Top-K Influential Nodes in Social Networks: A Game Perspective. In Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '17). Association for Computing Machinery, New York, NY, USA, 1029–1032. DOI: https://doi.org/10.1145/3077136.3080709

Link zum Git-Repo der Autoren: https://github.com/yuzhimanhua/Influence-Maximization


Mit diesem Skript werden die Knoten bestimmt die sich als beste Influencer eignen:

`./find_nodesets.sh #1 #2 #3 #4`

Bedeutung der Argumente: #1 = Inputgraph (liegen alle im Ordner `Data`), #2 = Anzahl der n besten Influencer, die berechnet werden sollen, #3 = `D` (für gerichteter Graph) oder `X` für ungerichteter Graph, #4 = Threshold (_linear/concave/convex/majority_)

Im Paper ist eine Dokumentation was die Thresholds genau bedeuten (Sektion 4). Ebenso steht drinnen welche Graphen gerichtet sind und welche nicht (Sektion 4).

Mit folgendem Skript wird dann der konkrete Influence berechnet (Bedeutung der Argumente bleibt die selbe)

`./infl_all_settings.sh #1 #2 #3 #4`

Eventuell muss man vorher `chmod +x <fileName>.sh` laufen lassen, damit das Shell Skript als ausführbar registriert wird.

Slides: https://de.overleaf.com/3845151781fmpmzjnmdhkg
