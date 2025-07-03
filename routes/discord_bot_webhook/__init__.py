from fastapi import APIRouter

from .nico_chan import router as nicoChanRouter


router = APIRouter(
    prefix="/discord-bot-webhook"
)

router.include_router(nicoChanRouter)