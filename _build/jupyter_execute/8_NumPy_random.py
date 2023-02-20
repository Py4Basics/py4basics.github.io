#!/usr/bin/env python
# coding: utf-8

# # `Numpy`: ランダム変数

# <div name="html-admonition" style="font-size: 0.8em">
# <input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="Google translation" style="color:#ffffff;background-color:#008080; height:25px" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/> in English or the language of your choice.
# </div><br>

# In[1]:


import japanize_matplotlib
import numpy as np
import pandas as pd


# ## はじめに

# 1日の生活はランダムな事象の連続と考えることができる。今朝，目覚ましがなったかもしれないが，事後的に考えると，壊れて音が鳴らずに授業に遅刻する確率は全くの`0`では無かったはずだ。家を出て駅に向かって歩いていると急に雨が降って来るかもしれない。これも大気の状態によって確率的に起こっていると考えることができる。生活する上で，このようなランダムな事象について特に意識しないかもしれないが，毎日がその連続と考えることができる。同様に，個々の企業もランダムな事象に直面している（例えば，ライバル企業の新たな商品・サービスの発表）。また，株式市場を見れば分かるように，需要者と供給者からなる市場の均衡もそうである。更には，日本経済全体では大小様々なランダムな事象が発生していると考えることができる。大きなランダムな事象の例としては，極端な緩和政策を取り続ける日本銀行が急に金融引き締めに動くことが挙げられる。もしくは，急に（可能性は囁かれていた）ロシアがウクライナを侵略することによりインフレが発生し，景気後退の引き金になったのも確率的な事象と捉えることができる。即ち，経済を考える上で，ランダムな事象は無視できない要素だということであ。
# 
# このような問題意識に基づき，本章の目的は`NumPy`を使ったランダム変数の生成方法について簡単に解説することである。

# ## ランダム変数生成コード

# `NumPy`の`random`モジュールを使いランダム変数を生成するが，`random`モジュールの中でまず最初に使う必要があるのが`default_rng()`関数である。以下では続くコードを分かりやすくするために`default_rng()`を変数`rng`に割り当てる。

# In[2]:


rng = np.random.default_rng()


# `rng`はrandom number generatorの略であり，様々なランダム変数のための下準備となる。言い換えると，`rng`はランダム変数を生成するための「種」であり，この「種」に分布関数を指定することによりランダム変数が生成される。以下では正規分布と一様分布の使い方を例に説明する。

# ```{tip}
# ランダム変数の生成にはパッケージ`SciPy`の`stats`モジュールを使うこともできる。興味がある人は[このリンク](https://py4etrics.github.io/5_SciPy_stats.html)を参照しよう。
# ```

# ### 正規分布

# 正規分布に従うランダム変数の生成方法につて説明する。
# 
# **コード**
# 
# `rng.normal(loc=0, scale=1, size=1)`
# 
# * `loc`：平均（デフォルトは`0`）
# * `scale`：標準偏差（デフォルトは`1`）
# * `size`：ランダム変数の数（デフォルトは`1`）

# ここで、`.normal()`は`rng`のメソッドである。例として、平均`5`，標準偏差`2`の標準正規分布から`10`のランダム変数を生成しよう。

# In[3]:


rng.normal(5, 2, 10)


# 上のコードを実行する度に値が変化することが確認できるはずだ。
# 
# 標準正規分布から`5`のランダム変数を生成する場合は`loc`と`scale`を省略する。ただし２つ以上のランダム変数を生成する場合はキーワード引数`size=`が必ず必要となる。

# In[4]:


rng.normal(size=5)


# 標準正規分布に従う100,000個のランダムを生成しヒストグラムをカーネル密度制定をプロットしてみよう。

# In[5]:


# ランダム変数のDatFrame
df_norm = pd.DataFrame({'標準正規分布':rng.normal(size=100_000)})

# ヒストグラム
ax_ = df_norm.plot(kind='hist', bins=50, density=True)

# カーネル密度関数
df_norm.plot(kind='density',ax=ax_)

# 横軸の表示幅の設定
ax_.set_xlim(-4,4)
pass


# ### 一様分布

# 一様分布に従うランダム変数の生成方法につて考える。
# 
# **コード**
# 
# `rng.uniform(low=0, high=1, size=1)`
# 
# * `low`：最小値（デフォルト`0`）
# * `high`：最大値（デフォルト`1`）
# * `size`：ランダム変数の数（デフォルト`1`）
# 
# `.uniform()`も`rng`のメソッドである。最小値`5`，最大値`30`の一様分布から`10`のランダム変数を生成してみよう。

# In[6]:


rng.uniform(5, 30, 10)


# 最小値`0`，最大値`1`の一様分布から`5`のランダム変数を生成する。

# In[7]:


