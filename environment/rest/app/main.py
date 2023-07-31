import uvicorn
from fastapi import FastAPI

from app.controllers.users import router as users_router

app = FastAPI()

app.include_router(users_router, prefix="/api")


def main():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
