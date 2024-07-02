import requests
from dotenv import load_dotenv
import os

def configure():
    """Starts load_dotenv() function"""
    load_dotenv()

def webHook(n: int, x: int, url: str):
    """
    Creating a webhook when number i can be diveded with x

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
            
            if response.status_code != 204:
                print(response.status_code)
                
configure()

channel_id = os.getenv('webhook_id')
webhook_token = os.getenv('webhook_token')

if channel_id is None or webhook_token is None:
    raise ValueError("Channel id or webhook token is None! Check your .env file!")

url = f"https://discord.com/api/webhooks/{channel_id}/{webhook_token}"


webHook(10, 3,url)
