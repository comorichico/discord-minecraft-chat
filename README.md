# discord-minecraft-chat
discordとminecraftで相互チャットするやつだよ！minecraftのバニラサーバーで使えるよ

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
