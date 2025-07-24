from fastapi import APIRouter, Depends, Request
from models.response_v1 import Response

router = APIRouter(
    prefix="/webhook",
    tags=["Webhook"],
    responses={404: {"description": "Not found"}},
)


@router.post("/test")
async def process_request(request: Request):

    try:
        request_body = await request.json()
    except Exception as e:
        return Response(success=False, message='Request could not be deserialized.', exceptionMessage=f"{e}")

    return Response(success=True, message=f'Request received. {request_body}')