from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from db.database import create_all_models

from routes import servers

import uvicorn

app = FastAPI()

app.include_router(servers.router)

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)