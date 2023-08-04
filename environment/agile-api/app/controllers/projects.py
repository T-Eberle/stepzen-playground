from fastapi import APIRouter

from app.models.projects import ProjectsResponse, Project
from app.services.projects.projects import list_projects, get_project

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


@router.get(
    "/project/{project_id}",
    responses={
        200: {
            "model": Project,
        },
        404: {},
    },
    response_model=Project,
)
async def project(project_id: int):
    return get_project(project_id)
