from typing import List

from pydantic import BaseModel, Field


class Project(BaseModel):
    id: str
    resource_ids: List[str]


class ProjectsResponse(BaseModel):
    projects: List[Project] = Field(alias="projects")
