from openai import OpenAI

load_dotenv()


class OpenAPI:
	def __init__(self, model, instructions, item, max_tokens):
		self.client = OpenAI()
		self.model = model
		self.instructions = instructions
		self.item = item
		self.max_tokens = max_tokens
