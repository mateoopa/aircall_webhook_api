from pydantic import BaseModel
from typing import Optional


class Response(BaseModel):
    success: bool
    message: str
    exceptionMessage: Optional[str] = None
    id: Optional[str] = None