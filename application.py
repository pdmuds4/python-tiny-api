from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["root"])
async def route():
    return JSONResponse({ "message": 'This is python-tiny-api!' })


if __name__=="__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=8000, reload=True)