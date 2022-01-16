#!/usr/bin/env python
# coding: utf-8

# # `Python`：基礎（その１）

# ## 最初の注意点

# ### 半角と全角 

# > **半角**を基本としてコード（スペースも含めて）を書くこと。
# 
# 次の２つケース以外で全角を使うとエラーが発生する。
# * 以下で説明する文字列型のデータ型の場合は全角を使っても構わない。
# * 半角の`#`の後であれば全角を使っても構わない（`Python`は`#`の後に続くコードを無視するためであり，よくコメントを書くのに使われる）。

# ```{margin}
# <div name="html-admonition">
# Do you want to read in a differnt language? Open the 
# <input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="Google translated version" style="color:#ffffff;background-color:#008080;" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/>
# in English or the language of your choice.
# </div>
# ```

# 例えば，次のコード・セルには半角の`10`の後に全角のスペースが紛れ込んでいるためエラーが発生している。

# In[1]:


10　


# 「全角スペース忍者」には要注意！

# ### 左詰め

# `Python`ではインデントが重要な役割を果たします。原則，コード・セルの中で左詰めでコードを書くようにすること。一方で，以下で説明するようにインデントが必須な場合（例えば，`for`ループや関数を定義する場合）もあり，その様な場合は**半角スペース4つ**を入れるのが慣例となっている。Jupyter Notebookでは，`Tab`を押すことにより半角スペース4つが自動で挿入される。

# ## ４つのデータ型

# `Python`には無数のデータ型があるが，まず基本となる3つを考える。
# * 整数型（`int`と表す）
# * 浮動小数点型（`float`と表す）
# * 文字列型（`str`と表す）
# * ブール型（`bool`と表す）
# 
# 整数型とは文字通り`1`や`100`などの整数のことであり，浮動小数点型とは小数を指す。`Python`では整数と小数を異なるデータ型として区別して扱うので，`1`と`1.0`はデータ型が異なるのである。

# ````{note}
# なぜ浮動小数点型を「少数」と呼ばないのか。数字の3.14を考えよう。表示方法によって次のように分けることができる。
# * 固定小数点型
#     
#     $$
#     3.14
#     $$
#     
#     この場合，小数点は3と1の間に固定されている。
#     
# * 浮動小数点型
# 
#     $$
#     3.14\times 10^0,\quad 31.4\times 10^{-1},\quad 314.0\times 10^{-10}
#     $$
#     
#     10の指数によって小数点が移動していることがわかる。
#     
# コンピュータは後者を利用しデータを2進法で表しているためである。
# ````

# In[2]:


1 


# In[3]:


1.0


# データ型を確認するために`type()`という関数が用意されているので，それを使ってみよう（関数に関しては後述する）。

# In[4]:


type(1)


# In[5]:


type(1.0)


# 整数型は`int`（integer），浮動小数点型は`float`と表示されている。文字列は

# In[6]:


'国内総生産'


# のように`'`で挟まれて定義される。`'`の代わりに`"`を使っても良い。どちらを使っても同じだが，クォートの中でクォートを使う必要がある場合は，それぞれ違ったものを使う。例えば，

# In[7]:


'He said "Python is very useful!" to me.'


# データ型を確認してみよう。

# In[8]:


type('神戸大学')


# `str`はstringの略である。注意が必要な点は次も文字列型となる。

# In[9]:


'0.1'


# In[10]:


type('0.1')


# 従って，後述する数字の加算や除算などはできない`0.1`である。一方で文字列型専用の「加算」と「乗算」があるので，そちらも後述する。
# 
# ブール型には`True`（真）, `False`（偽）がある。名前が示すように「真偽」を示すのがブール型であり，`True`と`False`を真偽値と呼ぶ。例えば，

# In[11]:


1==10


# 後ほど説明するが，`==`は「等しい」ということを意味する。また，`True`は`1`, `False`は`0`として計算される。

# In[12]:


True==1 # Trueは１なのでTrueを返す


# In[13]:


False==0 # Falseは0なのでTrueを返す


# In[14]:


True + True


# またそれぞれのデータ型を他のデータ系に変換することも可能である。
# 
# `float()`：浮動小数点数型への変換

# In[15]:


float(10)


# `int()`：整数型への変換

# In[16]:


int(10.0)


# `str()`：文字列型への変換

# In[17]:


str(10.0)


# 例：文字列型 $\rightarrow$ 浮動小数点数型

# In[18]:


float('10.0')


# 例：文字列型 $\rightarrow$ 浮動小数点数型 $\rightarrow$ 整数型

# In[19]:


int(float('10.0'))


# ちなみに`bool()`はブール型に変換するのではなく、`()`の中のオブジェクト（以下の説明を参照）の 真偽値（truth value; `True`か`False`）と呼ばれる値を返す。あるオブジェクトが「空」かどうかを確かめるの使われる。

# In[20]:


bool(100)


# In[21]:


bool(0)


# In[22]:


bool('神戸大学'), bool('')


# ````{tip}
# 1,000,000,000.0（10億）のような大きな数字は３桁ごとにコンマを入れると読みやすくなりますが，`Python`では`,`の代わりに`_`を使うことができます。例えば，35億を`x`に割り当てる場合は次の様に書くことができます。
# ```
# x = 3_500_000_000.0
# ```
# ````

# ## 計算機としての`Python`

# ### 算術演算子

# 基本的な算術演算子として以下を挙げることができる。
# * `+`（加算）
# * `-`（減算）
# * `*`（乗算）
# * `/`（除算）
# * `**`（累乗）
# * `%`（剰余演算）
# * `//`（切り捨て除算）

# In[23]:


100 + 1


# 整数型と整数型の加算なので整数型が返される。一方で，整数型と浮動小数点型で計算すると浮動小数点型が返される。

# In[24]:


100 - 1.0


# In[25]:


100 * 10.0


# 除算の場合は整数を使っても浮動小数点が返される。

# In[26]:


10 / 5


# In[27]:


10 ** 5.0


# 数学では`()`の中が先に計算されるが，`Python`でも同じである。

# In[28]:


(100 - 50) / 2


# 注意が必要な点は文字列型は上で説明した計算に使うとエラーが発生する。

# In[29]:


1 + '1.0'


# 浮動小数点型に変換する関数`float()`を使えばエラーは出ない。

# In[30]:


1+float('1.0')


# ちなみに文字列型`1`は関数`int()`整数型に変換できる。

# In[31]:


1+int('1')


# 次に剰余演算`%`についてだが，割り算の余を返す。次の例では`5`を`2`で割り余り`1`を返している。

# In[32]:


5 % 2


# `%`がよく使われる例を挙げると，整数を`2`で割ると偶数の場合は`0`（余りが`0`）が返されるので偶数・奇数を判断する場合に役に立つ。

# In[33]:


10 % 2 == 0


# 剰余演算と関係が深いのが切り捨て演算である。`x/y`の余りを返すのが剰余演算だが，整数部分を返すの切り捨て演算となる。例を考えよう。

# In[34]:


5 // 2


# `5➗２=2余り1`となるが，`5%2`は`1`を返し，`5//2`は`2`を返すことになる。即ち，
# 
# $$
# a　= (a//b)(b) + (a\%b)
# $$
# 
# が成立することになる。

# 最後に，文字列型にも`+`と`*`が使えることも付け加える。`+`は文字列を結合することになる。

# In[35]:


'1.0'+'1.00'


# In[36]:


'一人当たり' + 'GDP'


# 一方で，，，，

# In[37]:


'一人当たり' 'GDP'


# も同じ結果を返す。`+`は文字列の結合を明示的にする目印と考えれば良いだろう。

# また文字列に`*`を使うとリピートすることができる。

# In[38]:


'(^o^)/   '*3


# In[39]:


'-★'*20


# In[40]:


'😎🚀'*10


# ### 関係演算子

# 以下の関係演算子を使うことにより，変数の真偽を確認することができる。
# 
# * `==`（等号）
# * `!=`（等号不成立）
# * `<`（小なり）
# * `>`（大なり）
# * `<=`（小なりイコール）
# * `>=`（大なりイコール）
# 
# `==`はブール型を説明した際に使ったものと同じであり，値が同じかを確認する。

# In[41]:


10 == 10.0


# In[42]:


10 != 10


# In[43]:


10 > 5


# In[44]:


10 >= 10


# ### ブール演算子（論理演算子）

# * `not`：でない（否定）
# * `and`：且つ
# * `or`：又は
# 
# 例を考えるために，まず次の変数を設定しよう。

# In[45]:


a = 1
b = -1


# #### `not`

