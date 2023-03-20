from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from vue_component_bundle import VueComponentBundle
import vbuild
import os

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
app = FastAPI()

app.mount("/components", StaticFiles(directory="components"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def get():
    """Main route"""
    return FileResponse(path="home.html")


@app.get("/test")
async def get_component():
    """Api route for supplying the components."""
    return VueComponentBundle(path="components") # type: ignore

@app.get("/vbuild", response_class=HTMLResponse)
async def get_vs(request: Request):
    files = os.listdir(f"./components")
    components = vbuild.render([f"components/{x}" for x in files])
    print(components)
    return templates.TemplateResponse("home2.html", {"request": request, "components": components})
