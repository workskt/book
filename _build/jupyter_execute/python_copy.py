#!/usr/bin/env python
# coding: utf-8

# # copy
# 
# ---
# 
# `a`という名前のリストや辞書を編集したい場合、いったん別の名前の変数である`b`に、`=`を使って格納するとします。  
# その後`b`だけ編集した場合、pythonでは元の`a`も同様に編集されてしまいます。

# In[1]:


a = ['a', 'b', 'c', 'd']
b = a
a[0] = 'e'
print('リストa', a, id(a))
print('リストb', b, id(b))


# `b = a`でリスト`a`をリスト`b`にコピー(?)してから、リスト`a`の最初の要素を`e`に変更しました。  
# しかし、リスト`b`の最初の要素も`e`に変更されてしまっていることがわかります。

# In[2]:


a = {'A': 1, 'B': 2, 'C':3, 'D': 4}
b = a
b['A'] = 4
print('辞書a', a, id(a))
print('辞書b', b, id(b))


# 辞書の場合でも同様です。  
# 辞書`b`のキー`A`の値を`4`に変更すると、辞書`a`のキー`A`の値も`4`になってしまいました。

# ---
# `sorted()`を使って、リスト`a`を降順にソートしたものをリスト`b`に格納してから、リスト`b`の要素を変更してみます。

# In[3]:


a = ['a', 'b', 'c', 'd']
b = sorted(a, reverse=True)
print('リストa', a, id(a))
print('リストb', b, id(b))


# このように、sorted()関数を使って処理したものを他の変数に格納すれば、独立した変数として処理することができます。

# In[4]:


a = ['a', 'b', 'c', 'd']
b = a
b.sort(reverse=True)
print('リストa', a, id(a))
print('リストb', b, id(b))


# しかし、いったんリスト`a`をリスト`b`に代入した後に、リストのメソッドである`sort`を使った場合は、同一のオブジェクトとして扱われるようです。

# ---
# 
# オブジェクトをコピーしたい場合は、`copy`モジュールの`copy`メソッドを使用します。

# In[5]:


import copy
a = ['a', 'b', 'c', 'd']
b = copy.copy(a)
b[0] = 'e'
print('リストa', a, id(a))
print('リストb', b, id(b))


# リスト`a`とリスト`b`を独立して処理することができました。

# In[6]:


a = ['a', 'b', 'c', 'd']
b = copy.copy(a)
b.sort(reverse=True)
print('リストa', a, id(a))
print('リストb', b, id(b))


# `copy`メソッドでコピーしたあと、リスト`b`を`sort`メソッドで編集すれば、リスト`a`とリスト`b`を独立に扱うことができました。

# In[7]:


a = {'a': 1, 'b': 2, 'c':3, 'd': 4}
a.setdefault('e', {})
a['e'].setdefault('x', 5)
print(a)


# In[8]:


a = {'a': 1, 'b': 2, 'c':3, 'd': 4}
a.setdefault('e', {})
a['e'].setdefault('x', 5)
a['e'].setdefault('y', 6)

b = copy.copy(a)
print('辞書a', a, id(a))
print('辞書b', b, id(b))

b['e']['x'] = 10
print('辞書a', a, id(a))
print('辞書b', b, id(b))


# In[9]:


a = {'a': 1, 'b': 2, 'c':3, 'd': 4}
a.setdefault('e', {})
a['e'].setdefault('x', 5)
a['e'].setdefault('y', 6)

b = copy.deepcopy(a)
print('辞書a', a, id(a))
print('辞書b', b, id(b))

b['e']['x'] = 10
print('辞書a', a, id(a))
print('辞書b', b, id(b))


# In[10]:


a = 'tokyo'
b = a
print('文字a', a, id(a))
print('文字b', b, id(b))

b = 'osaka'
print('文字a', a, id(a))
print('文字b', b, id(b))


# In[ ]:




