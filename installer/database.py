import os
import secrets
import string

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

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def install(ops):
    if ops == "linux":
        print(f"{YELLOW}Installing MySQL server...{RESET}")
        os.system("sudo apt-get install mysql-server -y")

        print(f"{YELLOW}Starting MySQL server...{RESET}")
        os.system("sudo systemctl start mysql")

        mysql_root_password = generate_password()

        print(f"{YELLOW}Setting up MySQL...{RESET}")
        os.system(f"sudo mysql -e \"SET PASSWORD FOR 'root'@'localhost' = PASSWORD('{mysql_root_password}'); FLUSH PRIVILEGES;\"")

        print(f"{YELLOW}Installing Apache...{RESET}")
        os.system("sudo apt-get install apache2 -y")

        print(f"{YELLOW}Starting Apache...{RESET}")
        os.system("sudo systemctl start apache2")
        os.system("sudo systemctl enable apache2")

        print(f"{YELLOW}Installing phpMyAdmin...{RESET}")
        os.system("sudo apt-get install phpmyadmin -y")

        print(f"{YELLOW}Restarting Apache...{RESET}")
        os.system("sudo systemctl restart apache2")

        print(f"{GREEN}MySQL installed successfully!{RESET}")
        print(f"{GREEN}MySQL username: root{RESET}")
        print(f"{GREEN}MySQL password: {mysql_root_password}{RESET}")
        print(f"{GREEN}phpMyAdmin URL: http://localhost/phpmyadmin{RESET}")
        return 0

    elif ops == "windows":
        print(f"{YELLOW}Comming Soon!{RESET}")