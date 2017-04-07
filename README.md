# suwameter
すわわがハグしたい人メーター

 - Twitterから一定時間毎にすわわの画像を雑に検索します
 - あらかじめ学習させたAqours9人のうち画像に誰が写っているかをAIで判定します
 - すわわ以外の8人に対して、すわわと一緒に写っている画像の枚数を集計します
 - 一緒に写っている枚数が多いほどすわわと仲良しと判断します
 - ハグしてる写真への重み付けとかは特にありません
 
## Setup

以下Linuxで動作させることを前提にしています。なお運用環境はUbuntu 16.04 LTSです。

### 必要なもの

 - Python 2.7.x
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

`photo_url`は使ってません
以下のように初期値を入れておいてください（`name`だけあってれば他は変えても動きます）

```
+----+------------------+--------------------+-------------------+-----------+-------+
| id | name             | display_name       | display_full_name | photo_url | count |
+----+------------------+--------------------+-------------------+-----------+-------+
|  1 | anju_inami       | あんちゃん         | 伊波杏樹          | NULL      |    0 |
|  2 | rikako_aida      | りきゃこ           | 逢田梨香子        | NULL      |    0 |
|  3 | shuka_saito      | しゅかしゅー       | 斉藤朱夏          | NULL      |    0 |
|  4 | ai_furihata      | ふりりん           | 降幡愛            | NULL      |    0 |
|  5 | aika_kobayashi   | あいきゃん         | 小林愛香          | NULL      |    0 |
|  6 | kanako_takatsuki | きんぐ             | 高槻かなこ        | NULL      |    0 |
|  7 | arisa_komiya     | ありしゃ           | 小宮有紗          | NULL      |    0 |
|  8 | aina_suzuki      | あいにゃ           | 鈴木愛奈          | NULL      |    0 |
+----+------------------+--------------------+-------------------+-----------+-------+
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
 
#### suwawa

```
+-------+---------------+------+-----+---------+----------------+
| Field | Type          | Null | Key | Default | Extra          |
+-------+---------------+------+-----+---------+----------------+
| id    | int(11)       | NO   | PRI | NULL    | auto_increment |
| url   | varchar(1024) | NO   |     | NULL    |                |
+-------+---------------+------+-----+---------+----------------+
```
 
#### max_id
 
```
+-------+------------+------+-----+---------+-------+
| Field | Type       | Null | Key | Default | Extra |
+-------+------------+------+-----+---------+-------+
| id    | bigint(20) | NO   | PRI | NULL    |       |
+-------+------------+------+-----+---------+-------+
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
cronには`~/suwameter/api/clawler.py update`などと書いておきます。

### bot

crontabに`~/suwameter/api/bot.py`のように書いておくと適当にPostします。

```planintext
すわわがハグしたいのは・・・

1位 しゅかしゅー: 90
2位 あいにゃ: 84
3位 きんぐ: 71

すわわがハグしたい人メーター
suwameter.sato-t.net
#lovelive #lovelive_sunshine
```
