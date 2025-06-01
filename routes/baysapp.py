import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import APIRouter
from fastapi.responses import JSONResponse

import MeCab
from clients import SqliteClient

from model.baysapp.valueObject import *
from model.baysapp.dto import *
from model.baysapp.repository import *
from model.baysapp.usecase import *


router = APIRouter()

sqlite_client = SqliteClient("./static_data/words.db", "words")
work_repository = WordsRepository(client=sqlite_client)


@router.get("/baysapp", tags=["baysapp"])
async def bays():
    return JSONResponse({ "message": "This is/baysapp router!" })


@router.post("/baysapp/naive_bayse", tags=["baysapp"], response_model=PredictNaiveResponseDTO)
async def naive(req: PredictNaiveRequestDTO):
    request = PredictNaiveRequestDTO(
        sentence=Sentence(value=req.sentence.value)
    )

    words = ParseWordsUseCase(
        client=MeCab.Tagger(),
        request=request
    ).execute()

    predict = PredictNaiveUseCase(
        repository=work_repository,
        request=words 
    ).execute()
    
    return predict