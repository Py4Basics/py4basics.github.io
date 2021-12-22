#!/usr/bin/env python
# coding: utf-8

# (chap:pandas)=
# # `Pandas`：データ分析

# In[1]:


import pandas as pd
import numpy as np
from see import see


# ## 説明

# In[ ]:





# `Pandas`はデータを扱う上で欠かせないパッケージであり，エクセルをイメージすれば良いだろう。`Pandas`にはスプレッド・シートに対応する`DataFrame`（データ・フレーム）と`Series`（シリーズ）呼ばれるオブジェクトがあり，それらを駆使してデータ分析をおこなう。
# 
# データ・フレームは下の図のようになっている。`X`，`Y`，`Z`は「列ラベル」（アルファベットや記号など）であり、一番左の`1`，`2`，`3`は「行インデックス」（数字）である（「行ラベル」（アルファベットや記号など）を設定することも可能）。その他の数字がデータとなっている。

# ```{margin}
# <div name="html-admonition">
# Do you want to read in a differnt language? Open the 
# <input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="Google translated version" style="color:#ffffff;background-color:#008080;" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/>
# in English or the language of your choice.
# </div>
# ```

# |   | X  | Y    | Z   |
# |---|----|------|-----|
# | 0 | 10 |  5.0 | 3.0 |
# | 1 | 20 | 30.0 | 2.0 |
# | 2 | 30 | 15.0 | 5.0 |
# 
# `X`のデータはその列にある数字`10`，`20`，`30`であり，`Y`と`Z`も同様に同じ列にあるデータから構成される。`Series`は１つの列からなるスプレッド・シートと考えれば良いだろう。
# 
# この特徴により複雑なデータでも扱いが簡単になる。例えば，`NumPy`を使うと目的のデータがどこにあるのかは，何番目の行で何番目の列なのかを把握する必要があるが，`Pandas`では行・列にラベルを使うことにより（例えば，行「1980年」の列「GDP」のようにデータを特定することが可能となる），データの操作が非常に簡単になる。また，`Pandas`は`NumPy`に基づいているため，ベクトル演算の機能が使える。
# 
# ここで説明できない他の使い方については[このサイト](https://github.com/ysdyt/pandas_tutorial)と[このサイト](https://note.nkmk.me/python-pandas-post-summary/)が参考になる。
# 
# 通常`pd`という名前で読み込む。
# ```
# import pandas as pd
# ```

# ## データの読み込みとデータのチェック

# (sec:3-data)=
# ## データの読み込みとデータのチェック

# 様々なデータを読み込むことが可能だが，ここでは`read_csv()`関数を使ってインターネット上の`.csv`ファイルを読み込む。

# In[2]:


# url の設定
url = 'https://raw.githubusercontent.com/Haruyama-KobeU/Py4Basics/master/data/data1.csv'

# 読み込み
df = pd.read_csv(url)


# `df`全体を表示させる。

# In[3]:


df


# 行はインデックス（番号）になっており，そのまま使っても全く問題ない。ここでは列`year`を行ラベルに設定して`Pandas`の使い方について説明することにする。
# 
# * `set_index()`：選択された列を行ラベルにするメソッド

# In[4]:


df = df.set_index('year')
df


# ```{tip}
# * `df.set_index('year')`は直接`df`に影響を与えない。単に，書き換えるとどうなるかを表示している。ここでは`df`に再度割り当てることにより`df`自体を上書きしている。
# * 出力にある`NaN`（Not a Number）は欠損値を示す。
# * 行ラベルに`year`という列名が残るが，それを消すにはメソッド`.rename_axis('')`を使う。ここで`''`は空の文字列である。`.rename_axis(None)`でも同じ結果となる。
# ```

# 行数が大きい場合（例えば，10000），全てを表示してもあまり意味がない。そこでよく使うメソッドに最初や最後の数行だけを表示すものがある。
# 
# `df`の最初の５行を表示させる。

# In[5]:


df.head()


# 引数に2を指定すると最初の3行のみ表示される。

# In[6]:


df.head(2)


# 最後の5行を表示させる。引数に整数を入れて表示行数を指定することも可能。

# In[7]:


df.tail()


# `df`の情報を確認する。

# In[8]:


df.info()


# **説明**：
# * `<class 'pandas.core.frame.DataFrame'>`
#     * クラス名
#     * `type(1)`とすると`int`というデータ型が表示するが，これはクラス名でもある。`print(type(1))`とすると`<class 'int'>`と表示される。
# * `Int64Index: 11 entries, 2000 to 2010`
#     * 行のインデックスの情報
#     * データ型は`Int64`(整数）（データ型には`64`や`32`という数字がついている場合がある。それらは数字をコンピュータのメモリに記憶させる際，何ビット必要かを示している。より重要なのは`Int`（整数）の部分である。）
#     * 11個のデータで2000から2010
# * `Data columns (total 5 columns):`
#     * データ列の数（5つ）
# * `gdp  11 non-null int64`
#     * データ型は`int64`
#     * 11のデータがあり，欠損値なし（`non-null`とは欠損値ではないデータ）
# * `inv  10 non-null float64`
#     * データ型は`float64`
#     * 10のデータがあり，欠損値数は1（＝11-10）
# * `con  9 non-null float64`
#     * データ型は`float64`
#     * 9のデータがあり，欠損値数は2（＝11-9）
# * `pop  11 non-null int64`
#     * データ型は`int64`
#     * 11のデータがあり，欠損値数なし
# * `id   11 non-null object`
#     * データ型は`object`（文字列などの場合）
#     * 11のデータがあり，欠損値数なし
# * `dtypes: float64(2), int64(2), object(1)`
#     * `df`の列にどのようなのデータ型かを示す
#     * `float64`と`int64`が2列つずつ，文字列は１列
# * `memory usage: 528.0+ bytes`
#     * メモリー使用量は約528.0バイト
# 
# データを読み込んだら必ず`info()`を使って欠損値の数や列のデータ型を確認すること。
# 
# また，データの統計的な特徴は次のメソッドでチェックできる。

# In[9]:


df.describe()


# * `count`：観測値の数
# * `mean`：平均
# * `std`：標準偏差
# * `min`：最小値
# * `max`：最大値
# * `25%`：第１四分位数
# * `50%`：第２四分位数（中央値）
# * `75%`：第３四分位数
# * `max`：最大値
# 
# 
# 次のデータ属性を使って`df`の行と列の長さを確認することができる。返値はタプルで，`(行の数，列の数)`と解釈する。

# In[10]:


df.shape


# 返値はタプルなので，行数は以下で取得できる。

# In[11]:


df.shape[0]


# 以下でも行数を示すことができる。

# In[12]:


len(df)


# ## `DataFrame`の構成要素

# `DataFrame`には様々な属性があるが，ここでは以下の３点について説明する。
# 
# * データ：`df.to_numpy()`もしくは`df.values`で抽出できる。
# * 列ラベル：`df.columns`で抽出できる。
# * 行ラベル：`df.index`で抽出できる。
# 
# まずデータ自体を抽出する。

# In[13]:


df.to_numpy()


# In[14]:


type(df.to_numpy())


# これで分かることは，メインのデータの部分は`NumPy`の`ndarray`（`n`次元`array`）であることが分かる。即ち，`Pandas`は`NumPy`に基づいて構築されており，データ値の計算などは`array`が裏で動いているということである。また行と列のラベルを追加し，より直感的に使えるように拡張しているのである。

# 次に列ラベルを取り出してみる。

# In[15]:


df.columns


# `dtype='object'`から列ラベルに使われているデータ型（`dtype`）はオブジェクト型（`object`）だとわかる。
# 
# * オブジェクト型とは文字型を含む「その他」のデータ型と理解すれば良いだろう。
# * `dtype='object'`と`dtype=object`は同じ意味。
# 
# 列ラベル自体のクラスは次のコードで調べることができる。

# In[16]:


type(df.columns)


# `dir()`もしくは`see()`で調べると多くのメソッドや属性が確認できるが，その中に`.tolist()`が含まれており，これを使うことにより列ラベルをリストに変換することができる。

# In[17]:


df_columns = df.columns.tolist()
df_columns


# 行ラベルについても同じことができる。

# In[18]:


df.index


# 行ラベルのデータ型`dtype`は整数である`int64`。列`year`を行ラベルに指定したため，`name='year'`はその列ラベルを表示している。行ラベルのデータ型（クラス）は

# In[19]:


type(df.index)


# であり，ラベルをリストとして抽出することもできる。

# In[20]:


df_index = df.index.tolist()
df_index


# ## 要素の抽出

# `NumPy`の`array`の場合，`[,]`を使い要素を抽出した。`Pandas`の場合，様々な抽出方法があるが，覚えやすく少しでも間違いの可能性を減らすために，そして可読性向上のために`array`に対応する以下の２つの方法を使うことにする。
# 
# * ラベルを使う方法：`.loc[,]`
# * インデックスを使う方法：`.iloc[,]`（これは`array`の`[ ]`と同じと考えて良い）
# 
# １つ目の`loc`はラベルのlocationと覚えよう。２つ目はの`iloc`の`i`はインデックス（index）の`i`であり，index locationという意味である。使い方は`array`の場合と基本的に同じである。
# 
# * `,`の左は行，右は列を表す。
# * 行または列を連続して選択する（slicing）場合は`:`を使う。（`start:end`）
#     * `:`の左右を省略する場合は，「全て」という意味になる。
#     * `:`の左を省略すると「最初から」という意味になる。
#     * `:`の右を省略すると「最後まで」という意味になる。
#     * `.loc[,]`の場合，`end`を含む。（要注意！）
#     * `.iloc[,]`の場合，`end`は含まず，その１つ前のインデックスまでが含まれる。
# * `,`の右に書く`:`は省略可能であるが省略しないことを推奨する。
# 
# 「特例」として`.loc[,]`と`.iloc[,]`以外に
# * ラベルと`[]`だけを使い**列**を選択する方法
# 
# も説明する。

# ```{warning}
# * `.loc[,]`の場合，`end`を含む。（要注意！）
# * `.iloc[,]`の場合，`end`は含まず，その１つ前のインデックスまでが含まれる。
# ```

# ### `.loc[,]`（ラベル使用）

# **１つの行を`Series`として抽出**

# In[21]:


df.loc[2005,:]


# **１つの行を`DataFrame`として抽出**

# In[22]:


df.loc[[2005],:]


# **複数行を抽出**

# In[23]:


df.loc[[2005, 2010],:]


# **複数行を連続抽出（slicing）**

# In[24]:


df.loc[2005:2008,:]


# **１つの列を`Series`として抽出**

# In[25]:


df.loc[:,'gdp']


# **複数列を抽出**

# In[26]:


df.loc[:,['gdp','pop']]


# **複数列を連続抽出（slicing）**

# In[27]:


df.loc[:,'inv':'pop']


# ### `.iloc[]`（インデックス使用）

# (sec:3-iloc)=
# ### `.iloc[]`（インデックス使用）

# **１つの行を`Series`として抽出**

# In[28]:


df.iloc[1,:]


# **複数行を抽出**

# In[29]:


df.iloc[[1,4],:]


# **複数行を連続抽出（slicing）**

# In[30]:


df.iloc[1:4,:]


# **１つの列を`Series`として抽出**

# In[31]:


df.iloc[:,1]


# **１つの列を`DataFrame`として抽出**

# In[32]:


df.iloc[:,[1]]


# **複数列を選択**

# In[33]:


df.iloc[:,[1,3]]


# **複数列を連続抽出（slicing）**

# In[34]:


df.iloc[:,1:3]


# ### `[]`で列の選択（ラベル使用）

# **１つの列を`Series`として抽出**

# In[35]:


df['gdp']


# **１つの列を`DataFrame`として抽出**

# In[36]:


df[['gdp']]


# **複数列を選択**

# In[37]:


df[['gdp','pop']]


# ## ある条件の下で行の抽出

# ### １つの条件の場合

# #### 例１：GDPが100未満の行の抽出

# まず条件を作る。

# In[38]:


df['gdp'] < 100


# この条件では，GDPが100未満の行は`True`，以上の行は`False`となる。この条件を`cond`というの変数に割り当てる。`()`を省いても良いが，ある方が分かりやすいだろう。

# In[39]:


cond = (df['gdp'] < 100)


# `cond`を`.loc[,]`の引数とすることにより，`True`の行だけを抽出できる。（注意：`cond`を使って**行**を抽出しようとしているので`,`の左側に書く。）

# In[40]:


df.loc[cond,:]


# この条件の下で$inv$だけを抽出したい場合
# 
# * `df.loc[cond,'inv']`
# 
# とする。

# ```{warning}
# 以下のように抽出を連続ですることも可能だが，避けるように！
# * `df.loc[cond,:]['inv']`
# * `df.loc[cond,:].loc[:,'inv']`
# ```

# #### 例２：`id`が`a`の行を抽出

# In[41]:


cond = (df.loc[:,'id'] == 'a')
df.loc[cond,:]


# ### 複数条件の場合

# #### 例３

# 以下の条件の**両方**が満たされる場合：
# 
# * `gdp`が100以上
# * `inv`が30以下
# 
# それぞれの条件を作成する。

# In[42]:


cond1 = (df['gdp'] >= 100)
cond2 = (df['inv'] <= 30)


# ２つの条件が同時に満たされる条件を作成する。

# In[43]:


cond = (cond1 & cond2)


# `cond`を引数に使い行を抽出する。

# In[44]:


df.loc[cond, :]


# #### 例４

# 以下の条件の**どちらか**が満たされる場合：
# * `gdp`は200以上
# * `con`は60以下

# In[45]:


cond1 = (df['gdp'] >= 200)
cond2 = (df['con'] <= 60)
cond = (cond1 | cond2)

df.loc[cond, :]


# #### 例５

# 以下の条件の**どちらか**が満たされ
# * `gdp`は200以上
# * `con`は60以下
# 
# かつ以下の条件も**同時に**満たされる場合：
# * `id`が`a`と等しい

# In[46]:


cond1 = (df['gdp'] >= 200)
cond2 = (df['con'] <= 60)
cond3 = (df['id'] == 'a')
cond = ((cond1 | cond2) & cond3)

df.loc[cond, :]


# ### `query()`

# `query()`というメソッドでは文字列を使い行の抽出コードを書くことができる。これにより直感的なコード書くことが可能である。

# #### 例１の場合：

# In[47]:


df.query('gdp < 100')


# #### 例２の場合

# In[48]:


df.query('id == "a"')


# #### 例３の場合

# In[49]:


df.query('(gdp >= 100) & (inv <= 30)')


# #### 例４の場合

# In[50]:


df.query('(gdp >= 200) | (con <= 60)')


# #### 例５の場合

# In[51]:


df.query('(gdp >= 200 | con <= 60) & (id == "a")')


# ````{tip}
# `df`にない変数で条件を設定する場合`@`が必要になる。例えば，変数`z`という変数があるとしよう。
# 
# ```python
# z = 100
# ```
# 
# 変数`z`の値に基づいて行の抽出をする場合は次のようにする。
# 
# ```python
# df.query('gdp < @z')
# ```
# 
# {glue:}`glue0_txt`
# ````

# In[52]:


from myst_nb import glue
z = 100
glue0 = df.query('gdp < @z')
glue("glue0_txt", glue0)


# ```{warning}
# 数字で始まる列ラベルに`.query()`を使うとエラーが発生するため，列ラベルを変更する必要がある。列ラベルを変更できない場合は異なる方法を使うように。
# ```

# ## 列と行の追加と削除

# ### 列の追加 `[ ]`

# `[]`に列ラベルを使って列を抽出することができるが，`[]`は列の追加にも使えるので，ここではその使い方を説明する。まず，全ての行が`1.0`となる列を作成するとしよう。その場合，以下のようにする。

# In[53]:


df['Intercept'] = 1.0


# In[54]:


df.head(2)


# 次の例では既存の列から新たな列を作成する。まず１人当たりGDPの計算を計算し，それを変数`gdp_pc`に割り当てる。

# In[55]:


gdp_pc = df['gdp']/df['pop']
gdp_pc.head()


# これは`Series`であり，`GDPpc`として`df`に追加する。

# In[56]:


df['gdp_pc'] = gdp_pc


# In[57]:


df.head(2)


# ### 列の追加 `.loc[,]`

# `.loc[]`は行と列の抽出に使ったが，追加にも使える。`[]`と同じと考えれば良い。次の例では`pop`を2倍した列を追加している。

# In[58]:


df.loc[:,'2pop'] = 2*df['pop']


# ### 列の削除 `[ ]`

# In[59]:


del df['2pop']


# ### 列の削除 `drop()`

# `DataFrame`には`.drop()`というメソッドが用意されているので，それを使うことも可能である。
# 
# 下のコードの説明：
# * オプション`axis=`の値を`columns`の代わりに`１`でも可
# * コピーを作るだけなので，元のdfを書き換えたい場合は以下のどちらかが必要
#     * `df`に代入する
#     * オプション`inplace=True`（デフォルトは`False`）を追加する。

# In[60]:


df = df.drop(['Intercept','gdp_pc'], axis='columns')

# df.drop('Intercept', axis='columns', inplace=True)


# ### 行の追加 `.loc[,]`

# 行と列の抽出，そして列の追加に使ったが，行の追加にも使える。

# In[61]:


df.loc[2011,:] = [215, 100, 115, 22, 'b']


# In[62]:


df.tail(3)


# 上の例では，最初の4つの要素は整数として入力されたが，`df`の中では浮動小数点に変換されている。

# ### 行の削除 `drop()`

