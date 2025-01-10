from typing import Annotated
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from installer import database, language, webserver

app = FastAPI()

template = Jinja2Templates(directory="templates")

@app.get("/")
def root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)