# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json

import requests
import StockDataRetriever
import OpenAI


# Global API token
API_TOKEN = "PvtiPjUxowpaqJvpcMxo1vgZ9zArSMe2dXfxwJmr"


def get_stock_data(stock_ticker):
    # Define the API endpoint
    base_url = "https://api.stockdata.org/v1/data/quote"
    # Construct the URL with query parameters
    url = f"{base_url}?symbols={stock_ticker}&api_token={API_TOKEN}"

    try:
        # Make the GET request
        response = requests.get(url)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        # Parse the JSON response
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def format_json(data):
    return json.dumps(data, indent=4)


if __name__ == '__main__':
    #stocks = StockDataRetriever.StockDataRetriever()
    #print(stocks.get_stock_data("COF"))

    openai = OpenAI.OpenAIWrapper()

    response = openai.chat_completion("Hello!")

    # Extracting the 'content' field
    content = response.choices[0].message.content

    print(content)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