# これは列を削除する際に紹介したメソッド`.drop()`である。
# 
# * オプション`axis=`の値を`rows`の代わりに`0`でも可
# * コピーを作るだけなので，元のdfを書き換えたい場合は以下のどちらかが必要
#     * `df`に代入する
#     * オプション`inplace=True`（デフォルトは`False`）を追加する。

# In[63]:


df = df.drop(2011, axis='rows')

# df.drop(2011, axis=0, inplace=True)


# ## 欠損値の扱い

# `Pandas`では欠損値は`NaN`と表示されるが，`na`もしくは`null`と呼んだりもする。

# ### 欠損値の確認

# 欠損値があるかどうかの確認は，`df.info()`でもできるが，以下のメソッドを組み合わせることでも可能である。
# 
# * `isna()`：それぞれの要素について`NaN`の場合`True`を，そうでない場合は`False`を返す。（`DataFrame`の全ての要素が`True/False`となる。）
# * `sum()`：`df`の上から下に**行**（rows）を縦断して，それぞれの列の中にある`True`数える。
#     * デフォルトで引数`axis='rows'`が指定されている。
#     * 引数値`rows`は複数！（`0`でも可）
# * `sum(axis='columns')`：`df`の左から右に**列**（columns）を横断して，それぞれの行の中にある`True`を数える。
#     * 引数値`columns`は複数！（`1`でも可）
#     
# （注意）`sum()`の`axis`は「行を縦断」か「列を横断」かを指定する。

# In[64]:


df.isna().sum()


# `inv`と`con`に`NaN`があることがわかる。`axis='columns'`を設定すると`NaN`がある行を確認できる。

# In[65]:


df.isna().sum(axis='columns')


# ---
# `NaN`がある行だけを抽出したい場合がある。その場合はメソッド`any()`が役に立つ。
# 
# * `any()`：`df`の上から下に行（`rows`）を縦断して，それぞれの列の中で一つ以上`True`がある場合には`True`を，一つもない場合は`False`を返す。
#     * デフォルトで引数`axis='rows'`が指定されている。
#     * 引数値`rows`は複数！（`0`でも可）
# * `any(axis='columns')`：dfの左から右に列（`columns`）を横断して，それぞれの行の中で一つ以上`True`がある場合には`True`を，一つもない場合は`False`を返す。
#     * 引数値`columns`は複数！（1でも可）
# 
# （注意）`any()`の`axis`は「行を縦断」か「列を横断」かを指定する。

# In[66]:


cond = df.isna().any(axis='columns')
df.loc[cond,:]


# これで`NaN`がある行を抽出することができる。

# ### 欠損値がある行の削除

# 欠損値がある全ての行を削除する。

# In[67]:


df.dropna()


# このメソッドは，欠損値を削除するとどうなるかを示すだけであり`df`自体は影響は受けない。`df`自体から`NaN`がある行を削除する場合は`inplace=True`のオプション（デフォルトでは`False`になっている）を加えて
# ```
# df.dropna(inplace=True)
# ```
# とするか，削除後の`df`を`df`自体に再割り当てする。
# ```
# df = df.dropna()
# ```

# また，ある列で`NaN`がある行のみを削除する場合は，引数`subset`を使う。

# In[68]:


df.dropna(subset=['inv'])


# （注意）オプション`subset=`には削除する列が１つであってもリスト`[]`で指定する。

# ## 並び替え

# `df`を`gdp`の昇順に並び替える。

# In[69]:


df.sort_values('gdp').head()


# 降順の場合

# In[70]:


df.sort_values('gdp', ascending=False).head()


# 複数の列を指定する場合

# In[71]:


df.sort_values(['id','gdp'], ascending=['True','False']).head()


# ここでは`id`に従って先に並び替えられ，その後に`gdp`に従って並び替えられている。`ascending`は昇順（`True`）か降順（`False`）かを指定する引数であり，`['id','gdp']`と`ascending=['True','False']`の順番が対応している。

# ## 行インデックスと列ラベル

# ### インデックスを振り直す

# [](sec:3-data)でデータを読み込んだ後，直ぐに`.set_index('year')`を使い，列`year`を行ラベルに設定した。もちろん，必ずしもそうする必要はなく，行インデックス（`0`，`1`，`2`，...）のままで作業をおこなっても全く問題ない。また行ラベルを設定した後に，行インデックスに戻したい場合もあるだろう。その場合には，メソッド`.reset_index()`を使うと，行のインデックスを0,1,2,..と振り直すことができる。`df`を使うと次のようになる。

# In[72]:


df.reset_index()


