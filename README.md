# SSH Brute Force Tool

This tool attempts to brute-force SSH passwords for a given username and target website using a list of passwords.

## Description

This Python script leverages the Paramiko library to try and connect to an SSH server with a specified username and a list of passwords. It is designed to test the security of SSH servers by attempting to authenticate using common or guessed passwords. Please use this tool responsibly and only on systems where you have permission to do so.

## Features

- Uses Paramiko for SSH connections.
- Accepts a list of passwords from a file.
- Reports successful and unsuccessful login attempts.
- Handles connection errors gracefully.

## Prerequisites

Before you can run this tool, you need to have Python installed on your system along with the following Python libraries:
- `paramiko` for SSH connections
- `termcolor` for colored terminal output

## Installation

First, ensure you have Python installed on your system. Then, install the required libraries using pip:

```bash
pip install paramiko termcolor
```

## Usage
To use this tool, follow these steps:

* Clone this repository or download the script to your local machine.
* Prepare a text file containing potential passwords, one per line.
* Run the script from your terminal

When prompted, enter the username, path to your passwords file, and the target website (in the format www.example.com).
Please note: This tool is for educational purposes only. Do not attempt to test systems without explicit permission from the owners.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Disclaimer
This tool is provided for educational use only. Any misuse of this software will not be the responsibility of the author or any contributors.
