import logging.config
import os
import sys
import logging
import requests
from dotenv import load_dotenv



logging.config.fileConfig("logging_config.ini")
logger = logging.getLogger("my_logger")


class StreamToLogger:
    def __init__(self, logger, log_level):
        self.logger = logger  
        self.log_level = log_level 
        self.linebuf = ""  

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        pass


def configure():
    """Starts load_dotenv() function"""
    load_dotenv()


def WebHook(url: str):
    """
    Sends picture through discord webhook.
    url (str) - url of your discord webhook
    """
   

    for i in range(1, 4):
        try:
            with open(f"slika{i}.jpg", "rb") as f:
                file = {"file": f}
                response = requests.post(url, files=file)
                
        except FileNotFoundError:
            sys.stderr.write(f"File slika{i}.jpg not found\n")
        


def main():
    """Main part of the program

    Raises:
        ValueError: Raises valueError exception when token_id or channel id is None.
    """
    configure()

    sys.stdout = StreamToLogger(logger,logging.INFO)
    sys.stderr = StreamToLogger(logger,logging.ERROR)

    channel_id = os.getenv("webhook_id")
    token_id = os.getenv("webhook_token")
    if token_id is None or channel_id is None:
        raise ValueError("Channel_id or token_id is None! Check your .env file again.")

    url = f"https://discord.com/api/webhooks/{channel_id}/{token_id}"
    WebHook(url)


if __name__ == "__main__":
    main()
