import tkinter as tk


class Mainpage:
	def __init__(self):
		self.mainpage = tk.Tk()

		self.item_label = tk.Label(text="Item: ")
		self.item_entry = tk.Entry()

		self.model_label = tk.Label(text="Model: ")
		self.model_entry = tk.Entry()

		self.run_button = tk.Button(text="Run", command=self.run_command)


	def grid_features(self):
		self.item_label.grid(column=1, row=1)
		self.item_entry.grid(column=2, row=1)

		self.model_label.grid(column=1, row=2)
		self.model_entry.grid(column=2, row=2)

		self.run_button.grid(column=1, row=3)


	def run_command(self):
		"""returns True to the Run command"""
		return True
