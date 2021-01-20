#!/usr/bin/env python
# coding: utf-8

# In[16]:


from scipy import stats
# from statsmodels.stats.weightstats import ztest, ttest_ind

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# ## Importing experimental results
# 
# Reading the experimental results here, these depend on...
# * The algorithm used to predict most influential node set (Greedy++, Page Rank, Degree, Random)
# * The threshold used to determine when a node is turned active (linear, concave, convex, majority vote)
# * The data set
# 
# The CSV files contain info on...
# 
# * `Size`: Size of seed set
# * `Influence`: The predicted influence for a given setting, i.e. combination of values from the setting space defined above
# * `Node Runtime`: Time required to calculate prediction for most influential vertex set
# * `Inf Runtime`: Time required to calculate influence of given vertex set

# ### NetHEPT

# In[17]:


df_greedy_nethept_linear = pd.read_csv("Results/Greedy++_output_NetHept_linear/Influence.csv")
df_pagerank_nethept_linear = pd.read_csv("Results/PageRank_output_NetHept_linear/Influence.csv")
df_degree_nethept_linear = pd.read_csv("Results/Degree_output_NetHept_linear/Influence.csv")
df_random_nethept_linear = pd.read_csv("Results/Random_output_NetHept_linear/Influence.csv")


# In[18]:


df_greedy_nethept_convex = pd.read_csv("Results/Greedy++_output_NetHept_convex/Influence.csv")
df_pagerank_nethept_convex = pd.read_csv("Results/PageRank_output_NetHept_convex/Influence.csv")
df_degree_nethept_convex = pd.read_csv("Results/Degree_output_NetHept_convex/Influence.csv")
df_random_nethept_convex = pd.read_csv("Results/Random_output_NetHept_convex/Influence.csv")


# In[19]:


df_degree_nethept_concave = pd.read_csv("Results/Degree_output_NetHept_concave/Influence.csv")


# In[20]:


df_greedy_nethept_majority = pd.read_csv("Results/Greedy++_output_NetHept_majority/Influence.csv")
df_pagerank_nethept_majority = pd.read_csv("Results/PageRank_output_NetHept_majority/Influence.csv")
df_degree_nethept_majority = pd.read_csv("Results/Degree_output_NetHept_majority/Influence.csv")
df_random_nethept_majority = pd.read_csv("Results/Random_output_NetHept_majority/Influence.csv")


# ### NetPhy

# In[21]:


df_greedy_netphy = pd.read_csv("Results/Greedy++_output_NetPhy_linear/Influence.csv")
df_pagerank_netphy = pd.read_csv("Results/PageRank_output_NetPhy_linear/Influence.csv")
df_degree_netphy = pd.read_csv("Results/Degree_output_NetPhy_linear/Influence.csv")
df_random_netphy = pd.read_csv("Results/Random_output_NetPhy_linear/Influence.csv")


# ### Epinions

# In[22]:


df_greedy_epinions = pd.read_csv("Results/Greedy++_output_Epinions_linear/Influence.csv")
df_pagerank_epinions = pd.read_csv("Results/PageRank_output_Epinions_linear/Influence.csv")
df_degree_epinions = pd.read_csv("Results/Degree_output_Epinions_linear/Influence.csv")
df_random_epinions = pd.read_csv("Results/Random_output_Epinions_linear/Influence.csv")


# ### Epinions IC

# In[23]:


#df_greedy_epinions_IC = pd.read_csv("Results/Greedy++_output_Epinions_linear/Influence_IC.csv")
#df_pagerank_epinions_IC = pd.read_csv("Results/PageRank_output_Epinions_linear/Influence_IC.csv")
#df_degree_epinions_IC = pd.read_csv("Results/Degree_output_Epinions_linear/Influence_IC.csv")
#df_random_epinions_IC = pd.read_csv("Results/Random_output_Epinions_linear/Influence_IC.csv")


# ## Statistical tests
# 
# Attempting the following tests...
# 
# * **Mann Whitney U test**: To inspect effect of algorithm on influence, data obtained depend on seed set size and follow no normal distribution, therefore using a non-parametric test here. Furthermore, since each run of any given setting includes generation of random numbers we are using a non-paired test
# * **Unpaired t-test**: For a given seed set size inspect effect of algorithm on influence over multiple runs (here obtained values are reasoned to be independent and normally distributed around some mean)
# * **Comparison w/ original authors**: Probably also some test to compare our obtained values with those from the original authors...

# ### Comparing algorithms (various seed set sizes)

# In[24]:


stats.mannwhitneyu(df_greedy_nethept_linear[['Influence']], df_pagerank_nethept_linear[['Influence']])


# In[25]:


stats.mannwhitneyu(df_greedy_nethept_linear[['Influence']], df_degree_nethept_linear[['Influence']])


# In[26]:


stats.mannwhitneyu(df_greedy_nethept_linear[['Influence']], df_random_nethept_linear[['Influence']])


# ### Comparing algorithms (same seed set size, multiple runs)

# In[110]:


