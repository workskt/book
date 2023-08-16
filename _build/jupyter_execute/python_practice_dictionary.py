#!/usr/bin/env python
# coding: utf-8

# # 辞書
# 
# ---
# 
# ## 辞書について
# 
# <br>
# 
# ある複数の要素を紐づけて、その組み合わせを格納した変数を**辞書**と言います。  
# 辞書は**キー**と**値**から構成されます。  
# キーと値の組み合わせを辞書に代入した後、キーを指定すると、それに対応する値を返してくれます。  
# 以下のようにして辞書にキーと値を代入します。  
# 
# <br>
# 
# ```python
# 辞書の作成
# 変数名 = {キー1:値1, キー2:値2,　キー3:値3}
# ```
# 
# <br>
# 
# キーと値の組み合わせはコロン`:`で繋ぎ、それぞれの組み合わせはカンマ`,`で区切ります。  
# この組み合わせは何個でも代入することができます。  
# 
# 多くの遺伝子には複数の転写産物が存在し、その転写産物にはIDがつけられています。  
# キーをGene Symbol、値にrefSeq IDを紐づけた辞書を例として作成してみます。  

# In[2]:


genes_dict = {'TP53': 'NM_000546', 'EGFR': 'NM_001346897', 'MYC': 'NM_001354870', 'CDKN1A': 'NM_000389'}
print(genes_dict)


# 作成した辞書型の変数`genes_dict`を`print()`で出力すると、辞書の中身が表示されます。
# > <注>これらの遺伝子の転写産物は上記以外にも存在しますが、ここでは例として一つだけ使用しています。

# ---
# 
# ## 辞書からキー、値を取り出す
# 
# <br>
# 
# キーを指定して、そのキーに紐づけられた要素を取得することができます。  
# 辞書の変数に`[キーの名前]`をつけます。
# 
# <br>
# 
# ```
# 値の取り出し方
# 変数名[キーの名前]
# ```
# 
# <br>
# 
# 例えば、辞書型変数`genes_dict`から、キー`EGFR`に対応する値を取得するには以下のようにします。

# In[3]:


value = genes_dict['EGFR']
print(value)


# キーに`'EGFR'`を指定することで、EGFRの転写産物ID`NM_001346897`を取得できました。
# <br>

# <br>  
# 
# 辞書を使っていると、ある一つのキーや値だけでなく、全てのキーや値を取り出して使いたいと思うことがしばしばあります。  
# 辞書から**すべてのキーを取り出したいとき**には、辞書型のメソッド（辞書型のデータを処理する関数)である`keys( )`を使用します。  
# 
# ```python
# keys()メソッドの使い方
# 辞書型変数名.keys()
# ```
# <br>

# In[4]:


for key in genes_dict.keys():
    print(key)


# for文を使い、`keys()`で辞書`genes_dict`のキーをひとつずつ取り出し、`print()`で出力しました。

# <br>
# 
# 辞書から**すべての要素を取り出したいとき**には、`values()`メソッドを使用します。

# In[5]:


for value in genes_dict.values():
    print(value)


# for文を使い、`values()`で辞書`genes_dict`の要素をひとつずつ取り出し、`print()`で出力しました。

# <br>
# 
# 辞書から**キーと値の両方を同時に取り出したい**ときは、`items( )`を使用します。  

# In[6]:


for key, value in genes_dict.items():
    print('キー:', key, '\t値:', value)


# キーと値の両方を受け取ることができました。  
# `\t`はタブ区切りを意味します。  
# 出力の際、間隔を開けて見やすくするためにタブを入れました。
# 
# `dict( )`はキーと値の二つの値を返しますので、`key`と`value`という二つの変数で受け取っています。

# ---
# 
# ## あるキーを持っているかどうか調べる
# 
# <br>
# 
# 辞書があるキーを持っているかどうかを調べるには、`in`を使います。

# In[7]:


if 'EGFR' in genes_dict:
    print('EGFR\tYES')
else:
    print('EGFR\tNO')

