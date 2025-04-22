import uvicorn
from typing import Annotated
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(
    request: Request,
    name: str | None = "Пользователь",
    message: str | None = "Передай мне параметры в URL"
):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"name": name, "message": message}
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)