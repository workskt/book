#!/usr/bin/env python
# coding: utf-8

# # テキストファイルを開く・ファイルに出力する
# 
# ---
# 
# テキストファイルを処理するために、まずはテキストファイルを開いてみます。  
# 
# 今回はUCSCのサイトから、ヒトの転写産物情報が記載されているrefFlatファイルをダウンロードします。  
# https://genome.ucsc.edu/  
# Downloads -> Genome Data -> Human -> Annotations -> SQL table dump annotations -> refFlat.txt.gzをダウンロード  
# 
# gzファイルを解凍します。  
# > ターミナルであれば $ gunzip refFlat.txt.gz  
# > windownsの場合だと解凍用フリーウェアがあります。  
# 
# pythonでファイルを開くためには`open( )`と`with`を使います。   
# 
# 
# <br>
# 
# ```python
# with open(読み込みファイルパス) as ファイルオブジェクト:
#     処理
# ```
# 
# <br>
# 
# ファイルオブジェクトはそのファイルの内容を呼び出すときに使う名前のようなものと考えてください。  
# with以降の行はインデントを入れることで、ファイルを開いた状態での処理となります。  
# 
# ファイルを開いたあとは、そのファイルの内容を取り出す必要があります。  
# 内容を取り出すためには`readlines( )`メソッドを使います。  
# これは、ファイルの内容を一行ずつリスト形式にして取り出します。  
# ファイルオブジェクトと`readlines( )`を`.`で繋ぎます。  

# In[1]:


with open('refFlat.txt') as f:
    lines = f.readlines()
    for line in lines[:10]: #表示の都合上１０行だけ出力していますが、for line in lines:で全ての行を出力できます。
        print(line)    


# `readlines( )`でファイルの内容を一行ずつ分けて`lines`というリストに格納しました。  
# その後、**for文**を使ってリストの要素を一つずつ、つまりファイル内容を一行ずつ表示させています。  
# 
# `readlines( )`はファイルの内容を全て読み込みます。  
# バイオデータ解析では、次世代シーケンサーの配列データ（Fastq、SAM等）のように容量の大きなものを扱うことがあります。  
# メモリに負荷をかけないようにするため、一行だけ取り出して処理を行う、というのを繰り返した方がよい場合があります。  
# その場合は`in`の後ろに直接ファイルオブジェクトをもってきます。  

# In[2]:


with open('refFlat.txt') as f:
    line_num = 1 #表示の都合上１０行だけ出力していますが、コメントをつけている行（コメントアウト）を除けば全て表示できます。
    for line in f:
        print(line)
        
        line_num += 1 #全て出力する場合不要
        if line_num > 10: #全て出力する場合不要
            break #全て出力する場合不要


# `__sizeof__()`を使うと使用メモリを確認できます。

# In[3]:


with open('refFlat.txt') as f:
    lines = f.readlines()
    print(lines.__sizeof__())


# In[4]:


with open('refFlat.txt') as f:
    line_num = 1 #表示の都合上１０行だけ出力していますが、コメントをつけている行（コメントアウト）を除けば全て表示できます。
    for line in f:
        print(line.__sizeof__())
        
        line_num += 1 #全て出力する場合不要
        if line_num > 10: #全て出力する場合不要
            break #全て出力する場合不要 


# `readlines( )`を使用しない方が、一時的なメモリ使用量を少なく抑えられています。  
# 解析環境やデータサイズを考慮して使い分けましょう。  
# 

# ---
# 
# 通常は見えませんが、ファイルには行末に改行コードという文字が存在しています。  
# これが残っているとデータ処理に影響するので、この改行コードを`strip( )`メソッドを使って削除します。  
# 
# データを処理するため、取り出したデータを一列ごとに分割します。  
# 分割するためには`split( )`メソッドを使います。  
# カッコ内にどこで分割するかを指定します。  
# refFlat.txtはタブ区切りのファイルですので、カッコ内にタブを意味する`\t`を入力します。  
# 

# In[5]:


with open('refFlat.txt') as f:
    lines = f.readlines()
    line = lines[0].strip()
    cols = line.split('\t')
    print(cols)


