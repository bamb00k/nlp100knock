# -*- coding:utf-8 -*-
"""
    第2章: UNIXコマンドの基礎

    hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
    以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
    さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
"""

import subprocess

fname = "hightemp.txt"

# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
def no10():
    with open(fname, 'r') as f:
        lines = f.readlines()
        n_lines = sum([1 for line in lines])
        print('n_lines', n_lines)

    # UNIX command
    cmd = 'wc -l {}'.format(fname)
    print(subprocess.check_output(cmd, shell=True))


# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
def no11():
    with open(fname) as f:
        text = f.read().replace('\t', ' ')
        print(text)

    # UNIX command
    # sed -e "s/\t/ /g" hightemp.txt
    # cat hightemp.txt | tr '\t' ' '
    # expand -t 1 hightemp.txt


# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．
def no12():
    import pandas as pd

    df = pd.read_csv(fname, '\t', header=None)
    df[0].to_csv('col1.txt', index=False)
    df[1].to_csv('col2.txt', index=False)

    # Linuxコマンド
    # $ cut -f 1 hightemp.txt > col1.txt
    # $ cut -f 2 hightemp.txt > col2.txt

    # pandas を使わないパターン
    # with open(fname, 'r') as f:
    #     reader = csv.reader(f)
    #     with open('col1.txt', 'w') as f_col1, open('col2.txt', 'w') as f_col2:
    #         for row in reader:
    #             f_col1.write(row[0])
    #             f_col2.write(row[1])


# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目を
# タブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
def no13():
    import pandas as pd
    df1 = pd.read_csv('col1.txt', '\t', header=None)
    df2 = pd.read_csv('col2.txt', '\t', header=None)
    df = pd.concat([df1, df2], axis=1)
    df.to_csv('col_join.txt', '\t', index=False, header=None)

    # Linuxコマンド
    # $ paste col1.txt col2.txt > col_join.txt

    # pandas を 使わないパターン
    # f_col1 = open('col1.txt', 'r')
    # f_col2 = open('col2.txt', 'r')
    #
    # with open('col_join.txt', 'w') as f:
    #     for col1, col2 in zip(f_col1, f_col2):
    #         f.write("{}\t{}\n".format(col1.rstrip(), col2.rstrip()))


if __name__ == '__main__':
    no13()