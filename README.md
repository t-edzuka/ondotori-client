# おんどとりのデータにアクセスする例

API referenceを参考に
https://ondotori.webstorage.jp/docs/api/reference/devices_device.html
データの取得方法を実装した.

## 使い方

### 1. 依存関係インストール (開発用)

```shell
just install # https://github.com/casey/just <- How to install just command
```
もしくは直接 justファイルの中身を実行

### 2. アクセスするための情報を このプロジェクトルートの位置に.envファイルを作成する
```.dotenv
API_KEY="xxdfafega"
LOGIN_ID="xxx"
LOGIN_PASS="mypassword"
```

### 3. コマンドラインから実行する
```shell
python main.py
```
```shell
OndotoriResponse(devices=[])
```


