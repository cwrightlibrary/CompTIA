from __future__ import annotations

import time
import typer

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.progress import track
from rich.prompt import Prompt

app = typer.Typer()


class CLIApp:
	def __init__(self) -> None:
		self.console = Console()

	def print_banner(self) -> None:
		banner_text = """
    COMPTIA A+
    PROTOCOL v1.0"""
		panel = Panel(
			Text(banner_text, justify="center", style="bold magenta"),
			border_style="cyan",
			title="[ SYSTEM READY ]",
			subtitle="[ UNAUTHORIZED ACCESS PROHIBITED ]",
		)
		self.console.print(panel)

	def fake_loader(self, task_name: str) -> None:
		for _ in track(range(20), description=f"[green]{task_name}..."):
			time.sleep(0.05)

	def run_status(self):
		self.print_banner()
		self.fake_loader("Scanning Network")

		table = Table(title="System Status", border_style="green")
		table.add_column("Module", style="cyan", no_wrap=True)
		table.add_column("Status", style="magenta")
		table.add_column("Latency", justify="right", style="green")

		table.add_row("Core", "ONLINE", "12ms")
		table.add_row("Database", "CONNECTED", "4ms")  # Fixed typo "Databae"
		table.add_row("Security", "ACTIVE", "0ms")

		self.console.print(table)

	def run_connect(self, target: str) -> None:
		self.print_banner()
		self.console.print(
			f"[bold yellow]Initiating handshake with {target}...[/bold yellow]"
		)

		with self.console.status(
			"[bold green]Authenticating keys...[/bold green]", spinner="dots"
		):
			time.sleep(2)
			self.console.log("Keys verified.")
			time.sleep(1)
			self.console.log("Encryption established.")

		self.console.print(
			Panel(f"Connection to [bold]{target}[/bold] successful.", style="on green")
		)

	def run_interactive(self) -> None:
		self.print_banner()
		self.console.print("[dim]Type 'exit' to quit.[/dim]")

		while True:
			command = Prompt.ask(
				"[bold cyan]admin@openclaw[/bold cyan] [bold white]>[/bold white]"
			)
			if command == "exit":
				self.console.print("[red]Terminating session...[/red]")
				break
			elif command == "status":
				self.run_status()
			elif command == "help":
				self.console.print(
					"Available commands: status, connect, exit", style="yellow"
				)
			else:
				self.console.print(
					f"[red]Error:[/red] Command '{command}' not recognized."
				)


# 1. Instantiate the logic handler
cli = CLIApp()


# 2. Define the Typer commands as simple wrappers
@app.command()
def status():
	"""Check system health."""
	cli.run_status()


@app.command()
def connect(target: str = "127.0.0.1"):
	"""Connect to a remote terminal."""
	cli.run_connect(target)


@app.command()
def interactive():
	"""Enter the persistent shell."""
	cli.run_interactive()


if __name__ == "__main__":
	app()
