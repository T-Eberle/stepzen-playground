from app.models.projects import ProjectsResponse, Project
from app.storage.projects.projects import projects


class ProjectNotFound(Exception):
    pass


def list_projects() -> ProjectsResponse:
    return ProjectsResponse(projects=[Project(**x) for x in projects()])
