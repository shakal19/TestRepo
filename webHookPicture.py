import requests
import os
import logging
from dotenv import load_dotenv

logging.basicConfig(
    filename="app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d - %b - %y %H:%M:%S",
    level=logging.ERROR,
)


def configure():
    """starts load_dotenv() function"""
    load_dotenv()


def WebHook(url: str):
    """
    Sends picture through discord webhook.
    url (str) - url of your discord webhook
    """

    for i in range(1, 4):
        try:
            with open(f"slika{i}.jpg", "rb") as f:
                # open("your picture", "rb") as f:...
                file = {"file": f}
                response = requests.post(url, files=file)
                if response.status_code != 200:
                    print(response.status_code)
        except FileNotFoundError:
            logging.error("FileNotFound Error happened!", exc_info=True)


def main():
    """Main part of the program

    Raises:
        ValueError: Raises valueError exception when token_id or channel id is None.
    """

    channel_id = os.getenv("webhook_id")
    token_id = os.getenv("webhook_token")
    if token_id is None or channel_id is None:
        raise ValueError("Channel_id or token_id is None! Check your .env file again.")

    configure()

    url = f"https://discord.com/api/webhooks/{channel_id}/{token_id}"
    WebHook(url)


if __name__ == "__main__":
    main()
