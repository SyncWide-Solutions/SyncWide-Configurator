from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from installer import database, language, webserver

app = FastAPI(title="SyncWide Configurator")

app.mount("/static", StaticFiles(directory="static"), name="static")
template = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

# index handler
@app.get("/install")
def install(
    request: Request,
    os_type: str,
    install_type: str
):
    if os_type == "linux":
        if install_type == "webserver":
            return RedirectResponse(url="/service/webserver/linux")
        elif install_type == "language":
            return RedirectResponse(url="/service/language/linux")
        elif install_type == "database":
            return RedirectResponse(url="/service/database/linux")
    elif os_type == "windows":
        if install_type == "language":
            return RedirectResponse(url="/service/language/windows")
        elif install_type == "database":
            return RedirectResponse(url="/service/database/windows")
        elif install_type == "webserver":
            return RedirectResponse(url="/service/webserver/windows")

# Second Question
@app.get("/service/{service_name}/{os}")
def service(request: Request, service_name: str, os: str):
    if os == "linux":
        if service_name == "language":
            return template.TemplateResponse("language/linux.html", {"request": request})
        elif service_name == "database":
            return template.TemplateResponse("database/linux.html", {"request": request})
        elif service_name == "webserver":
            return template.TemplateResponse("webserver/linux.html", {"request": request})
    elif os == "windows":
        if service_name == "language":
            return template.TemplateResponse("language/windows.html", {"request": request})
        elif service_name == "database":
            return template.TemplateResponse("database/windows.html", {"request": request})
        elif service_name == "webserver":
            return template.TemplateResponse("webserver/windows.html", {"request": request})

# Installer
@app.get("/install/{service}/{os}")
def install(os: str, service: str, install_service: str):
    if os == "linux":
        # Install Language
        if service == "language":
            if install_service == "php":
                return language.php(os)
            elif install_service == "python":
                return language.python(os)
            elif install_service == "nodejs":
                return language.nodejs(os)
        # Install Database
        elif service == "database":
            if install_service == "mysql":
                return {"message": "Not supported yet!"}
            elif install_service == "mongodb":
                return {"message": "Not supported yet!"}
            elif install_service == "postgresql":
                return {"message": "Not supported yet!"}
        # Install Webserver
        elif service == "webserver":
            if install_service == "apache":
                return webserver.apache(os)
            elif install_service == "nginx":
                return webserver.nginx(os)
    elif os == "windows":
        # Install Language
        if service == "language":
            if install_service == "php":
                return language.php(os)
            elif install_service == "python":
                return language.python(os)
            elif install_service == "nodejs":
                return language.nodejs(os)
        # Install Database
        elif service == "database":
            if install_service == "mysql":
                return {"message": "Not supported yet!"}
            elif install_service == "mongodb":
                return {"message": "Not supported yet!"}
            elif install_service == "postgresql":
                return {"message": "Not supported yet!"}
        # Install Webserver
        elif service == "webserver":
            if install_service == "xampp":
                return webserver.xampp()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web-setup:app", host="0.0.0.0", port=8000, reload=True)