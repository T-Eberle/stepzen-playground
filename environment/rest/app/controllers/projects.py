from fastapi import APIRouter

from app.models.projects import ProjectsResponse
from app.services.projects.projects import list_projects

router = APIRouter()


@router.get(
    "/projects/",
    responses={
        200: {
            "model": ProjectsResponse,
        },
        404: {},
    },
    response_model=ProjectsResponse,
)
async def projects():
    return list_projects()
