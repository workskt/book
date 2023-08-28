#!/usr/bin/env python
# coding: utf-8

# # 関数一覧  
# 
# ---
# 
# ### ターミナルからの入力を受け取る  
# 
# `sys`モジュール `argv( )`関数
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
# `subprocess`モジュール `run( )`関数  
# 
# ```python
# import subprocess
# subprocess.run(['mkdir', 'new_dir'])
# ```
# <br>
# 
# 実行するコマンドはリスト形式で与える。
# 
# `shell=True`を使うと、文字列でコマンドを与えることができる。変数がない場合はこちらでもよい。  
# 
# ```python
# import subprocess
# subprocess.run(['mkdir new_dir'], shell=True)
# ```
# 
# ---
# 
# ### ファイルパスを取得する
# 
# `glob`モジュール `glob( )`関数  
# 
# ```python
# import glob
# filelist = glob.glob('directory/*.txt')
# ```
# <br>
# 
# リストとして取得できる。  
# `glob( )`では、ワイルドカードは`*`を使う。  
# 正規表現とは異なるので注意。  
# 
# ---
# 
# ### 中央値、最頻値を計算  
# 
# ライブラリ`statistics`を使用  
# 
# ```python
# import statistics
# 
# v = [1, 2, 3, 3, 4, 5, 5, 6]
# print(statistics.mode(v)) #最頻値
# print(statistics.median(v)) #中央値
# print(statistics.stdev(v)) #標準偏差
# print(statistics.variance(v)) #不偏分散
# ```
# 

# In[ ]:




