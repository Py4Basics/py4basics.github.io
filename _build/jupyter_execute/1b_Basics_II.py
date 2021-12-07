#!/usr/bin/env python
# coding: utf-8

# # `Python`：基礎（その２）

# ## 関数

# コードを書くうえで関数は非常に重要な役割を果たすのが関数である。主に２つのタイプに分けることができる。
# * 組み込み関数（最初から準備されている関数）
# * ユーザー定義の関数（ユーザー自身が作成する関数）

# ```{margin}
# <div name="html-admonition">
# Do you want to read in a differnt language? Open the 
# <input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="Google translated version" style="color:#ffffff;background-color:#008080;" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/>
# in English or the language of your choice.
# </div>
# ```

# ### 組み込み関数

# 組み込み関数（built-in functions）とは，ユーザーが使えるように事前に準備された関数である。データ型を調べる際に使った`type()`もその１つである。頻繁に使う関数を３つ紹介する。

# #### `sum()`

# `sum()`は合計を計算する関数である。

# In[1]:


gdp_component = [10, 20, 30, 40]

sum(gdp_component)


# #### `print()`

# `print()`は表示するための関数だが，Jupyter Notebookでは`print()`を使わなくとも出力が表示される。例えば，

# In[2]:


10


# しかし複数行の場合は最後の行しか表示されない。

# In[3]:


10
200


# `print()`を使うと両方を表示することができる。

# In[4]:


print(10)
print(200)


# 異なるオブジェクトを表示するには`,`を使う。

# In[5]:


print('2019年の実質GDP：約', 500+34, '兆円')


# 文字列の中で`\n`は改行を示す。

# In[6]:


print('マクロ\n経済学')


# 次に`f-string`を紹介する。文字列の前に`f`を書き加え，文字列の中で`{}`を使うことにより，割り当てた変数の値や計算結果などを表示することが可能となる。次の例を考えよう。

# In[7]:


x = 1/3

print(f'3分の1は{x}です。')


# 小数点第二位まで表示する場合は，`x`の後に`:.2f`を付け加える。

# In[8]:


print(f'10割る3は{x:.2f}です。')


# `2`を`5`にすると，小数点第五位までの表示となる。

# #### `range()`

# `range()`は連続する整数を用意する関数である。例えば，`0`から`9`までの`10`の整数を生成するには 

# In[9]:


range(10)


# とする。用途が明確ではないと感じるかもしれないが，後述する`for`ループで多用することになる。またリストとして表示するには`list()`を使う。

# In[10]:


x_list = list(range(10))
x_list


# #### `len()`

# 要素の個数などを返す関数。

# In[11]:


len(x_list)


# ### ユーザー定義の関数

# #### 基本

# `def`を使って関数を定義し，引数が設定される（省略される場合もある）。ここでは基本となる引数のみを考えるが，引数の**位置**と`=`が重要な役割を果たすことになる。例を使いながら説明する。最初の例は数字の2乗を計算する関数である。

# In[12]:


def func_0(x):
    return x**2


# * １行目：
#     * `def`で始まり（`def`はdefinitionの省略形）`:`で終わる。
#     * `func_0`が関数名，`x`が第１引数（ひきすう）であり、この例では唯一の引数である。
# * ２行目：
#     * `return`は評価した値を「戻す」もしくは「返す」という意味。必ず`return`の前にはインデント（通常4つの半角スペース）が必要であり，ないとエラーになる。
#     * `x**2`という戻り値（返り値）の設定をする
# 
# 関数を評価するには，引数に数字を入れて実行する。

# In[13]:


func_0(2)


# 引数が無い関数を定義することを可能である。

# In[14]:


def func_100():
    return 10**2

func_100()


# `print()`関数を追加することもできる。

# In[15]:


def func_kobe(x):
    print('経済学はおもしろい(^o^)/')
    return x**2

func_kobe(10)


# #### 引数の位置が重要

# 引数が複数ある場合にその位置が重要になってくる。次の例を考えよう。

# In[16]:


def func_1(a, b, c):
    return a / b + c


# In[17]:


func_1(10, 2, 10)


# In[18]:


func_1(2, 10, 10)


# #### 実行する際に`=`を使う

# 関数を実行する際、引数に`=`を使って値を指定することも可能である。この場合，引数の順番を変えることが可能となる。

# In[19]:


func_1(10, c=10, b=2)


# `=`が付いていない引数は該当する位置に書く必要があり，`10`が最初に来ないとエラーとなる。一般的なルールとして，`=`を使う引数は全て`()`の右端にまとめる。

# * 関数を実行する際に`=`無しで関数に渡される引数は，その位置が重要であるため「位置引数」と呼ばれる。
# * 関数を実行する際に`=`付きで関数に渡される引数は「キーワード引数」と呼ばれる。

# #### 関数を定義する際に`=`を使う

# 関数を定義する際に`=`を使って引数のデフォルトの値を設定することができる。即ち，引数を入力すると入力された数値を使うが，引数を入力しない場合は引数に予め設定した値（デフォルトの値）が使われて評価される。次の例では`c`のデフォルトの値が`10`に設定されている。

# In[20]:


def func_2(a, b, c=10):
    return sum([a,b])*c


# `c`の値を設定しない場合とする場合を比較してみる。

# In[21]:


func_2(2, 3), func_2(2, 3, 100)


# #### 戻り値が複数の場合

# In[22]:


def func_3(x):
    return x, x**2, x**3

func_3(3)


# この場合、戻り値はタプルとして返される。これを利用して、関数を実行する際に変数にに戻り値のを割り当てることができる。

# In[23]:


a, b, c = func_3(4)
print(a)
print(b)
print(c)


# ````{tip}
# 上のコードの戻り値はタプルなため，それに合わせて次のように書くこともできる。
# ```
# (a, b, c) = func_3(4)
# ```
# しかしタプルは`,`で定義されるので、`()`を省いても問題ない。
# ````

# また次のコードでも同じ結果となる。

# In[24]:


d = func_3(4)
print(d[0])
print(d[1])
print(d[2])


# ここでは返り値のタプル自体を`d`に割り当て、その各要素を`print()`関数で表示している。

# In[25]:


d


# #### `lambda`関数

# `def`を使い複雑な関数を定義することができるが，単純な関数の場合，より簡単な方法がある。それが`lambda`関数である。例として，$x^2$を計算する関数を考えよう。
# ```
# def function_name(x):
#     return x**2
# ```
# この関数を`lambda`関数で書き直すと次の様になる。
# ```
# function_name = lambda x: x**2
# ```
# 右辺にある`lambda`は`lambda`関数を定義する部分であり，`def`のように必ず必要である。実際に実行してみよう。

# In[26]:


func_3 = lambda x: x**2


# In[27]:


func_3(2)


# ### 経済学を考える

# #### 将来価値

# * `t`：時間（年; 0,1,2,...）
# * `i`：名目利子率（例えば，0.02）
# * `r`：実質利子率（例えば，0.05）
# * `pi`：インフレ率（例えば，0.03）
# 
# 次の式が成立する。
# 
# $$
# 1+r=\dfrac{1+i}{1+pi}
# $$
# 
# `x`万円を年率`i`%の利息を得る金融商品に投資し，`t`年後に現金化するとしよう。その間のインフレ率は`pi`%とした場合の`x`万円の実質将来価値を計算する関数を考える。

# In[28]:


def future_value(x, i, pi, t):
    r = (1+i)/(1+pi)-1
    return x*(1+r)**t


# In[29]:


future_value(100, 0.05, 0.03, 10)


# #### 現在価値

# `t`年後に`x`万円をもらえるとしよう。`x`万円の現在価値を計算する関数を考える。

# In[30]:


def current_value(x, i, inf, t):
    r = (1+i)/(1+inf)-1
    return x/(1+r)**t


# In[31]:


current_value(100, 0.05, 0.03, 10)


# #### 複利計算

# * `y0`：元金
# * `t`：投資期間
# * `r`：実質利子率（年率）
# * `m`：複利の周期（年間の利息発生回数）
#     * 例えば，毎月利息が発生する場合は`m=12`
# * `yt`：`t`年後の元利合計
# 
# $$
# yt=y0\left( 1+\dfrac{r}{m}  \right)^{mt}
# $$
# 
# `t`年後の元利合計を計算する関数を考えよう。

# In[32]:


def calculate_yt(y0=100, r=0.05, m=1, t=10):
    return y0*( 1+r/m )**(m*t)


# In[33]:


calculate_yt()


# In[34]:


calculate_yt(m=12)


# (object)=

# ## オブジェクトと属性

# `Python`を習うと「オブジェクト」という単語が必ず出てくる。今の内にイメージをつかむために自転車をオブジェクトの例として考えてみよう。通常の自転車には車輪が２つあり、サドルが１つあり、左右にペダルが２つある。これらの数字が自転車に関する**データ**である。またペダルを踏むことにより前に動き、ハンドルを右にきると右方向に進むことになる。即ち、あることを実行すると、ある結果が返されるのである。これは数学の**関数**と同じように理解できる。$y=x^2$の場合、$x$が`2`であれば$y$の値として`4`が返される。このように自転車はデータと関数が備わっているオブジェクトとして考えることができる。また、車輪の数やペダルを踏むことは自転車特有のデータと関数であり、他のオブジェクト（例えば、冷蔵庫）にはない。即ち、世の中の「オブジェクト」にはそれぞれ異なるデータと関数が存在していると考えることができる。
# 
# `Python`の世界でも「すべて」をこれと同じように考える。上のコードの`10`にもデータと関数が備わっており、それらを**属性**（attributes）と呼ぶ。`10`は単なる数字に見えるが、実は様々な属性から構成されるオブジェクトなのである。上の例の自転車のように、`Python`の「属性」は次の２つに分類される。`10`を例にとると、
# 1. `10`が持つ様々な**データ（属性）**（data attributes）（例えば、`10`という値や整数という情報）
# 1. `10`特有の関数である**メソッド（属性）**（method attributes）（例えば、加算、除算のように`10`というデータに働きかける関数）
# 
# を指す。自転車と冷蔵庫は異なるデータと関数を持つように、整数`10`と文字列`マクロ経済学`は異なるデータと関数を備えるオブジェクトなのである。この考え方は`Python`のすべてに当てはまる。即ち、Everything is an object in Python.

# データ属性の例として浮動小数点型`10.0`を`y`に割り当てよう。

# In[35]:


y = 10.0


# `y`の属性は`dir()`という組み込み関数を使うことにより表示できる。

# In[36]:


dir(y)


# この中の最後にある`real`は数字の実部を表し，実数である`10.0`の実部は`10.0`である。一方，`imag`は複素数の虚部を表すが，`10.0`は複素数ではないので`0.0`になっている。（上で紹介しなかったが，データ型に複素数型もある。）

# In[37]:


y.real, y.imag


# 上の属性のリストにある`_`はアンダースコア（underscore）と呼ぶが，２つ連続した場合`__`となりダブル・アンダースコア（double underscore）と呼ぶ。長いのでダンダー（dunder）と省略する場合が多々ある。ダンダーが付いている属性は`Python`が裏で使うものでありユーザーが直接使う属性ではない。
# 
# 次にメソッドを考えるために次のリストを例に挙げる。

# In[38]:


my_list = [1,2,3]

dir(my_list)


# この中に`append`があるが，`my_list`に要素を追加するメソッドである。

# In[39]:


my_list.append(100)

my_list


# ```{note}
# * データ属性と異なりメソッドは`()`が必要となる。これは関数の`()`に対応している。
# 
# ```

# ## `for`ループ

# ### 説明

# `for`ループは同じコードを複数回リピートして実行したい場合に有効な方法である。次のような書き方となる。
# 
# ```
# for ＜イタラブルの要素を割り当てる変数＞ in ＜イタラブル＞:
#     ＜毎回実行したい内容１＞
#     ＜毎回実行したい内容２＞
#     ＜毎回実行したい内容３＞
#     ...
# ```
# 
# * 1行目
#     * `＜イタラブル＞`（iterable）とはリストやタプルのように要素を１つずつ返すことができる反復可能なデータ型（オブジェクト）を指す。文字列や後で説明する`Numpy`の`array`も含まれる。    
#     * `＜イタラブルの要素を割り当てる変数＞`とはループを１回実行する際に`＜イタラブル＞`の要素の値を割り当てる変数のこと。よく`i`や`j`などが使われ，比較的に短い変数名が使われる。
#     * `for`で始まり`:`で終わり，`＜イタラブル＞`の前に`in`が入る。
# * 2行目以降
#     * 慣例では4つの半角スペースのインデント後に実行したいコードを書く。
# 
# 以下では例を使って説明する。

# ### `print()`を使う例

# 次のリストにはGDPの構成要素が並んでいる。

# In[40]:


gdp_components = ['消費', '投資', '政府支出', '純輸出']


# このリストにある文字列を表示したいとしよう。

# In[41]:


for i in gdp_components:
    print(i)


# ＜コードの説明＞
# * １回目のループ
#     * 1行目で`gdp_components`の0番目の要素`消費`を`i`に割り当てる。
#     * 2行目で`print()`関数を使い変数`i`の値を表示する。
# * ２回目のループ
#     * 1行目で`gdp_components`の1番目の要素`投資`を`i`に割り当てる。
#     * 2行目で`print()`関数を使い変数`i`の値を表示する。
# * ３回目のループ
#     * 1行目で`gdp_components`の2番目の要素`政府支出`を`i`に割り当てる。
#     * 2行目で`print()`関数を使い変数`i`の値を表示する。
# * ４回目のループ
#     * 1行目で`gdp_components`の最後の要素`純輸出`を`i`に割り当てる。
#     * 2行目で`print()`関数を使い変数`i`の値を表示する。
# 
# この例では`gdp_components`の要素の数だけループが行われる。

# ### `.append()`を使う例

# リストにはメソッド`.append()`が実装されており，これを使うとリストに値を追加することができる。`.append()`と`for`ループを使い，空のリストに値を追加し新たなリストを作成する方法を紹介する。まず元になるリストを作成しよう。

# In[42]:


var_list = [1,2,3,4,5]


# 以下では，`var_list`のそれぞれの要素の10倍からなるリストを新たに作成する。

# In[43]:


my_list = []              # 1

for i in var_list:        # 2
    x = 10*i              # 3
    my_list.append(x)     # 4

my_list                   # 5


# ＜コードの説明＞
# 
# 1. 空のリストの作成（`my_list`に10倍にした数字を格納する）
# 2. ここから`for`ループの始まり。`i`はリスト`[1,2,3,4,5]`の要素を割り当てる変数。
#     * １回目のループでは`i`に`1`を割り当てる。
#     * ２回目のループでは`i`に`2`を割り当てる。
#     * ３回目のループでは`i`に`3`を割り当てる。
#     * ４回目のループでは`i`に`4`を割り当てる。
#     * ５回目のループでは`i`に`5`を割り当てる。
# 3. `10*i`を計算し`x`に割り当てる。
# 1. `.append()`を使い`x`の値を`my_list`に追加する。
# 1. `my_list`を表示する。

# ### 消費関数

# `for`ループを使い，所得によって消費がどのように変化するかを考えてみよう。まず消費関数を次のように仮定する。

# In[44]:


def consumption(y):
    return 100 + 0.7 * y


# * `100`：自発的消費（autonomous consumption）
# * `0.7`：限界消費性向（marginal propensity to consume）
# 
# 所得は次のリストで与えられるとする。

# In[45]:


income_list = [1000, 1100, 1500, 2000, 2300, 3000] 


# In[46]:


c_list = []               # 1

for y in income_list:     # 2
    con = consumption(y)  # 3
    c_list.append(con)    # 4

c_list                    # 5


# ＜コードの説明＞
# 
# 1. 空のリストの作成（消費の値を格納する）
# 2. ここから`for`ループの始まり。`y`はリスト`income_list`の要素を割り当てる変数。
#     * １回目のループでは`y`に`1000`を割り当てる。
#     * ２回目のループでは`y`に`1100`を割り当てる。
#     * ３回目のループでは`y`に`1500`を割り当てる。
#     * ４回目のループでは`y`に`2000`を割り当てる。
#     * ５回目のループでは`y`に`2300`を割り当てる。
#     * ６回目のループでは`y`に`3000`を割り当てる。
# 3. 関数`consumption(y)`を計算し`con`に割り当てる。
# 4. `.append()`を使い`con`の値を`c_list`に追加する。
# 5. `c_list`を表示する。

# ### `for`ループの２つの書き方

# 次のようなリストを作成したいとしよう。

# In[47]:


[10*i for i in range(10)]


# この例を使って`for`ループの２つの書き方を説明する。目的は動学的な変数の変化を考えるためのコード作成の基礎作りである。次のコードが一つ目の方法である。

# In[48]:


my_list = [0]           # １行目

for i in range(9):      # ２行目
    y = my_list[i] + 10 # ３行目
    my_list.append(y)   # ４行目
    
my_list                 # ５行目


# ＜コードの説明＞
# * （１行目）`my_list`の最初の要素として`0`を入れている。以下では`my_list`に値を追加して目的のリストを作成する。
# * （２行目）ループの開始。
#     * イタラブルとして`range(9)`を使っている。`list(range(9))`と置いても良いが，`range(9)`で十分である。
#     * `range(9)`は`0`から`8`までの整数を準備し，9回ループが実行されることになる。
#     * `0`から`8`までの整数を順次`i`に割り当てることになる。
# * １回目のループ
#     * （３行目）`my_list`の`0`番目の要素である`0`を抽出し，それに`10`をを足すことにより右辺は`10`となる。それを`y`に割り当てる。
#     * （４行目）`y`の値`10`を`my_list`に追加する。`10`は`my_list`の1番目の要素となる。
# * ２回目のループ
#     * （３行目）`my_list`の`1`番目の要素である`10`を抽出し，それに`10`をを足すことにより右辺は`20`となる。それを`y`に割り当てる。
#     * （４行目）`y`の値`20`を`my_list`に追加する。`20`は`my_list`の2番目の要素となる。
# * ３回目のループ
#     * （３行目）`my_list`の`2`番目の要素である`20`を抽出し，それに`10`をを足すことにより右辺は`30`となる。それを`y`に割り当てる。
#     * （４行目）`y`の値`30`を`my_list`に追加する。`30`は`my_list`の3番目の要素となる。
# * 同様のループ計算が合計で9回繰り返される。
# * （５行目）`my_list`を表示する。

# この例では，ループ用の変数`i`が３行目で使われており，比較的に分かりやすいと思う人も多いだろう。一方で，`i`に対応する変数（即ち，`my_list[i]`）が何を指しているのかを考える必要があり少し煩雑と感じる人もいるだろう。
# 
# 次のコードでも同じ結果となるが，`i`に対応する変数の値を考える必要はない。

# In[49]:


y = 0                   # １行目

my_list = [y]           # ２行目

for i in range(9):      # ３行目
    y = y + 10          # ４行目
    my_list.append(y)   # ５行目
    
my_list                 # ６行目


# ＜コードの説明＞
# * （１行目）最初の`y`の値を設定する。また`y`はループのアップデート用の変数として使われる。
# * （２行目）最初の`y`の値`0`からなるリストの作成する。以下では`my_list`に値を追加して目的のリストを作成する。
# * （３行目）ループの開始。
#     * イタラブルとして`range(9)`を使っている。`list(range(9))`と置いても良いが，`range(9)`で十分である。
#     * `range(9)`は`0`から`8`までの整数を準備し，9回ループが実行されることになる。
#     * `0`から`8`までの整数を順次`i`に割り当てることになる。
#     * ４〜５行目に`i`は使われていない。従って，`i`の役割は`0`から`8`までの整数の「捨て場」のようなものである。そのような場合，`i`の代わりに`_`を使うこともある。
# * １回目のループ
#     * （４行目）右辺の`y`の値は１行目で割り当てた`0`である。それに`10`を足し右辺は`10`となり，それを左辺の`y`に割り当てる。この時点で，１行目の`y=0`は「無効」となり，`y=10`として更新される。
#     * （５行目）`y`の値`10`を`my_list`に追加する。
# * ２回目のループ
#     * （４行目）右辺の`y`の値は`10`である。それに`10`を足し右辺は`20`となり，それを左辺の`y`に割り当てる。この時点で`y=10`は「無効」となり，`y=20`として更新される。
#     * （５行目）`y`の値`20`を`my_list`に追加する。
# * ３回目のループ
#     * （４行目）右辺の`y`の値は`20`である。それに`10`を足し右辺は`30`となり，それを左辺の`y`に割り当てる。この時点で`y=20`は「無効」となり，`y=30`として更新される。
#     * （５行目）`y`の値`30`を`my_list`に追加する。
# * 同様のループ計算が合計で9回繰り返される。
# * （６行目）`my_list`を表示する。

# １行目で`y=0`を設定していたが，ループ終了後の値を確認してみよう。

# In[50]:


y


# `my_list`の最後の要素と同じであり，`for`ループ内で更新用の変数として使われたのがわかる。
# 
# ２つの書き方を紹介した。基本的にどちらを使っても良い。上でも書いたが，最初の方法は`i`に対応する変数の値を追う必要があるので，それを分かりやすいと感じる人もいるだろうし，面倒と感じる人もいるかも知れない。一方，２つ目の方法は`i`を確認する必要がない。もちろん，初期値の変数`y=0`を`for`ループの外に作る必要があるが，これは次の例で説明するように，関数の中で使う場合はそれほど問題にはならないだろう。このサイトでは主に２つ目の手法を多用することになる。

# ### 将来価値の時系列

# 元本`x0`万円を投資すると実質年率`r`％の利息を得る金融商品を考えよう。`t`年間の将来価値（期首の値）をリストで示す関数を作成する。

# In[51]:


def calculate_futre_value(x0, r, t):  # 1
    
    x = x0                            # 2
    
    value_list = [x]                  # 3
    
    for year in range(1,t+1):         # 4
        x = x*(1+r)                   # 5
        value_list.append(x)          # 6
    
    return value_list                 # 7


# ＜コードの説明＞
# 1. 引数
#     * `x0`は元本，`r`実質利子率，`t`投資期間
# 2. `x`が`for`ループでのアップデート用の変数として使われる。初期値として元本`x0`を設定する。
# 3. `value_list`に将来価値を追加して目的のリストを作成する。初期値の値である元本`x`がリストの0番目の要素として入っている。
# 4. `range(1,t+1)`を使って`1`から`t`までの整数を準備する。`year`は`1`から`t`までの値を割り当てるだけで他の役割はない。
# 5. 右辺の`x`は今期の価値であり，来季の価値は`x*(1+r)`になる。それを左辺の`x`に割り当てる。その時点で`x`がアップデートされる。
# 6. `x`の値を`value_list`に追加される。
# 7. 戻り値として`value_list`を設定する。

# 次の値を使って将来価値を計算してみよう。
# * 元本：`x0=100`
# * 実質利子率：`r=0.02`
# * 期間：`t=5`

# In[52]:


values = calculate_futre_value(100, 0.02, 5)
values


# 次に`for`ループを使って見易く表示してみよう。

# In[53]:


for i, v in enumerate(values):   # 1
    print(f'{i}期：{v:.1f}万円')  # 2


# ＜コードの説明＞
# 
# このコードでは`enumerate()`が重要な役割を果たしている。`enumerate()`ついて説明するために次のリストを考えよう。
# ```
# ['A','B']
# ```
# `0`番目の要素は`A`，`1`番目の要素は`B`である。ここで`0`と`1`が要素インデックスであり，`emunerate()`はリストの要素インデックスと要素をタプルとして返す。このことは次のコードで確認できる。

# In[54]:


list(enumerate(['A','B']))


# ここでは`list()`を使ってリストとして表示している。また次のコードで`a`と`b`に`0`と`A`を割り当てることができる。
# ```
# a, b = (0, 'A')
# ```
# この特徴を利用して，上のコードでは`for`ループを実行している。
# * １回目のループ
#     * （１行目）`enumerate(values)`から`(0,100.0)`が引き出され，それぞれが`i`と`v`に割り当てられる。
#     * （２行目）`print()`関数を使い`i`と`v`を表示する。
#         * f-stringを使っている。
#         * `{v:.1f}`の`:.1f`は小数点第一位までの表示を指定している。
# * ２回目のループ
#     * （１行目）`enumerate(values)`から`(1,102.0)`が引き出され，それぞれが`i`と`v`に割り当てられる。
#     * （２行目）`print()`関数を使い`i`と`v`を表示する。
# * 同様のループが合計6回おこなわれる。

# ## 内包表記

# 内包表記とは`for`ループの考えを使い、リストや辞書などを簡単に１行で生成する方法である。リストの場合、次のような書き方となる。
# ```
# [＜何かをする＞ for i in ＜イタラブル＞]
# ```
# 
# * `for i in ＜イタラブル＞`の箇所は`for`ループの１行目と同じとなる。
#     * `＜イタラブル＞`はリストや`array`を指す。
#     * `i`は`＜イタラブル＞`の要素を割り当てる変数。
# * `＜何かをする＞`の箇所でしたい事を指定する。
#     
# `＜イタラブル＞`の例として`range(5)`を考えよう。まず`for`ループを使って、それぞれの要素を２乗にしたリストを生成するとしよう。

# In[55]:


lst = []

for i in range(5):
    lst.append(i**2)

lst


# `for`ループを使うと３行のコードとなるが、内包表記を使うと１行で済む。

# In[56]:


[i**2 for i in range(5)]


# `lst`の要素を全て文字列に変換してみよう。

# In[57]:


[str(i) for i in lst]


# 上のコードの`str()`は組み込み関数だが，`def`を使って作成した自前の関数を使うことも可能である。試してみよう。

# ## `if`文

# `if`文を使うと，あるブール型（真偽）の条件のもとでコードを実行することが可能となる。例えば，`change_in_gdp`をGDPの変化だとしよう。`change_in_gdp`の値が正の場合，
# 
# `print('GDPは増加しています。')`
# 
# を実行したいとしよう。

# In[58]:


change_in_gdp = 1000


# In[59]:


if change_in_gdp > 0:              # 1
    print('GDPは増加しています。')    # 2
    
else:                              # 3
    pass                           # 4


# ＜コードの説明＞
# 1. `if`で始まり`:`で終わる。`change_in_gdp>0`は`change_in_gdp`が正であれば`True`を，そうでなければ`False`を返す。
# 1. ４つの半角スペースのインデントが入り，`change_in_gdp>0`が`True`の場合に実行される。
# 1. `else`とは「`change_in_gdp>0`以外の場合」という意味であり，`change_in_gdp>0`が`False`の場合に続く行が実行される。`else`の後には必ず`:`が入る。
# 1. `pass`は「何もしない」という意味。
# 
# ここで`else`以下を省略してもエラーにはならない（結果も変わらない）。即ち，`else`以下がない場合は，それが省略されていると考えれば良い。

# 次に，複数の条件を導入するために次の関数を考える。
# 
# 1. `print('GDPは変化していません。)`
# 1. `print('GDPは増加しています。)`
# 1. `print('GDPは減少加しています。)`
# 
# `change_in_gdp`の値がゼロの場合は`1`を，正の場合は`2`を，負の場合は`3`を表示したいとしよう。

# In[60]:


change_in_gdp = -200


# In[61]:


if change_in_gdp == 0:
    print('GDPは変化していません。')
    
elif change_in_gdp > 0:
    print('GDPは増加しています。')
    
else:
    print('GDPは減少しています。')


# ＜説明＞
# * `if`が１つ目の条件, `elif`が２つ目の条件, `else`が３つ目の条件を指定している。
# * `if`, `elif`, `else` で始まる行の最後は`:`となる。
# * `print()`の行は４つの半角スペースのインデントが入る。
# * `else`の行に`change_in_gdp<0`は不要（残りの可能性は`X<0`しかないため）
# * `elif`は`else if`の省略形であり，２つ目の条件を定義する。
# * `elif`は`if`と`else`の間に複数入れることが可能である。

# ---
# 次の例として一般的な生産関数を考えよう。
# 
# $$
# Y=F(K,L)
# $$
# 
# 要素間の代替の弾力性は次のように定義される。
# 
# $$
# \sigma = 
# \dfrac{\log(L/K)}{\log\left(\frac{dF}{dK}/\frac{dF}{dL}\right)}
# $$
# 
# $\sigma$が一定な生産関数はCES生産関数（Constant Elasticity of Substitution）と呼ばれ，次の式で与えられる。
# 
# $$
# Y = A\left[a(bK)^\rho+(1-a)(cL)^\rho\right]^{\frac{1}{\rho}}
# $$
# 
# ここで
# * $\sigma=\dfrac{1}{1-\rho}$
# * $\rho\leq 1$：要素の代替の程度を決定する。
# * $0<a<1$：要素の貢献度のシェアを決定する。
# * $b>0,c>$：要素の単位に依存する。
# * $A>0$：生産の単位に依存する（生産性）。
# 
# また，$\rho$の値によって次のような生産関数となる。
# 
# $$
# Y = 
# \begin{cases}
#     &A\left[a bK+(1-a)cL\right],\quad\rho=1\quad \text{（完全代替型）}\\
#     &AK^a L^{1-a},\quad\rho=0\quad\text{（コブ・ダグラス型）}\\
#     &A\cdot\text{min}\left\{bK, cL\right\},\quad\rho=-\infty\quad\text{（完全補完型またはレオンティエフ型）}
# \end{cases}
# $$
# 
# 次のコードで$\rho=-\infty$以外のケースを関数で表している。

# In[62]:


def ces_production(k, l, rho=0, A=1, a=0.3, b=1, c=1):
    
    if rho > 1:
        print('rhoには１以下の数字を入力してください。')

    elif rho == 1:
        return A*( a*b*k + (1-a)*c*l )
    
    elif rho == 0:
        return A*k**a * l**(1-a)
    
    else:
        return A*( a*(b*k)**rho + (1-a)*(c*l)**rho )**(1/rho)


# In[63]:


ces_production(10,3,rho=-1)


# ## ヘルプ

# 組み込み関数`help()`を使うと関数やモジュールなど説明を表示させることができる。例えば，`print()`を例として挙げる。

# In[64]:


help(print)


# 引数は関数名であり`()`は付いていないことに留意しよう。`()`を付けると`print()`を評価した結果に対しての説明が表示されることになる。英語での説明だがパターンを理解すればこれだけでも有用に感じることだろう。 
# 
# `help()`の代わりに`?`を使うこともできる。

# In[65]:


get_ipython().run_line_magic('pinfo', 'print')


# ## パッケージとモジュール

# ### 説明

# Pythonには組み込み関数が多く用意されているが，Jupyter Notebookで`Python`のセッションを開始しても全ての関数が使える状態になっていない。使えるようにするためには，モジュール（modules）やパッケージ（package）と呼ばれるものを読み込む必要がある。２つの違いを簡単にいうと
# * モジュール（module）は**１つ**のファイル（拡張子が`.py`）にまとめられた関数群であり，
# * パッケージは（package）**複数**つのファイル（拡張子が`.py`）で構成されている（フォルダーにまとめられている）
# 
# となる。従って，モジュール全体を読み込んだり，あるパッケージの１つのモジュールだけを読み込むということも可能である。授業では，`NumPy`，`SciPy`，`Pandas`を使うが，ここでは例として数学用の`math`モジュールを考える。
# 
# 含まれる関数を使うためには`import`を使って読み込む必要がある。モジュールの全てを読み込むとモジュール内の全ての関数が使用可能となる。

# ````{note}
# 更に付け加えると，サブパッケージ（subpackage）とサブモジュール（submodule）がある大きなパッケージもある。次の章で説明する[Numpy](chap:numpy)パッケージを例として挙げることができる。フォルダーのの構成で考えると次のようになる。
# ```
# package（フォルダー）
# |-- __init__.py（ファイル）
# |-- module.py（ファイル; 関数が配置）
# |-- subpackage（フォルダー）
#         |-- __init__.py（ファイル）
#         |-- submodule.py（ファイル; 関数が配置）
# ```
# ここで`__init__.py`はパッケージとサブパッケージのフォルダーに必ず必要なファイルであり，空の場合もあれば関数が含まれる場合もある。
# ````

# ### `math`モジュール

# 名前が示すように数学に関する関数がまとめられているモジュールとなる（[詳細はこのリンクを参照](https://docs.python.org/ja/3/library/math.html)）。`math`を次のコードで読み込むことができる。

# In[66]:


import math


# 最初の例として平方根を計算してみよう。使う関数名は，square rootの略となる`sqrt()`。

# In[67]:


math.sqrt(4)


# `math.sqrt`とは「`math`モジュールの`sqrt`」という意味であり，`math`をつけるのは他のモジュール等の`sqrt`とバッティングしないようにするためである。モジュール名が長い場合は，短い名前で読み込むことも可能である。

# In[68]:


import math as m


# In[69]:


m.sqrt(9)


# モジュール内の特定の関数だけを読み込むことも可能である。

# In[70]:


from math import sqrt, log   # logは自然対数で, sqrtの両方を読み込む


# このコードは「`math`モジュールから`sqrt`と`log`を読み込む」と読むことができる。

# In[71]:


sqrt(10), log(10)


# ただ、この場合は他のモジュールやパッケージ、もしくは自分が定義した関数をバッティングしないように注意する必要がある。

# ### `random`モジュール

# `random`モジュールを使うことにより乱数を発生させることができる（[詳細はこのリンクを参照](https://docs.python.org/ja/3/library/random.html)）。まず`random`をインポートしよう。

# In[72]:


import random


# 様々な関数が用意されているが，その中の`randint()`関数は，引数で指定するランダムな整数を返す。次のコードは，サイコロの目（1~6）の１つを返す。

# In[73]:


random.randint(1,6)


# 内包表記を使って10回サイコロを振った結果を表示してみよう。

# In[74]:


[random.randint(1,6) for i in range(10)]


# ### `see`モジュール

# [オブジェクトと属性](object)の節で属性を確認する`dir()`関数について説明した。`dir()`は組み込み関数であるため，パッケージやモジュールをインポートしなくても使えるので便利である。しかし通常使う必要がないダンダー`__`が付いている属性（例えば，`__init__`）まで表示される。それらを省いて，属性のリストを見やすく表示する`see`モジュールを紹介する。使い方は簡単で，まず次のコードでインポートする。

# In[75]:


from see import see


# 後はインポートした関数を`dir()`と同じように使うだけである。簡単な例を考えよう。

# In[76]:


x = 10.99


# `dir()`を使うと通常は必要ないものまで表示される。

# In[77]:


dir(x)


# `see()`を使うとダンダー属性は表示されない。

# In[78]:


see(x)


# `see()`を使う利点がもう一つある。表示されたリストを見ると，メソッドには`()`が付けられているが，単なるデータ属性には付いていない。（表示さている属性・メソッドが全て使えるわけではないので注意しよう）。例えば，`is_integer()`は整数であれば`True`を返すメソッドであり，`.real`と`.imag`は複素数の実部と虚部を返す属性となる。

# In[79]:


x.is_integer()


# In[80]:


x.real, x.imag


# ## スコープ

# ### 説明

# スコープとは、変数が所属し直接アクセスできるコードの中の「領域」を示す。類似する概念に名前空間（Namespace）もあるが、スコープの情報を記す「表」のことであり、スコープ（Scope）と同義と理解すれば良い。
# 
# ここでは基本的に以下のように理解すれば良いであろう。
# 
# * Jupyter Notebookを開始した時点からglobalスコープが始まる。
# * 関数を定義すると、その関数の範囲内でlocalスコープが生成される。
# * globalスコープで定義された変数は、localスコープからアクセスできるが、globalスコープからlocalスコープの変数にはアクセスできない。
# * 関数を実行すると次の順番で変数を探す。
#     1. 関数のローカス・スコープ
#     2. グローバル・スコープ
# 
# 次の例を考えよう。

# In[81]:


s = "Kobe University"  # globalスコープ

def scope_0():
    s = "神戸大学"  # localスコープ
    return s

scope_0()


# この関数を実行すると、Pythonはまず関数`scope_0`のローカル・スコープ内で変数`s`を探すことになる。ローカル・スコープに`s`があるので、それを返している。次の関数を考えよう。

# In[82]:


def scope_1():
    return s

scope_1()


# この例では、まず`Python`はローカル・スコープに`s`があるかを確かめる。ローカル・スコープにないため、次にグローバル・スコープに`s`がないかを確かめている。グローバル・スコープに`s`があったので、それを返している（ないとエラーが出る）。
# 
# 次の例では、グローバル・スコープからローカル・スコープの変数へのアクセスを考える。

# In[83]:


def scope_2():
    s_local = 'Pythonは楽しい(^o^)/'
    return s_local

scope_2()


# `s_local`は関数`scope_2`のローカル・スコープで定義されている。グローバル・スコープからアクセスしようとするとエラーが発生する。

# In[84]:


s_local


# ### 教訓１

# > * 関数内で使う変数は、可能な限り関数内で定義する方が意図しない結果につながるリスクを軽減できる。
# > * グローバル・スコープで定義した変数を関数に使いたい場合は、引数として同じ変数を使う。
# 
# 次の例を考えよう。

# In[85]:


a


# `a`は既に定義されたが，この値を忘れて（知らずに）`10`だったと勘違いして次の関数を定義したとしよう。

# In[86]:


def scope_3(x):
    return x + a


# `scope_3(10)`は`20`を返すと思って実行すると意図しない結果になる。

# In[87]:


scope_3(10)


# このような場合は`a`を引数に使うことにより問題を回避できる。`a`は`10`として関数を実行すると意図した結果となる。

# In[88]:


def scope_4(x,a):
    return x + a

scope_4(10,10)


# この場合、関数`scope_4(x,a)`の`a`はローカス・スコープで定義され、グルーバル・スコープの`a`とは異なる。実際、グルーバル・スコープの`a`の値を確認してみると以前と同じ値である。

# In[89]:


a


# ちなみに、グローバル・スコープの変数名や関数名は`%who`もしくは`%whos`のコマンドで確認できる。

# In[90]:


get_ipython().run_line_magic('who', '')


# このリストにある`s`はグローバル・スコープの`s`である。またローカル・スコープにある`s_local`はこのリストには含まれていない。

# ### 教訓２

# > `for`ループの１行目に使う変数は再割り当てされても構わない変数を使おう。
# 
# 例を使って説明しよう。

# In[91]:


for i in range(5):
    print(i)


# この`for`ループの`i`は`range(5)`の連番`0`、`1`、`2`、`3`、`4`を指す変数として使われるが、グローバル・スコープの変数として存在し、ループの最後の値が割り当てられている。確認してみよう。

# In[92]:


i


# `for`ループで使う変数は、ループ用の変数（例えば，`i`，`j`，`k`など）を使うのが良いだろう。
