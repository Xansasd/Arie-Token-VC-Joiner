import json
import time
import ssl
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor

server_id = input("[?] Sunucu ID'yi girin: ").strip()
channel_id = input("[?] Ses Kanalı ID'yi girin: ").strip()

def get_input(prompt):
    return input(prompt).strip().lower() == 'y'

mute = get_input("[?] Mikrofona mute atılsın mı? (y/n): ")
deaf = get_input("[?] Kulaklık sağırlık (deaf) açılsın mı? (y/n): ")
stream = get_input("[?] Yayın (stream) açılsın mı? (y/n): ")
video = get_input("[?] Kamera açılsın mı? (y/n): ")

try:
    with open("tokens.txt", "r") as file:
        tokenlist = [line.strip() for line in file.readlines() if line.strip()]
    print(f"[INFO] {len(tokenlist)} token yüklendi.")
except FileNotFoundError:
    print("[!] Hata: tokens.txt dosyası bulunamadı!")
    exit()

if not tokenlist:
    print("[!] Hata: tokens.txt dosyasında geçerli bir token bulunamadı!")
    exit()

executor = ThreadPoolExecutor(max_workers=70)  

def connect_to_vc(token):
    while True:
        try:
            ws = WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=8&encoding=json", sslopt={"cert_reqs": ssl.CERT_NONE})

            hello = json.loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval'] / 1000  

            ws.send(json.dumps({
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {
                        "$os": "windows",
                        "$browser": "Discord",
                        "$device": "desktop"
                    }
                }
            }))

            ws.send(json.dumps({
                "op": 4,
                "d": {
                    "guild_id": server_id,
                    "channel_id": channel_id,
                    "self_mute": mute,
                    "self_deaf": deaf,
                    "self_stream": False,  
                    "self_video": False  
                }
            }))

            ws.send(json.dumps({
                "op": 18,
                "d": {
                    "type": "guild",
                    "guild_id": server_id,
                    "channel_id": channel_id,
                    "preferred_region": "singapore"
                }
            }))

            print(f"[✔] Token {token[:5]}... ile VC'ye katıldı!")

         
            while True:
                ws.send(json.dumps({"op": 1, "d": None}))  
                time.sleep(heartbeat_interval * 0.9)  

        except Exception as e:
            print(f"[!] Token {token[:5]}... bağlantı kesildi, tekrar bağlanıyor: {e}")
            time.sleep(5)  


for index, token in enumerate(tokenlist):
    executor.submit(connect_to_vc, token)
    time.sleep(2)  

input("\n[✔] VC Spammer çalışıyor! Durdurmak için ENTER'a bas.")
