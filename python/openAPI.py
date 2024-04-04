from openai import OpenAI
from bazaarAPI import BazaarAPI
import logging

bazaar = BazaarAPI()
client = OpenAI()

logger = logging.getLogger("openAPI")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.info("Logger setup complete")


class OpenAPI:
	def __init__(self, model, instructions, item, max_tokens):
		self.model = model
		self.instructions = instructions
		self.item = item
		self.max_tokens = max_tokens


	def choose_model(self, model):
		models = {"3.5": "gpt-3.5-turbo-0125", "4": "gpt-4-0125-preview"}
		for _ in models:
			if model == "3.5":
				logger.info("Model gpt-3.5-turbo-0125 selected")
				return models["3.5"]
			elif model == "4":
				logger.info("Model gpt-4-0125-preview selected")
				return models["4"]
			else:
				raise Exception("Invalid Model. Please choose either 3.5 or 4")


	def get_item_data(self, item_name):
		data = bazaar.get_bazaar_data()
		products = data.get('products', {})
		item_data = products.get(item_name)
		if item_data:
			logger.info(f"Item {item_name} data successfully received")
			return item_data
		else:
			raise Exception("Item not found")
