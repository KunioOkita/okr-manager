## chatgpt に出す指示

# 概要
* Pythonで flask フレームワークを利用し、OKR管理ツールのAPIを作成してください

# 仕様

## 基本設計

* OKRという目標管理フレームワークの管理ツール
* OKRの各データについて、CRUDできるAPIを用意する

## データ設計

以下のデータが必要です

* {Objective}: 目標
* {KeyResult}： キーリザルト
* {Member}：メンバ
* {Organaization}：組織

{Objective}は上位の{KeyResult}に紐づく場合があります
{KeyResult}は{Objective}に紐づきます。
{KeyResult}には{Member}が複数紐づきます
{Organaization}には{Member}が複数紐づきます。

## 出力結果

* サンプルコードおよび説明を出力してください。

## 制約

* Flaskフレームワークを利用してください
* model, routesはディレクトリを分けて、model毎にファイルを分けてください
* SQLiteを利用してください。
  
-----
key_result と member は 多対多にする必要があります。

-----
Organaizationは階層関係があります。


-----

-----
# {Objective}のCRUD仕様

## Create
入力される値

  Objectiveの名前
　組織ID

## Read

入力される値

  ObjectiveのID

## Update

入力される値

  ObjectiveのID
  Objectiveの名前

## Delete

入力される値

  ObjectiveのID

