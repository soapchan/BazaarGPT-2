from openai import OpenAI
from bazaarAPI import BazaarAPI
import logging

bazaar = BazaarAPI()
client = OpenAI()

logger = logging.getLogger("openAPI")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.info("Logger setup complete")


instructions = ("You are a helpful assistant designed to review and explain the trends of the "
				"item in the json provided that has information of the item in the hypixel skyblock bazaar. "
				"You are to describe and analyse the current statistics of the item in a way that is easy to"
				" understand and creates a clear and concise info report on the item stats. You must also use logic and"
				" advanced reasoning to determine if the item economy could be falsely manipulated."
				"Once the user sends the data, you must respond with the prior instructions, but in the format of"
				"This entire response must be formatted in .md format, and at the very bottom of the output"
				" must be a disclaimer"
				"saying \"This was generated by a chatGPT API, coded by Mrmii321/Soapchan\". You must strictly follow"
				" all conventions listed above."
				"The template you are required to use for the response is:"
				"```md"
				"#{item_name}"
				"### Sell:"
				"- Lowest price: {lowest_sell_price} coins | {sell_quantity_lowest} available"
				"- Highest price: {highest_sell_price} coins | {sell_quantity_highest} available"
				"- Total volume: {total_sell_volume}"
				"#### {Short description of sell data (20 words)}"
				"### Buy:"
				"- Highest price: {highest_buy_price} coins | {buy_quantity_highest} available"
				"- Lowest price: {lowest_buy_price} coins | {buy_quantity_lowest} available"
				"- Total volume: {total_buy_volume}"
				"#### {Short description of buy data (20 words)}"

				"### Overall Analysis:"
				"- The ratio of buy_price:sell_price is {lowest_buy}:{highest_sell ratio}."
				"- There is a {accurate description of cost difference} between the highest buy and lowest sell prices."
				"- {Explain why or why not it would or wouldn't be profitable to perform bazaar flipping on this item}"
				"#### {Short description of overall data (50 words)}"
				"BazaarGPT is brought to you by Mrmii32/Soapchan```. ")


class OpenAPI:
	def __init__(self, max_tokens, model, item):
		self.model = model
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


	def get_item_data(self, item_name):
		data = bazaar.get_bazaar_data()
		products = data.get('products', {})
		item_data = products.get(item_name)
		if item_data:
			logger.info(f"Item {item_name} data successfully received")
			return item_data
		else:
			raise Exception(f"Item ({item_name}) not found")


	def run_ai(self):
		response = client.chat.completions.create(
			model="gpt-3.5-turbo-0125",
			messages=[
				{"role": "system", "content": f"{instructions}"},
				{"role": "user", "content": f"The json data is {self.item}."}
			],
			max_tokens=self.max_tokens,
		)
		logger.info("openAI API call complete")
		return response


	def output_info(self):
		"""gets the output json"""
		try:
			response = self.run_ai()
			json_response = response.model_dump_json(indent=4)
			logger.info("Converted API output into JSON")
		except Exception as e:
			logger.error("Failed to convert API output into JSON")

		print(json_response)
		return json_response


	def get_message_output(self):
		"""retrieves the message for the client"""
		message = self.output_info().choices[0].message.content
		print(message)
		return message
