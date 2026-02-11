from __future__ import annotations

import json
from pathlib import Path


def main():
	data_json = Path("src/data.json")
	data = None

	with data_json.open() as f:
		data = json.load(f)
		f.close()

	for port_protocol in data["ports_protocols"]:
		print(port_protocol)

	for command_line in data["command_line"]:
		print(command_line)


if __name__ == "__main__":
	main()
