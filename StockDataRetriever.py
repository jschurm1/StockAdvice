import requests
import json


class StockDataRetriever:
    # Private class variable for the API key
    __API_TOKEN = "PvtiPjUxowpaqJvpcMxo1vgZ9zArSMe2dXfxwJmr"

    def __init__(self):
        pass

    def get_stock_data(self, stock_ticker):
        """
        Public method to fetch stock data for a given ticker symbol.
        """
        base_url = "https://api.stockdata.org/v1/data/quote"
        url = f"{base_url}?symbols={stock_ticker}&api_token={self.__API_TOKEN}"

        try:
            # Make the GET request
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            # Return formatted JSON using the private formatting method
            return self.__format_json(data)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def __format_json(self, data):
        """
        Private method to format JSON data into a pretty-printed string.
        """
        return json.dumps(data, indent=4)

