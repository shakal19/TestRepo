import requests
# from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def WebHook(n: int, x: int, url: str):
    """Creating a webhook when number i can be diveded with x

    Args:
        n (int): upper bound
        x (int): number , divisor
    """
    for i in range(1, n):
        if i % x == 0:
            message = (f"Number {i} can be divided with {x}")
            
            send_info = {
                "content": message
            }
            header = {
                "content-type" : "application/json"
            }
            response = requests.post(url,json=send_info,headers=header)
            # print(response.status_code)
            
            if response.status_code != 204:
                print('Error has occured')
                
configure()
url = f"https://discord.com/api/webhooks/{os.getenv('webhook_id')}/{os.getenv('webhook_token')}"
# webhook = DiscordWebhook(url=url,content="New message!")
# response = webhook.execute()

WebHook(10, 3,url)