# ここでは行のインデックスが`year`として新たな列として追加されているが、`reset_index()`に引数`drop=True`を加えると，列`year`が自動的に削除されることになる。

# In[73]:


df.reset_index(drop=True).head()


# ### 列のラベルの変更

# メソッド`.rename()`を使い列のラベルを変更する。引数は次の形で設定する。
# 
# $$\text{.rename}\left(\text{columns=}辞書\right)$$
# 
# ここで「辞書」は次のルールで指定する。
# * `key`:元のラベル
# * `value`：新しいラベル
# 
# 下のコードでは，`df`の`pop`を`pop_new`に，`id`を`id_new`に変更している。

# In[74]:


df.rename(columns={'pop':'pop_new','id':'id_new'}).head()


# ただし，再割り当てしないと`df`は変更されないので注意しよう。即ち，上のコードでは`df`の行ラベルは変更されていない。
# 
# `.rename()`以外にも次のように変更することも可能である。

# In[75]:


df.columns = ['gdp','inv','con','pop_new','id']


# このコードは
# > 右辺の文字列のリストを`df.columns`に割り当てる
# 
# と読むことができる。実際このコードにより割り当てが完了し，`df`は変更されることになる。`df`を表示してみよう。

# In[76]:


df.head(2)


# さらにもう一つ注意点がある。全ての列ラベルをリストとして準備する必要がある点である。列の数が多いと面倒なので，そういう場合は`.rename()`の方が使いやすいだろう。

# ## よく使うのメソッド

# `DataFrame`には様々なメソッドが用意されており，ここでは頻繁に用いるメソッド幾つか紹介しよう。

# ### 統計関連のメソッド

# 上でも出てきたが`.sum()`は各列の合計を返す（`axis='rows'`がデフォルト）。その際，欠損値は無視される。注意する点は合計を計算して意味のある列のみを選択することである。

# In[77]:


df.iloc[:,:-1].sum()


# 各行の合計を計算したい場合は引数`axis=1`もしくは`axis='columns'`を指定する。ここで`columns`となるのは列を横断すると覚えれば良いだろう。古い`Pandas`のバージョンでは自動で文字列を無視していたが，より新しいバージョンでは合計できる列だけを選択する必要がある。

# In[78]:


df.iloc[:,:-1].sum(axis='columns')


# 同じ使い方で次のメソッドが利用できる。
# * `.max()`：最大値
# * `.min()`：最小値
# * `.mean()`：（算術）平均
# * `.std()`：標準偏差
# * `.var()`：分散
# 
# 次の２つも便利である。計算する際，欠損値は無視され，結果は`DataFrame`として返される。
# * `.cov()`：分散共分散行列
# * `.corr()`：相関係数
# 
# 例えば，`.cov()`を計算してみよう。

# In[79]:


df.iloc[:,:-1].cov()


# 対角成分は分散であり，その他は行と列のラベルに対応する共分散となる。`.corr()`も同じ位置関係となる。
# 
# また変数の変化率（成長率）を計算するには`.pct_change()`が便利である（percent changeの略）。これは毎期ごとの変化率を返すことになる。

# In[80]:


df.iloc[:,:-1].pct_change()


# `1999`年が無いため，`2000`年の成長率は欠損値となっている。`.pct_change()`と`.mean()`を続けて書くと簡単に（算術）平均成長率を計算することができる。

# In[81]:


df.iloc[:,:-1].pct_change().mean()


# ### その他

# 列`id`には文字列があり，行のデータをカテゴリー別に分けていると考えることができる。メソッド`.unique()`を使うと，選択した列に重複したデータがある場合，ユニークなものだけを抽出できる。

# In[82]:


df['id'].unique()


# まな類似するメソッドに`.nunique()`があり，カテゴリー数を返す。

# In[83]:


df['id'].nunique()


# 関連するメソッドに`.value_counts()`がある。これを使うとカテゴリーの内訳を確認するすることができる。カテゴリーの行数を表示するには

# In[84]:


df.loc[:,'id'].value_counts()


# とする。引数`normalize=True`を追加すると，頻度（パーセント）として表示できる。

# In[85]:


df.loc[:,'id'].value_counts(normalize=True)


# `df`のように行数が少ない`DataFrame`の場合，これらのメソッドの有用性を見出すことは難しいが，何千行あるデータを扱っていると想像してみよう。そのような大きなデータを扱う場合は非常に重宝するメソッドとなる。

# ## `Series`について

# `Series`について簡単に説明する。`Series`はスプレッド・シートから１つの行または列を取り出したようなデータとイメージすれば良いだろう。まず`df`の列`gdp`から`Series`を作ってみよう。

