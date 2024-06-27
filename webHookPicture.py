import os
import sys
import logging
import requests
from dotenv import load_dotenv

logging.basicConfig(
    filename="app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d - %b - %y %H:%M:%S",
    level=logging.ERROR,
)


def configure():
    """Starts load_dotenv() function"""
    load_dotenv()


def WebHook(url: str):
    """
    Sends picture through discord webhook.
    url (str) - url of your discord webhook
    """
    sys.stderr = open("app.log", "a")
    sys.stdout = open("app.log", "a")

    for i in range(1, 4):
        try:
            with open(f"slika{i}.jpg", "rb") as f:
                file = {"file": f}
                response = requests.post(url, files=file)
                if response.status_code != 200:
                    sys.stderr.write(
                        f"Failed to send file slika{i}.jpg. HTTP status code: {response.status_code}\n"
                    )
                else:
                    sys.stdout.write(f"Successfully sent file slika{i}.jpg.\n")
        except FileNotFoundError:
            sys.stderr.write(f"File slika{i}.jpg not found\n")
            sys.stdout.write(f"File slika{i}.jpg not found\n")
        except Exception as e:
            logging.error("An error occurred", exc_info=True)

    sys.stderr.close()
    sys.stdout.close()


def main():
    """Main part of the program

    Raises:
        ValueError: Raises valueError exception when token_id or channel id is None.
    """
    configure()

    channel_id = os.getenv("webhook_id")
    token_id = os.getenv("webhook_token")
    if token_id is None or channel_id is None:
        raise ValueError("Channel_id or token_id is None! Check your .env file again.")

    url = f"https://discord.com/api/webhooks/{channel_id}/{token_id}"
    WebHook(url)


if __name__ == "__main__":
    main()
