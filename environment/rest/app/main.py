import json

from fastapi import FastAPI, HTTPException

from app.services.users.users import UserNotFound, get_user

app = FastAPI()


@app.get("/api/health")
async def health():
    return {"message": "up"}


@app.get("/api/users/{user_id}")
async def users(user_id: str):
    try:
        user = get_user(user_id)
        return {"user": json.dumps(user)}
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found")
