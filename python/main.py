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


	def main(self):
		openapi.choose_model(model=self.model)

		openapi.get_item_data(item_name=self.item)

		openapi.run_ai()
		openapi.output_info()
		openapi.get_message_output()
		exit()


main = Main()
openapi = OpenAPI(max_tokens=300, model=main.model, item=main.item)


main.main()
