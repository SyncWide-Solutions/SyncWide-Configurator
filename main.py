from installer import language, webserver, database

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

# Web Server
#   Apache (recommended)
#   Nginx
#
# Programming Languages
#   Python
#   NodeJS
#   PHP
#
# Databases
#   MySQL
#   MongoDB
#   PostgreSQL
#   SQLite

def start():
    start_choise = input(f"{YELLOW}What do you want to install?{RESET}\r\n{RED}[1]{RESET} Web Server\r\n{RED}[2]{RESET} Programming Languages\r\n{RED}[3]{RESET} Databases (Comming Soon!)\r\n{RED}[4]{RESET} Exit\r\n")

    if start_choise == "1":
        webserver.install()
    elif start_choise == "2":
        language.install()
    elif start_choise == "3":
        database.install()
    elif start_choise == "4":
        exit()
    else:
        print(f"{RED}Invalid choise!{RESET}")
        start()

if __name__ == "__main__":
    start()
