import os
import re
import time
from mcrcon import MCRcon
import discord
from dotenv import load_dotenv
from discord.ext import tasks
from concurrent.futures import ThreadPoolExecutor
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers.polling import PollingObserver

load_dotenv()

discord_bot_token = os.environ["DISCORD_BOT_TOKEN"]
channel_id = int(os.environ["CHANNEL_ID"])
server_address = os.environ["SERVER_ADDRESS"]
rcon_password = os.environ["RCON_PASSWORD"]
rcon_port= int(os.environ["RCON_PORT"])
target_dir = os.environ["TARGET_DIR"]
target_file = os.environ["TARGET_FILE"]

client = discord.Client(intents=discord.Intents.all())

message_list = []

def SendMessage(message: str) -> None:
    message_list.append(message)
    print(message)

def MessageCreation(text: str):
    # 参加,退出以外のメッセージが必要な場合はここに書く

    mach = re.findall(r"<(\w+)> (.+)", text)
    if mach:
        replacement = f"{mach[0][0]}: {mach[0][1]}"
        return replacement

    mach = re.findall(": (.*) joined the game", text)
    if len(mach) == 1:
        return str(mach[0]) + " が参加しました"

    mach = re.findall(": (.*) left the game", text)
    if len(mach) == 1:
        return str(mach[0]) + " が退出しました"
    
    return None

def GetLog(filepath: str):
    # 最終行のテキストを取得
    with open(filepath, "r") as f:
        endtxt = f.readlines()[-1]

    # 送信メッセージ作成
    text = MessageCreation(endtxt)

    if text is not None:
        SendMessage(text)

class ChangeHandler(FileSystemEventHandler):
    # フォルダ変更時のイベント
    def on_modified(self, event):
        filepath = event.src_path

        # ファイルでない場合無視する
        if os.path.isfile(filepath) is False:
            return

        # 監視対応のファイルでない場合無視する
        filename = os.path.basename(filepath)
        if filename != target_file:
            return

        GetLog(filepath)

@tasks.loop(seconds=0.2)
async def printer():
    global message_list
    if len(message_list) > 0:
        channel = client.get_channel(channel_id)
        await channel.send(message_list.pop(0))

@printer.before_loop
async def before_printer():
    print('waiting...')
    await client.wait_until_ready()

# bot起動準備完了
@client.event
async def on_ready():
    print(f'{client.user.name}がログインしました。')
    printer.start()

# discordでメッセージを受信した時の処理
@client.event
async def on_message(message):

    # 自分自身には反応しない
    if message.author == client.user:
        return
    
    # 指定のチャンネル以外では反応しない
    if message.channel.id != channel_id:
        return
    
    # discordのメッセージをminecraft内に送る
    with MCRcon(server_address, rcon_password, rcon_port) as mcr:
        name = ""
        if message.author.nick:
            name = message.author.nick
        else:
            name = message.author.global_name
        print(name + ":" + message.content)
        log=mcr.command("/say " + name + ":" + message.content)
        print(log)

# 監視
def watching():
    while 1:
        event_handler = ChangeHandler()
        observer = PollingObserver()
        observer.schedule(event_handler, target_dir, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

# bot起動
def discordbot():
    client.run(discord_bot_token)

# main処理
if __name__ in "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        a = executor.submit(watching)
        b = executor.submit(discordbot)
        print(a.result())
        print(b.result())
    
    