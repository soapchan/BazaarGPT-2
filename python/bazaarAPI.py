import requests
from dotenv import load_dotenv
import os

load_dotenv()


class BazaarAPI:
    def __init__(self):
        self.api_key = os.getenv("HYPIXEL_KEY")

    def get_bazaar_data(self):
        response = requests.get(f"https://api.hypixel.net/skyblock/bazaar?key={self.api_key}")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch Bazaar data")

    def get_item_data(self, item_name):
        data = self.get_bazaar_data()
        products = data.get('products', {})
        item_data = products.get(item_name)
        if item_data:
            return item_data
        else:
            raise Exception("Item not found")
