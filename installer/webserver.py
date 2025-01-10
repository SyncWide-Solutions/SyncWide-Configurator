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

def apache(ops):
    if ops == "linux":
        print(f"{YELLOW}Installing Apache2...{RESET}")
        os.system("sudo apt-get install apache2 -y")
        try:
            with open("/var/www/html/index.html", "w") as file:
                file.write("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Default SyncWide Configurator Page</title>
        <link rel="icon" type="image/png" href="https://cdn.syncwi.de/img/logo.png" />
        <link rel="stylesheet" href="https://cdn.syncwi.de/css/maintenance.css">
    </head>
    <body>
        <div class="container">
            <h1>Default SyncWide Configurator Web Page</h1>
            <p>This Page has been Automaticly gernerated by the <a href="https://github.com/SyncWide-Solutions/SyncWide-Configurator">SyncWide Configurator</a>.</p><br>
            <p>If you want to change the default page, please edit the <code>index.html</code> file in the <code>/var/www/html</code> folder.</p><br>
            <p>To make this Page accessable to the Public make a Port forwarding in you Router for port 80 and 443.</p><br>
            <p>If you want to buy a Domain we recommend buying it from <a href="https://24fi.re/ref/syncwide">24fire GmbH</a>.</p><br>
            <p>If you have any questions, please contact <a href="mailto:info@syncwi.de">info@syncwi.de</a>.</p><br>
        </div>
        <footer>
            &copy; <script src="https://cdn.syncwi.de/js/year.js"></script> <a href="https://syncwi.de">SyncWide Solutions</a>. All rights reserved.
        </footer>
    </body>
    </html>
    """)
            print(f"{GREEN}Apache2 installed successfully!{RESET}")
            return 0
        except Exception as e:
            print(f"{RED}Error whilest installing Apache2{RESET}")
            return 1

def nginx(ops):
    if ops == "linux":
        print(f"{YELLOW}Installing Nginx...{RESET}")
        os.system("sudo apt-get install nginx -y")
        try:
            with open("/var/www/html/index.html", "w") as file:
                file.write("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Default SyncWide Configurator Page</title>
        <link rel="icon" type="image/png" href="https://cdn.syncwi.de/img/logo.png" />
        <link rel="stylesheet" href="https://cdn.syncwi.de/css/maintenance.css">
    </head>
    <body>
        <div class="container">
            <h1>Default SyncWide Configurator Web Page</h1>
            <p>This Page has been Automaticly gernerated by the <a href="https://github.com/SyncWide-Solutions/SyncWide-Configurator">SyncWide Configurator</a>.</p><br>
            <p>If you want to change the default page, please edit the <code>index.html</code> file in the <code>/var/www/html</code> folder.</p><br>
            <p>To make this Page accessable to the Public make a Port forwarding in you Router for port 80 and 443.</p><br>
            <p>If you want to buy a Domain we recommend buying it from <a href="https://24fi.re/ref/syncwide">24fire GmbH</a>.</p><br>
            <p>If you have any questions, please contact <a href="mailto:info@syncwi.de">info@syncwi.de</a>.</p><br>
        </div>
        <footer>
            &copy; <script src="https://cdn.syncwi.de/js/year.js"></script> <a href="https://syncwi.de">SyncWide Solutions</a>. All rights reserved.
        </footer>
    </body>
    </html>
    """)
            print(f"{GREEN}Nginx installed successfully!{RESET}")
            return 0
        except Exception as e:
            print(f"{RED}Error whilest installing Nginx{RESET}")
            return 1

def xampp():
    print(f"{YELLOW}Installing XAMPP...{RESET}")
    os.system("winget install -e --id ApacheFriends.Xampp.8.1")
    try:
        with open("C:/xampp/htdocs/index.html", "w") as file:
            file.write("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Default SyncWide Configurator Page</title>
        <link rel="icon" type="image/png" href="https://cdn.syncwi.de/img/logo.png" />
        <link rel="stylesheet" href="https://cdn.syncwi.de/css/maintenance.css">
    </head>
    <body>
        <div class="container">
            <h1>Default SyncWide Configurator Web Page</h1>
            <p>This Page has been Automaticly gernerated by the <a href="https://github.com/SyncWide-Solutions/SyncWide-Configurator">SyncWide Configurator</a>.</p><br>
            <p>If you want to change the default page, please edit the <code>index.html</code> file in the <code>/var/www/html</code> folder.</p><br>
            <p>To make this Page accessable to the Public make a Port forwarding in you Router for port 80 and 443.</p><br>
            <p>If you want to buy a Domain we recommend buying it from <a href="https://24fi.re/ref/syncwide">24fire GmbH</a>.</p><br>
            <p>If you have any questions, please contact <a href="mailto:info@syncwi.de">info@syncwi.de</a>.</p><br>
        </div>
        <footer>
            &copy; <script src="https://cdn.syncwi.de/js/year.js"></script> <a href="https://syncwi.de">SyncWide Solutions</a>. All rights reserved.
        </footer>
    </body>
    </html>""")
            print(f"{GREEN}XAMPP installed successfully!{RESET}")
            return 0
    except Exception as e:
        print(f"{RED}Error whilest installing XAMPP{RESET}")
        return 1

def install(ops):
    if ops == "linux":
        what_web_server = input(f"{YELLOW}Witch Web Server do you want to install?{RESET}\r\n{RED}[1]{RESET} Apache2 (recommended)\r\n{RED}[2]{RESET} Nginx\r\n{RED}[3]{RESET} Exit\r\n")

        if what_web_server == "1":
            apache(ops)
        elif what_web_server == "2":
            nginx(ops)
        elif what_web_server == "3":
            exit()
        else:
            print(f"{RED}Invalid choise!{RESET}")
            install("linux")
    elif ops == "windows":
        what_web_server = input(f"{YELLOW}Witch Web Server do you want to install?{RESET}\r\n{RED}[1]{RESET} XAMPP\r\n{RED}[2]{RESET} Exit\r\n")

        if what_web_server == "1":
            xampp()
        elif what_web_server == "2":
            exit()
        else:
            print(f"{RED}Invalid choise!{RESET}")
            install("windows")