from installer import language, webserver, database
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

def header():
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
        what_os = input(f"{YELLOW}What OS do you use?{RESET}\r\n{RED}[1]{RESET} Linux\r\n{RED}[2]{RESET} Windows\r\n{RED}[3]{RESET} Mac\r\n{RED}[4]{RESET} Exit\r\n")
        if what_os == "1":
            linux()
        elif what_os == "2":
            print(f"{RED}Windows is not supported yet!{RESET}")
        elif what_os == "3":
            print(f"{RED}Mac is not supported yet!{RESET}")
        elif what_os == "4":
            exit()
        else:
            print(f"{RED}Invalid choise!{RESET}")
            header()

if __name__ == "__main__":
    header()
