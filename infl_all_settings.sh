# type this into terminal
# chmod +x infl_all_settings.sh (only once)
# ./infl_all_settings.sh <input graph> <top k> <directed/undirected> <threshold>

echo "Recompile calculation of influence"
rm Calc_Inf
g++ -o Calc_Inf Calc_Inf.cpp

echo "Influence: Simulation"
./Calc_Inf $1 out_sim.txt $2 $3 $4

echo "Influence: PageRank"
./Calc_Inf $1 out_pr.txt $2 $3 $4

echo "Influence: Degree"
./Calc_Inf $1 out_degree.txt $2 $3 $4

echo "Influence: Random"
./Calc_Inf $1 out_random.txt $2 $3 $4
