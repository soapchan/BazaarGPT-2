from bazaarAPI import BazaarAPI
from openAPI import OpenAPI
import logging

bazaar = BazaarAPI()


logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.info("Logger setup complete")


class Main:
	def __init__(self):
		self.model = input("Choose a model: ")
		self.item = input("Choose an item: ")
		self.debug_mode = True


	def main(self):
		"""The main function"""
		if not self.debug_mode:
			self.choose_model()

			openapi.get_item_data(item_name=self.item, debug_mode=False)

			openapi.response_runner()
			openapi.output_info()
		elif self.debug_mode:
			openapi.retrieve_key_data()


	def choose_model(self):
		"""The model selection"""
		models = {"3.5": "gpt-3.5-turbo-0125", "4": "gpt-4-0125-preview"}
		for _ in models:
			if self.model == "3.5":
				logger.info("Model gpt-3.5-turbo-0125 selected")
				return models["3.5"]
			elif self.model == "4":
				logger.info("Model gpt-4-0125-preview selected")
				return models["4"]


main = Main()
openapi = OpenAPI(max_tokens=300, model=main.choose_model(), item=main.item)


main.main()
