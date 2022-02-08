#!/usr/bin/env python
# coding: utf-8

# # 移動平均

# In[1]:


import numpy as np
import pandas as pd
import py4macro


# ## はじめに

# ```{margin}
# <div name="html-admonition">
# Do you want to read in a differnt language? Start
# <input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="Google" style="color:#ffffff;background-color:#008080;" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/><input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="translation" style="color:#ffffff;background-color:#008080;" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/>
# in English or the language of your choice.
# </div>
# ```

# [インフレ率とマネーストックの増加率](https://py4macro.github.io/11_Macro_Variables.html#id11)では，インフレ率とマネーストックの増加率の長期的な関係について考察し，`resample`を使い分析を進めた。ここでは移動平均を使い，同様なデータ整形ができることを説明する。また，移動平均は季節調整やトレンド抽出にも使えることも覚えておこう。

# ## 移動平均とは

# 次の`DataFrame`（変数名は`df_ex`）を使って移動平均について説明する。

# In[2]:


month_list = [f'{i}月' for i in range(1,13)]
df_ex = pd.DataFrame({'月':month_list,'A':range(10,130,10)})
df_ex['B'] = df_ex['A'].rolling(3).mean()
df_ex['C'] = df_ex['B'].iloc[2::3]


# In[3]:


df_ex


# 列`A`には10から120までの数字が並んでおり，それぞれを1月から12月までの値と考えてみよう。１四半期には3ヶ月あるので，第１四半期は列0〜2となる。この３行をここではwindowと呼ぶ。最初のwindowの平均は`20.0`であり，それが列`B`の2番目の行に入っている。次にwindowを1行下げると，2〜4月をカバーすることになり，その平均は`30.0`となり，列`B`の3番目の行の値となっている。同じように，windowを1行下げると，3〜6月に移り，その平均`40.0`は列`B`の4番目の値になっている。更にwindowを１行ずらすと第２四半期の4〜6月となり，平均`50.0`は列`B`の5番目に入っている。この計算を最後まで続けると列`B`が埋まる事になり，これが移動平均である。列`A`から列`B`を作るには`df_ex`のメソッド`.rolling()`と`.mean()`を結合させて次のように使う。
# ```
# df_ex['A'].rolling(window=3).mean()
# ```
# 引数`window`が上の説明にあるwindowの数を指定している。`.rolling`はwindowが下に動いていることをイメージすれば良いだろうし，windowごとに何らかの計算を可能にするメソッドである。
# 
# ```{tip}
# 平均を計算するために`.mean()`を使ったが，`.rolling()`には他のメソッドもある。例えば，
# * `.rolling(3).sum()`：`window`の合計を返す。
# * `.rolling(3).max()`：`window`の最大値を返す
# * `.rolling(3).min()`：`window`の最小値を返す
# * `.rolling(3).median()`：`window`の中央値を返す
# ```
# 
# 実際に`df_ex`の列`A`の移動平均を作成してみよう。

# In[4]:


df_ex.loc[:,'A'].rolling(3).mean()


# このコードでは`window=`を省いている。`df_ex`の列`B`と同じであることが分かる。以上が移動平均の計算方法である。
# 
# ````{note}
# 列`B`の0番目と1番目の行に`NaN`が入っており，移動平均には欠損値が必ず発生することになる。一方で`NaN`の位置を変えるために，`.rolling()`には引数`center=True`が用意されている。
# ```
# df_ex.rolling(3, center=True).mean()
# ```
# 上の例では１四半期の平均値は四半期の最後の月に該当する行に入っているが，この`center=True`を使うと平均値は真ん中の月に該当する行に入り（例えば，第１四半期の平均は1番目の行に入る），`NaN`は0番目と最後の行に入ることになる。
# ````

# ## 四半期・年次・３年次データの作成方法

