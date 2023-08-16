#!/usr/bin/env python
# coding: utf-8

# # 5. if文 wihle文
# 
# ---
# 
# ## 5.1 if文
# 
# ある条件に当てはまる時だけ処理を行いたい場合には、**if文** を使用します。
# 
# <br>
# 
# ```python
# if 条件式1:
#   命令1
# elif 条件式2:
#   命令2
# else:
#   命令3
# ```
# 
# <br>
# 
# `elif`の条件は増やしても構いません。  
# また、条件が一つだけで、当てはまらない場合に何も処理をしないのであれば、`if`だけでも構いません。  
# <br>
# 
# 以下のコードは、リストから条件に当てはまる要素だけ`print`するif文の例です。

# In[1]:


a = ['TP53', 'EGFR', 'MYC', 'CDKN1A']
for gene in a:
    if gene == 'EGFR':
        print(gene)
    else:
        print('others')


# for文を使ってリスト`a`の要素を順番に取り出し、`if`で遺伝子名が`EGFR`と一致する場合はその名前を、そうでなければ`else`で`others`と出力するよう命令しています。  
# <br>
# 
# `==`は同一であることを示す比較演算子です。  
# `=`は等しいという意味ではなく、代入するための演算子ですので気をつけてください。
# <br>
# 
# 他の比較演算子の例です。  
# `>` より大きい  
# `>=` 以上  
# `<` 未満  
# `<=` 以下  
# `==` 同じ  
# `!=` 異なる  
# `in` 含む  
# `not` 存在しない  

# <br>
# 
# ある要素がリストの中に存在するか確認したいときには`in`を使うと便利です。  
# 

# In[2]:


a = ['TP53', 'EGFR', 'MYC', 'CDKN1A']
if 'MYC' in a:
    print('MYC YES')
else:
    print('MYC NO')


# 文字列に対しても使用できます。

# In[3]:


a = 'tumor protein p53'
if 'm' in a:
    print('m YES')

if 'x' in a:
    print('x YES')


# **if文**で条件に該当しない場合に何もしないのであれば、`else`を書く必要はありません。

# <br>
# 
# `and`（かつ）や`or`（または）を使って（ブール演算子）複数の条件を指定することもできます。

# In[4]:


a = ['TP53', 'EGFR', 'MYC', 'CDKN1A']
for gene in a:
    if gene == 'EGFR' or gene == 'MYC':
        print(gene)
    else:
        print('others')


# In[5]:


a = ['TP53', 'EGFR', 'MYC', 'CDKN1A']
for gene in a:
    if 'C' in gene and 'D' in gene:
        print(gene)
    else:
        print('others')


# <br>
# 
# 前にも説明しましたが、文字列は必ず**クォーテーション**で囲む必要があります。  
# これを忘れると`EGFR`という変数を意味することになりますが、`EGFR`という変数はこれまでに定義されていないため、エラーが出力されます。

# In[6]:


a = ['TP53', 'EGFR', 'MYC', 'CDKN1A']
for gene in a:
    if gene == EGFR:
        print(gene)
    else:
        print('others')


# In[ ]:





# ---
# 
# ## 5.2 while文
# 
# 条件に合致している限り処理を繰り返したい場合は、**while文**を使用します。
# 
# ```python3
# while 条件式:
#     繰り返したい処理
# ```
# 
# 以下のように使います。

# In[7]:


a = 0
while a < 5:
    a += 1
    print(a)


# `a`が5未満であれば、1を足して出力します。
# 
# `a`が5以上だと、条件式が真ではないので、繰り返しを終了します。
# 
# `+=` は変数に1を足す演算子です。

# 条件式を`True`にすると抜け出す処理を与えない限り繰り返します。  
# 繰り返しを中断するには`break`を使います。

# In[8]:


a = 0
while True:
    a += 1
    print(a)
    if a >= 10:
        break

