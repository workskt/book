#!/usr/bin/env python
# coding: utf-8

# # 文字列
# 
# ---
# 
# ## 変数に文字列を代入する
# 
# 
# 変数に代入した文字列は、一文字取り出したり、逆順にしたりと、いろんな処理を行うことができます。  
# DNA配列を扱う際に便利であることは容易に想像できると思います。
# 
# 
# 例として、変数`a`に、`tumor protein p53`という文字列を代入してみます。

# In[1]:


a = 'tumor protein p53'
print(a)


# ---
# 
# ## 特定の文字を取り出す
# 
# 変数の後ろに`[ ]`をつけて、その中に数字を入れると、その数字の順番の文字を取り出すことができます。  
# この数値は**添字**や**インデックス**と呼ばれます。  
# **この順番は0から始まる**ので注意してください。  
# 最初の文字を取り出したければ、0を入力することになります。

# In[2]:


b = a[0]
print(b)


# インデックスに`0`を指定したので、先頭の`t`が表示されます。

# In[3]:


c = a[4]
print(c)


# インデックスに`4`を指定したので、５文字目の`r`が表示されます。
# 
# <br>
# 
# **マイナスの数値**を入力すると、後ろから順番に文字を取り出せます。  
# −1は最後から1番目の文字、−2は最後から2番目の文字、といった具合です。

# In[4]:


d = a[-1]
print(d)


# インデックスに`-1`を指定したので、最後の文字の`3`が表示されます。

# In[5]:


e = a[-3]
print(e)


# インデックスに`-3`を指定したので、最後から３文字目の`p`が表示されます。

# ---
# 
# ## 複数の文字を取り出す
# 
# **コロン**`:`を使って、複数の文字を取得することができます。
# 
# この操作を**スライス**と呼びます。
# 
# <br>
# 
# ```python
# 変数[始点:終点]
# ```
# 
# <br>
# 
# この時、**終点の1つ前**までを取得することができます。  
# ここで入力する順番は、もちろん**最初を0**としたときの順番です。

# In[6]:


f = a[6:13]
print(f)


# 7文字目(インデックスでは6)から13文字目(インデックスでは12)までの文字`protein`が表示されます。  
# **スペースも一文字とカウント**されます。  
# 終点で指定した順番の一つ前まで、というのが、慣れるまでは少しややこしいかもしれません。
# 
# <br>
# 
# 始点だけ記入した場合は、その**始点から最後まで**を取得できます。

# In[7]:


g = a[6:]
print(g)


# 7文字目以降の`protein p53`が表示されます。
# 
# <br>
# 
# 同様に、終点だけ記載した場合は、**最初から終点の一つ前まで**を取得できます。

# In[8]:


h = a[:13]
print(h)


# 13文字目(インデックスでは12)までの`tumor protein`が表示されます。
# 
# <br>
# 
# `[::-1]`と書くと**逆順**の文字列を取得できます。

# In[9]:


r = a[::-1]
print(r)

