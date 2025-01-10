import os
import threading
import zipfile
import requests
from tqdm import tqdm

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
        return 0
    elif ops == "windows":
        print(f"{YELLOW}Installing Python...{RESET}")
        os.system("winget install -e --id Python.Python.3.11")
        print(f"{GREEN}Python installed successfully!{RESET}")
        return 0

def nodejs(ops):
    if ops == "linux":
        print(f"{YELLOW}Installing NodeJS...{RESET}")
        os.system("sudo apt-get install nodejs -y")
        print(f"{GREEN}NodeJS installed successfully!{RESET}")
        return 0
    elif ops == "windows":
        print(f"{YELLOW}Installing NodeJS...{RESET}")
        os.system("winget install -e --id OpenJS.NodeJS")
        print(f"{GREEN}NodeJS installed successfully!{RESET}")
        return 0

# Shared variable to track download progress
downloaded_size = 0
download_lock = threading.Lock()

def download_chunk(url, start, end, part_file, progress_bar):
    global downloaded_size
    headers = {"Range": f"bytes={start}-{end}"}
    with requests.get(url, headers=headers, stream=True) as response:
        with open(part_file, "wb") as f:
            for chunk in response.iter_content(1024):  # 1KB chunks
                if chunk:
                    f.write(chunk)
                    with download_lock:
                        downloaded_size += len(chunk)
                        progress_bar.update(len(chunk))

def parallel_download_with_progress(url, output_file, num_threads=4):
    global downloaded_size
    # Get file size
    response = requests.head(url)
    file_size = int(response.headers.get("content-length", 0))
    if file_size == 0:
        print("Failed to retrieve file size.")
        return False

    # Divide file size into chunks
    chunk_size = file_size // num_threads
    threads = []
    part_files = []

    # Progress bar setup
    with tqdm(total=file_size, unit="B", unit_scale=True, desc="Downloading PHP") as progress_bar:
        # Start threads for downloading chunks
        for i in range(num_threads):
            start = i * chunk_size
            end = start + chunk_size - 1 if i < num_threads - 1 else file_size - 1
            part_file = f"part_{i}.tmp"
            part_files.append(part_file)
            thread = threading.Thread(target=download_chunk, args=(url, start, end, part_file, progress_bar))
            threads.append(thread)
            thread.start()

        # Wait for threads to complete
        for thread in threads:
            thread.join()

    # Merge chunks
    with open(output_file, "wb") as output:
        for part_file in part_files:
            with open(part_file, "rb") as part:
                output.write(part.read())
            os.remove(part_file)

    print("Download completed!")
    return True

# Update the PHP installer script
def php(ops):
    if ops == "linux":
        print(f"{YELLOW}Installing PHP...{RESET}")
        os.system("sudo apt-get install php -y")
        print(f"{GREEN}PHP installed successfully!{RESET}")
        return 0

    if ops == "windows":
        try:
            url = "https://windows.php.net/downloads/releases/php-8.4.2-nts-Win32-vs17-x86.zip"
            output_file = "php.zip"
            
            print(f"{GREEN}Downloading PHP{RESET}")
            if not parallel_download_with_progress(url, output_file, num_threads=4):
                print(f"{RED}Failed to download PHP!{RESET}")
                return 1

            print(f"{GREEN}Making PHP Directory...{RESET}")
            os.system("mkdir C:/php")
 
            print(f"{GREEN}Unzipping The PHP File...{RESET}")
            try:
                with zipfile.ZipFile(output_file, "r") as zip_ref:
                    zip_ref.extractall("C:/php")
            except Exception as e:
                print(f"{RED}Error while unzipping PHP: {str(e)}{RESET}")
                return 1
            os.system('setx PATH "%PATH%;C:/php"')

        except Exception as e:
            print(f"{RED}Error during installation: {str(e)}{RESET}")
            return 1

        os.system(f"del {output_file}")
        print(f"{GREEN}PHP installed successfully!{RESET}")
        return 0
        
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