infl_random = pd.read_csv(f"Results/iterations/Random_output_NetHept_linear/Influence.csv")[['Influence']]
infl_greedy = pd.read_csv(f"Results/iterations/Greedy++_output_NetHept_linear/Influence.csv")[['Influence']]
infl_pr = pd.read_csv(f"Results/iterations/PageRank_output_NetHept_linear/Influence.csv")[['Influence']]
infl_degree = pd.read_csv(f"Results/iterations/Degree_output_NetHept_linear/Influence.csv")[['Influence']]


# In[111]:


infl_random.hist(bins=10, edgecolor='black')


# In[112]:


stat, p = stats.shapiro(infl_random)

if p > 0.05:
    print("Random influences: Normally distributed:", p)
else:
    print("Random influences: Not(!) normally distributed:", p)


# In[113]:


infl_greedy.hist(bins=7, edgecolor='black')


# In[114]:


stat, p = stats.shapiro(infl_greedy)

if p > 0.05:
    print("Greedy influences: Normally distributed:", p)
else:
    print("Greedy influences: Not(!) normally distributed:", p)


# In[115]:


infl_pr.hist(bins=7, edgecolor='black')

stat, p = stats.shapiro(infl_pr)

if p > 0.05:
    print("PageRank influences: Normally distributed:", p)
else:
    print("PageRank influences: Not(!) normally distributed:", p)


# In[116]:


infl_degree.hist(edgecolor='black')

stat, p = stats.shapiro(infl_degree)

if p > 0.05:
    print("Degree influences: Normally distributed:", p)
else:
    print("Degree influences: Not(!) normally distributed:", p)


# In[117]:


stats.ttest_ind(infl_greedy, infl_random)


# In[118]:


stats.ttest_ind(infl_greedy, infl_pr)


# In[119]:


stats.ttest_ind(infl_degree, infl_pr)


# ## Visualization
# 
# * Visualizing effect of algorithm on influence for given data sets
# * Visualizing run time of determining the prediction for most influencial node set for given data set, algorithm (threshold: linear)

# In[5]:


def plot_inf(data, df_greedy, df_pagerank, df_degree, df_random, threshold):
    plt.clf()
    plt.title(f"{threshold} threshold, data: {data}")
    plt.plot(df_greedy.Size, df_greedy.Influence, marker="o", color="red", )
    plt.plot(df_pagerank.Influence, marker="x", color="green")
    plt.plot(df_degree.Influence, marker="^", color="purple")
    plt.plot(df_random.Influence, marker="s", color="lightblue")

    plt.legend(['Greedy++', 'Page Rank', 'Degree', 'Random'])
    plt.xticks(np.arange(0, 21))
    plt.xlabel("Seed set size")
    plt.ylabel("Influence spread")


    plt.savefig(f"./Results/plots/influence_vis_{data}_{threshold}.png")

    plt.clf()
    plt.title(f"Run times, data: {data}")
    plt.bar(range(4), [(sum(df_degree.InfRuntime)/len(df_degree.InfRuntime)), 
                       (sum(df_random.InfRuntime)/len(df_random.InfRuntime)),
                       (sum(df_pagerank.InfRuntime)/len(df_pagerank.InfRuntime)),
                       (sum(df_greedy.InfRuntime)/len(df_greedy.InfRuntime))])
    plt.xticks(range(4), ['Degree', 'Random', 'PageRank', 'Greedy++'])
    plt.savefig(f"./Results/plots/runtime_vis_{data}_{threshold}.png")
    
plot_inf("NetHept", 
         df_greedy_nethept_linear, 
         df_pagerank_nethept_linear, 
         df_degree_nethept_linear, 
         df_random_nethept_linear,
         "Linear")


# In[8]:


plot_inf("NetHept", 
         df_greedy_nethept_convex, 
         df_pagerank_nethept_convex, 
         df_degree_nethept_convex, 
         df_random_nethept_convex,
         "Convex")


# In[10]:


plot_inf("NetHept", 
         df_greedy_nethept_convex, 
         df_pagerank_nethept_convex, 
         df_degree_nethept_concave, 
         df_random_nethept_convex,
         "Concave")


# In[18]:


plot_inf("NetHept", 
         df_greedy_nethept_majority, 
         df_pagerank_nethept_majority, 
         df_degree_nethept_majority, 
         df_random_nethept_majority,
         "Majority vote")


# In[61]:


plot_inf("NetPhy", df_greedy_netphy, df_pagerank_netphy, df_degree_netphy, df_random_netphy,
         "Linear")


# In[132]:


plot_inf("Epinions", df_greedy_epinions, 
         df_pagerank_epinions, df_degree_epinions, df_random_epinions, "Linear")


# ## Comparison with Published Results

# In[13]:


def get_reference_result(dataset, algorithm, threshold):
    path = f"Reference_Results/{dataset}_{threshold}_data.csv"
    df = pd.read_csv(path, header=0, skiprows=[1])
    cols = df.columns.values
    new_cols = []
    colname = None
    for i, col in enumerate(cols):
        if i % 2 == 0:
            colname = col
            new = colname + "_X"
        else:
            new = colname + "_Y"
        new_cols.append(new)
    df.columns = new_cols
    return df[[f"{algorithm}_Y"]]


