#!/usr/bin/env python
# coding: utf-8

# # 関数一覧  
# 
# ---
# 
# ### ターミナルからの入力を受け取る  
# 
# `sys`モジュール `argv()`関数
# 
# ```python
# import sys
# 
# inputfile1 = sys.argv[1]
# inputfile2 = sys.argv[2]
# ```
# <br>
# 
# ターミナルからの入力をリストとして出力  
# 最初の要素sys.argv[0]は実行ファイル  
# 
# ---
# 
# ### pythonでターミナルのコマンドを実行する
# 
# `subprocess`モジュール `run()`関数  
# 
# ```python
# import subprocess
# subprocess.run(['mkdir', 'new_dir'])
# ```
# <br>
# 
# 実行するコマンドはリスト形式で与える。
# 
# `shell=True`を使うと、文字列でコマンドを与えることができる。変数も使用可。  
# 
# ```python
# import subprocess
# subprocess.run('mkdir new_dir', shell=True)
# ```
# 
# ---
# 
# ### ファイルパスを取得する
# 
# `glob`モジュール `glob()`関数  
# 
# ```python
# import glob
# filelist = glob.glob('directory/*.txt')
# ```
# <br>
# 
# リストとして取得できる。  
# `glob()`では、ワイルドカードは`*`を使う。  
# 正規表現とは異なるので注意。  
# 
# ---
# 
# 

# ### 多重比較補正  
# 
# `statsmodels`ライブラリの`multipletests`を使用する。  
# [statsmodels リンク](https://www.statsmodels.org/dev/generated/statsmodels.stats.multitest.multipletests.html)
# 

# In[1]:


import statsmodels.stats.multitest as multi

pvalues = [0.1, 0.3, 0.5, 0.4, 0.1, 0.01, 0.05, 0.9, 0.4, 0.3]
qvalues = multi.multipletests(pvalues, alpha = 0.05, method = 'fdr_bh', is_sorted = False)[1].tolist()
for i in range(len(qvalues)):
    print(pvalues[i], qvalues[i], sep = '\t')


# 戻り値はtupleで、インデックス[0]はTure or False、[1]は補正されたp-value。  
# 要素のタイプはnumpy.ndarray。  
# ここでは`tolist()`でリストに変換している。  
# <br>
# インプットするp値がソートされていない場合は、`is_sorted = False`を指定する。  
# 昇順にソートされている場合は、`is_sorted = True`を指定する。

# In[2]:


pvalues = [0.1, 0.3, 0.5, 0.4, 0.1, 0.01, 0.05, 0.9, 0.4, 0.3]
pvalues_sorted = sorted(pvalues)
qvalues = multi.multipletests(pvalues_sorted, alpha = 0.05, method = 'fdr_bh', is_sorted = True)[1].tolist()
for i in range(len(qvalues)):
    print(pvalues[i], qvalues[i], sep = '\t')


# `method = 'fdr_bh'` Benjamini/Hochberg  
# `method = 'bonferroni'`　ボンフェローニ  
# 
# ---

# ### ヒートマップの作成  
# 
# `seaborn`の`clustermap`を使用する。  
# [clustermap リンク](https://seaborn.pydata.org/generated/seaborn.clustermap.html)  
# <br>
# ここでは例として`sklearn`のIrisのデータを使用する。

# In[3]:


import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns = iris.feature_names)
print(df)


# In[4]:


import seaborn as sns
from matplotlib import pyplot as plt

plt.figure()
sns.clustermap(df, method='ward', vmin = 0, vmax = 10)
plt.show()


# In[5]:


plt.figure()
sns.clustermap(df[:20], method='ward', vmin = 0, vmax = 10, linewidth = 0.5)
plt.show()


# <br>
# 
# `matplotlib.colors.LinearSegmentedColormap.from_list`でヒートマップの色を指定する。  
# [matplotlib.colors.LinearSegmentedColormap リンク](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap)

# In[6]:


import matplotlib as mpl

colormap = mpl.colors.LinearSegmentedColormap.from_list('colormap_test',['navy','lightgray','crimson'])
plt.figure()
sns.clustermap(df, method='ward', cmap = colormap, vmin = 0, vmax = 10)
plt.show()


# ---
# 
# 

# ### jitter plot  
# 
# `seaborn`の`stripplot`を使用する。  

# In[7]:


import pandas as pd
from sklearn.datasets import load_boston
dia = load_boston()
print(dia.keys())
print(dia['DESCR'])
df = pd.DataFrame(dia['data'], columns = dia['feature_names'])
print(df)
#df = pd.DataFrame(iris.data, columns = iris.feature_names)
#df['target'] = iris.target #品種情報も追加
#print(df)


# In[8]:


import seaborn as sns
from matplotlib import pyplot as plt

print(df.columns[1])
plt.figure()
sns.stripplot(x = 'target', y = df.columns[2], data = df, jitter = 0.2)
plt.show()


# In[ ]:




