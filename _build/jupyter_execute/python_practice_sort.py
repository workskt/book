#!/usr/bin/env python
# coding: utf-8

# # ソート
# 
# ---
# 
# ## リストのソート
# 
# <br>
# 
# リストの中身を並び替えたい場合は、以下の二通りの方法があります。  
# (1) `sort( )`を使う  
# (2) `sorted( )`を使う

# ---
# 
# (1) `sort( )`を使う  
# 
# これはリスト型のメソッドですので、ソートしたいリストと`sort( )`を`.`で繋ぎます。  
# 指定したリストの要素が並び替えられ、上書きされます。

# In[1]:


a = ['TP53', 'EGFR', 'MYC', 'CDKN1A']
a.sort()
print(a)


# リスト`a`の要素が、アルファベット順に並び替えられました。  
# 上書きされるので、元の順番を持つ配列は残っていません。

# (2) `sorted( )`を使う
# 
# これは組み込み関数（最初から使える関数）で、新しいリストを返します。  
# 
# > 組み込み関数の一覧はこちらから。  
# > https://docs.python.org/ja/3/library/functions.html  
# > 組み込み関数でないものは、事前にimportする必要があります（後述）。

# In[2]:


a = ['TP53', 'EGFR', 'MYC', 'CDKN1A']
b = sorted(a)
print(b)
print(a)


# 新しく定義した`b`に並び替えられたリストが代入されました。  
# 元のリスト`a`はそのまま残っています。

# 降順に並べ替えたい場合は、カッコ内に`reverse=True`と書きます。

# In[3]:


a = ['TP53', 'EGFR', 'MYC', 'CDKN1A']
a.sort(reverse=True)
print(a)


# In[4]:


a = ['TP53', 'EGFR', 'MYC', 'CDKN1A']
b = sorted(a, reverse=True)
print(b)


# ---
# 
# ## 文字列のソート
# 
# <br>
# 
# 文字列を並び替える場合は、`sorted( )`を使用します。  
# 結果はリスト型として返されます。

# In[5]:


a = 'tumor protein p53'
b = sorted(a)
print(b)
print(type(b))
c = sorted(a, reverse=True)
print(c)
print(type(c))


# リスト型だと使いにくいので、文字列に戻す場合は、リスト型のメソッド`join( )`を使います。  
# `join( )`はリストの要素を、指定した区切り文字をはさんで連結してくれます。
# 
# <br>
# 
# ```python
# '区切り文字'.join( )
# ```
# <br>

# In[6]:


d = ''.join(b)
print(d)
print(type(d))


# カンマで区切って出力することもできます。

# In[7]:


d = ','.join(b)
print(d)


# ---
# 
# ## 辞書のソート
# 
# <br>
# 
# 辞書を並び替えたい場合も、`sorted( )`を使用します。  
# 
# キーを並び替えたい場合は、`keys( )`を使います。  
# 結果はリスト形式で返されます。

# In[8]:


genes_dict = {'TP53': 100, 'EGFR': 300, 'MYC': 400, 'CDKN1A': 200}
a = sorted(genes_dict.keys())
print(a)
print(type(a))


# 要素を並び替えたい場合は、`values( )`を使います。

# In[9]:


genes_dict = {'TP53': 100, 'EGFR': 300, 'MYC': 400, 'CDKN1A': 200}
b = sorted(genes_dict.values())
print(b)


# 降順で並べ替えたい場合は、カッコ内に`reverse=True`と書きます。

# In[10]:


genes_dict = {'TP53': 100, 'EGFR': 300, 'MYC': 400, 'CDKN1A': 200}
c = sorted(genes_dict.values(), reverse=True)
print(c)


# <br>
# 
# さて、要素の順番で並び替えて、その順番でキーを取得したいときはどうすればよいでしょうか。  
# 遺伝子名と発現量が格納された辞書を使って、遺伝子を発現量順に並べるといったことはしばしばあります。  
# 
# この場合、辞書型のメソッド`items( )`、**key関数**、**lambda関数**を使用します。  
# 結果はタプル型で返されます。

# In[11]:


genes_dict = {'TP53': 100, 'EGFR': 300, 'MYC': 400, 'CDKN1A': 200}
d = sorted(genes_dict.items(), key=lambda x:x[1], reverse=True)
print(d)


# 要素の降順に並び替えられて、タプル型で結果が返ってきました。
# 
# `sorted( )`のカッコ内がちょっと難しいかもしれませんが、とりあえずそのまま覚えましょう。  
# 慣れた頃に調べてみると、理解できるようになっていると思います。  

# もし遺伝子名をリストで取得したければ、リスト内包表記を使いましょう。

# In[12]:


genes_dict = {'TP53': 100, 'EGFR': 300, 'MYC': 400, 'CDKN1A': 200}
e = [gene for gene, expression in sorted(genes_dict.items(), key=lambda x:x[1], reverse=True)]
print(e)

