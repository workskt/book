#!/usr/bin/env python
# coding: utf-8

# # pandasデータフレームの扱い方
# 

# ## テストデータの取得
# 
# <br>
# 
# （すでにタブ区切りのテストデータが手元にある場合は、下の「データの読み込み」まで読み飛ばしてください。）
# 
# <br>
# データフレームを扱うために、pandasをインポートします。
# 
# また、定番中の定番データであるirisを取得するため、load_irisをインポートします。

# In[1]:


import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()


# <br>
# 
# irisはdictionary-like objectのようですので、とりあえず`keys( )`で項目を確認してみます。

# In[2]:


iris.keys()


# <br>
# 
# データの中身も確認してみます。
# 
# sklearn.datasetsのデータを確認するためには、データの変数と項目名をドットで繋ぎます。

# In[3]:


iris.feature_names


# <br>
# 
# 'data'は各個体のデータ、'target'は品種のインデックス、'target_names'は品種名、'feature_names'はデータ項目が格納されているようです。
# 
# 扱いやすくするために、`pandas`の`DataFrame( )`でデータフレームの形式に変換します。
# 
# `columns`で列ラベル情報を指定します。

# In[4]:


df = pd.DataFrame(iris.data, columns=iris.feature_names)


# <br>
# 
# dfの中身を確認します。

# In[5]:


df


# <br>
# 
# 列ラベル'target'を作って、target情報も追加します。

# In[6]:


df['target'] = iris.target


# In[7]:


df


# target（品種のインデックス）が追加されました。
# 
# <br>
# 
# targetがインデックスだとわかりにくいので、品種名に変換します。
# 
# **特定の行だけ取得する**ためには、`loc[ ]`を使います。
# 
# <br>
# 
# ```python
# df.loc[行番号]
# ```
# 
# <br>

# In[8]:


df.loc[0:4]


# <br>
# 
# `loc.[ ]`の`[ ]`内に条件を入れると、その条件と一致する行だけ取得できます。

# In[9]:


df.loc[df['target'] == 0]


# targetが0の行だけ出力されました。
# 
# <br>
# 
# 以下のようにすると、指定の条件に一致する場合だけ、指定した列に値を代入できます。
# 
# <br>
# 
# ```python
# loc[条件, 列ラベル] = 代入する値
# ```
# 
# <br>

# In[10]:


df.loc[df['target'] == 0, 'target'] = 'setosa'
df.loc[df['target'] == 1, 'target'] = 'versicolor'
df.loc[df['target'] == 2, 'target'] = 'virginica'


# In[11]:


df


# <br>
# 
# ## データフレームのファイルへの出力
# 
# <br>
# 
# このデータフレーム形式をいったんタブ区切りファイルに出力します。
# 
# 出力のためには`to_csv( )`を使います。
# 
# `( )`内に出力ファイルのパスを記入します。
# 
# `sep='\t'`を指定することでタブ区切りファイルとして出力できます。
# 
# 指定しない場合はcsvファイルとして出力します。
# 
# 行ラベル(index)は必要ないので、`index=False`を指定します。
# 
# もし列ラベルが不要であれば、`header=False`を指定します。

# In[12]:


df.to_csv('irisdata.txt', sep='\t', index=False)


# ---
# 
# ## データの読み込み
# 
# <br>
# 
# ファイルをデータフレームとして読み込むためには、以下の関数を使用します。
# 
# `pd.read_table( )`
# タブ区切りファイルの読み込み
# 
# `pd.read_csv( )`
# csvファイルの読み込み

# In[13]:


df = pd.read_table('irisdata.txt')


# In[14]:


df


# <br>
# 
# 読み込む時に行ラベル(index)にする列を指定する場合は、`index_col=`で列ラベルか列番号を指定します。

# In[15]:


df2 = pd.read_table('irisdata.txt', index_col=4)


# In[16]:


df2


# <br>
# 
# 特定の列だけ取得するには、`[ ]`の中に列ラベルを指定します。
# 
# <br>
# 
# ```python
# df['列ラベル']
# ```
# 
# <br>

# In[17]:


df['target']


# <br>
# 
# 特定の行だけ取得するには、`loc[ ]`を使用します。
# 
# <br>
# 
# ```python
# df.loc[行ラベル]
# ```
# 
# <br>

# In[18]:


df.loc[149]


# In[19]:


df.loc[145:149]


# <br>
# 
# 条件に該当する行だけ出力する場合にも、`loc[ ]`を使用します。

# In[20]:


df.loc[df['target'] == 'virginica']


# In[21]:


df.loc[df['sepal length (cm)'] >= 7]


# ---
# 
# ## データフレームの連結
# 
# <br>
# 
# 空のデータフレームを作成するには、`DataFrame( )`を使用して以下のようにします。
# 
# <br>
# 
# ```python
# pd.DataFrame(index=[])
# ```
# 
# <br>

# In[22]:


df2 = pd.DataFrame(index=[])


# <br>
# 
# 
# データフレームの連結には、`concat( )`を使用します。
# 
# 縦方向に連結する場合は以下のようにします。
# 
# <br>
# 
# ```python
# pd.concat([df1, df2], axis=0)
# ```
# 
# <br>
# 
# axisは省略可

# In[23]:


df3 = pd.concat([df2, df[df['target'] == 'setosa']], axis=0)


# In[24]:


df3


# In[25]:


df4 = pd.concat([df3, df[df['target'] == 'virginica']], axis=0)


# In[26]:


df4


# <br>
# 
# 横方向に連結
# 
# <br>
# 
# ```python
# pd.concat([df1, df2], axis=1)
# ```
# 
# <br>

# In[27]:


df5 = pd.concat([df[df['target'] == 'setosa'], df[df['target'] == 'virginica']], axis=1)


# In[28]:


df5


# <br>
# 
# 行列をひっくり返す
# 
# <br>
# 
# ```python
# df.T
# ```
# 
# <br>

# In[29]:


df6 = df[df['target'] == 'setosa'].T


# In[30]:


df6

