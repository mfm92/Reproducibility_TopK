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

# executable = f"./Calc_Inf_LT_{threshold_type}"
executable = "./Calc_Inf_IC"
if not os.path.isfile(executable):
    command = f"g++ {executable}.cpp -o {executable}"
    os.system(command)
    st = os.stat(executable)
    os.chmod(f'{executable}', st.st_mode | stat.S_IEXEC)

influence_data = []
for size in range(21):
    start_time = perf_counter()
    print(f"{size}/20 Executing {executable} for seed size: {size}")
    res = subprocess.check_output([executable, data_path, f"{output_path}/out{size}.txt", str(size), graph_type])
    res_str = res.decode("utf-8").partition('\n')[0]

    influence = int(res_str[20:])
    end_time = perf_counter()
    seconds = end_time - start_time
    influence_data.append(influence)
    print(f"Done in {int(seconds // 60)} minutes {seconds % 60:.2f} seconds")

df = pd.read_csv(f"{output_path}/Influence.csv")

print("Creating DataFrame...", end="")
df["Influence"] = influence_data
df.to_csv(output_path + "/Influence_IC.csv", index=False)
print(" Done")