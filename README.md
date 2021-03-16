# fixpointプログラミング試験

設問ごとにquestion1 ~ 4のプログラムを作成しました。<br>
ログデータのサンプルとしてlog_data.txtを同ディレクトリに用意しました。<br>

## プログラム実行について
Python3環境での動作を想定しています。<br>
右上の緑色のボタンでリポジトリをコピーしたのち、各設問に応じたコマンドでプログラムが実行できます。<br>

## question1
### 実行コマンド
```
python question1.py
```
### 説明
設問1。<br>
logファイルを読み込み、初めてタイムアウトを確認した日付、復旧した日付を出力するプログラムです。<br>
```
Breakdown ip:{故障したサーバーのIP} {故障した日付}
Restoration ip:{故障したサーバーのIP} {復旧した日付}
```
上記のフォーマットで結果が出力されます。

### 実行結果
サンプルデータ(log_data.txt)を読み込みquestion1.pyを実行した結果は以下の通りです。
応答結果がタイムアウトしたサーバーのipと日付がそれぞれ出力されています。
```
kazuaki$ /opt/anaconda3/bin/python /Users/kazuaki/job_hunting/fixpoint/question1.py
Breakdown ip:10.20.30.1/16 2020/10/19 13:33:24
Restoration ip:10.20.30.1/16 2020/10/19 13:33:44
Breakdown ip:10.20.30.2/16 2020/10/19 13:33:35
Restoration ip:10.20.30.2/16 2020/10/19 13:33:45
```

## question2
### 実行コマンド
```
python question2.py
N
```
プログラム実行後、上記の形式でパラメータNの値となる整数値を入力してください。

### 説明
設問2。<br>
pingのタイムアウトがN回以上計測されたサーバーのIP、初めてタイムアウトを確認した日付、復旧した日付を出力するプログラムです。<br>
出力のフォーマットは設問1と同じです。<br>


### 実行結果
サンプルデータ(log_data.txt)を読み込みプログラムを実行した結果は以下の通りです。
なお結果は、引数Nを2とした時のものです。
応答結果が2回以上タイムアウトしたipのみが出力されています。
```
kazuaki$ /opt/anaconda3/bin/python /Users/kazuaki/job_hunting/fixpoint/question2.py
2
Breakdown ip:10.20.30.1/16 2020/10/19 13:33:24
Restoration ip:10.20.30.1/16 2020/10/19 13:33:44
```

## question3
### 実行コマンド
```
python question3.py
N
m t
```
プログラム実行後、上記の形式でパラメータN,m,tの値となる整数値を入力してください。

### 説明
設問3。<br>
設問2の故障したサーバーについての情報に加え、各サーバーごとに直近m回のpingの平均応答時間を求め、t以上の場合を過負荷状態とし、初めて過負荷状態を確認した日付、負荷状態を回復した日付を出力するプログラムです。
```
Breakdown ip:{故障したサーバーのIP} {故障した日付}
Restoration ip:{復旧したサーバーのIP} {復旧した日付}
Overload ip:{過負荷状態のサーバーのIP} {過負荷状態を確認した日付}
Load Reduction ip:{負荷状態を回復したサーバーのIP} {負荷状態を回復した日付}
```
上記のフォーマットで結果が出力されます。

### 実行結果
サンプルデータ(log_data.txt)を読み込みプログラムを実行した結果は以下のようになりました。
なお結果は引数N,m,tを2,2,200とした時のものです。
```
kazuaki$ /opt/anaconda3/bin/python /Users/kazuaki/job_hunting/fixpoint/question3.py
2
2 200
Overload ip:10.20.30.1/16 2020/10/19 13:32:24
Breakdown ip:10.20.30.1/16 2020/10/19 13:33:24
Restoration ip:10.20.30.1/16 2020/10/19 13:33:44
```