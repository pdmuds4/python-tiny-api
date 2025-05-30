from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()


@app.get("/", tags=["root"])
async def route():
    return JSONResponse({ "message": 'This is python-tiny-api!' })


if __name__=="__main__":
    uvicorn.run("main:app",port=3000, reload=True)