import argparse
import os
import stat
import subprocess
import pandas as pd
from time import perf_counter

ap = argparse.ArgumentParser()
ap.add_argument("algorithm", help="Type of algorithm to use", type=str, choices=["Greedy++", "PageRank", "Degree", "Random"])
ap.add_argument("data", help="path to data",  type=str)
ap.add_argument("--threshold", "-t", help="threshold type", type=str,
                choices=["linear", "concave", "convex", "majority"], required=False)
ap.add_argument("network", help="Directed or Undirected Graph", type=str, choices=["D", "U"], default="U")
args = ap.parse_args()
algorithm = args.algorithm
data_path = args.data
threshold_type = args.threshold
graph_type = args.network

base = os.path.basename(data_path)
output_path = f"./{algorithm}_output_{os.path.splitext(base)[0]}_{threshold_type}"
if not os.path.exists(output_path):
    os.mkdir(output_path)

if algorithm == "Greedy++":
    executable = f"./Greedy++_{threshold_type}"
    if not os.path.isfile(executable):
        command = f"g++ {executable}.cpp -o {executable}"
        os.system(command)
        st = os.stat(executable)
        os.chmod('{executable}', st.st_mode | stat.S_IEXEC)
else:
    executable = f"python3 ./pagerank.py {data_path} 20 0.9 {graph_type} {algorithm}"

total_start = perf_counter()
for size in range(21):
    start_time = perf_counter()
    if algorithm == "Greedy++":
        command = f"{executable} {data_path} {output_path}/out{size}.txt {size} {graph_type}"
    else:
        command = f"{executable} {data_path} {size} 0.9 {graph_type} > {output_path}/out{size}.txt"
    print(f"{size}/20 Executing {executable} for seed size: {size}")
    print(command)
    ret_code = os.system(command)
    if ret_code != 0:
        print("Error in command")
        break
    seconds = perf_counter() - start_time
    print(f"{size}/20 Done in {int(seconds // 60)} minutes {seconds % 60:.2f} seconds", end="\n\n")

print("\n\n" + "."*20)
seconds = perf_counter() - total_start
print("Experiment ran successfully!\nCalculating influence data from output")
print(f"Total time: {int(seconds // 60)} minutes {seconds % 60:.2f} seconds", end="\n\n")
executable = f"./Calc_Inf"
if not os.path.isfile(executable):
    command = f"g++ {executable}.cpp -o {executable}"
    os.system(command)
    st = os.stat(executable)
    os.chmod('{executable}', st.st_mode | stat.S_IEXEC)

influence_data = []
for size in range(21):
    start_time = perf_counter()
    print(f"{size}/20 Executing {executable} for seed size: {size}")
    res = subprocess.check_output([executable, data_path, f"{output_path}/out{size}.txt", str(size), graph_type])
    res_str = res.decode("utf-8").partition('\n')[0]

    influence = int(res_str[20:])
    influence_data.append((size, influence))

    end_time = perf_counter()
    seconds = end_time - start_time
    print(f"Done in {int(seconds // 60)} minutes {seconds % 60:.2f} seconds")

print("Creating DataFrame...", end="")
df = pd.DataFrame(influence_data, columns=["Size", "Influence"])
df.to_csv(output_path + "/Influence.csv", index=False)
print(" Done")
