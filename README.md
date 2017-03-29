# suwameter
すわわがハグしたい人メーター

 - Twitterから一定時間毎にすわわの画像を雑に検索します
 - あらかじめ学習させたAqours9人のうち画像に誰が写っているかをAIで判定します
 - すわわ以外の8人に対して、すわわと一緒に写っている画像の枚数を集計します
 - 一緒に写っている枚数が多いほどすわわと仲良しと判断します
 - ハグしてる写真への重み付けとかは特にありません
 
## Setup

以下Linuxで動作させることを前提に記述します。

### 必要なもの

 - Python
 - MySQL
 - Apache
 - node
 - npm

### MySQL
 
セットアップに使ったSQLどっかいったので・・・
 
#### member
 
```
+-------------------+--------------+------+-----+---------+-------+
| Field             | Type         | Null | Key | Default | Extra |
+-------------------+--------------+------+-----+---------+-------+
| id                | int(11)      | NO   | PRI | NULL    |       |
| name              | varchar(32)  | NO   |     | NULL    |       |
| display_name      | varchar(32)  | NO   |     | NULL    |       |
| display_full_name | varchar(32)  | NO   |     | NULL    |       |
| photo_url         | varchar(255) | YES  |     | NULL    |       |
| count             | int(11)      | YES  |     | NULL    |       |
+-------------------+--------------+------+-----+---------+-------+
```

#### photo

```
+-------+---------------+------+-----+---------+----------------+
| Field | Type          | Null | Key | Default | Extra          |
+-------+---------------+------+-----+---------+----------------+
| id    | int(11)       | NO   | PRI | NULL    | auto_increment |
| name  | varchar(32)   | NO   |     | NULL    |                |
| url   | varchar(1024) | NO   |     | NULL    |                |
+-------+---------------+------+-----+---------+----------------+
 ```
 
### Web API用Pythonモジュールのインストール
 
```
$ pip install falcon
$ pip install mysql-connector
$ pip install gnuicorn
```

### Angular用Nodeモジュールのインストール

```
$ cd www
$ npm install
```

### コンパイル

```
$ cd www
$ npm run build
```

`/usr/bin/env: ‘node’: No such file or directory`とか言われたら

```
$ ln -s /usr/bin/nodejs /usr/bin/node
```
 
### Apache

`www/src`をDocumentRootにしてください

mod_rewriteを有効にしてください

### アプリケーションの設定

`api/facesearch/constants.py`と`api/dbconf.py`をそれぞれの`.exapmple`を参考に作成してください
## 実行

### Web API

```
$ cd api
$ gunicorn -b 0.0.0.0:8000 resources:api
```

### クローラの初回実行

```
$ cd api
$ ./clawler.py init
```

パラメータに`init`を指定すると初期データ用に1000件（くらい）、それ以外を適当に指定すると前回取得からの差分を取得します。
cronには`./clawler.py update`などと書いておきます。
