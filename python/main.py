from bazaarAPI import BazaarAPI
from openAPI import OpenAPI
from gui import Mainpage
import logging

mainpage = Mainpage()
openapi = OpenAPI(max_tokens=300, model=mainpage.model_entry.get(), item=mainpage.item_entry.get())
bazaar = BazaarAPI()


logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.info("Logger setup complete")


class Main:
	def __init__(self):
		pass


	def run_ai(self):
		if mainpage.run_command():
			openapi.run_ai()
			logger.info("openAI API successfully run")
			openapi.output_info()
		elif not mainpage.run_command():
			logger.error("Failed to run openAI API | mainpage.run_command() is False")
		else:
			logger.error("main run_ai() failed. Please contact developer for support")


	def main(self):
		self.run_ai()
		mainpage.mainpage.mainloop()


main = Main()

if __name__ == '__main__':
	main.main()
