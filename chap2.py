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


if __name__ == '__main__':
    no10()