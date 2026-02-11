from __future__ import annotations

import json
import questionary
from pathlib import Path
from typing import List

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table


class CLI:
	def __init__(self) -> None:
		self.console: Console = Console()

		self.data_path: Path = Path("src/data.json")
		self.data = json.load(self.data_path.open())

		self.ports_protocols: List = self.data["ports_protocols"]
		self.command_line: List = self.data["command_line"]

	def display_welcome(self) -> None:
		self.console.print(
			Panel(
				"[bold cyan]CompTIA A+ Study Tool[/bold cyan]",
				expand=False,
				border_style="blue",
			)
		)

	def show_table(self, category: List) -> None:
		title = (
			"Ports & Protocols" if category == self.ports_protocols else "Command Line"
		)

		if title:
			table = Table(
				title=title,
				show_header=True,
				header_style="bold magenta",
				border_style="bright_black",
			)

			if title == "Ports & Protocols":
				table.add_column("Port #", style="cyan", width=4)
				table.add_column("Protocol Name", style="white")
				table.add_column("Default Transport", style="white")
				table.add_column("Description", justify="left", style="green")

				for item in category:
					table.add_row(
						str(item["port_number"]),
						str(item["protocol_name"]),
						str(item["default_transport"]),
						str(item["description"]),
					)
			else:
				table.add_column("Command", style="cyan", width=12)
				table.add_column("Utility", style="white")
				table.add_column("Common Switch", style="white")
				table.add_column("Scenario", justify="left", style="green")

				for item in category:
					table.add_row(
						str(item["command"]),
						str(item["utility"]),
						str(item["common_switch"]),
						str(item["scenario"]),
					)

			self.console.print(table)

	def main_prompt(self) -> None:
		rev_pp = "Review Ports & Protocols"
		rev_cl = "Review Command Line"

		task = questionary.select(
			"What would you like to do?",
			choices=[rev_pp, rev_cl, "Exit"],
			style=questionary.Style(
				[
					("qmark", "fg:#673ab7 bold"),
					("question", "bold"),
					("pointer", "fg:#673ab7 bold"),
					("highlighted", "fg:#673ab7 bold"),
					("selected", "fg:#cc5454"),
				]
			),
		).ask()

		if task == rev_pp:
			self.show_table(self.ports_protocols)
			self.main_prompt()
		elif task == rev_cl:
			self.show_table(self.command_line)
			self.main_prompt()
		elif task == "Exit":
			self.console.print("\n[bold]Thank you for studying today.[/bold]")

	def start(self) -> None:
		self.display_welcome()
		self.main_prompt()


if __name__ == "__main__":
	app = CLI()
	app.start()