# まず`not`から考えよう。次の様な挙動となる。
# * `True`の前に置くと`False`を返す。
# * `Flase`の前に置くと`True`を返す。

# In[46]:


not True


# In[47]:


not (a > 1)


# In[48]:


not False


# In[49]:


not (a < 1)


# #### `and`

# 次に`and`を考えよう。

# In[50]:


True and True


# 「`True`且つ`True`」なので全体では`True`となる。簡単に理解できるはずである。次も基本的には同じである。

# In[51]:


(a > 0) and (b < 0)


# 次の例には`False`が入っている。

# In[52]:


False and True


# In[53]:


(a < 0) and (b < 0)


# #### `or`

# 簡単なので１つの例だけ表示する。

# In[54]:


True or False


# In[55]:


(a > 0) and (b > 0)


# #### `and`と`or`は何を返しているのか

# 上の例を見ると`and`と`or`は`True`もしくは`False`のみを返しているような印象を持つかも知れないが，実はそうではない。次の条件に従って，`and`は左の変数もしくは右の変数を返している。`or`も同様である。
# 
# | 演算      |        結果                         |
# |:--------:|:------------------------------------|
# | x  or y  | x  が`False`なら y, そうでなければ x を返す  |
# | x  and y | x   が`False`なら   x , そうでなければ y を返す |
# 
# では`5`や`神戸`など`True`や`False`でないものはどうなるのだろう。次の例を考えよう。

# In[56]:


'' or 5


# ここでは真偽値ではなく整数`5`が返されている。上の表に基づくと，空の文字列`''`は`False`と判断されていることが分かる。実は次のルールに従って，**値の真偽**を評価しているのである。
# 
# ＜`False`と評価される値＞
# * `False`（当たり前だが真偽値の`False`）
# * `None`
# * `0`（整数型）
# * `0.0`（浮動小数点型）
# * `''`（空の文字列）
# * `[]`（空のリスト）
# * `()`（空のタプル）
# * `{}`（空の辞書）
# * 等々
# 
# ＜これら以外は全て`True`と評価される＞
# 
# `False`と評価されるのは「無」，「空」に対応する値と覚えておけば良いだろう。値の真偽を確認したい場合は関数`bool()`を使うことも覚えておこう。例えば，

# In[57]:


bool(''), bool(5)


# これで次の例も理解できるだろう。

# In[58]:


'' and 5


# ## `=`による変数の割り当て

# ### `=`の役割

# 関係演算子に`=`を他の記号と一緒に使ったが，単独で使う場合は「**変数の割り当て**」に使う。次の例では値`10`を変数$x$に割り当てている。

# In[59]:


x = 10


# $x$の値を表示すには、$x$を書いたセルを評価するだけである。

# In[60]:


x


# ここで「代入する」と説明せずに「割り当てる」という表現を使ったが，その理由を説明する。簡単にいうと，`x`と`10`は全く別物であるためである。これを理解するために、多くの品物が保管されている大きな倉庫を考えてみよう。倉庫の管理者はどの品物がどこに保管されているかを記録する在庫リストを作成し、そこに品物が保管されている棚を示す記号を記入しているとしよう。この例を使うと、
# * `10`　→　倉庫の棚に保管されている品物
# * `x`　→　在庫リストに記載されている棚の記号
# 
# となる。品物と棚の記号は別物である。`Python`では、品物である`10`がコンピューター内のメモリーの所定の場所に保存され、その場所を示すのが変数`x`となる。即ち、`x`は品物`10`の実態とは異なる単なる「参照記号」なのである。
# * `10`　→　PCのメモリーに保存されている情報
# * `x`　→　参照記号
# 
# この点を明確にするために、上のコードは「`10`を記号`x`に**割り当てる**」と考える。ここで`=`の**右辺**を先に読み，その次に**左辺**を読んでいることに注意しよう。`=`を右から左に読む（考える）ことを習慣づけることが、今後`Python`を勉強する上で重要となる。この点を示すために次のコードを考えてみよう。

# In[61]:


x = x + 1


# 「？」と思うかもしれない。暗に方程式として考えるためであろう（私がそうだった）。これを右から左に読むとスッキリする。
# 1. 上で`10`を`x`に割り当てたが、問題のコードの右辺の`x`がその`10`である。`10`に`1`を加えたものが`11`であり、それが右辺である。
# 1. `=`を使い右辺の`11`を左辺の`x`に割り当てている。この時点で、`10`の参照記号であった`x`は`11`の参照記号に変更される。
# 
# 実際に`x`を表示してみよう。

# In[62]:


x


# 「品物と参照記号の関係」は今の段階ではそれ程重要ではないが，先に進むにつれて重要性が増してくるので，今のうちにこのようなイメージを持つと良いだろう。

# ### 複数の変数の割り当て

# `=`を使い１つの変数への割り当てを考えたが、実は複数の変数への割り当ても可能である。次の例を考えよう。（`=`の右辺から読む！）

# In[63]:


a, b, c = 3.14, '神戸', 2021


# `3.14`を`a`に，`'神戸'`を`b`に，`2021`を`c`に割り当てている。それぞれの変数を`,`で区切っていることにも留意しよう。

# In[64]:


print(a, b, c)


# 次の例では`a`と`b`を入れ替えている。（右辺から読む！）

# In[65]:


a, b = b, a


# In[66]:


print(a,b)


# ### 累算代入演算子

# 上で`x = x + 1`が出てきたが、これを短縮して`x += 1`と書くことができる。次のコードを考えようてみよう。

# In[67]:


x = 10
x += 1
x += 1
x += 1
x += 1
x += 1
x


# `x += 1`は`x`の値を`1`ずつ増やしていることが分かると思う。
# 
# 同様に他の算術演算子についても次の様に書くことができる。
# * `x = x-1` $\Rightarrow$ `x -= 1`
# * `x = x*10` $\Rightarrow$ `x *= 10`
# * `x = x/10` $\Rightarrow$ `x /= 10`
# * `x = x**2` $\Rightarrow$ `x **= 2`

# In[68]:


x=2
x **= 2
x **= 2
x


# ## 予約語

# アルファベットで分かりやすい変数名にするのが可読性が高いコードを書くコツである。しかし，変数の名前を作る上で守らなくてはならないルールがある。
# 
# * `(a-z, A-Z)`もしくは`_`（アンダースコア）で始める
# * 最初の文字以外であれば`(a-z, A-Z)`と`_`に加え数字も可
# * 長さに制限はない
# * 小文字と大文字は異なる記号としてあつかう
# * 次の単語は特定の目的のために事前に定義されている「予約語」なため，変数名としては使えない（使うとエラーが出る）。

# In[69]:


import keyword
keyword.kwlist


# これらに加え，
# 
# * 変数の頭文字は小文字とする
# 
# というのが慣例（エラーにはならない）であり，大文字で始まる変数は通常`class`と呼ばれるオブジェクトに使う。

# ## コンテナデータ型

# 上では基本となるデータ型を説明したが，そのような（それらだけではないが）データ型の集合となるデータ型も存在する。それがコンテナデータ型（Container Datatypes）と呼ばれるものであり，次の４種類が用意されている。
# * リスト（list）
# * タプル（tuple）
# * 辞書（dict）
# * 集合（set）
# 
# 授業では集合を使わないので，それ以外の３つだけを説明する。

# ### リストとタプル

# #### リスト

# リストは`[]`を使って作成する。また何かをリストに変換する場合は`list()`を使う。

# In[70]:


list0 = [10, 3 , 2]
list0


# 要素のデータ型が違っても構わない。

# In[71]:


list1 = ['A', True, 100]
type(list1)


# 要素が１つのリストの生成も可能。

# In[72]:


[100]


# 次に説明するタプルをリストに変換したい場合は`list()`を使うことができる。

# #### タプル

# タプルは`()`を使って作成する。また何かをタプルに変換する場合は`tuple()`を使う。

# In[73]:


tuple0 = ('A', True, 100)
type(tuple0)


# リストと変わりないように見えるが，大きな違いは要素を変更できるかできないかという点である。
# 
# * リストの要素は変更可能
# * タプルの要素は変更不可能
# 
# リストの要素の変更方法は以下で説明する。
# 
# 上で通常タプルは`(`と`)`を使って作成できると説明したが、実は、コンマ`,`によってタプルは定義されるため`(`と`)`は必須ではない。例えば、次のコードでもタプルとなる。

# In[74]:


'1', 'GDP', '消費'


# 従って、`(`と`)`はタプルを明確にするためと考えて良い。
# 
# 要素が１つのタプルも生成可能だが、その場合も必ず`,`を付ける事を忘れないように。

# In[75]:


('1',)


# 上で定義した`list1`をタプルに変換したい場合は`tuple()`を使う。

# In[76]:


tuple(list1)


# #### 要素のアクセス方法

# リストもタプルも要素のインデックス（位置）を考える場合，次の図のように左から`0`，`1`，`2`...，右からは`-1`，`-2`，`-3`と数える。
# ```
#    0   1   2   3   4   5  （左から数える） 
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#   -6  -5  -4  -3  -2  -1　（右から数える）
# ```
# 例えば，次のリストを考えよう。

# In[77]:


my_list = ['A', 'B', 'C', 'D', 'E', 'F']
my_tuple = (100, 200, 300, 400, 500, 600)


# `'A'`は０番目，`'B'`１番目，`'C'`は２番目と数える。例えば，`A`を抽出したい場合，

# In[78]:


my_list[0]


# In[79]:


my_tuple[0]


# 連続する複数の要素を選択する場合（スライシング）は`:`を使う。`:`の左右にインデックス番号を置き要素を選択するが，次のルールに従う。
# ```
# ＜選択する最初のインデックス＞:＜選択する最後の次のインデックス＞
# ```
# 即ち，`:`の右側にあるインデックスの要素は抽出されない。例えば，`my_list`の１番目から３番目の要素を抽出したい場合は`1:4`となる。

# In[80]:


my_list[1:4]


# In[81]:


my_tuple[1:4]


# `:`の左側の番号を省略すると`0`と解釈され，`:`右側を省略すると「最後まで」と解釈される。

# In[82]:


my_list[:4]


# In[83]:


my_tuple[3:]


# `+`を使い，複数のリストを結合することができる。

# In[84]:


my_list + [1,2,3]


# タプルも同様である。

# In[85]:


my_tuple[4:] + ('GDP','GNP')


# この場合，元のタプルを変更しているのではなく，新しいタプルを生成している。

# #### 要素の入れ替え

# 要素の入れ替え方法を説明するために，上で作成したリスト`list0`を考えてみよう。

# In[86]:


list0


# 1番目の要素は`3`だが，これを文字列`'Kobe'`に入れ替えてみよう。方法は簡単で次のコードとなる。

# In[87]:


list0[1] = 'Kobe'
list0


# 右辺から読めば理解できる。`'Kobe'`を`list0[1]`に割り当てており，ここでは「入れ替え」となる。この例の右辺は文字列だが，他のデータ型でもOKなので色々試してみよう。

# 一方，タプルは要素を変更できないので上のようなコードはエラーが発生することになる。

# In[88]:


tuple0[1] = 'Kobe'


# #### 要素の削除

# 要素を削除するには色々な方法が用意されているが，最も簡単なのは`del`（deleteの略）を使うことだろう。`del`の後に削除したい要素を書き実行するだけである。もちろんスライシングにも対応している。例えば，

# In[89]:


del list0[1]
list0


# `Kobe`が削除されている。

# ### 辞書

# 辞書（dictionary）はキー（key）と値（value）のペアとなって定義され，`:`を挟んで１つのペアとなる。全てを`{}`で囲み辞書を定義する。もしくは`dict()`でも生成することができる。

# In[90]:


dict0 = {'a':10, 'b':'失業率'}


# もしくは

# In[91]:


dict0 = dict(a=10, b='失業率')


# `dict0`には２つのペアがある。`a`のキーには値`10`が対応しており，`b`には`'失業率'`が設定されている。今の段階では辞書を使う目的が不明確でしっくりこないと思うが，勉強を進めるととてもパワフルなツールだと気づくだろう。

# In[92]:


print(type(dict0))


# 値にアクセスするにはキーを次のように使う。

# In[93]:


dict0['a']


# In[94]:


dict0['b']


# 辞書はキーと値のペアとなっているが，変更できるのは値だけである。方法は`=`の左辺に変更したいキーを選び，右辺に変更後の値を配置するだけである。例えば，`dict0`の`失業`を`完全雇用`に入れ替えてみよう。

# In[95]:


dict0['b'] = '完全雇用'
dict0


# どうしてもキーを変更したい場合は，キー・値のペアを削除し，新たに追加することになる。例えば，`'a':10`を`'A':10`に「変更」するには次のコードとなる。

# In[96]:


del dict0['a']
dict0['A'] = 10
dict0


# ここでの`del`はリストの要素を削除した際に使った同じ`del`である。
