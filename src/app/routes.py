import logging

from fastapi import APIRouter


logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/app")
async def root():
    logger.info("My /app route was called")
    return {"message": "Hello World"}
