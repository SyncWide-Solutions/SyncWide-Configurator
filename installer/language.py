import os
import zipfile
import requests

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

def python(ops):
    if ops == "linux":
        print(f"{YELLOW}Installing Python...{RESET}")
        os.system("sudo apt-get install python3 -y")
        print(f"{GREEN}Python installed successfully!{RESET}")
    elif ops == "windows":
        print(f"{YELLOW}Installing Python...{RESET}")
        os.system("winget install -e --id Python.Python.3.11")
        print(f"{GREEN}Python installed successfully!{RESET}")

def nodejs(ops):
    if ops == "linux":
        print(f"{YELLOW}Installing NodeJS...{RESET}")
        os.system("sudo apt-get install nodejs -y")
        print(f"{GREEN}NodeJS installed successfully!{RESET}")
    elif ops == "windows":
        print(f"{YELLOW}Installing NodeJS...{RESET}")
        os.system("winget install -e --id OpenJS.NodeJS")
        print(f"{GREEN}NodeJS installed successfully!{RESET}")

def php(ops):
    if ops == "linux":
        print(f"{YELLOW}Installing PHP...{RESET}")
        os.system("sudo apt-get install php -y")
        print(f"{GREEN}PHP installed successfully!{RESET}")
    if ops == "windows":
        try:
            print(f"{GREEN}Downloading PHP...{RESET}")
            # Using GitHub releases for faster download
            url = "https://windows.php.net/downloads/releases/php-8.4.2-nts-Win32-vs17-x86.zip"
            response = requests.get(url, stream=True, timeout=30)
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024 * 1024  # 1MB chunks
            downloaded = 0

            with open("php.zip", "wb") as file:
                for data in response.iter_content(block_size):
                    downloaded += len(data)
                    file.write(data)
                    done = int(50 * downloaded / total_size)
                    mb_downloaded = downloaded / (1024 * 1024)
                    total_mb = total_size / (1024 * 1024)
                    print(f"\r[{'█' * done}{'.' * (50-done)}] {mb_downloaded:.1f}MB/{total_mb:.1f}MB", end='', flush=True)
            print(f"\n{GREEN}Making PHP Directory...{RESET}") 
            os.system("mkdir C:/php")
            print(f"{GREEN}Unzipping The PHP File{RESET}")
            try:
                with zipfile.ZipFile("php.zip", "r") as zip_ref:
                    zip_ref.extractall("C:/php")
            except Exception as e:
                print(f"{RED}Error while unzipping PHP: {str(e)}{RESET}")
                return
        except Exception as e:
            print(f"{RED}Error while downloading PHP: {str(e)}{RESET}")
            return
            
        os.system("del php.zip")
        print(f"{GREEN}PHP installed successfully!{RESET}")
        
def install(ops):
    what_programming_language = input(f"{YELLOW}What Programming Language do you want to install?{RESET}\r\n{RED}[1]{RESET} Python\r\n{RED}[2]{RESET} NodeJS\r\n{RED}[3]{RESET} PHP\r\n{RED}[4]{RESET} Exit\r\n")

    if what_programming_language == "1":
        python(ops)
    elif what_programming_language == "2":
        nodejs(ops)
    elif what_programming_language == "3":
        php(ops)
    elif what_programming_language == "4":
        exit()
    else:
        print(f"{RED}Invalid choise!{RESET}")
        install()