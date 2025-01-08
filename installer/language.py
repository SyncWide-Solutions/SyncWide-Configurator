import os

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

BOLD = "\033[1m"
UNDERLINE = "\033[4m"

def python(os):
    if os == "linux":
        print(f"{YELLOW}Installing Python...{RESET}")
        os.system("sudo apt-get install python3 -y")
        print(f"{GREEN}Python installed successfully!{RESET}")

def nodejs(os):
    if os == "linux":
        print(f"{YELLOW}Installing NodeJS...{RESET}")
        os.system("sudo apt-get install nodejs -y")
        print(f"{GREEN}NodeJS installed successfully!{RESET}")

def php(os):
    if os == "linux":
        print(f"{YELLOW}Installing PHP...{RESET}")
        os.system("sudo apt-get install php -y")
        print(f"{GREEN}PHP installed successfully!{RESET}")

def install(os):
    what_programming_language = input(f"{YELLOW}Witch Programming Language do you want to install?{RESET}\r\n{RED}[1]{RESET} Python\r\n{RED}[2]{RESET} NodeJS\r\n{RED}[3]{RESET} PHP\r\n{RED}[4]{RESET} Exit\r\n")

    if what_programming_language == "1":
        python(os)
    elif what_programming_language == "2":
        nodejs(os)
    elif what_programming_language == "3":
        php(os)
    elif what_programming_language == "4":
        exit()
    else:
        print(f"{RED}Invalid choise!{RESET}")
        install()