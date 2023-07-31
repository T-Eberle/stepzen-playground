from fastapi import APIRouter, HTTPException

from app.models.users import UserResponse
from app.services.users.users import get_user, UserNotFound

router = APIRouter()


@router.get(
    "/users/{user_id}",
    responses={
        200: {
            "model": UserResponse,
        },
        404: {},
    },
    response_model=UserResponse,
)
async def users(user_id: str):
    try:
        user = get_user(user_id)
        return UserResponse(**user)
    except UserNotFound as ex:
        raise HTTPException(status_code=404, detail=f"User not found {str(ex)}")
    except Exception:
        raise HTTPException(status_code=500, detail="unexpected exception")