# 読み込んだファイルの一行目`lines[0]`の改行コードを`stirp( )`で削除して`line`という変数に格納し、  
# `line`を`split(\t)`でタブで分割し、返されたリスト形式のデータを`cols`という変数に格納しました。  
# 
# `strip( )`と`split( )`は一行で書くこともできます。

# In[6]:


with open('refFlat.txt') as f:
    lines = f.readlines()
    cols = lines[0].strip().split('\t')
    print(cols)


# <br>
# 
# refFlatファイルの二列目はRefSeq IDです。  
# mRNAにはNM_から始まるIDが付けられています。  
# non-coding RNAにはNR_から始まるIDが付けられています。
# 次にmRANだけ取り出して表示させてみます。  
# 
# 特定の文字列を探したい場合は、`re`モジュールの`search( )`を使います。  
# 
# <br>
# 
# ```python
# re.search('探したい文字列', 対象の変数)
# ```
# 
# <br>
# 
# `re`モジュールをインポートしてから使います。

# In[7]:


import re
with open('refFlat.txt') as f:
    lines = f.readlines()
    for line in lines[:50]: #表示の都合上最初の５０行だけ処理していますが、for line in lines:で全て処理できます
        cols = line.strip().split('\t')
        if re.search('NM_', cols[1]):
            print(cols[1])


# refFlatファイルの一列目はgene symbolです。  
# gene symbolをキーに、RefSeq IDを値とする辞書を作成し、gene symbolとRefSeq IDを紐付けしましょう。  
# ほとんどの遺伝子には複数の転写産物が存在するので、一つのキーに対して複数の値を格納するため、辞書の値はリスト形式にしてみます。  

# In[8]:


genes = {} #空の辞書を作成
with open('refFlat.txt') as f:
    lines = f.readlines()
    for line in lines:
        cols = line.strip().split('\t')
        if re.search('NM_', cols[1]):
            genes.setdefault(cols[0], []) #値には空のリストを指定する
            genes[cols[0]].append(cols[1]) 

line_num = 0 #表示の都合上最初の１０キー分だけ出力していますが、以下のコメントをつけている行（コメントアウト）を除けば全て表示できます。
for symbol, refseqid_list in genes.items():
    refseqid = ','.join(refseqid_list)
    print(symbol, refseqid)
    
    line_num += 1 #全て出力する場合不要
    if line_num > 10: #全て出力する場合不要
        break #全て出力する場合不要


# 情報をファイルに出力して保存する場合も、`with`と`open`を使用します。  
# 出力する場合は、ファイルハンドルの後ろに出力方法を指定する必要があります。  
# 
# <br>
# 
# ```python
# with open(出力ファイルパス, '出力方法') as ファイルオブジェクト:
# ```
# 
# <br>
# 
# ファイルの新規作成は`w`を出力方法に指定します。  
# この場合、指定したファイル名が存在しない場合は、新たにファイルを作成してくれます。  
# また、すでに指定したファイル名が存在する場合は内容が上書きされます。  
# 
# `a`を指定すると、指定したファイルに追加書き込みを行います。  
# 
# `refFlat_out1.txt`というファイルに、gene symbolとRefSeq IDを出力します。

# In[9]:


genes = {} #空の辞書を作成
with open('refFlat.txt') as f:
    lines = f.readlines()
    for line in lines:
        cols = line.strip().split('\t')
        if re.search('NM_', cols[1]):
            genes.setdefault(cols[0], []) #値には空のリストを指定する
            genes[cols[0]].append(cols[1]) 

with open('refFlat_out1.txt', 'w') as out:
    for symbol, refseqid_list in genes.items():
        refseqid = ','.join(refseqid_list)
        print(symbol, refseqid, sep='\t', file=out)


# `refFlat_out1.txt`というファイルが作成されていますので、excel等で開いて中身を確認してみましょう。  
# 
# `print( )`のカッコ内に、`file=出力ファイルオブジェクト`で出力先を指定します。  
# `sep=`で、`print( )`内の出力内容の区切り方を指定します。  
# 今回は、gene symbolとRefSeq IDをタブで区切って出力したかったので、`sep='\t'`と記載しています。  
