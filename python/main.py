from bazaarAPI import BazaarAPI
from openAPI import OpenAPI
from gui import Mainpage
import logging

mainpage = Mainpage()
openapi = OpenAPI(max_tokens=300)
bazaar = BazaarAPI()


logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.info("Logger setup complete")

mainpage.grid_features()
mainpage.mainpage.mainloop()


class Main:
	def __init__(self):
		pass


	def run_ai(self):
		if mainpage.run_command():
			openapi.run_ai()
			logger.info("openAI API successfully run")
			openapi.output_info()
			logger.info("Successfully output JSON info")
			openapi.get_message_output()
			logger.info("Successfully output JSON message content")
			exit()
		elif not mainpage.run_command():
			logger.error("Failed to run openAI API | mainpage.run_command() is False")
		else:
			logger.error("main run_ai() failed. Please contact developer for support")


main = Main()


main.run_ai()
