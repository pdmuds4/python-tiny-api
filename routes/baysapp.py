import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import APIRouter
from fastapi.responses import JSONResponse

import MeCab, pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination

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

network_model = DiscreteBayesianNetwork([('sex', 'use_time'), ('time', 'use_time'), ('use_time', 'category')])
network_model.fit(pd.read_csv('./static_data/screentime.csv'))
network_infer = VariableElimination(network_model)


@router.get("/baysapp", tags=["baysapp"])
async def bays():
    return JSONResponse({ "message": "This is /baysapp router!" })


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


@router.post("/baysapp/predict_network", tags=["baysapp"], response_model=PredictNetworkResponsePayload)
async def network(req: PredictNetworkRequestPayload):
    try:
        request = PredictNetworkRequestDTO(
            type=PredictTypes(value=req.type),
            evidence=EvidenceEntity(
                category=CategoryEvidence(value=req.evidence.category),
                sex=SexEvidence(value=req.evidence.sex),
                time=TimeEvidence(value=req.evidence.time),
                use_time=UseTimeEvidence(value=req.evidence.use_time)
            )
        )
        
        predictNetworkService = PredictNetworkService(client=network_infer)

        predictNetworkUseCase = PredictNetworkUseCase(
            request=request,
            predictNetworkService=predictNetworkService
        )

        response = predictNetworkUseCase.execute()

        return PredictNetworkResponsePayload(
            type=response.type.value,
            score={
                category: score["value"] for category, score in response.score.model_dump().items()
            }
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