import requests
from dotenv import load_dotenv
import os


def configure():
    """ starts load_dotenv() function
    """
    load_dotenv()


def WebHook(url):
    """
        sends picture through discord webhook
    """

    for i in range(1, 3): 
        with open(f"picture{i}.ext", "rb") as f: # put your picture name here
            file = {'file': f}
            response = requests.post(url,files= file)
            if response.status_code != 200:
                print(response.status_code)

if __name__ == '__main__':
        channel_id = os.getenv('webhook_id')
        token_id = os.getenv('webhook_token')
        if token_id is None or channel_id is None:
            raise ValueError('Something is None')
        configure()
        url = f"https://discord.com/api/webhooks/{channel_id}/{token_id}"
        WebHook(url)
