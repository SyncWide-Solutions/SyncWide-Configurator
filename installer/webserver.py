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

def apache():
    print(f"{YELLOW}Installing Apache...{RESET}")
    os.system("sudo apt-get install apache2 -y")
    print(f"{GREEN}Apache installed successfully!{RESET}")

def nginx():
    print(f"{YELLOW}Installing Nginx...{RESET}")
    os.system("sudo apt-get install nginx -y")
    print(f"{GREEN}Nginx installed successfully!{RESET}")

def install():
    what_web_server = input(f"{YELLOW}Witch Web Server do you want to install?{RESET}\r\n{RED}[1]{RESET} Apache (recommended)\r\n{RED}[2]{RESET} Nginx\r\n{RED}[3]{RESET} Exit\r\n")

    if what_web_server == "1":
        apache()
    elif what_web_server == "2":
        nginx()
    elif what_web_server == "3":
        exit()
    else:
        print(f"{RED}Invalid choise!{RESET}")
        install()