from installer import language, webserver, database
import platform
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

def windows():
    start_choise = input(f"{YELLOW}What do you want to install?{RESET}\r\n{RED}[1]{RESET} Web Server\r\n{RED}[2]{RESET} Programming Languages\r\n{RED}[3]{RESET} Databases (Comming Soon!)\r\n{RED}[4]{RESET} Exit\r\n")

    if start_choise == "1":
        print(f"{RED}Comming in V1.1!{RESET}")
    elif start_choise == "2":
        language.install("windows")
    elif start_choise == "3":
        database.install("windows")
    elif start_choise == "4":
        exit()
    else:
        print(f"{RED}Invalid choise!{RESET}")
        windows()

def linux():
    start_choise = input(f"{YELLOW}What do you want to install?{RESET}\r\n{RED}[1]{RESET} Web Server\r\n{RED}[2]{RESET} Programming Languages\r\n{RED}[3]{RESET} Databases (Comming Soon!)\r\n{RED}[4]{RESET} Exit\r\n")

    if start_choise == "1":
        webserver.install("linux")
    elif start_choise == "2":
        language.install("linux")
    elif start_choise == "3":
        database.install("linux")
    elif start_choise == "4":
        exit()
    else:
        print(f"{RED}Invalid choise!{RESET}")
        linux()

class ConfigProcessor:
    def __init__(self):
        self.debug_mode = False
        self.os_type = None
        
    def set_os_type(self, what_os):
        os_map = {
            "Windows": "windows",
            "Linux": "linux"
        }
        
        if what_os not in os_map:
            print(f"{RED}Your OS is not supported!{RESET}")
            exit()
            
        self.os_type = os_map[what_os]
        
    def process_line(self, line_content, database, webserver, language):
        parts = line_content.split()
        if len(parts) != 2:
            return False
            
        component, choice = parts
        
        if component == "debug" and choice.lower() == "true":
            self.debug_mode = True
            return True
            
        if component == "language":
            language_map = {
                "python": language.debug.python if self.debug_mode else language.python,
                "nodejs": language.debug.nodejs if self.debug_mode else language.nodejs,
                "php": language.debug.php if self.debug_mode else language.php
            }
            if choice.lower() in language_map:
                language_map[choice.lower()](self.os_type)
                return True
                
        elif component == "webserver":
            if self.os_type == "windows":
                if choice.lower() == "xampp":
                    if self.debug_mode:
                        webserver.debug.xampp()
                    else:
                        webserver.xampp()
                    return True
            elif self.os_type == "linux":
                webserver_map = {
                    "apache": webserver.debug.apache if self.debug_mode else webserver.apache,
                    "nginx": webserver.debug.nginx if self.debug_mode else webserver.nginx
                }
                if choice.lower() in webserver_map:
                    webserver_map[choice.lower()](self.os_type)
                    return True
                
        elif component == "database":
            if self.debug_mode:
                database.debug.install(self.os_type)
            else:
                database.install(self.os_type)
            return True
            
        return False

def main():
    print("""
.oooooo..o                                   oooooo   oooooo     oooo  o8o        .o8                                
d8P'    `Y8                                    `888.    `888.     .8'   `"'       "888                                
Y88bo.      oooo    ooo ooo. .oo.    .ooooo.    `888.   .8888.   .8'   oooo   .oooo888   .ooooo.                      
 `"Y8888o.   `88.  .8'  `888P"Y88b  d88' `"Y8    `888  .8'`888. .8'    `888  d88' `888  d88' `88b                     
     `"Y88b   `88..8'    888   888  888           `888.8'  `888.8'      888  888   888  888ooo888                     
oo     .d8P    `888'     888   888  888   .o8      `888'    `888'       888  888   888  888    .o                     
8""88888P'      .8'     o888o o888o `Y8bod8P'       `8'      `8'       o888o `Y8bod88P" `Y8bod8P'                     
            .o..P'                                                                                                    
            `Y8P'                                                                                                     
                                                                                                                      
  .oooooo.                          .o88o.  o8o                                                .                      
 d8P'  `Y8b                         888 `"  `"'                                              .o8                      
888           .ooooo.  ooo. .oo.   o888oo  oooo   .oooooooo oooo  oooo  oooo d8b  .oooo.   .o888oo  .ooooo.  oooo d8b 
888          d88' `88b `888P"Y88b   888    `888  888' `88b  `888  `888  `888""8P `P  )88b    888   d88' `88b `888""8P 
888          888   888  888   888   888     888  888   888   888   888   888      .oP"888    888   888   888  888     
`88b    ooo  888   888  888   888   888     888  `88bod8P'   888   888   888     d8(  888    888 . 888   888  888     
 `Y8bood8P'  `Y8bod8P' o888o o888o o888o   o888o `8oooooo.   `V88V"V8P' d888b    `Y888""8o   "888" `Y8bod8P' d888b    
                                                 d"     YD                                                            
                                                 "Y88888P'                                                            
                                                                                                                      
""")
    config_processor = ConfigProcessor()
    config_processor.set_os_type(platform.system())
    print(f"{MAGENTA}Operating System: {platform.system}{RESET}\n")

    have_file = input(f"{YELLOW}Do you have a .syncwide config file?{RESET}\r\n{RED}[1]{RESET} Yes\r\n{RED}[2]{RESET} No\r\n")

    if have_file == "1":
        where_file = input(f"{YELLOW}What is the path to your .syncwide config file?{RESET}\r\n")
        
        try:
            with open(where_file, "r") as file:
                print(f"{GREEN}Config file found!{RESET}")
                print(f"{YELLOW}Trying to read the config file...{RESET}")
                for line in file:
                    line = line.strip()
                    print(line)
                    valid_config = config_processor.process_line(line, database, webserver, language) 
        except Exception as e:
            print(f"{RED}Error reading the config file: {e}{RESET}")
            exit()
            
    elif have_file == "2":
        if platform.system() == "Windows":
            windows()
        elif platform.system() == "Linux":
            linux()
        else:
            print(f"{RED}Your OS is not supported!{RESET}")
            exit()
    else:
        print(f"{RED}Invalid choice!{RESET}")
        exit()


if __name__ == "__main__":
    main()