# suwameter
すわわがハグしたい人メーター

 - Twitterから一定時間毎にすわわの画像を雑に検索します
 - あらかじめ学習させたAqours9人のうち画像に誰が写っているかをAIで判定します
 - すわわ以外の8人に対して、すわわと一緒に写っている画像の枚数を集計します
 - 一緒に写っている枚数が多いほどすわわと仲良しと判断します
 - ハグしてる写真への重み付けとかは特にありません
 
## Setup
 
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
 
### Web API用モジュールのインストール
 
```
$ pip install falcon
$ pip install mysql-connector
$ pip install gnuicorn
```

### Angular用モジュールのインストール

```
$ cd www
$ npm install
```
 
### Apache

`www/src`をDocumentRootにしてください
