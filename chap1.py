# -*- coding:utf-8 -*-
"""
    第１章準備運動
"""

# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
def no00():
    str = "stressed"
    print(str[::-1])

# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
def no01():
    str = "パタトクカシーー"
    print(str[::2])

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
def no02():
    word1 = "パトカー"
    word2 = "タクシー"
    str = [w1 + w2 for w1, w2 in zip(word1, word2)]
    print("".join(str))

# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を
# 単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
def no03():
    text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    text = text.replace(',', '').replace('.', '')
    print([len(w) for w in text.split()])


# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine.
# New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
def no04():
    text = "Hi He Lied Because Boron Could Not Oxidize Fluorine." \
           " New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    words = text.replace(".", "").split()
    single = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    elements = {}

    for idx, word in enumerate(words, start=1):
        if idx in single:
            elements[word[:1]] = idx
        else:
            elements[word[:2]] = idx

    print(elements)


# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
def gen_n_gram(seq, n):
    n_gram = []
    for i in range(len(seq) - n + 1):
        n_gram.append(seq[i:i + n])
    return n_gram

def no05():
    n = 2

    # 文字bi-gram
    text = "I am an NLPer"
    print(gen_n_gram(text, n))

    # 単語bi-gram
    words = text.split()
    print(gen_n_gram(words, n))


# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
import copy
def no06():
    x_text = "paraparaparadise"
    y_text = "paragraph"
    X = set(gen_n_gram(x_text, 2))
    Y = set(gen_n_gram(y_text, 2))
    print('X', X)
    print('Y', Y)

    # 和集合
    # print('X+Y', X.union(Y))
    print('X+Y', X | Y)

    # 積集合
    # print('X*Y', X.intersection(Y))
    print('X*Y', X & Y)

    # 差集合
    # print('X-Y', X.difference(Y))
    print('X-Y', X - Y)
    # print('Y-X', Y.difference(X))
    print('Y-X', Y - X)

    # "se"
    print('"se" within X :', "se" in X)
    print('"se" within Y :', "se" in Y)


# 07. テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
def template(x, y, z):
    return "{}時の{}は{}".format(x, y, z)

def no07():
    print(template(x=12, y="気温", z=22.4))


if __name__ == '__main__':
    no07()