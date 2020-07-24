import os

from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()


@app.middleware("http")
async def process_valohai_prefix(request: Request, call_next):
    path = request.scope["path"]
    for prefix in (
        request.headers.get("X-VH-Prefix"),
        os.environ.get("VH_DEFAULT_PREFIX"),
    ):
        if not prefix:  # Could have no header or no envvar, so skip
            continue
        if path.startswith(prefix):  # If the path starts with this prefix,
            # ... then strip the prefix out as far as FastAPI is concerned.
            request.scope["path"] = "/" + path[len(prefix) :].lstrip("/")
            break
    return await call_next(request)


@app.get("/predict")
def predict(name: str):
    return {"predicted_first_letter": name[:1].lower()}
