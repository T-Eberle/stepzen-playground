from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    id: str = Field(alias="id")
    firstname: str = Field(alias="firstname")
    lastname: str = Field(alias="lastname")
