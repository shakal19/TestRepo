import os
import json
import requests
from dotenv import load_dotenv


def parsing_json(path: str) -> None:
    """
    Parsing json files

    Args:
        path (str): filename
    """
    try:

        with open(path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError as e:
        print("Exception message:", e)
    return None

def convert_to_json(files):
    """
    Converts python object to json format

    Args:
        files (list): a list with filenames

    Returns:
        python object: returns parsed combined json file
    """
    embeds = []
    for file in files:
        embed = parsing_json(file)
        embeds.append(embed)

    combined_json = {"embeds": embeds}
    with open("combined.json", "w",encoding="utf-8") as f_out:
        json.dump(combined_json, f_out, indent=4)

    data = parsing_json("combined.json")
    return data


def webhook_embed(url: str):
    """
    sends embed through webhook

    Args:
        url (str): webhook url
    """

    files = ["embed2.json", "embed3.json"]

    data = convert_to_json(files)

    response = requests.post(url, json=data, timeout=2.5)
    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(response.status_code)


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
