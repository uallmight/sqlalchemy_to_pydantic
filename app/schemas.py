from pydantic import BaseModel
from typing import List


class RoleSchema(BaseModel):
    name: str
    is_active: bool


class UserSchema(BaseModel):
    username: str
    email: str

    roles: List[RoleSchema] = []
