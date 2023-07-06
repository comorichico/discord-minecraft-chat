# discord-minecraft-chat
discordとminecraftで相互チャットするやつだよ！minecraftのバニラサーバーで使えるよ

<img width="291" alt="2023-07-07 (3)" src="https://github.com/comorichico/discord-minecraft-chat/assets/96755854/9d10cfef-3b89-467d-8a65-415198fb4d6b">
<img width="1282" alt="2023-07-07 (2)" src="https://github.com/comorichico/discord-minecraft-chat/assets/96755854/b953d402-4c37-42bd-9882-5236ca308901">

使い方

Microsoft StoreからPython3.10をインストールする

gitをインストールする

コマンドプロンプト、PowerShell、ターミナルなどで以下のコマンドを打つ

git clone https://github.com/comorichico/discord-minecraft-chat.git

cd discord-minecraft-chat

pip install -r requirements.txt

sample.envのファイル名を.envに変更する

.envをメモ帳などで開いて編集する

tokenをdiscordのbotのトークンに置き換える

0000000000000000000を使用したいdiscordのチャンネルIDに置き換える

localhostはそのままでいいはず

passwordを何でもいいので複雑な文字列にする

25575はそのままでもいいし好きなポートに変更しても良い

C:/Users/user/minecraft-dir/logsは自分のminecraftのserver.jarのあるlogsフォルダを指定する

latest.logはそのままでいいはず

minecraftのserver.propertiesを編集する

rcon.port=25575（.envと同じポート番号にする）

enable-rcon=true

rcon.password=（.envと同じpasswordにする）

コマンドプロンプト、PowerShell、ターミナルなどを新規に開いて以下のコマンドを打つ

cd discord-minecraft-chat

python main.py

これでdiscordとminecraftで相互にチャットができるようになるはず

おつかれさまでした！