# In[86]:


s = df.loc[:,'gdp']
s


# ````{note}
# ```
# df.loc[:,['gdp']]
# ```
# もしくは
# ```
# df[['gdp']]
# ```
# で列を抽出すると`DataFrame`が返される。また次のように`s`のメソッド`.to_frame()`を使うと`Series`を`DataFrame`に変換できるので、覚えておくと便利かも知れない。
# ```
# s.to_frame()
# ```
# ````

# ### 構成要素

# この例を使い`Series`の構成要素について説明する。
# 
# * データ：`s.to_numpy()`もしくは`s.values`で抽出可能
# * `Series`名：`s.name`で抽出可能
#     * `df`の列ラベルから引き継がれているが、空の場合もある。
# * インデックス・ラベル（index label）：`s.index`で抽出可能
#     * `df`の行ラベルから引き継がれている
#     * インデックス（index）は`0`,`1`,`2`,...の順番で表される。
# * インデックス名：`s.index.name`で抽出可能
#     * `df`の行ラベル名から引き継がれていが、空の場合もある。
# 
# まずデータ自体を抽出する。

# In[87]:


s.to_numpy()


# In[88]:


type(s.to_numpy())


# `Series`名の抽出

# In[89]:


s.name


# インデックスの抽出

# In[90]:


s.index


# 戻り値の最後に`name='year'`とあるように、インデックス名は`year`であり、次のコードでアクスすできる。

# In[91]:


s.index.name


# また`dtype='int64'`とあるが、インデックスは整数であることがわかる。

# ### 要素の抽出

# 要素の抽出方法は`NumPy`の`array`と辞書に似ている。この点を説明するために、次のコードを使い`s`からインデックスを文字列に変換した`s_new`を作成する。

# In[92]:


s_new = s.copy()
s_new.index = [i for i in 'abcdefghijk']
s_new


# > １行目：`s`のコピーを作り`s_new`に割り当てる。
# >
# > ２行目の右辺：内包表記を使い次のリストを作成する。
# >
# > `['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']`
# >
# > ２行目：`s_new`のインデックス・ラベルを変更
# > ３行目：`s_new`の表示

# まずインデックスを使い一つの要素の抽出は次のようにする。

# In[93]:


s_new[5]


# 複数のインデックスを使うことも可能である。

# In[94]:


s_new[[1,3,5]]


# これは`array`と同じである。またスライシングも同様にできる。

# In[95]:


s_new[5:-2]


# ````{warning}
# `s`の場合、順番を表すインデックスで要素アクセスしようとするとエラーが発生する。これはラベルが整数`2000,2001...`になっている理由のようである。この場合は、ラベルである`2000`や`2008`を使い次のようにするとエラーは発生しない。
# ```
# s[2000]
# ```
# ````

# 次にラベルを使った要素のアクセス方法を考える。この場合は辞書と同じ形になる。

# In[96]:


s_new['b']


# In[97]:


s_new[['b','e','j']]


# ### 統計学関連メソッド

# `Series`にも`DataFrame`と同じような統計学関連メソッドが実装されているので，`see`で調べてみよう。

# In[98]:


see(s_new)


# ## グループ計算

# 上で使った`df`を表示してみよう。

# In[99]:


df.head()


# `df`のメソッド`.mean()`を使うと列の平均を簡単に計算できる。列を取り出して計算してみよう。

# In[100]:


df.iloc[:,1:-1].mean()


# 一方で，列`id`には`a`と`b`があり，`df`を２つのグループに分けることができる。ここで問題になるのは，グループ別に列の平均を計算したい場合である。まず考えられる方法は`a`グループだけを抽出して平均を計算し，同じように`b`も計算するということだろう。もしグループ数が多い場合は`for`ループが必要になり，より長いコードを書く必要が発生し面倒に感じることになる。
# 
# こういう場合のために，`DataFrame`には簡単にグループ計算を可能にする方法が用意されている。それが`.groupby()`というメソッドである。以下では`.groupby()`の使い方を`df`を使って３つのステップに分けて説明する。

# ### ステップ１：グループ化する列を指定

# 最初のステップでは，**グループ化したい列名**を引数として`.groupby()`を実行する。`df`を`id`でグループ化したいので次のコードとなる。
# ```
# df.groupby('id')
# ```
# 
# **＜注意＞**<br>
# このコードは`DataFrame`を返すわけでは**ない**。返すのはグループ計算用のオブジェクトであり，それを使ってグループ計算をおこなう事になる。
# 
# 実際にコードを実行し，変数`df_groupby`に割り当てよう。

# In[101]:


df_groupby = df.groupby('id')


# `df_groupby`を実行してみよう。

# In[102]:


df_groupby


# 何も返されない。表示されているのは，PCメモリーのある箇所に`DataFrameGroupBy`というオブジェクトが存在すると伝えているだけである。

# ### ステップ２：グループ計算したい列を指定

# 次にグループ計算したい列を指定するが，次の様な書き方となる。
# ```
# df_groupby[＜グループ計算したい列ラベル＞]
# ```
# ここで`[]`を使っていることに注意しよう。例として`gdp`をグループ計算するとしよう。

# In[103]:


df_groupby['gdp']


# ここでも新たなオブジェクト`SeriesGroupBy`のメモリーアドレスが表示されるだけである。どの様に計算するかを指定することにより，計算結果が返されることになる。それが次のステップである。

# ### ステップ３：計算方法の指定

# ステップ１と２がグループ計算の準備段階であり，あとは実際にどのように計算したいかを指定する。例として，平均を考えてみよう。上でも出てきたが，平均はメソッド`.mean()`を使う。

# In[104]:


df_groupby['gdp'].mean()


# グループ計算結果は`Series`として返されている。`.mean()`以外にも使える関数は準備されいる。`see()`を使って属性・メソッドを調べてみよう。

# In[105]:


see(df_groupby['gdp'])


# 主なメソッドとして次を挙げることができる（これらの計算で欠損値は無視される）。
# * `mean()`：平均
# * `median()`：中央値
# * `max()`：最大値
# * `min()`：最小値
# * `std()`：標準偏差
# * `var()`：分散
# * `sum()`：合計
# * `cumsum()`：累積和
# * `first()`：最初の値
# * `last()`：最後の値
# * `count()`：要素数
# * などなど
# 
# このリストにない計算をしたい場合もあるだろう。その場合は，上のリストにもある`.agg()`（`aggregate()`も同じ）を使い`NumPy`や自作の関数を指定する。例えば，`NumPy`の`np.mean()`で平均を計算する場合は次の様になる。

# In[106]:


df_groupby['gdp'].agg(np.mean)


# 次に平均を計算する自作の関数`my_mean`を考えてみよう。

# In[107]:


def my_mean(x):
    return sum(x)/len(x)


# ここでの`x`はステップ２で指定する計算する対象の列と考えれば良いだろう。実際に実行してみよう。

# In[108]:


df_groupby['gdp'].agg(my_mean)


# ```{warning}
# `np.mean`の場合も`my_mean`の場合も`()`がなく，関数名だけを`.agg()`の引数にしている。関数名だけを`.agg`に渡し，`.agg`が渡された関数を実行するというイメージである。`()`を付けると`.agg()`に渡す前に関数を実行することになりエラーとなってしまう。
# ```

# ### 次のステップ

# #### １行で書く

# 上の説明では３つのステップに分けたが，もちろん次のように３つのステップを次のように１行で書いても構わないし，むしろその場合が多いだろう。

# In[109]:


df.groupby('id')['gdp'].mean()


# このコードは次の様に読むことができる。
# > `df`を`id`でグループ分けして，`gdp`の平均を計算する。

# #### 複数選択

# 各ステップでは列や関数を一つだけ選択・設定しているが，それぞれ複数選択することも可能である。
# * ステップ１ではグループ化する上で基準となる列を複数選択
# * ステップ２では計算対象となる列を複数選択
# * ステップ３では`.agg()`の引数に複数の関数を指定
# 
# という具合である。ただその場合は，リストとして列や関数名を指定する必要がある。例えば，ステップ２で`gdp`と`inv`を選ぶとしよう。

# In[110]:


df.groupby('id')[['gdp','inv']].mean()


# 結果は`DataFrame`として返されている。ステップ１もしくは３で複数選択すると`DataFrame`が`MultiIndex`（階層的な行と列）として返されることになるが，その簡単な説明については[Gapminder](https://py4basics.github.io/Gapminder.html)を参照して欲しい。より詳しい説明は他のサイトに譲ることにする。
# 
# `df`のような小さな`DataFrame`では`.groupby`の威力はあまりピンとこないかも知れない。しかし大きな`DataFrame`を使うとその恩恵を強く感じることだろう。[Gapminder](https://py4basics.github.io/Gapminder.html)ではマクロ経済データを使い`.groupby()`の使い方の例を示している。興味がある人は是非！
