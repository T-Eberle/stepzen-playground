from typing import List

from pydantic import BaseModel, Field


class Project(BaseModel):
    id: str
    resource_ids: List[str]
    name: str
    description: str
    agile_method: str
    team_members_amount: int
    is_completed: bool


class ProjectsResponse(BaseModel):
    projects: List[Project] = Field(alias="projects")
