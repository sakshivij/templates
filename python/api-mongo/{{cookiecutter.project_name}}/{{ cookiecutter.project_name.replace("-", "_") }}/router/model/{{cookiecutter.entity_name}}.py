from pydantic import BaseModel


class {{ cookiecutter.entity_name|capitalize }}Create(BaseModel):
    name: str

class {{ cookiecutter.entity_name|capitalize }}(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
