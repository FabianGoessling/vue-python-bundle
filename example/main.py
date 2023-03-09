from fastapi import FastAPI
from fastapi.responses import FileResponse
from vue_component_bundle import VueComponentBundle

app = FastAPI()


@app.get("/")
async def get():
    """Main route"""
    return FileResponse(path="home.html")


@app.get("/test")
async def get_component():
    """Api route for supplying the components."""
    return VueComponentBundle(path="components") # type: ignore
