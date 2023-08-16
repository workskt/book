#!/usr/bin/env python
# coding: utf-8

# # 繰り返し
# 
# ---
# 
# ## for文
# 
# 複数の要素について同じ処理を繰り返す時、以下のような**for文**を使います。
# 
# <br>
# 
# ```python
# for 取り出した要素を代入する変数 in 複数の要素を持つ変数:
# (インデント)処理したい内容
# ```
# <br>
# 
# 例えば、遺伝子名のリストを作成して、その要素を順番に取り出して出力するためには以下のように書きます。

# In[1]:


a = ['TP53', 'EGFR', 'MYC', 'CDKN1A']
for gene in a:
    print(gene)


# リストに格納された要素である遺伝子名が順番に出力されます。  
# <br>
# 
# 最初の行で、まず複数の遺伝子名を持つリスト`a`を作成しています。  
# 
# その次の行からがfor文です。  
# `in`の後ろに書いた変数`a`から要素が一つ取り出されて、`for`の後ろに記載した変数`gene`に代入されます。  
# そして**コロン**の次の行以降に書いてある処理が行われます。  
# この処理が終わると、次の要素が`for`の後ろに書いた変数に代入され、同様の処理が繰り返されます。  
# <br>
# 
# `for`の後ろの変数の名前は自由につけることができます。  
# `for`の行の最後には必ず**コロン**`:`が必要です。  
# 
# 処理内容を記載する部分には、必ず**インデント**を入れる必要があります。  
# このインデントにより、どこまでがfor文かを判断しています。  
# そのため、**インデント** がないとfor文から抜け出してしまいますので注意してください。  
# **インデント** は、**スペース4個** が推奨されているようですが、タブでも大丈夫です。  
# ただし、インデントは**コードの中で統一しなければいけません**。  
# <br>
# 
# 以下のように、リストの全ての要素に同じ処理をする時などに使います。

# In[2]:


for gene in a:
    output = gene + '_expression'
    print(output)


# ---
# 
# ## range関数
# 
# 0,1,2,3...のように、連続する数値を生成させたい時には、`range`関数を使います。  
# これとfor文を組み合わせて繰り返し処理をさせることもあります。  
# 
# <br>
# 
# ```python
# for 数値を代入する変数 in range(終点):
# (インデント)処理したい内容
# ```  
# 
# <br>
# 
# **0から終点の数値の一つ前まで**の数値を順番に変数に代入していきます。  
# <br>

# In[3]:


for i in range(4):
    print(i, a[i])


# 最初は`0`が`i`に代入されます。  
# `print(i)`の命令により`0`が表示されます。  
# 次の行もインデントを挟んで`print(a[i])`という命令が書かれていますので、これも繰り返し処理されます。  
# 今は変数`i`には`0`が代入されていますので、`a[0]`はリストの一番目の要素である`TP53`を出力します。  
# ここで繰り返し処理の命令は終わりですので、次の数値`1`が`i`に代入され、同じ処理が繰り返されます。  
# 
# 
# `for`の後ろの変数は好きな名前をつけても構いませんが、iterationを意味する`i`がよく使われます。  

# <br>
# 
# `range( )`関数は、以下のように繰り返しの条件を細かく指定することができます。
# 
# ```python
# for 数値を代入する変数 in range(始点, 終点, 間隔):
# (インデント)処理したい内容
# ```  
# 
# 数値を一つだけ入力した場合は、最初の例のように終点となります。
# 
# 例えば、二つ目の要素から処理したい場合は、始点を**1**から始めます。

# In[4]:


for i in range(1, 4):
    print(i, a[i])


# 一つ飛ばしで取り出したい場合には、間隔を**2**にします。

# In[5]:


for i in range(0, 4, 2):
    print(i, a[i])
