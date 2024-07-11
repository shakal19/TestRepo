import os
import json
import requests
from dotenv import load_dotenv


def webhook_embed(url: str):
    """
    sends embed through webhook

    Args:
        url (str): webhook url
    """

    with open("embed.json", "r") as f:
        data = json.load(f)

        response = requests.post(url, json=data)
        if response.status_code == 204:
            print("Message sent successfully")


def main() -> None:
    """
    Main function

    Raises:
        ValueError: when token or channel id is None, raises ValueError
    """

    load_dotenv()

    channel_id = os.getenv("channel_id")
    token_id = os.getenv("token_id")
    if token_id is None or channel_id is None:
        raise ValueError("Channel_id or token_id is None! Check your .env file again.")
    url = f"https://discord.com/api/webhooks/{channel_id}/{token_id}"
    webhook_embed(url)


if __name__ == "__main__":
    main()
