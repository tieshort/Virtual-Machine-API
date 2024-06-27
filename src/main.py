from fastapi import FastAPI

from routes import servers

import uvicorn

app = FastAPI()

app.include_router(servers.router)

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)