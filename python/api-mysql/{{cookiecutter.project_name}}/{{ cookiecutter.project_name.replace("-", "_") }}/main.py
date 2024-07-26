import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import EnvironmentVariables
from .router.{{cookiecutter.table_name}} import router as {{cookiecutter.table_name}}_router

app = FastAPI()
env = EnvironmentVariables()

origins = env.origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router({{cookiecutter.table_name}}_router)

if __name__ == "__main__":
    uvicorn.run(app, host=env.host, port=env.port)
