import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import APIRouter
from fastapi.responses import JSONResponse

import MeCab
from clients import SqliteClient
from model._error import BaseError

from model.baysapp.dto import *
from model.baysapp.payload import *

from model.baysapp.valueObject import *
from model.baysapp.repository import *
from model.baysapp.usecase import *
from model.baysapp.service import *

router = APIRouter()

sqlite_client = SqliteClient("./static_data/words.db", "words")
work_repository = WordsRepository(client=sqlite_client)


@router.get("/baysapp", tags=["baysapp"])
async def bays():
    return JSONResponse({ "message": "This is/baysapp router!" })


@router.post("/baysapp/predict_naive", tags=["baysapp"], response_model=PredictNaiveResponsePayload)
async def naive(req: PredictNaiveRequestPayload):
    try:
        request = PredictNaiveRequestDTO(
            sentence=Sentence(value=req.sentence)
        )

        parseWordsService = ParseWordsService(client=MeCab.Tagger())
        predictNaiveService = PredictNaiveService(repository=work_repository)

        predictNaiveUseCase = PredictNaiveUseCase(
            request=request,
            parseWordsService=parseWordsService,
            predictNaiveService=predictNaiveService
        )

        response = predictNaiveUseCase.execute()
        
        return PredictNaiveResponsePayload(
            weather=response.weather.value,
            life=response.life.value,
            sports=response.sports.value,
            culture=response.culture.value,
            economy=response.economy.value
        )
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