from fastapi import FastAPI
from a2wsgi import ASGIMiddleware
from routers import webhook_v1


def create_app():
    fastapi_app = FastAPI()
    fastapi_app.include_router(webhook_v1.router, prefix="/v1")
    fastapi_app.title = "AirCall Slack API"
    fastapi_app.description = "Supports AirCall Slack Summaries"
    fastapi_app.version = "1.0"
    return fastapi_app


app = create_app()
wsgi_app = ASGIMiddleware(app)
