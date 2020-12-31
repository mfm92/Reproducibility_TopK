echo "Recompile Greedy..."

rm Greedy++
g++ -o Greedy++ Greedy++.cpp

echo "Run simulation..."
./Greedy++ $1 out_sim.txt $2 $3 Simulate $4

echo "Run degree..."
./Greedy++ $1 out_degree.txt $2 $3 Degree $4

echo "Run Random..."
./Greedy++ $1 out_random.txt $2 $3 Random $4

echo "Run PageRank.."
readonly RANDOM_JUMP_PARAM=0.9
python pagerank.py $1 $2 ${RANDOM_JUMP_PARAM} $4 > out_pr.txt