# In[14]:


def plot_reference_comparison(df_greedy, df_page, df_degree, df_random, dataset: str, threshold: str):
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(df_greedy.Size, df_greedy.Influence, marker="o", color="red", linewidth=2)
    ax.plot(df_page.Influence, marker="x", color="green", linewidth=2)
    ax.plot(df_degree.Influence, marker="^", color="purple", linewidth=2)
    ax.plot(df_random.Influence, marker="s", color="lightblue", linewidth=2)
    
    ref_greedy = get_reference_result(dataset, "Greedy++", threshold)
    ref_pagerank = get_reference_result(dataset, "PageRank", threshold)
    ref_degree = get_reference_result(dataset, "Degree", threshold)
    ref_random = get_reference_result(dataset, "Random", threshold)
    
    ax.plot(ref_greedy.index, ref_greedy, marker="o", color="red", 
            linewidth=1, linestyle="--", alpha=0.85) #, mec="black")
    ax.plot(ref_pagerank.index, ref_pagerank, marker="x", color="green", linewidth=1, linestyle="--", alpha=0.85)
    ax.plot(ref_degree.index, ref_degree, marker="^", color="purple", linewidth=1, linestyle="--", alpha=0.85)
    ax.plot(ref_random.index, ref_random, marker="s", color="lightblue", linewidth=1, linestyle="--", alpha=0.85)
    
    
    ax.legend(['Greedy++', 'Page Rank', 'Degree', 'Random', 'Reference', 'Reference', 'Reference', 'Reference'], 
              fontsize=12, ncol=2)
    ax.set_xticks(np.arange(0, 21))
    ax.set_xlabel("Seed set size", fontsize=12)
    ax.set_ylabel("Influence spread", fontsize=12)
    ax.set_title(f"Comparison to Published Results of {dataset} {threshold} threshold", fontsize=16)
    # ax.set_yticks(fontsize=16)
    plt.savefig(f"./Results/plots/ref_comp_{dataset}_{threshold}.png", dpi=250)


# ### NetHEPT linear

# In[15]:


plot_reference_comparison(df_greedy_nethept_linear, df_pagerank_nethept_linear, df_degree_nethept_linear, df_random_nethept_linear,
                       dataset="NetHEPT", threshold="linear")


# ### NetHEPT concave

# In[ ]:





# ### NetHEPT convex

# In[167]:


plot_reference_comparison(df_greedy_nethept_convex, df_pagerank_nethept_convex, df_degree_nethept_convex, df_random_nethept_convex,
                       dataset="NetHEPT", threshold="convex")


# ### NetHEPT majority

# In[168]:


plot_reference_comparison(df_greedy_nethept_majority, df_pagerank_nethept_majority, df_degree_nethept_majority, df_random_nethept_majority,
                       dataset="NetHEPT", threshold="majority")


# ### NetPhy linear

# In[169]:


plot_reference_comparison(df_greedy_netphy, df_pagerank_netphy, df_degree_netphy, df_random_netphy,
                       dataset="NetPHY", threshold="linear")


# ### Epinions linear

# In[178]:


plot_reference_comparison(df_greedy_epinions, df_pagerank_epinions, df_degree_epinions, df_random_epinions,
                       dataset="Epinions", threshold="linear")


# In[180]:


#plot_reference_comparison(df_greedy_epinions_IC, df_pagerank_epinions_IC, df_degree_epinions_IC, df_random_epinions_IC,
#                       dataset="Epinions", threshold="linear")


# ## t-Test of Residuals

# In[10]:


import scipy
scipy.__version__


# In[16]:


def t_test(dataset, threshold):
    result_df = pd.read_csv(f"Results/Greedy++_output_{dataset}_{threshold}/Influence.csv")
    reference = get_reference_result(dataset, "Greedy++", threshold)
    
    residuals = result_df["Influence"].values - reference["Greedy++_Y"].values
    mad = np.mean(np.absolute(residuals))
    tstat, pvalue = stats.ttest_1samp(residuals, popmean = 0)
    s = "HAS to be rejected" if pvalue < 0.1 else "CANNOT be rejected"
    print(f"The value of the test statistic is {tstat} with a p-value of {pvalue}.\n" + 
          f"With a conficence level of 90% the Null-Hypothesis {s}.\n" + 
          f"The MAD of the residuals is {mad}.")


# In[17]:


t_test("NetHept", "linear")


# In[18]:


t_test("NetHept", "convex")


# In[20]:


t_test("NetHept", "majority")


# In[21]:


t_test("NetPhy", "linear")


# Although the Null-Hypothesis has to be rejected for convex and majority thresholds the mean absolute deviations for the residuals is very small and might be due to errors in the data extraction process.

# In[22]:


t_test("Epinions", "linear")


# In[ ]:




