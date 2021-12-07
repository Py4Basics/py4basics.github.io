---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 経済学のためのPython入門

```{epigraph}
**Python Basics for Economics**

[春山 鉄源](https://t-haruyama.github.io)

神戸大学経済学研究科
```

```{code-cell} python3
import datetime
dt = datetime.datetime.now()
print('Version:',dt.strftime('%Y年%m月%d日'))
```

<!---
%H:%M:%S
dt = datetime.datetime.now()
dt = datetime.datetime.today()
-->

```{margin}
<div name="html-admonition">
Do you want to read in a differnt language? Open the
<input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="Google translated version" style="color:#ffffff;background-color:#008080;" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/>
in English or the language of your choice.
</div>
```

本サイトに関するコメント等はGitHubの[Discussions](https://github.com/Py4Basics/py4basics.github.io/discussions)もしくは<haruyama@econ.kobe-u.ac.jp>にご連絡ください。

<br>

## はじめに
本サイトの目的は次の２つのサイトを学習するために必要な`Python`の基礎の解説である。
* [Pythonで学ぶマクロ経済学（中級＋レベル）](https://py4macro.github.io)
* [Pythonで学ぶ入門計量経済学](https://py4etrics.github.io)

<!-- 新聞，雑誌やインターネット上で「AI」，「ビッグデータ」，「機械学習」どのプログラミングに関連するキーワードを頻繁に見聞きすると思うが，それらの分野で`Python`は広く使われている。一方で`Python` -->

次の8章から構成されている。
1. **`Python`の基礎（その１）**<br>
  プログラミング言語である`Python`は，日本語と同様に文法・表現・単語が決まっており，それらの使い方を説明する。外国語を学ぶことと似た様なものかと不安になる人もいるかも知れないが，そうではない。殆どの人は英語を学んだと思うが，実は`Python`は英語で書かれているため，英語感覚でコードを読み書きすることができるのが一つの大きな利点である。しかし，英作文をイメージすると間違いである。理由は，正確性が要求されるからである。話し言葉・書き言葉は曖昧な表現になり得る。例えば，I kind of like him.（もしくは，I kinda like him.）ここでの"kind of"は「種類」と言う意味ではなく「曖昧さ」を表している。訳すと「まぁ，好きかなぁ，，，」の様なイメージだろうか。しかし，話すタイミングや語調によっては「実はそうでもないかも」の含みがある様にも聞こえるかも知れない。このように正確さにかける英語ではコンピュータに命令を伝えることは難しい。一般的にプログラミング言語は正確性が重視されるため，味気ない「文章」になる。更には少しでも間違えると「何言ってるか分かんない」という意味でエラーが発生する。一つのスペルミスでもエラーが発生するのである。この章では，「`Python`語」を使いコンピュータに正確に命令を伝えて実行させる方法を学習する。
1. **`Python`の基礎（その２）**<br>
  その１の内容はそれほど難しいとは感じないかも知れない。その２では`Python`の基礎をもう一歩踏み込んで解説する。特に，コードを書く上で欠かせない関数や`for`ループ，`if`文などを紹介する。今後より複雑なコードを書く上でその要となる概念なので，それらの仕組みを十分に理解することが重要となる。
1. **`NumPy`： 高速化**<br>
  インストールした`Python`をそのままの「素」で使うことができる。しかし用途によっては物足りないと感じる場合がある。「素」の`Python`を４人乗りの家族用乗用車とイメージしてみよう。通常の生活では十分だが，自動車レースに参加するとなると明らかに不十分である。目的によって機能を補ってくれるのがパッケージと呼ばれるもので，この章を含めて残りの章を使って主な（外部）パッケージについて説明する。`NumPy`（Numerical Pythonの略でナンパイと読む）は，名前が示すように計算を高速化させるパッケージであり，乗用車をレース用にチューンアップしてくれる。シミュレーションを行う際には欠かせないパッケージである。
1. **`Pandas`： データ分析**<br>
  データを扱う際に欠かせないパッケージである。イメージ的には，`Python`版のExcelと思えば良いだろう。名前は計量経済学の授業で出てきたパネル・データ（Panel Data）から派生した可愛らしい名前になっている。データを扱うのであれば`NumPy`で良いのではと思うかも知れない。実際，`Pandas`のデータの部分は`NumPy`の`array`と呼ばれるデータ型に簡単に変換できるようになっている。どこに利点があるかと言うと，行・列にラベル名（例えば，「Real GDP」）が使えるためデータの直感的な操作が可能となる。またデータを整形するのに便利な関数が多く用意されている。このパッケージ無ければデータを扱いが非常に面倒に感じる事になるだろう。
1. **`Matplotlib`： 図示**<br>
  データをプロット（図示）するためのパッケージである。`NumPy`，`Pandas`，`SciPy`と並んで`Python`のエコシステムを構成している。プロットするためのパッケージには様々なものが開発されているが，`Matplotlib`が基本となっている。プロットのためのコードには幾つかのパターンがあり，オブジェクト指向と呼ばれる考えに基づく方法を紹介する。
1. **`Pandas`： 図示**<br>
  上で紹介した`Pandas`にもプロットする機能が備わっている。裏では`Matplotlib`が動いているが，手っ取り早くプロットしたい場合に重宝する。図の細かい所まで設定したい場合は`Matplotlib`を直接使った方が良いが，`Pandas`のプロット機能を知っていると非常に便利に感じるだろう。
1. **`SciPy.stats`： 確率分布**<br>
  `SciPy`はScientific Pythonの略であり，科学技術計算用のパッケージである。非常に大きなパッケージであり，その中には様々な用途（積分，統計，最適化問題など）に合わせたサブパッケージが用意されている。その中の一つである統計学用の`scipy.stats`の使い方について簡単に説明する。統計学の授業で学んだ概念などを実際にコードを書いて実行することができる。ちなみに，`SciPy`には`NumPy`と重複する機能も含んでおり，仕様が微妙に違ったりする。このサイトと上述の経済学のサイトでは，`NumPy`にあるものは`NumPy`のものを使うことにする。
1. **`SciPy.optimize`： 解の求め方と最適化問題**<br>
  経済学では最適化問題が至る所で出てくる。消費者の効用最大化問題，企業の利潤最大化もしくは費用最小化問題など。`scipy.optimize`はそのためのツールを提供してくれる。また単なる最大化・最小化問題を数値的に解くのではなく，制約式の下での最適化問題も解くことが可能である。また等式制約と不等式制約の両方に対応している。経済学を勉強する上で欠かせないツールである。

また次のトピックについても取り上げているので参考にして欲しい。
* **ツールのインストールと説明**<br>
  Pythonやと関連ツール（GitやGitHubなど）のインストールと使い方について説明する。
* **Tipsと注意点**<br>
  コードを書く上で役に立つ点をまとめる。是非読んでみよう！
* **学業成績の分析**<br>
神戸大学のウリボーネット上にある成績を使い学業成績分析を行う。成績をコピーして使うので他大学でも使えるかもしれない？
* **Gapminder**<br>
  Gapminderは世界経済のGDPなどデータを駆使し興味深い分析をおこなっているサイトである。そのデータを使って，グループ別（例えば，アジア・欧州・アフリカなど）の計算を簡単に行うことができる`Pandas`の`groupby`の使い方と`Multi-index`を紹介する。


## 本サイトで使うPythonとパッケージのバージョン
```{code-cell} python3
import gapminder, matplotlib, numpy, pandas, scipy, see
from platform import python_version

packages = ['Python', 'gapminder', 'matplotlib', 'numpy','pandas', 'scipy','see']
versions = [python_version(), gapminder.__version__, matplotlib.__version__, numpy.__version__, pandas.__version__, scipy.__version__, see.__version__]

for pack, ver in zip(packages, versions):
    print('{0:14}{1}'.format(pack,ver))
```

---

[Economists（経済学を勉強する人も含めて(?)）と付き合わない方が良い２１＋$\alpha$の理由]( http://inesad.edu.bo/developmentroast/2012/10/21-reasons-why-you-should-never-date-an-economist/)

---

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Haruyama-KobeU/for_binder/main?filepath=for_binder.ipynb) for an interactive Jupyter Notebook session with empty code cells.
