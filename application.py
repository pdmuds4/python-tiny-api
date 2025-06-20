import os, dotenv, uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from routes import *
from model._error import BaseError

app = FastAPI()
dotenv.load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/socket.io/mhjoinup", mhJoinUpSocketApp)


@app.middleware("http")
async def api_key_authentication(request: Request, call_next):
    api_key = os.getenv("API_KEY")
    api_key_auth = os.getenv("API_KEY_AUTH")
    
    try:
        match api_key_auth:
            case "true":
                if request.url.path in config["aka_ignore_paths"] or request.headers.get("X-API-KEY") == api_key:
                    return await call_next(request)
                else:
                    return JSONResponse(
                        status_code=401,
                        content={"message": "Unauthorized: Invalid API Key"}
                    )
            case "false":
                return await call_next(request)
    except Exception as e:
        if isinstance(e, BaseError):
            return JSONResponse(
                status_code=e.status_code,
                content={
                    "message": e.message,
                    "detail": e.detail,
                    "level": e.level
                }
            )
        else:
            return JSONResponse(
                status_code=500,
                content={
                    "message": "An unexpected error occurred.",
                    "detail": str(e),
                    "level": "unknown"
                }
            )



@app.get("/", tags=["root"])
async def route():
    return JSONResponse(
        status_code=200,
        content={ "message": 'This is python-tiny-api!' }
    )


app.include_router(baysAppRouter)
app.include_router(mhJoinUpRouter)


if __name__=="__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=8000, reload=True)