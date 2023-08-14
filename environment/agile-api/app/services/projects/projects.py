from app.models.projects import ProjectsResponse, Project
from app.storage.projects.projects import projects


class ProjectNotFound(Exception):
    pass


def list_projects() -> ProjectsResponse:
    return ProjectsResponse(projects=projects())


def get_project(project_id: int) -> Project:
    ps = [p for p in projects() if p.id == project_id]
    return ps[0]