# 次に，[インフレ率とマネーストックの増加率](https://py4macro.github.io/11_Macro_Variables.html#id11)で計算した四半期，年次，3年次データの作成方法を説明する。
# 
# `df_ex`の列`C`は四半期の平均だけを抜き取りその他は`NaN`になっている。月次データを四半期データに変換するには，`NaN`が含まれない列`C`を作成すれば良い。即ち，列`B`から該当する行だけを抽出すれば良いことになる。そのために[Pandasの章](https://py4basics.github.io/3_Pandas.html#id3)で説明した`.iloc[]`を使う。`.iloc`は`DataFrame`や`Series`の行インデックを使い要素を抽出するメソッドであるが，スライシングの場合は次のように指定することになる。
# ```
# .iloc[row_start:row_end:row_step, col_start:col_end:col_step]
# ```
# * `row_start`：スライスする最初の行番号
# * `row_end`：スライスする最後の行番号の次の番号
# * `row_step`：何行ごとに抽出するかを指定する
#     * `1`は「１行ごと」で全ての行という意味。デフォルトなので`:1`は省略可能。
#     * `2`は「２行ごと」で１行飛ばしという意味。
#     * `3`は「３行ごと」で２行飛ばしという意味。
#     * 一般的に$n\geq1$は「$n$行ごと」で$n-1$行飛ばしという意味。
#     * `-1`は1と同じだが逆の順番から抽出する。
# * `col_start`：スライスする最初の列番号
# * `col_end`：スライスする最後の列番号の次の番号
# * `col_step`：何列ごとに抽出するかを指定する
#     * `1`は「１列ごと」で全ての列という意味。デフォルトなので`:1`は省略可能。
#     * `2`は「２行ごと」で１列飛ばしという意味。
#     * `3`は「３行ごと」で２列飛ばしという意味。
#     * 一般的に$n\geq1$は「$n$列ごと」で$n-1$列飛ばしという意味。
#     * `-1`は`1`と同じだが逆の順番から抽出する。

# 例えば，次のコードでは2番目の行から10番目の行の全ての列を抽出しており，`:row_step`は省いているので`row_step=1`と設定されている。
# ```
# .iloc[2:11,:]
# ```
# 一方，次のコードは2番目の行から10番目の行を２行ごと（(2-1=)1行飛ばしで）抽出することになる。
# ```
# .iloc[2:11:2,:]
# ```
# `df_ex`に戻ろう。四半期の平均は列`B`の2番目，5番目，8番目，11番目の行であり，それらを抽出するには
# ```
# .iloc[2::3,:]
# ```
# となる。`row_start=2`の`2`は第１四半期の平均がある行を指しており，そこからスタートとなる。`row_step=3`の`3`は３行ごとに四半期の平均があるので，その3を表している。従って，月次データを四半期データに変換するには
# ```
# df_ex['A'].rolling(3).mean().iloc[2::3]
# ```
# 実際に実行してみよう。`df_ex['A'].rolling(3).mean()`は`Series`を返すので`.iloc[2::3]`となっている。

# In[5]:


df_ex['A'].rolling(3).mean().iloc[2::3]


# 同様に，月次データを年次データに変換する場合は
# ```
# .rolling(12).mean().iloc[11::12]
# ```
# となり，3年期データに変換する場合は
# ```
# .rolling(36).mean().iloc[35::36]
# ```
# となる。

# 列`C`の`NaN`以外の値と同じであることが確認できる。

# ## 実際のデータを使って

# では実際に`jpn-money`のデータを使いデータを整形しよう。まず月次データを読み込み`month`に割り当てる。

# In[6]:


month = py4macro.data('jpn-money')
month.tail()


# いつもの通り`.info()`を使ってデータの内容を確認しよう。

# In[7]:


month.info()


# 行ラベルが`DatetimeIndex`となっており，時系列データ用に設定されていることが分かる。
# 
# 四半期データに変換して変数`quarter`に割り当てることにする。

# In[8]:


quarter = month.rolling(3).mean().iloc[2::3,:]


# これで３ヶ月の値の平均からなる四半期データを作成した事になる。確かめてみよう。

# In[9]:


quarter.head()


# 四半期の最後の日が行ラベルになっていることが分かる。同様に，年次データと3年期データを作成する。

# In[10]:


annual= month.rolling(12).mean().iloc[11::12,:]
annual.head()


# In[11]:


annual3= month.rolling(36).mean().iloc[35::36,:]
annual3.head()


# ここで作成した`quarter`，`annual`，`annual3`は，[インフレ率とマネーストックの増加率](https://py4macro.github.io/11_Macro_Variables.html#id11)の同じ変数名の`DataFrame`と同じである。
