from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table


class ExampleApp:
	def __init__(self) -> None:
		"""Initialize the console and app state."""
		self.console = Console()
		self.user_name = ""
		self.hardware_data = [
			{
				"acronym": "CPU",
				"def": "Central Processing Unit",
				"hint": "The primary chip",
			},
			{
				"acronym": "RAM",
				"def": "Random Access Memory",
				"hint": "Short-term storage",
			},
			{
				"acronym": "SSD",
				"def": "Solid-State Drive",
				"hint": "Fast flash storage",
			},
			{
				"acronym": "PSU",
				"def": "Power Supply Unit",
				"hint": "Voltage converter",
			},
		]

	def display_welcome(self) -> None:
		self.console.print(
			Panel(
				"[bold cyan]CompTIA A+ Tech Glossary Tool[/bold cyan]",
				expand=False,
				border_style="blue",
			)
		)

	def get_user_info(self) -> None:
		self.user_name = Prompt.ask(
			"[bold green]Enter your name[/bold green]",
			default="Technician",
		)
		self.console.print(
			f"\n[italic]Welcome, {self.user_name}. Initializing diagnostics...[/italic]\n"
		)

	def show_table(self) -> None:
		table = Table(
			title="System Components",
			show_header=True,
			header_style="bold magenta",
			border_style="bright_black",
		)

		table.add_column("Acronym", style="cyan", width=12)
		table.add_column("Definition", style="white")
		table.add_column("Hint", justify="right", style="green")

		for item in self.hardware_data:
			table.add_row(item["acronym"], item["def"], item["hint"])

		self.console.print(table)

	def run_diagnostics(self) -> None:
		is_stable = Prompt.ask(
			"Is the system stable?",
			choices=["yes", "no"],
			default="yes",
		)

		if is_stable == "no":
			self.console.print(
				"\n[bold white on red] !!! CRITICAL ERROR: BSOD DETECTED !!! [/bold white on red]"
			)
		else:
			self.console.print(
				"\n[bold green]All systems nominal. Happy troubleshooting![/bold green]"
			)

	def start(self) -> None:
		self.display_welcome()
		self.get_user_info()
		self.show_table()
		self.run_diagnostics()
