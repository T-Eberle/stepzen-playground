import uvicorn
from fastapi import FastAPI

from app.controllers.projects import router as projects_router

app = FastAPI()

app.include_router(projects_router, prefix="/api")


def main():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