if 'ERBB2' in genes_dict:
    print('ERBB2\tYES')
else:
    print('ERBB2\tNO')


# <br>
# 
# 要素に存在するかどうかを調べるためには、`values( )`を合わせて使います。

# In[8]:


if 'NM_000546' in genes_dict.values():
    print('NM_000546\tYES')

if 'NM_000000' in genes_dict.values():
    print('NM_000000\tYES')


# ---
# 
# ## 辞書からキーや要素を取り出してリスト形式にする
# 
# <br>
# 
# `keys()`や`values()`で返されるデータは`dict_keys`という形式のものです。

# In[9]:


c = genes_dict.keys()
print('キー', c)
print('型', type(c))


# `type()`関数を使うと、変数がどのような型であるかを調べることができます。  
# `keys()`で返されるデータは`dict_keys`という型であると教えてくれます。  
# <br>
# 
# もしキーの情報をリストに変更したければ、`list()`関数を使用します。  

# In[10]:


d = list(c)
print(d)
print(type(d))


# ---
# 
# ## setdefaultで辞書に新しいキーと要素を追加する
# 
# <br>
# 
# 辞書に新しいキーと値を追加したい場合は、以下のように書きます。  

# In[12]:


genes_dict = {} #空の辞書を作成
genes_dict['TP53'] = 'NM_000546'
print(genes_dict)


# 辞書に新しいキーと値の組み合わせが格納されました。  
# この書き方では、同じキーにさらに値を代入した場合、値は上書きされてしまいます。　　
# 

# In[13]:


genes_dict = {} #空の辞書を作成
genes_dict['TP53'] = 'NM_000546'
genes_dict['TP53'] = 'NM_001126116'
print(genes_dict)


# すでに辞書がキーと値を持っている場合、上書きされてしまうと都合が悪い場合もあります。  
# その場合は`setdefault`を使います。  
# 
# <br>
# 
# ```python
# 辞書.setdefault(キー, キーが存在しない場合にそのキーに対応する値)
# ```
# 
# <br>
# 
# `setdefault`では、キーが存在していない場合、カッコ内の二つ目に指定した引数を値として格納します。  
# **もしキーが存在していた場合、何もしません。**  
# 

# In[14]:


genes_dict = {} #空の辞書を作成
genes_dict.setdefault('TP53', 'NM_000546')
print(genes_dict)

genes_dict.setdefault('TP53', 'NM_001126116')
print(genes_dict)


# 2回目の`setdefault( )`では、すでにキーが存在しているので何もしていません。  
# 
# キーがすでに存在する場合、値を追加して紐付けたい場合もあります。  
# その場合は、例えば値に空のリストを作成します。  

# In[16]:


genes_dict = {} #空の辞書を作成
genes_dict.setdefault('TP53', []) #キーに対して空のリストを作成
genes_dict['TP53'].append('NM_000546') #作成した空のリストにappendで要素を追加
print(genes_dict)

genes_dict.setdefault('TP53', []) #もしキーが存在していなければ、空のリストを作成。キーが存在していれば何もしない。
genes_dict['TP53'].append('NM_001126116')
print(genes_dict)


# 値に辞書を指定することもできます。  

# In[17]:


genes_dict = {} #空の辞書を作成
genes_dict.setdefault('patient1', {}) #キーに対して空の辞書を作成
genes_dict['patient1'].setdefault('TP53', 100) #作成した辞書にさらにsetdefaultでキーと値を格納
print(genes_dict)

genes_dict.setdefault('patient1', {}) #もしキーが存在していなければ、空の辞書を作成
genes_dict['patient1'].setdefault('EGFR', 200) #作成した辞書にさらにsetdefaultでキーと値を格納
print(genes_dict)

genes_dict.setdefault('patient2', {}) #もしキーが存在していなければ、空の辞書を作成
genes_dict['patient2'].setdefault('TP53', 300) #作成した辞書にさらにsetdefaultでキーと値を格納
print(genes_dict)


# サンプルごとに全遺伝子の発現量を格納した辞書を作るときなどに役に立ちます。  