rng.uniform(size=5)


# $[0,1]$の一様分布に従う100,000個のランダムを生成しヒストグラムをカーネル密度制定をプロットしてみよう。

# In[8]:


# ランダム変数のDatFrame
df_uni = pd.DataFrame({'一様分布':rng.uniform(size=100_000)})

# ヒストグラム
ax_ = df_uni.plot(kind='hist', bins=50, density=True)

# カーネル密度関数
df_uni.plot(kind='density',ax=ax_)

# 横軸の表示幅の設定
ax_.set_xlim(-0.2,1.2)
pass


# ### 多変量正規分布

# 多変量正規分布に従うランダム変数の生成方法につて説明するが，例として２つの変数の場合を考える。
# 変数の数が$N>2$の場合は，引数の`mean`と`cov`を適宜変更すれば良い。
# 
# **コード**
# 
# `rng.multivariate_normal(mean, cov, size=1)`
# 
# * `mean`：平均
#     * 2変数の平均ののリストもしくは`array`
#     * 例１：`[0,5]`
#     * 例２：`np.array([0,5])`
# * `cov`：分散共分散行列
#     * 2次元のリストもしくは`array`
#     * 例１：`[[1,0.5],[0.5,1]]`
#     * 例１：`np.array([[1,0.5],[0.5,1]])`
# * `size`：ランダム変数の組数（デフォルトは`1`）

# ここで、`.multivariate_normal()`は`rng`のメソッドである。例として、平均は

# In[9]:


mean = [0, 5]


# 共分散`m`は

# In[10]:


m = 3


# 分散共分散は

# In[11]:


cov = [[5, m],
       [m, 10]]


# のランダム変数を`n`組

# In[12]:


n = 5


# 生成しよう。

# In[13]:


rng.multivariate_normal(mean, cov, size=n)


# 各列がランダム変数の値を示しており，行が２つのランダム変数の１組ということになる。
# 
# ２つのランダム変数を標準正規分布とするが，共分散は`m`のランダム変数を生成する場合も`mean`と`cov`は省略できない。

# In[14]:


mean = [0, 0]
m = 0.8
cov = [[1, m],
       [m, 1]]

rng.multivariate_normal(mean, cov, size=5)


# 上の平均と分散共分散の２変量正規分布に従う1000個のランダムを生成し散布図をプロットしてみよう。

# In[15]:


# ランダム変数の生成
vals = rng.multivariate_normal(mean, cov, size=1_000)

# DatFrameの作成，列ラベルをXとY
df_2norm = pd.DataFrame(vals, columns=['X','Y'])

# 散布図
df_2norm.plot('X', 'Y', kind='scatter', alpha=0.5)
pass


# `X`と`Y`の共分散は`m=0.8`となっているため，正の相関が観測される。
# 相関係数を計算してみよう。

# In[16]:


df_2norm.corr().iloc[0,1]


# ## 古い書き方

# 上で説明した`np.random.default_rng()`を使うコードが現在推奨されている書き方となるが，この書き方が導入される前の書き方を紹介する。現時点でも古い書き方を使うことができるが，ランダム変数の統計学的特徴という観点からは推奨されるコードの書き方の方が良いとされる。
# 
# コードの違いを説明するために，標準正規分布のランダム変数を１つ生成するコードを考えてみよう。
# `NumPy`をインポートするコードも含めると，上では次のように書いた。
# ```
# import numpy as np
# rng = np.random.default_rng()
# rng.normal()
# ```
# 最後の２行を１行にまとめて書くこともできる。
# ```
# import numpy as np
# np.random.default_rng().normal()
# ```
# 実際に実行してみよう。

# In[17]:


np.random.default_rng().normal()


# 古い書き方では書き方では次のようになる。
# ```
# import numpy as np
# np.random.normal()
# ```
# 実際に実行してみよう。

# In[18]:


np.random.normal()


# ２つを比べると，推奨される書き方には`.default_rng()`が追加されていることが分かる。
# その部分が「より良い統計学的特徴」を発生させるコードとなる。
# 
# 次の表にまとめることができる（インポートの行は省く）。

# ```{div} full-width
# 
# ||推奨コード   | 古い書き方 |
# |:----|:----------|:-------------------------------------|
# |平均1<br>標準偏差5の<br>正規分布| np.random.default_rng().normal(1,5,size=10) | np.random.normal(1,5,size=10) |
# |最小値1<br>最大値5の<br>一様分布| np.random.default_rng().uniform(1,5,size=10) | np.random.uniform(1,5,size=10) |
# |平均`mean`<br>分散共分散`cov`の<br>多変量正規分布| np.random.default_rng().multivariate_normal(mean,cov,size=n) | np.random.multivariate_normal(mean,cov,size=n) |
# 
# ```
